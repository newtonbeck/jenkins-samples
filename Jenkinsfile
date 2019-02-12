pipeline {
  agent { docker { image 'python' } }
  stages {
    stage('Build') {
      steps {
        retry(3) {
          sh 'python flaky.py'
        }

        timeout(time: 3, unit: 'SECONDS') {
          sh 'python timeout.py'
        }
      }
    }
  }
}
