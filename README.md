# 🚀 InsurPredict AI: End-to-End Insurance Premium Category Prediction

InsurPredict AI is a production-grade Machine Learning application that categorizes health insurance risks. This project demonstrates a full-stack ML deployment involving a **FastAPI** backend, a **Streamlit** frontend, and containerization via **Docker** for deployment on **AWS EC2**.

---

## 🏗️ System Architecture

The application follows a decoupled architecture to ensure scalability and ease of maintenance.


![aws diagram (1)](https://github.com/user-attachments/assets/ffaf5359-6260-4f8f-953a-92ed434954dd)


### **Workflow:**
1. **Frontend:** Users interact with a **Streamlit** dashboard to input demographic and health data.
2. **Communication:** The frontend sends a POST request to the **FastAPI** backend.
3. **Inference:** FastAPI loads the **Random Forest Classifier** (`classifier.pkl`) and predicts the insurance category.
4. **Response:** The result is sent back as JSON and displayed instantly to the user.
5. **Infrastructure:** The entire stack is containerized with **Docker** and hosted on an **AWS EC2** instance.

---

## 🛠️ Tech Stack
- **Machine Learning:** Scikit-Learn (Random Forest)
- **Backend API:** FastAPI (Python)
- **Frontend UI:** Streamlit
- **DevOps:** Docker, Docker Compose
- **Cloud:** AWS (EC2, Ubuntu)

---

## 🚀 How to Run Locally

### **Using Docker (Recommended)**
1. Clone the repository:
   ```bash
   git clone [https://github.com/StevenGerardMascarenhas/InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction.git](https://github.com/StevenGerardMascarenhas/InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction.git)
   cd InsurPredict-AI-End-to-End-Insurance-Premium-Category-Prediction
