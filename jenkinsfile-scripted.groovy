node {


        def testImage = docker.build("zip-job-docker", "/home/system/mydocker")
        testImage.inside("--privileged --label zip-job-docker --network system_default -e 'VERSION=${env.VERSION}'") {
        stage('Build') {
            sh 'python3 /tmp/zip_job.py'
        }
        stage('Publish') {
            if (currentBuild.currentResult == 'SUCCESS') {
                def server = Artifactory.newServer url: 'http://10.101.0.137:8081/artifactory/', username: 'super-user', password: 'Qw12856!'
                def uploadSpec = """{
                    "files": [
                    {
                       "pattern": "*.zip",
                        "target": "binary-storage/${VERSION}/"
                    }
                         ]
                    }"""
                 server.upload spec: uploadSpec, failNoOp: true
            }
        }
        stage('Report') {
            emailext body: "The Jenkins job ${env.JOB_NAME} has completed with status ${currentBuild.currentResult}",
            subject: "${currentBuild.currentResult}: Job ${env.JOB_NAME}",
            to: 'some-email@example.com'
        }
        stage('Cleanup') {
            deleteDir()
        }
    }
}
