pipeline {
    agent any
    
    environment{
        registry = "thuuha/jenkintest"
        registryCredential = "jenkin"
        // registryPass= "jenkinPassword"
        // registryuUser= "jenkinUser"
    }
    stages {
        // stage ('run python script'){
        //     steps {
        //         sh 'uvicorn main:app --host 0.0.0.0 --port 8000'
        //     }
        // }
        stage ('build images'){

            steps {
                sh 'docker build -t thuuha/jenkintest .'
            }
        }

        stage ('push') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.registryCredential)]) {
        	    sh "docker login -u ${env.jenkinUser} -p ${env.jenkinPassword}"
                sh 'docker push thuuha/jenkintest'
            }
        }
    }
        stage ('test') {
            steps {
                sh "echo test "
            }
        }
}
}