![cover](cover.png)

# Customer Segmentation & Lifetime Value Prediction 🧠

🎯 هدف پروژه: تحلیل رفتاری مشتریان یک فروشگاه آنلاین و پیش‌بینی ارزش طول عمر آن‌ها جهت بهینه‌سازی بازاریابی


دیتاست : https://archive.ics.uci.edu/dataset/352/online+retail

خروجی: https://cbanalytics.streamlit.app


## 🔧 ابزارهای استفاده‌شده

- Python (Pandas, Scikit-learn, Streamlit)
- Excel
- Power BI (داشبورد تعاملی)
- GitHub for version control

## 📈 مراحل پروژه

1. آماده‌سازی و پاک‌سازی داده‌ها (Online Retail dataset)
2. ساخت مدل RFM برای گروه‌بندی مشتریان
3. خوشه‌بندی با KMeans و تحلیل هر خوشه
4. ساخت مدل پیش‌بینی برای شناسایی مشتریان خاموش
5. طراحی داشبورد با Power BI و اپ تعاملی با Streamlit

## 🚀 خروجی‌ها

- فایل RFM نهایی: `data/rfm_clusters.csv` 
- 📊 داشبورد Power BI (`dashboard.pbix`)
- 🌐 اپ Streamlit (`app/app.py`)
- 📋 تحلیل عددی + نمودارها (Jupyter Notebook)

## 🎯 برای اجرای اپ Streamlit:

```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```

### 🌐 اجرای اپ آنلاین در Streamlit Cloud:
https://cbanalytics.streamlit.app/


## 📁 ساختار فایل‌ها
```bash
customer-clustering-project/
│
├── 📁 data/
│   └── rfm_clusters.csv              # دیتای نهایی
│
├── 📁 notebook/
│   └── analysis_rfm.ipynb           # تحلیل داده و مدل‌سازی (Jupyter Notebook)
│
├── 📁 app/
│   └── app.py                       # اپ Streamlit
│   └── requirements.txt             # لیست کتابخانه‌ها
│
├── 📁 dashboard/
│   └── dashboard.pbix               # فایل Power BI
│   └── dashboard-screenshot.png     # تصویر داشبورد نهایی
│
├── 📄 README.md                     # توضیح پروژه (همین فایل)
```

## 🧑‍💻 توسعه‌دهنده

این پروژه توسط یک علاقه‌مند به تحلیل داده و یادگیری ماشین طراحی و اجرا شده  
با هدف شرکت در موقعیت "کارآموز تحلیلگر داده / دیتا ساینتیست".

✨ هدف: توسعه نمونه کار قابل ارائه، تمرین تحلیل واقعی، یادگیری مدل‌سازی حرفه‌ای و تفسیر مدل
