-- SALES TREND BY MONTH
SELECT 
       -- MONTH
       Month AS Month_total_sales,
       -- ALL THE SALARIES IN THE MONTH
       SUM(Sales) AS Total_Sales_trend_by_month
FROM sales
-- GROUP
GROUP BY Month_total_sales
-- SORT
ORDER BY Month_total_sales;