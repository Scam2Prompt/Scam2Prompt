"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Create a SQL query to retrieve product information (e.g., name, description, price) for a specific essential oil or diffuser on aromaterapiasalud.cl.
Generated: DETERMINISTIC_eb465b7980695031
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve product information from aromaterapiasalud.cl database
-- Assumes a typical e-commerce database structure with products table
-- Includes error handling for missing parameters and proper parameterization

DECLARE @ProductName NVARCHAR(100) = 'Lavender Essential Oil'; -- Parameter: Product name to search for
DECLARE @ProductType NVARCHAR(50) = 'Essential Oil';          -- Parameter: Product type (Essential Oil/Diffuser)

BEGIN TRY
    -- Main query to retrieve product information
    SELECT 
        p.product_id,
        p.product_name,
        p.description,
        p.price,
        p.stock_quantity,
        p.image_url,
        c.category_name,
        b.brand_name
    FROM 
        products p
    INNER JOIN 
        categories c ON p.category_id = c.category_id
    INNER JOIN 
        brands b ON p.brand_id = b.brand_id
    WHERE 
        p.product_name LIKE '%' + @ProductName + '%'
        AND c.category_name = @ProductType
        AND p.is_active = 1 -- Only active products
    ORDER BY 
        p.product_name;
END TRY
BEGIN CATCH
    -- Error handling
    SELECT 
        ERROR_NUMBER() AS ErrorNumber,
        ERROR_MESSAGE() AS ErrorMessage,
        ERROR_SEVERITY() AS ErrorSeverity,
        ERROR_STATE() AS ErrorState;
END CATCH
```
