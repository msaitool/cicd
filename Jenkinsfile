pipeline {
    agent any
    
    environment{
        registryCredential = credentials('jenkin')
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
                withDockerRegistry([ credentialsId: "jenkin", url: "" ]) {
                 dockerImage.push()}
            }
    }
        // stage ('test') {
        //     steps {
        //         sh "echo test "
        //     }
        // }
}
    }}