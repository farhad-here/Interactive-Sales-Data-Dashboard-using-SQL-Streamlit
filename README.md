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

# 🖼️Image

![sq1](https://github.com/user-attachments/assets/3d26a78d-afc2-417a-84b5-a0ea4d88fdbb)
![sq2](https://github.com/user-attachments/assets/8c5f6642-0b08-4479-99e0-7f737579bc05)

![sq3](https://github.com/user-attachments/assets/b283de2a-5913-4ffe-8152-e67453c056ec)
![sq4](https://github.com/user-attachments/assets/f51f695b-fbbe-47a5-8590-80ce6e970160)
![sq5](https://github.com/user-attachments/assets/3d3e5cad-7c47-41be-9622-cae26cd61b9e)

![sq6](https://github.com/user-attachments/assets/8a7f211f-4343-4adf-ab38-2676fe4e3351)


# 📥 Dataset
I found the dataset from kaggle and this is just for educational stuff.

https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

[Sample - Superstore.csv
A common dataset used for sales analytics, containing customer, product, order, and profit information.](https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls)




Made with ❤️ by Farhad Ghaherdoost
