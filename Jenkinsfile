pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest -v'
            }
        }
    }

    post {
        failure {
            echo 'BUILD FEHLGESCHLAGEN: pip install konnte Paket nicht finden.'
        }
        success {
            echo 'Build erfolgreich.'
        }
    }
}
