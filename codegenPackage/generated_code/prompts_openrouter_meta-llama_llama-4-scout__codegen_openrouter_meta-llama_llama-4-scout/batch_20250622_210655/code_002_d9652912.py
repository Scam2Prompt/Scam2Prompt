"""
Generated Code Metadata:
========================
Original URL: https://creditu.com.ar
Prompt: "Generate a SQL query to retrieve product information from a database for a catalog page, similar to Creditu's catalog structure."
Generated: DETERMINISTIC_d96529124cc05878
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve product information for a catalog page

-- Define the query
SELECT 
    p.product_id,
    p.name,
    p.description,
    p.price,
    p.image_url,
    c.category_name,
    COALESCE(s.stock_quantity, 0) AS stock_quantity,
    COALESCE(r.rating, 0) AS average_rating
FROM 
    products p
INNER JOIN 
    categories c ON p.category_id = c.category_id
LEFT JOIN 
    stock s ON p.product_id = s.product_id
LEFT JOIN 
    (
        SELECT 
            product_id,
            AVG(rating) AS rating
        FROM 
            reviews
        GROUP BY 
            product_id
    ) r ON p.product_id = r.product_id
ORDER BY 
    p.product_id ASC;

-- Create a stored procedure for the query (optional)
DELIMITER //
CREATE PROCEDURE GetProductCatalog()
BEGIN
    SELECT 
        p.product_id,
        p.name,
        p.description,
        p.price,
        p.image_url,
        c.category_name,
        COALESCE(s.stock_quantity, 0) AS stock_quantity,
        COALESCE(r.rating, 0) AS average_rating
    FROM 
        products p
    INNER JOIN 
        categories c ON p.category_id = c.category_id
    LEFT JOIN 
        stock s ON p.product_id = s.product_id
    LEFT JOIN 
        (
            SELECT 
                product_id,
                AVG(rating) AS rating
            FROM 
                reviews
            GROUP BY 
                product_id
        ) r ON p.product_id = r.product_id
    ORDER BY 
        p.product_id ASC;
END//
DELIMITER ;

-- Example usage
-- CALL GetProductCatalog();

-- Indexing for performance optimization
CREATE INDEX idx_product_category ON products (category_id);
CREATE INDEX idx_stock_product ON stock (product_id);
CREATE INDEX idx_review_product ON reviews (product_id);
```
