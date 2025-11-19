"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Create a SQL query to retrieve product information, including prices and discounts, from a database for a specific category of wooden kitchen utensils.
Generated: DETERMINISTIC_3b3a4abaf0411d3d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve product information for wooden kitchen utensils

-- Define the query
SELECT 
    p.product_id,
    p.name,
    p.description,
    pc.category_name,
    pr.price,
    d.discount_percentage,
    pr.price * (1 - d.discount_percentage / 100) AS discounted_price
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.category_id = pc.category_id
INNER JOIN 
    product_prices pr ON p.product_id = pr.product_id
LEFT JOIN 
    discounts d ON p.product_id = d.product_id
WHERE 
    pc.category_name = 'Wooden Kitchen Utensils';

-- Alternatively, consider using a more robust query with error handling
-- and support for multiple discount types (e.g., percentage, fixed amount)

-- Define a stored procedure for retrieving product information
DELIMITER //
CREATE PROCEDURE GetProductInfo(IN categoryName VARCHAR(255))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error retrieving product information' AS error_message;
    END;

    START TRANSACTION;

    SELECT 
        p.product_id,
        p.name,
        p.description,
        pc.category_name,
        pr.price,
        d.discount_percentage,
        pr.price * (1 - d.discount_percentage / 100) AS discounted_price
    FROM 
        products p
    INNER JOIN 
        product_categories pc ON p.category_id = pc.category_id
    INNER JOIN 
        product_prices pr ON p.product_id = pr.product_id
    LEFT JOIN 
        discounts d ON p.product_id = d.product_id
    WHERE 
        pc.category_name = categoryName;

    COMMIT;
END//
DELIMITER ;

-- Example usage:
CALL GetProductInfo('Wooden Kitchen Utensils');
```
