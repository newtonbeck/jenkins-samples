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
  post {
    always {
      echo 'This will always run'
    }
    success {
      echo 'This will run only when things go right'
    }
    failure {
      echo 'This will run only when things go wrong'
    }
    unstable {
      echo 'This will run when when the run is marked as unstable'
    }
    changed {
      echo 'The pipeline status has changed!'
    }
  }
}
