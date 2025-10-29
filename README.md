# 💧 Water Quality Prediction using Machine Learning

This project focuses on predicting the **potability of water** (whether it is safe for drinking) using **Machine Learning** classification algorithms such as **Logistic Regression** and **Support Vector Classifier (SVC)**. The goal is to use physicochemical parameters like pH, hardness, solids, and conductivity to predict water quality efficiently and accurately.

---

## 🧠 **Abstract**
Water quality is a critical environmental issue that affects human health. Traditional methods for determining water quality are often time-consuming and prone to human error.  
This project applies **Machine Learning techniques** to automate and improve the accuracy of water quality predictions using the **Water Potability dataset**.  
Algorithms such as **Logistic Regression** and **SVM (Support Vector Machine)** are implemented, compared, and evaluated for their accuracy and efficiency.

---

## 🎯 **Objectives**
- Predict whether a given water sample is potable or not.  
- Apply classification algorithms to analyze physicochemical properties of water.  
- Evaluate and compare performance metrics like **accuracy**, **precision**, and **recall**.

---

## 🧩 **Proposed Approach**
1. **Data Collection:**  
   Water potability dataset containing pH, hardness, solids, chloramines, sulfate, and conductivity values.

2. **Data Preprocessing:**  
   - Handling missing and null values  
   - Removing duplicates and outliers  
   - Normalizing features for uniform scaling  

3. **Model Development:**  
   - Split data into training and testing sets  
   - Train models using:
     - Logistic Regression  
     - Support Vector Classifier (SVC)  
   - Evaluate model accuracy and visualize results.

4. **Model Evaluation:**  
   - Confusion Matrix  
   - Accuracy Score  
   - Graphical analysis using heatmaps, boxplots, and scatter plots

---

## 🧪 **Technologies Used**
- **Python 3.x**
- **Jupyter Notebook**
- **NumPy, Pandas, Matplotlib, Seaborn**
- **Scikit-learn**
- **Anaconda Navigator**

---

## 📂 **Project Structure**
| File Name | Description |
|------------|-------------|
| `water_quality.ipynb` | Jupyter Notebook containing complete project code |
| `water_potability.csv` | Dataset used for model training |
| `model.pkl` | Saved trained model |
| `Internship report sushma.pdf` | Detailed project report |
| `water quality prediction.pptx` | Project presentation |
| `requirements.txt` | Python libraries used |
| `README.md` | Project overview |

---

## 📊 **Results**
- **Best Algorithm:** Support Vector Classifier (SVC)  
- **Accuracy Achieved:** ~85%  
- Visualized data distributions using **heatmaps**, **pairplots**, and **boxplots**.  
- Model effectively classifies water samples as **potable** or **non-potable**.

---

## ⚙️ **How to Run**
1. Clone this repository:
   ```bash
   git clone https://github.com/sushmapolireddy-tech/Water-Quality-Prediction-ML.git
