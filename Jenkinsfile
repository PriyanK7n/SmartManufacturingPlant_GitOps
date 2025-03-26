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
        

        stage('Install Kubectl & ArgoCD CLI Setup') {
            steps {
                // echo 'Installing Kubectl and ArgoCD CLI...'
                sh '''
                echo 'installing Kubectl & ArgoCD cli...'
                curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                chmod +x kubectl
                mv kubectl /usr/local/bin/kubectl

                curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                chmod +x /usr/local/bin/argocd
                '''
            }
        }
        

        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                script {

                    kubeconfig(credentialsId: 'kubeconfig', serverUrl: 'https://192.168.49.2:8443') {
                        sh '''
                        argocd login 34.45.12.249:31173 --username admin --password $(kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
                        argocd app sync gitopsappsmartmanufacturing
                        '''
                        }
                }
            }
        }

    }
}
