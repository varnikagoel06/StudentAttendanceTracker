
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .ci-venv
                    .ci-venv/bin/python -m pip install -r requirements.txt
                    .ci-venv/bin/python -m py_compile app.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.ci-venv/bin/python -m unittest discover -s tests -v'
            }
        }

        stage('Package') {
            steps {
                sh 'zip -r attendance-app.zip app.py templates requirements.txt'
                archiveArtifacts artifacts: 'attendance-app.zip', fingerprint: true
            }
        }
    }
}
