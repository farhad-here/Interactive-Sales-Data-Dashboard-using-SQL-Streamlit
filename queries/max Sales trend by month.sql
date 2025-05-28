-- SALES TREND BY MONTH (highest month only)
WITH monthly_sales AS (
    SELECT 
        Month AS Month_total_sales,
        SUM(Sales) AS Total_Sales_trend_by_month
    FROM sales
    GROUP BY Month
)
SELECT *
FROM monthly_sales
WHERE Total_Sales_trend_by_month = (
    SELECT MAX(Total_Sales_trend_by_month) FROM monthly_sales
)
ORDER BY Month_total_sales;
