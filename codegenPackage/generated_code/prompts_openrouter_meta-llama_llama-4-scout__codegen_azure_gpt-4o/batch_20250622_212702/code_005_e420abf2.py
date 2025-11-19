"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Create a SQL query to retrieve a list of best-selling coffee products from a database, considering factors like product sales and customer reviews.
Generated: DETERMINISTIC_e420abf2f4505b47
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to retrieve a list of best-selling coffee products
-- This query assumes the existence of the following tables:
-- 1. `products`: Contains product details (id, name, category, etc.)
-- 2. `sales`: Contains sales data (id, product_id, quantity_sold, sale_date, etc.)
-- 3. `reviews`: Contains customer reviews (id, product_id, rating, review_date, etc.)

-- The query calculates the total sales and average customer rating for each coffee product
-- and ranks them based on total sales and average rating.

WITH ProductSales AS (
    -- Calculate total quantity sold for each product
    SELECT
        p.id AS product_id,
        p.name AS product_name,
        SUM(s.quantity_sold) AS total_quantity_sold
    FROM
        products p
    INNER JOIN
        sales s ON p.id = s.product_id
    WHERE
        p.category = 'Coffee' -- Filter for coffee products
    GROUP BY
        p.id, p.name
),
ProductRatings AS (
    -- Calculate average rating for each product
    SELECT
        r.product_id,
        AVG(r.rating) AS average_rating
    FROM
        reviews r
    GROUP BY
        r.product_id
),
RankedProducts AS (
    -- Combine sales and ratings data, and rank products
    SELECT
        ps.product_id,
        ps.product_name,
        ps.total_quantity_sold,
        COALESCE(pr.average_rating, 0) AS average_rating, -- Handle products with no reviews
        RANK() OVER (ORDER BY ps.total_quantity_sold DESC, pr.average_rating DESC) AS rank
    FROM
        ProductSales ps
    LEFT JOIN
        ProductRatings pr ON ps.product_id = pr.product_id
)
-- Final query to retrieve the best-selling coffee products
SELECT
    product_id,
    product_name,
    total_quantity_sold,
    average_rating,
    rank
FROM
    RankedProducts
WHERE
    rank <= 10 -- Retrieve the top 10 best-selling coffee products
ORDER BY
    rank;
```
