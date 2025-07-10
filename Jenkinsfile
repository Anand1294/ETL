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
            script {
                emailext (
                    subject: '✅ Jenkins Build Successful: ${JOB_NAME} #${BUILD_NUMBER}',
                    body: 'The build was successful.\n\nPlease find the generated files attached.',
                    to: 'devopsdev.0111@gmail.com',
                    attachmentsPattern: 'output*.csv, *.pkl'
                )
            }
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
