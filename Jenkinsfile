pipeline {
    agent any

    stages {
        stage('Python1') {
            steps {
                echo 'Running 1.py...'
                bat "python -u 1.py"
                echo 'Python 1 successful'
            }
        }

        stage('Python2') {
            steps {
                echo 'Running 2.py...'
                bat "python -u sport.py"
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'output*.csv, *.pkl', fingerprint: true
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
