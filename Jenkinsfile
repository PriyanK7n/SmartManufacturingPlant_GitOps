pipeline {
    agent any
    environment {
        Docker_HUB_REPO = "priyank179/gitops_project" 
        Docker_HUB_CREDENTIALS_ID = "gitOps-dockerHub-Token"
    }
    
    stages {
        
        stage('Checkout Github') {
            steps {
                echo 'Checking out code from GitHub...'		    
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/PriyanK7n/SmartManufacturingPlant_GitOps.git']])    

            }
        } 


        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    dockerImage = docker.build("${Docker_HUB_REPO}:latest")
                    }
            }
        }
        

        stage('Push Image to DockerHub') {
            steps {
                script {
                echo 'Pushing Docker image to DockerHub...'
                docker.withRegistry("https://registry.hub.docker.com", "${Docker_HUB_CREDENTIALS_ID}") {
                    dockerImage.push("latest") // Use the dockerImage variable from previous stage to push into docker hub
                    }
                }
            }
        }
        
        stage('Install Kubectl & ArgoCD CLI') {
            steps {
                echo 'Installing Kubectl and ArgoCD CLI...'
            }
        }
        
        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                echo 'Applying Kubernetes and syncing with ArgoCD...'
            }
        }
    }
}
