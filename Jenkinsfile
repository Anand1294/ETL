pipeline {
    agent any

    stages {
        stage('Python1') {
            steps {
                echo 'Running extract_data.py...'
                sh "python -u 1.py"
            }
        }

        stage('Python2') {
            steps {
                echo 'Running transform_data.py...'
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
