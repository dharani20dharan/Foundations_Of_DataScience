# Client Subscription Prediction

This project predicts whether a client will subscribe to a term deposit based on their demographic and campaign-related data. It uses supervised machine learning algorithms such as K-Nearest Neighbors (KNN) and Logistic Regression to classify client responses.

##  Project Overview
The goal is to build and compare different classification models to identify which performs best on the client subscription dataset. The dataset includes features such as age, job, education, marital status, and past campaign outcomes.

##  Technologies Used
- Python
- NumPy, Pandas
- Scikit-learn
- Matplotlib, Seaborn

##  Models Implemented
- **K-Nearest Neighbors (KNN)**  
- **Logistic Regression**

##  Results
| Model | Accuracy |
|--------|-----------|
| KNN | **92.51%** |
| Logistic Regression | 88.52% |

##  Key Steps
1. Data preprocessing and encoding categorical variables.  
2. Feature scaling for model optimization.  
3. Training multiple ML models.  
4. Evaluating performance metrics and comparing accuracies.

##  File Description
- `client_subscription.ipynb` — Main notebook containing all analysis, training, and evaluation.

## 🏁 Conclusion
KNN outperformed Logistic Regression, achieving an accuracy of **92.51%**. The model demonstrates effective classification capability for predicting client subscriptions.
