pipeline {
    agent any
    
    environment{
        registryCredential = "jenkin"
        // registryPass= "jenkinPassword"
        // registryUser= "jenkinUser"
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
            //     withCredentials([usernamePassword(credentialsId: env.registryCredential)]) {
        	//     // sh "docker login -u ${env.registryUser} -p ${env.registryPass}"
            //     // sh 'docker push thuuha/jenkintest'
            // }
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
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