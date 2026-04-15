pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh """
                    sudo docker rmi nginx:latest 2>/dev/null || true
                    sudo docker pull nginx:latest
                """
            }
        }
        
        stage('Deploy'){
            steps{
                sh """
                    sudo docker stop nginx 2>/dev/null || true
                    sudo docker rm nginx 2>/dev/null || true
                    sudo docker run -d -p 80:80 -v ./index.html:/usr/share/nginx/html/index.html --name nginx nginx:latest
                """
            }
        }
    }
}
