# 🚀 Smart Manufacturing Machines Efficiency Prediction

A full-scale MLOps project focused on building and deploying an ML model for predicting machine efficiency in the automobile manufacturing industry. The goal is to improve **predictive maintenance**, optimize **machine health**, and ensure better **cost management** through a seamless and automated CI/CD workflow powered by **Jenkins**, **Argo CD**, and **GitOps** principles.

---

## Application

<img width="1337" alt="image" src="https://github.com/user-attachments/assets/fa1f41d3-989b-4b7e-8d04-f11bdc7483ac" />


### CI Workflow using Jenkins

<img width="1258" alt="image" src="https://github.com/user-attachments/assets/b1d479cd-b2bd-47b9-a1c2-12eeb3c6d0a3" />


### CD Workflow using Argo CD 

![Pasted Graphic](https://github.com/user-attachments/assets/1aaae714-93c7-406f-8f23-c6062e94fde2)


## 🎯 Target Audience

- Automobile Manufacturing Industry
- Maintenance Engineers
- Factory Floor Automation Experts
- MLOps Enthusiasts

---


## 🧠 Use Case

By predicting the efficiency of smart manufacturing machines:
- 🔧 We enable **predictive maintenance**
- 💸 Reduce **downtime and repair costs**
- 📈 Improve **production efficiency**

---


## ⚙️ Project Workflow

| Step | Description |
|------|-------------|
| 1️⃣ | Project Setup & Folder Structure Defined |
| 2️⃣ | Initial testing with **Jupyter Notebooks** |
| 3️⃣ | Data Processing (cleaning, feature engineering) |
| 4️⃣ | ML Model Training & Evaluation |
| 5️⃣ | User App Development using Flask |
| 6️⃣ | Dockerfile & Kubernetes Manifests created |
| 7️⃣ | Version Control of code and data with GitHub |
| 8️⃣ | GCP VM Instance setup with Minikube, `kubectl`, Docker |
| 9️⃣ | Jenkins Setup (Inside Minikube) |
| 🔟 | GitHub Integration with Jenkins |
| 1️⃣1️⃣ | CI Pipeline: Jenkins builds & pushes Docker images to Docker Hub |
| 1️⃣2️⃣ | Argo CD Installation & Configuration |
| 1️⃣3️⃣ | Continuous Deployment Code (K8s manifests + Git repo integration) |
| 1️⃣4️⃣ | Argo CD Deployment Automation using Webhooks |

---


## 🧪 Tech Stack

- **CI Tool**: Jenkins
- **CD Tool**: Argo CD
- **Orchestration**: Kubernetes (via Minikube)
- **Containerization**: Docker
- **Cloud Provider**: Google Cloud Platform (GCP VM)
- **Source Control**: GitHub (Truth Source)
- **Monitoring**: GitHub Webhooks + Argo CD Rollbacks

---


## 🔁 CI/CD Architecture

```mermaid
flowchart TD
    A[Code Push to GitHub] --> B[Jenkins CI Trigger]
    B --> C[Build Docker Image]
    C --> D[Push Image to Docker Hub]
    D --> E[GitHub Commit for Deployment]
    E --> F[Argo CD Detects Change]
    F --> G[Deploys to K8s via Manifests]
    G --> H[Production Environment]
