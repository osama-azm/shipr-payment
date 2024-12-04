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
                curl -L "https://github.com/docker/compose/releases/download/2.24.0/docker-compose-Linux-x86_64" -o ./docker-compose
                chmod +x ./docker-compose
                ./docker-compose --version
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
