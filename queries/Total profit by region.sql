-- TOTAL PROFIT BY REGION
SELECT Region, SUM(Profit) AS Total_Profit_By_Region
FROM sales

GROUP BY Region
-- SORT FOR TOTAL PROFIT BY REGION
ORDER BY Total_Profit_By_Region DESC;