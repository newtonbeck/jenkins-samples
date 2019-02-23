pipeline {

  agent { docker { image 'newtonbeck/pytest' } }

  environment {
    MY_ENV = 'xenkins'
  }

  stages {
    stage('Test') {
      steps {
        sh 'rm -rf report'

        sh 'mkdir report'

        sh 'pytest --junitxml=report/junit.xml'
      }
    }

    stage('Deploy') {
      steps {
        sh 'python env_var.py'

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
      junit 'report/junit.xml'
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
