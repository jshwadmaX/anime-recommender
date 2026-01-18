# 🎌 Anime Recommendation System
<img width="799" height="300" alt="Screenshot (958)" src="https://github.com/user-attachments/assets/272159e7-a9b6-4aa8-9dbb-cb93d43a0291" />

A **content-based anime recommendation web application** that suggests similar anime based on user selection.  
Built using **machine learning**, **Flask**, and a clean **HTML/CSS frontend**, this project demonstrates practical application of similarity algorithms in real-world systems.

🔗 **Live Demo**: https://anime-recommender-mp2v.onrender.com/

---

## 📌 Overview

This Anime Recommendation System analyzes anime metadata such as **genres, description, tags, and ratings** to recommend anime that are most similar to the one selected by the user.

The recommendation logic is powered by **cosine similarity with a linear kernel**, ensuring fast and accurate results.

---

## ✨ Features

- 🎯 **Content-Based Recommendations**
- 🧠 **Machine Learning Similarity Model**
- ⚡ **Fast & Lightweight Backend**
- 🎨 **Modern UI with Video Background**
- 🌐 **Flask Web Application**
- ☁️ **Deployed on Render**

---

## 🧠 Recommendation Logic

- Text features are vectorized using **TF-IDF**
- Similarity is computed using **Cosine Similarity (Linear Kernel)**
- Top-N similar anime are returned as recommendations

This approach ensures recommendations are **relevant and explainable**, unlike black-box models.

---

## 🏗️ Tech Stack

### Backend
- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**

### Machine Learning
- TF-IDF Vectorization
- Cosine Similarity (Linear Kernel)

### Frontend
- **HTML**
- **CSS**
- **Jinja2 Templates**

### Deployment
- **Render**

---

anime-recommender/
│
├── static/ # CSS, images, background video
├── templates/ # HTML templates
│
├── app.py # Flask app (routes & integration)
├── model.py # Recommendation logic & ML model
├── cleaned_anime.csv # Preprocessed anime dataset
├── requirements.txt # Dependencies
├── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/jshwadmaX/anime-recommender.git
cd anime-recommender

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

📊 Dataset

Source: Anime metadata dataset (cleaned & preprocessed)

File: cleaned_anime.csv

Key Attributes:

Anime Name

Genres

Tags

Description

Rating

Episodes

Release Year

🧪 Model Details

Vectorization: TF-IDF

Similarity Metric: Cosine Similarity

Kernel: Linear

Type: Content-Based Filtering

This design avoids cold-start problems and does not require user history.

🛠️ Future Enhancements

🔍 Search auto-suggestions

❤️ User favorites & history

🤖 Hybrid recommendation (content + collaborative)

📱 Responsive mobile UI

🎥 Trailer integration
