pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                curl -L "https://github.com/docker/compose/releases/download/v2.30.3/docker-compose-linux-x86_64" -o ./docker-compose
                chmod +x ./docker-compose
                ./docker-compose --version
                apt install docker-ce
                ./docker-compose build
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
    }
}
