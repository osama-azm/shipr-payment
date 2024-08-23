from main import redis, Order
import time

key = "refund_order"
group = "payment-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists, skipping creation")

while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)
        
        if results != []:
            for result in results:
                obj = result[1][0][1]

                order = Order.get(obj['pk'])
                order.status = "refunded"
                order.save()
                print(f"Order {obj['pk']} refunded.")
                
    except Exception as e:
        print(str(e))

    time.sleep(5)