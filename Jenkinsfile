pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh """
                    echo "Running Build Stage"
                    sudo cp index.html /var/www/html/index.nginx-debian.html
                    echo "Build Completed"
                """
            }
        }
        stage('Deploy'){
            steps{
                sh """
                    echo "Running Deploy Stage"
                    sudo systemctl restart nginx
                    echo "Deploy Completed"
                """
            }
        }
    }
}
