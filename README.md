
This final README.md is tailored specifically to the frontend interface shown in your images. It highlights the full input field set (including Occupation, City, and Smoker Status) and the exact classification output from your model.

🚀 InsurPredict AI: End-to-End Insurance Premium Category Prediction
InsurPredict AI is a production-grade Machine Learning application that categorizes health insurance risks into premium tiers. This project demonstrates a full-stack ML deployment featuring a FastAPI backend, a Streamlit frontend, and containerization via Docker for cloud deployment on AWS EC2.

🏗️ System Architecture
The application follows a decoupled architecture where the frontend and backend communicate via RESTful API requests.

The Workflow:
User Input: Users enter demographic and health details (Age, Weight, Height, Income, Smoker Status, City, and Occupation) through the Streamlit UI.

REST API: The frontend triggers a POST request to the FastAPI backend.

ML Inference: The backend loads a pre-trained Random Forest Classifier (classifier.pkl) to categorize the risk.

Probability Analysis: The model returns the final category along with a detailed breakdown of class probabilities.

Deployment: The entire environment is containerized with Docker and hosted on AWS EC2.

🛠️ Tech Stack
Machine Learning: Scikit-Learn (Random Forest)

Backend API: FastAPI (Uvicorn)

Frontend UI: Streamlit

DevOps: Docker

Cloud: AWS (EC2 Ubuntu Instance)

📊 Live Prediction Example
As seen in the application interface, the model performs granular risk assessment:

Input Feature	Sample Value
Age	30
Weight	65.0 kg
Height	1.70 m
Annual Income	10.0 LPA
Smoker	True
Occupation	Retired
Model Output:

Predicted Category: Low

Confidence Score: 0.47

Class Probabilities: * Low: 0.47

Medium: 0.45

High: 0.08

🚀 How to Run Locally
1. Clone the repository
Bash
git clone https://github.com/StevenGerardMascarenhas/InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction.git
cd InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction
2. Build and Run with Docker
Bash
# Build the Docker image
docker build -t insurpredict-ai .

# Run the container
docker run -p 8501:8501 -p 8000:8000 insurpredict-ai
Access the Frontend at http://localhost:8501 and API Docs at http://localhost:8000/docs

👤 Author
Steven Gerard Mascarenhas LinkedIn | GitHub

Final Deployment Tip:
Since your screenshots show specific occupation categories like "retired", "private_job", and "business_owner", ensure your requirements.txt includes the exact versions of scikit-learn and pandas you used during training to avoid any "Inconsistent Version" errors during the Docker build!
