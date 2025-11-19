"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Write a SQL query to track the effectiveness of vitrinismo strategies, such as weekly updates to store displays, by comparing sales data before and after implementing changes.
Generated: DETERMINISTIC_b79a105363f13efd
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to track effectiveness of vitrinismo strategies by comparing sales before and after display changes
WITH sales_data AS (
    SELECT 
        product_id,
        product_name,
        display_change_date,
        SUM(CASE WHEN sale_date < display_change_date THEN quantity_sold ELSE 0 END) AS pre_change_sales,
        SUM(CASE WHEN sale_date >= display_change_date THEN quantity_sold ELSE 0 END) AS post_change_sales,
        SUM(CASE WHEN sale_date < display_change_date THEN revenue ELSE 0 END) AS pre_change_revenue,
        SUM(CASE WHEN sale_date >= display_change_date THEN revenue ELSE 0 END) AS post_change_revenue,
        COUNT(DISTINCT CASE WHEN sale_date < display_change_date THEN sale_id ELSE NULL END) AS pre_change_transactions,
        COUNT(DISTINCT CASE WHEN sale_date >= display_change_date THEN sale_id ELSE NULL END) AS post_change_transactions
    FROM 
        sales s
    JOIN 
        products p ON s.product_id = p.id
    JOIN 
        display_changes dc ON p.display_group = dc.display_group
    WHERE 
        sale_date BETWEEN DATE_SUB(display_change_date, INTERVAL 30 DAY) 
                      AND DATE_ADD(display_change_date, INTERVAL 30 DAY)
    GROUP BY 
        product_id, product_name, display_change_date
)

SELECT 
    product_id,
    product_name,
    display_change_date,
    pre_change_sales,
    post_change_sales,
    post_change_sales - pre_change_sales AS sales_difference,
    ROUND((post_change_sales - pre_change_sales) / NULLIF(pre_change_sales, 0) * 100, 2) AS sales_change_percentage,
    pre_change_revenue,
    post_change_revenue,
    post_change_revenue - pre_change_revenue AS revenue_difference,
    ROUND((post_change_revenue - pre_change_revenue) / NULLIF(pre_change_revenue, 0) * 100, 2) AS revenue_change_percentage,
    pre_change_transactions,
    post_change_transactions,
    post_change_transactions - pre_change_transactions AS transaction_difference,
    ROUND((post_change_transactions - pre_change_transactions) / NULLIF(pre_change_transactions, 0) * 100, 2) AS transaction_change_percentage,
    CASE 
        WHEN post_change_sales > pre_change_sales THEN 'Positive Impact'
        WHEN post_change_sales < pre_change_sales THEN 'Negative Impact'
        ELSE 'No Impact'
    END AS impact_assessment
FROM 
    sales_data
ORDER BY 
    sales_change_percentage DESC;
```
