node {
    stage('Build') {
        checkout scm
        docker.image('python:3.13.1-alpine3.21').inside {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    stage('Test') {
        docker.image('qnib/pytest').inside {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        }
        junit 'test-reports/results.xml'
    }
/*     stage('Manual Approval') {
        input message: 'Lanjutkan ke tahap Deploy?', ok: 'Lanjutkan'
    } */
    stage('Deploy') {
        docker.image('python:3.13.1-alpine3.21').inside('-u root') {
            sh 'pip install pyinstaller'
            sh 'pyinstaller --onefile sources/add2vals.py'
            //sleep 60
            //echo 'Pipeline has finished successfully.'
        }
        archiveArtifacts artifacts: 'dist/add2vals', onlyIfSuccessful: true
    }
}