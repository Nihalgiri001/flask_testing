pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'apt install python3-pytest python3-flask'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests -v'
            }
        }
    }

    post {
        success {
            echo 'Flask application tested successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}