pipeline {
    agent any

    stages {
        stage('Python1') {
            steps {
                echo 'Running 1.py...'
                sh "python -u 1.py"
            }
        }

        stage('Python2') {
            steps {
                echo 'Running 2.py...'
                sh "python -u 1.py"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
