SELECT 
    [Customer Name], 
    Country,
    City,
    [State],
    Category,
    COUNT([Order ID]) AS order_times
FROM 
    sales
GROUP BY 
    [Customer Name]
HAVING 
    [order_times] > 10
ORDER BY 
    order_times ASC;
