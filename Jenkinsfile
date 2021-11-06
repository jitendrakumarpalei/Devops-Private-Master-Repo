pipeline {
    agent { label 'Docker_Host'}
  
    stages {
        stage('Jfrog Health Checkup') {
            steps {
                sh 'curl http://192.168.1.102:8082/'
            }
            post {
                failure {
                    mail to: 'ashanta.palei@gmail.com',
                        from: 'techcare.devops@gmail.com',
                        subject: "${env.BUILD_NUMBER} - Failed",
                        body: "Hey There, Build#${env.BUILD_NUMBER} and Stage Name ${STAGE_NAME} failed"
                }
            }
        }
        stage('Splunk Health Checkup') {
            steps {
                sh 'curl http://192.168.1.104:8000/en-GB/app/launcher/home'
            }
            post {
                failure {
                    mail to: 'ashanta.palei@gmail.com',
                        from: 'techcare.devops@gmail.com',
                        subject: "${env.BUILD_NUMBER} - Failed",
                        body: "Hey There, Build#${env.BUILD_NUMBER} and Stage Name ${STAGE_NAME} failed"
                }
            }
        }
    }
}
