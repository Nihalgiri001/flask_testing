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
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m unittest discover -s tests -v'
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