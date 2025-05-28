-- AVERAGE SALES PER CATEGORY
SELECT category, AVG(Sales) AS [Average sales per category]
FROM sales
-- PER CATEGORY
GROUP BY category;