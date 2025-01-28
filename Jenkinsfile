node {

    stage('Build') {
        checkout scm
        docker.image('python:2-alpine').inside {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }

    stage('Test') {
        docker.image('qnib/pytest').inside {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        }
        junit 'test-reports/results.xml'
    }

    stage('Manual Approval') {
        input message: 'Lanjutkan ke tahap Deploy?'
    }
    
    stage('Deploy') {
        checkout scm
        docker.image('python:3.9').inside('-u root') {
            sh 'pip install pyinstaller'
            sh 'pyinstaller --onefile sources/add2vals.py'
            sleep 60
            echo 'Eksekusi pipeline sukses.'
        }

        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
            sh 'docker build -t hidawaa/simple-python-pyinstaller-app .'
            sh "echo $PASS | docker login -u $USER --password-stdin"
            sh 'docker push hidawaa/simple-python-pyinstaller-app'
        }

        def dockerrun = 'docker run -p 3000:3000 -d hidawaa/simple-python-pyinstaller-app:latest'
            
        sshagent(['ec2']) {
                sh "ssh -o StrictHostKeyChecking=no ubuntu@54.242.20.102 ${dockerrun}"
        }

        archiveArtifacts artifacts: 'dist/add2vals', onlyIfSuccessful: true
    }
}