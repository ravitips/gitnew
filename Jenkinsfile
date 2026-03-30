pipeline{
    agent any
    parameters{
        string(name: 'SOURCE_FILE',description: 'Enter your webpage file', defaultValue: 'index.html')
        string(name: 'DESTINATION_FILE',description: 'Enter your target path', defaultValue: '/var/www/html/index.nginx-debian.html')
        choice(name: 'SERVICE',choices: ['nginx','apache','docker'],description: 'Enter your service name')
    }
    
    stages{
        stage('Build'){
            steps{
                sh """
                    sudo cp -r ${params.SOURCE_FILE} ${params.DESTINATION_FILE}
                """
            }
        }
        stage('Deploy'){
            steps{
                sh """
                    sudo systemctl restart ${params.SERVICE}
                """
            }
        }
    }
}
