pipeline {
  agent any

  environment {
    IMAGE_NAME = 'dhwanii08/whong4_student-survey-form-flask'
    IMAGE_TAG = "${BUILD_NUMBER}"  // dynamic tag
    KUBECONFIG_PATH = '/var/lib/jenkins/kubeconfig-flask.yaml'
  }

  stages {
    stage('Checkout GitHub Repository') {
      steps {
        checkout scm
      }
    }

    stage('Build Flask Docker Image') {
      steps {
        script {
          sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
            sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
          }
        }
      }
    }

    stage('Deploy to Rancher') {
      steps {
        script {
		  sh 'kubectl set image deployment/swe-645-flask-survey-form container-0=dhwanii08/whong4_student-survey-form-flask:$BUILD_NUMBER'
        }
      }
    }
  }
}
