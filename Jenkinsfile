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
                curl -L "https://github.com/docker/compose/releases/download/v2.30.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                chmod +x /usr/local/bin/docker-compose
                docker-compose --version
                docker-compose build
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
