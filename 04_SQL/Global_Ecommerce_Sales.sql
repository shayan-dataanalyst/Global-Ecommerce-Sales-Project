USE Global_Ecommerce_Sales;

SELECT DATABASE();
SHOW TABLES;
DESCRIBE ecommerce_sales;

-- 1: Basic + KPI Analysis
SELECT * FROM ecommerce_sales;

SELECT COUNT(*) AS Total_Rows
FROM ecommerce_sales;

-- Finding Total Customers
SELECT COUNT(DISTINCT Customer_Name) AS Total_Customers
FROM ecommerce_sales;

-- Finding Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity_Sold
FROM ecommerce_sales;

-- Finding Total Sales
SELECT SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales;

-- Finding Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM ecommerce_sales;

-- Finding Average Order Value
SELECT 
    ROUND(SUM(Total_Sales) / COUNT(DISTINCT Order_ID), 2)
    AS Average_Order_Value
FROM ecommerce_sales;

-- Finding Profit Margin
SELECT 
    ROUND(
        (SUM(Profit) / SUM(Total_Sales)) * 100,
        2
    ) AS Profit_Margin_Percentage
FROM ecommerce_sales;

-- Finding Average Discount
SELECT 
    ROUND(AVG(Discount_Percent), 2)
    AS Average_Discount
FROM ecommerce_sales;

-- 2: Business Analysis
-- Finding Sales by Region
SELECT 
    Region,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Finding Profit by Region
SELECT 
    Region,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Finding Sales by Product Category
SELECT 
    Product_Category,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;

-- Finding Profit by Product Category
SELECT 
    Product_Category,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Profit DESC;

-- Finding Sales by Customer Segment
SELECT 
    Customer_Segment,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Segment
ORDER BY Total_Sales DESC;

-- Finding Sales by Payment Method
SELECT 
    Payment_Method,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;

-- 3: Top Products & Customers
-- Finding Top 10 Products by Sales
SELECT 
    Product_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Finding Top 10 Products by Profit
SELECT 
    Product_Name,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;

-- Finding Top 10 Products by Quantity
SELECT 
    Product_Name,
    SUM(Quantity) AS Total_Quantity
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Quantity DESC
LIMIT 10;

-- Finding Top 10 Customers by Sales
SELECT 
    Customer_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Finding Top Customers by Number of Orders
SELECT 
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_sales
GROUP BY Customer_Name
ORDER BY Total_Orders DESC
LIMIT 10;

-- 4: Country Analysis
-- Finding Top 10 Countries by Sales
SELECT 
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 10;

-- Finding Top 10 Countries by Profit
SELECT 
    Country,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Profit DESC
LIMIT 10;

-- 5: Monthly Trend
-- Finding Monthly Sales
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;

-- Finding Monthly Profit
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Month,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Month;

-- 6: Discount Analysis
-- Finding Average Profit by Discount
SELECT 
    Discount_Percent,
    ROUND(AVG(Profit), 2) AS Average_Profit
FROM ecommerce_sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;

-- Finding Sales Before Discount
SELECT 
    ROUND(
        SUM(Total_Sales / (1 - Discount_Percent / 100)),
        2
    ) AS Sales_Before_Discount
FROM ecommerce_sales;

-- 7: Important Business Questions
-- Finding Best Region
SELECT 
    Region,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;

-- Finding Best Category
SELECT 
    Product_Category,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC
LIMIT 1;

-- Finding Most Profitable Category
SELECT 
    Product_Category,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Profit DESC
LIMIT 1;

-- Finding Best Customer Segment
SELECT 
    Customer_Segment,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Segment
ORDER BY Total_Sales DESC
LIMIT 1;

-- Finding Best Payment Method
SELECT 
    Payment_Method,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC
LIMIT 1;
