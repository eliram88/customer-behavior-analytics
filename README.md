![cover](cover.png)

# 🧠 Customer Segmentation & Lifetime Value Prediction

🎯 Project goal: Analyzing customer behavior for an online retail store and predicting Customer Lifetime Value (CLV) to optimize marketing strategies.

Dataset: [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/dataset/352/online+retail)  
Result: https://cbanalytics.streamlit.app


## 🔧 Tools & Libraries

- Python (Pandas, Scikit-learn, Streamlit)
- Excel
- Power BI (interactive dashboard)
- GitHub for version control

## 📈 Project Workflow


1. Data cleaning & preparation (Online Retail dataset)
2. Building RFM model for customer segmentation
3. Clustering with KMeans and analyzing each segment
4. Predictive modeling for identifying churn customers
5. Designing dashboards with Power BI and an interactive app with Streamlit


## 🚀 Outputs

📂 Final RFM dataset → data/rfm_clusters.csv
📊 Interactive Dashboard → dashboard/dashboard.pbix
🌐 Streamlit App → app/app.py
📋 Analytical results & visualizations → Jupyter Notebook


## 🎯 Run the Streamlit App

```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```


### 🌐 Online App

[Streamlit Cloud Deployment](https://cbanalytics.streamlit.app/)



## 📁 Project Structure
```bash
customer-clustering-project/
│
├── 📁 data/
│   └── rfm_clusters.csv              #  Final dataset
│
├── 📁 notebook/
│   └── analysis_rfm.ipynb           # Data analysis & modeling (Jupyter Notebook)
│
├── 📁 app/
│   └── app.py                       # Streamlit app
│   └── requirements.txt             # Dependencies
│
├── 📁 dashboard/
│   └── dashboard.pbix               # Power BI dashboard
│   └── dashboard-screenshot.png     # Dashboard screenshot
│
├── 📄 README.md                     # Project documentation
```

## 🧑‍💻 Developer

This project was developed by a data analysis and machine learning enthusiast with the goal of:

- Building a professional portfolio project
- Practicing real-world analytics & modeling
- Gaining hands-on experience with interactive dashboards and app deployment


