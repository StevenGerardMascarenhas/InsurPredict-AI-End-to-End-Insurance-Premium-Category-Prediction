

### 🚀 InsurPredict AI: End-to-End Insurance Premium Category Prediction

"InsurPredict AI is a production-grade, containerized Machine Learning pipeline that uses a Random Forest Classifier to predict health insurance premium categories (Low, Medium, or High) based on demographic and health data, featuring a full-stack deployment with a RESTful FastAPI backend, a Streamlit frontend  ,dockerized with docker and deployed on AWS EC2."

🏗️ System Architecture

The application follows a decoupled architecture where the frontend and backend communicate via RESTful API requests.

![aws diagram](https://github.com/user-attachments/assets/f4f5fec2-f016-4097-a87a-89eb4c6ea11c)


The Workflow:

• User Input: Users enter demographic and health details (Age, Weight, Height, Income, Smoker Status, City, and Occupation) through the Streamlit UI.

• REST API: The frontend triggers a POST request to the FastAPI backend.

• ML Inference: The backend loads a pre-trained Random Forest Classifier (classifier.pkl) to categorize the risk.

• Probability Analysis: The model returns the final category along with a detailed breakdown of class probabilities.

• Deployment: The entire environment is containerized with Docker and hosted on AWS EC2.

🛠️ Tech Stack

• Machine Learning: Scikit-Learn (Random Forest)

• Backend API: FastAPI (Uvicorn)

• Frontend UI: Streamlit

• DevOps: Docker

• Cloud: AWS (EC2 Ubuntu Instance)

📊 Live Prediction Example
As seen in the application interface, the model performs granular risk assessment:

->Input Feature	Sample Value
Age	30
• Weight	65.0 kg
• Height	1.70 m
• Annual Income	10.0 LPA
• Smoker	True
• Occupation	Retired

->Model Output:
• Predicted Category: Low
• Confidence Score: 0.47
• Class Probabilities: * Low: 0.47
• Medium: 0.45
• High: 0.08

🚀 Execution & Deployment Workflow


-> Clone the repository
• git clone https://github.com/StevenGerardMascarenhas/InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction.git
• cd InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction

-> Build and Run with Docker
• docker build -t insurpredict-ai .
• docker run -p 8501:8501 -p 8000:8000 insurpredict-ai

-> Docker Hub Workflow (Pushing)
• docker login
• docker tag insurpredict-ai:latest <your-username>/insurpredict-ai:latest
• docker push <your-username>/insurpredict-ai:latest

 AWS EC2 Production Deployment
Follow these steps to deploy on a clean Ubuntu t2.micro instance:

Step 1: AWS Account Setup 
Create an AWS account at aws.amazon.com. A debit/credit card is required for verification, but free tier usage incurs no cost.

Step 2: Launch EC2 Instance
Use the AWS Management Console to launch an EC2 instance with the following specs:
- Operating System: Ubuntu
- Instance Type: t2.micro (1GB RAM, free tier eligible)
- Security: Enable SSH (port 22) access from anywhere

Step 3. Key Pair Setup
Create or use an existing key pair (.pem file) to enable SSH access to the instance.

Step 4. Connect to EC2
Connect via AWS console’s in-browser terminal or using an SSH client with the key pair.

Step 5. 5. EC2 Preparation
• sudo apt update && sudo apt install docker.io -y
• sudo systemctl start docker
• sudo systemctl enable docker
# Grant permissions (Requires re-login to take effect)
• sudo usermod -aG docker $USER && exit

Step 6: Pull and Run Docker Image
(Pull the Docker image from Docker Hub and run the container, starting the UVicorn server on port 8000.)
• docker pull <your-username>/insurpredict-ai:latest
• docker run -d -p 8000:8000 -p 8501:8501 <your-username>/insurpredict-ai:latest

Step 7: Security Group Configuration Ensure your AWS Inbound Rules allow:

• Modify EC2 security group inbound rules to open port 8000 for TCP traffic from any IP address, allowing external access to the API.
Go to EC2 Dashboard > Instances > Select your instance.

• Click the Security tab and select the Security Group.

• Edit Inbound Rules and add a new rule:

• Type: Custom TCP

• Port Range: 8000

• Source: 0.0.0.0/0 (Anywhere)

Click Save rules.


Step 8: Access the Application
Once the container is running and the ports are open, the user can access the project via their web browser:

Copy the API URL that is the EC2 instance public IP address and paste it in the streamlit frontend code 
and run streamlit frontend.py


• streamlit run app.py

incase you want to check the API : write the following API URL below with your EC2 instance public IP address and correct port assigned:

• Backend (API Docs): http://<EC2-Public-IP>:8000/docs




👤 Author
Steven Gerard Mascarenhas 
https://www.linkedin.com/in/stevengerardmascarenhas/


