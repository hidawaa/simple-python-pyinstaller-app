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
    stage('Deploy') {
        docker.image('cdrx/pyinstaller-linux:python2').inside('--entrypoint=""') {
            sh 'python -m ensurepip --upgrade'
            sh 'pip install pyinstaller'
            sh 'pyinstaller --onefile sources/add2vals.py'
        }
        post {
            success {
                archiveArtifacts artifacts: 'dist/add2vals', onlyIfSuccessful: true
            }
        }
    }
}