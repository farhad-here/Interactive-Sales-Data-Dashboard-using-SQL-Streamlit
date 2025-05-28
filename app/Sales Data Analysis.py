#Library
import pandas as pd
import sqlite3
import streamlit as st
import os
#function for reading the query
def run_query(file_name):
       current_dir = os.path.dirname(os.path.abspath(__file__))

       file_path = os.path.join(current_dir, '..', 'queries', file_name)
       file_path = os.path.normpath(file_path)

       if not os.path.exists(file_path):
              raise FileNotFoundError(f"فایل پیدا نشد: {file_path}")
    
       with open(file_path, 'r', encoding='utf-8') as file:
              query = file.read()
       return pd.read_sql_query(query, conn)
# read dataset

df = pd.read_csv('../data/Sample - Superstore.csv',encoding='ISO-8859-1')
#connect to sqlite3
conn = sqlite3.connect('sales_data.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

#Top 10 customers by total sales
st.title('# Top 10 customers by total sales')
top_ten_customers_by_total_sales = run_query('../queries/Top 10 customers by total sales.sql')
st.dataframe(top_ten_customers_by_total_sales)
st.bar_chart(data=top_ten_customers_by_total_sales, x='Customer Name', y='Sales')
st.line_chart(data=top_ten_customers_by_total_sales, x='Customer Name', y='Sales')
st.markdown('---')

#Average sales per category
st.title('# Average sales per category')
average_sales_per_category = run_query('../queries/Average sales per category.sql')
st.dataframe(average_sales_per_category)
st.bar_chart(data=average_sales_per_category, x='Category', y='Average sales per category')
st.line_chart(data=average_sales_per_category, x='Category', y='Average sales per category')
st.markdown('---')

#Most profitable products

st.title('# Most profitable products')
most_profitable_products = run_query('../queries/Most profitable products.sql')
st.dataframe(most_profitable_products)
st.bar_chart(data=most_profitable_products,x='Product Name',y='Total_Profit')
st.line_chart(data=most_profitable_products,x='Product Name',y='Total_Profit')
st.markdown('---')

#Total profit by region
st.title('# Total profit by region')
total_profit_by_region=run_query('../queries/Total profit by region.sql')
st.dataframe(total_profit_by_region)
st.bar_chart(data=total_profit_by_region,x='Region',y='Total_Profit_By_Region')
st.line_chart(data=total_profit_by_region,x='Region',y='Total_Profit_By_Region')
st.markdown('---')
#Sales trend by month

st.title('# Sales trend by month')
sales_trend_by_month =run_query('../queries/Sales trend by month.sql')
st.dataframe(sales_trend_by_month)
st.bar_chart(data=sales_trend_by_month,x='Month_total_sales',y='Total_Sales_trend_by_month')
st.line_chart(data=sales_trend_by_month,x='Month_total_sales',y='Total_Sales_trend_by_month')
# max Sales trend by month
st.title('# Max Sales trend by month')
st.dataframe(run_query('../queries/max Sales trend by month.sql'))
st.markdown('---')
# Customers who ordered more than 10 times
st.title('# Customers who ordered more than 10 times')
customers_ordered_more_ten_times = run_query('../queries/Customers who ordered more than 10 times.sql')
st.dataframe(customers_ordered_more_ten_times)
st.bar_chart(data=customers_ordered_more_ten_times,x='Customer Name',y='order_times')
st.line_chart(data=customers_ordered_more_ten_times,x='Customer Name',y='order_times')
