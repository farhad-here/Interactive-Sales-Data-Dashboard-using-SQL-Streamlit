# 🛍️ Interactive Sales Data Dashboard

This project demonstrates how to analyze and visualize Superstore sales data using SQL for data querying and Streamlit for building an interactive dashboard.

## 📊 Features

- 📌 Top 10 customers by total sales
- 📌 Average sales per category
- 📌 Most profitable products
- 📌 Total profit by region
- 📌 Monthly sales trends
- 📌 Maximum monthly sales
- 📌 Customers with more than 10 orders

## 🧰 Technologies Used

- **Python** (pandas, sqlite3, streamlit)
- **SQL** (SQLite dialect)
- **Streamlit** for interactive data visualization

## 🗂️ Project Structure
```
├── data/
│   └──   Sample - Superstore.csv
│
├── queries/
│ ├── Top 10 customers by total sales.sql
│ ├── Average sales per category.sql
│ ├── Most profitable products.sql
│ ├── Total profit by region.sql
│ ├── Sales trend by month.sql
│ ├── max Sales trend by month.sql
│ └── Customers who ordered more than 10 times.sql
│
├── sales_data.db
└── app.py
```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sales-dashboard.git
   cd sales-dashboard
   ```
2. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run
    ```cmd
    streamlit run app.py
    ```
    
# 📥 Dataset
Sample - Superstore.csv
A common dataset used for sales analytics, containing customer, product, order, and profit information.




Made with ❤️ by Farhad Ghaherdoost
