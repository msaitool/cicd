pipeline {
    agent any
    
    environment{
        registry = "thuuha/jenkintest"
        registryCredential = "jenkin"
    }
    stages {
        stage ('run python script'){
            steps {
                sh 'python3 main.py'
            }
        }
        stage ('build images'){
            steps {
                sh 'docker build -t thuuha/jenkintest .'
            }
        }

        stage ('push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'jenkin', passwordVariable: 'jenkinPassword', usernameVariable: 'jenkinUser')]) {
        	    sh "docker login -u ${env.jenkinUser} -p ${env.jenkinPassword}"
                sh 'docker push thuuha/jenkintest'
            }
        }
    }
}
}