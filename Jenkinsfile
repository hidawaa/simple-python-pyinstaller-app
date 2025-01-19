node {
    stage('Build') {
        checkout scm
        docker.image('python:2-alpine').inside {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    stage('Test') {
        checkout scm
        docker.image('qnib/pytest').inside {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        }
        junit 'test-reports/results.xml'
    }
    stage('Deploy') {
        checkout scm
        def volume = "${pwd()}/sources:/src"
        def image = 'cdrx/pyinstaller-linux:python2'
        
        dir(env.BUILD_ID) {
            unstash name: 'compiled-results'
            
            sh """
                docker run --rm -v ${volume} ${image} sh -c 'pyinstaller -F /src/add2vals.py'
            """
        }

        archiveArtifacts artifacts: 'sources/dist/add2vals', onlyIfSuccessful: true

        sh """
            docker run --rm -v ${volume} ${image} sh -c 'rm -rf /src/build /src/dist'
        """
    }
}