pipeline {
    agent any
    
    environment{
        registryCredential = 'jenkin'
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
                script{
                withDockerRegistry([ credentialsId: env.registryCredential, url: "https://registry-1.docker.io/" ]) {
                //  dockerImage.push()
                 }
                 sh 'docker push thuuha/jenkintest '
                
            }
    }
        // stage ('test') {
        //     steps {
        //         sh "echo test "
        //     }
        // }
}
    }}