import streamlit as st
import pandas as pd

# خواندن داده
df = pd.read_csv('rfm_clusters.csv')

st.title("📊 داشبورد تحلیلی مشتریان")

# انتخاب Segment
segment = st.selectbox("یک Segment انتخاب کن:", options=df['Segment'].unique())

# فیلتر داده بر اساس Segment
filtered = df[df['Segment'] == segment]

# نمایش داده‌ها
st.subheader("📋 لیست مشتریان در این Segment:")
st.dataframe(filtered[['CustomerID', 'Recency', 'Frequency', 'Monetary']])

# آمار کلیدی
st.subheader("📈 آمار خلاصه:")
st.metric("تعداد مشتری", len(filtered))
st.metric("میانگین Monetary", round(filtered['Monetary'].mean(), 2))
