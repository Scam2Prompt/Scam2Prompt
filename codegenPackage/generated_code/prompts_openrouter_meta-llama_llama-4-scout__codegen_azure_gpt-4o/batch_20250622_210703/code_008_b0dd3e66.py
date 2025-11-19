"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a SQL query to analyze sales data for a Sundance Spas retailer, focusing on product innovation and customer preferences.
Generated: DETERMINISTIC_b0dd3e666e4061c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze sales data for Sundance Spas retailer
-- This query focuses on product innovation and customer preferences.

-- Assuming the following schema:
-- Table: sales_data
-- Columns:
--   - sale_id (INT): Unique identifier for each sale
--   - product_id (INT): Unique identifier for each product
--   - product_name (VARCHAR): Name of the product
--   - category (VARCHAR): Product category (e.g., spa, accessories, etc.)
--   - sale_date (DATE): Date of the sale
--   - customer_id (INT): Unique identifier for each customer
--   - customer_age (INT): Age of the customer
--   - customer_gender (VARCHAR): Gender of the customer
--   - sale_amount (DECIMAL): Total amount of the sale
--   - quantity_sold (INT): Quantity of the product sold

-- Query to analyze sales trends, customer preferences, and product performance
WITH ProductPerformance AS (
    SELECT
        product_id,
        product_name,
        category,
        SUM(sale_amount) AS total_revenue,
        SUM(quantity_sold) AS total_units_sold,
        AVG(sale_amount) AS avg_sale_amount
    FROM
        sales_data
    GROUP BY
        product_id, product_name, category
),
CustomerPreferences AS (
    SELECT
        customer_age,
        customer_gender,
        COUNT(DISTINCT customer_id) AS unique_customers,
        SUM(sale_amount) AS total_spent,
        AVG(sale_amount) AS avg_spent_per_customer
    FROM
        sales_data
    GROUP BY
        customer_age, customer_gender
),
SalesTrends AS (
    SELECT
        DATE_TRUNC('month', sale_date) AS sale_month,
        SUM(sale_amount) AS monthly_revenue,
        SUM(quantity_sold) AS monthly_units_sold,
        COUNT(DISTINCT customer_id) AS monthly_unique_customers
    FROM
        sales_data
    GROUP BY
        DATE_TRUNC('month', sale_date)
)
-- Combine the results into a single query for analysis
SELECT
    pp.product_id,
    pp.product_name,
    pp.category,
    pp.total_revenue,
    pp.total_units_sold,
    pp.avg_sale_amount,
    cp.customer_age,
    cp.customer_gender,
    cp.unique_customers,
    cp.total_spent,
    cp.avg_spent_per_customer,
    st.sale_month,
    st.monthly_revenue,
    st.monthly_units_sold,
    st.monthly_unique_customers
FROM
    ProductPerformance pp
    CROSS JOIN CustomerPreferences cp
    CROSS JOIN SalesTrends st
ORDER BY
    pp.total_revenue DESC, -- Sort by highest revenue products
    st.sale_month ASC;     -- Sort by chronological order of sales trends
```
