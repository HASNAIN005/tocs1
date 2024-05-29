pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'dsadasf' 
            }
        }

        stage('Deploy to Google Cloud') {
            steps {
                script {
                    try {
                        withCredentials([file(credentialsId: 'keyy', variable: 'GCP_KEY_FILE')]) {
                            sh 'gcloud auth activate-service-account --key-file=$GCP_KEY_FILE'
                            sh 'gcloud config set project genuine-habitat-423301-a2' 
                            sh 'gcloud compute ssh ar784419@husnainjenkins --zone=us-central1-a --command="sudo mkdir -p /var/www/html && sudo chmod 777 /var/www/html"' 
                            sh 'gcloud compute scp index.html ar784419@husnainjenkins:/var/www/html --zone=us-central1-a' 
                            echo 'Successfully deployed index.html to Google Cloud server'
                        }
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Failed to deploy index.html to Google Cloud server: ${e.message}")
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Successfully deployed!'
        }
    }
}
