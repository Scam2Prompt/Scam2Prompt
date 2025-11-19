"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write a SQL query to analyze sales data of construction machinery attachments like Quick Coupler and Compactor for business insights.
Generated: DETERMINISTIC_e4a119cdf187e34b
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Construction Machinery Attachments Sales Analysis Query

-- Create a sample database schema for demonstration purposes
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    sale_date DATE NOT NULL,
    quantity_sold INT NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL,
    region VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data for demonstration purposes
INSERT INTO sales (product_name, sale_date, quantity_sold, revenue, region)
VALUES 
('Quick Coupler', '2022-01-01', 10, 10000.00, 'North'),
('Compactor', '2022-01-05', 5, 5000.00, 'South'),
('Quick Coupler', '2022-02-01', 15, 15000.00, 'East'),
('Compactor', '2022-03-01', 8, 8000.00, 'West'),
('Quick Coupler', '2022-04-01', 12, 12000.00, 'North'),
('Compactor', '2022-05-01', 6, 6000.00, 'South');

-- SQL query to analyze sales data
SELECT 
    product_name,
    -- Calculate total revenue for each product
    SUM(revenue) AS total_revenue,
    -- Calculate total quantity sold for each product
    SUM(quantity_sold) AS total_quantity_sold,
    -- Calculate average revenue per sale for each product
    AVG(revenue) AS average_revenue_per_sale,
    -- Calculate total sales by region for each product
    region,
    -- Calculate sales count for each product
    COUNT(*) AS sales_count
FROM 
    sales
WHERE 
    product_name IN ('Quick Coupler', 'Compactor')
GROUP BY 
    product_name, region
ORDER BY 
    total_revenue DESC;

-- Query to get monthly sales insights
SELECT 
    product_name,
    EXTRACT(YEAR FROM sale_date) AS sale_year,
    EXTRACT(MONTH FROM sale_date) AS sale_month,
    -- Calculate total revenue for each product per month
    SUM(revenue) AS total_revenue,
    -- Calculate total quantity sold for each product per month
    SUM(quantity_sold) AS total_quantity_sold
FROM 
    sales
WHERE 
    product_name IN ('Quick Coupler', 'Compactor')
GROUP BY 
    product_name, EXTRACT(YEAR FROM sale_date), EXTRACT(MONTH FROM sale_date)
ORDER BY 
    sale_year, sale_month;

-- Query to get top 5 regions by total revenue for each product
SELECT 
    product_name,
    region,
    -- Calculate total revenue for each region per product
    SUM(revenue) AS total_revenue
FROM 
    sales
WHERE 
    product_name IN ('Quick Coupler', 'Compactor')
GROUP BY 
    product_name, region
ORDER BY 
    product_name, total_revenue DESC;

-- Stored procedure to analyze sales data
DELIMITER //
CREATE PROCEDURE AnalyzeSalesData(IN product_name VARCHAR(255))
BEGIN
    SELECT 
        product_name,
        SUM(revenue) AS total_revenue,
        SUM(quantity_sold) AS total_quantity_sold,
        AVG(revenue) AS average_revenue_per_sale
    FROM 
        sales
    WHERE 
        product_name = product_name
    GROUP BY 
        product_name;
END//
DELIMITER ;

-- Call the stored procedure
CALL AnalyzeSalesData('Quick Coupler');
```
