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
-- Retrieve product information for a specific essential oil or diffuser

-- Define the database and table structure
-- For this example, let's assume we have a 'products' table with the following structure:
-- CREATE TABLE products (
--     id INT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     description TEXT,
--     price DECIMAL(10, 2) NOT NULL,
--     product_type ENUM('essential_oil', 'diffuser') NOT NULL,
--     slug VARCHAR(255) UNIQUE NOT NULL
-- );

-- SQL query to retrieve product information
SELECT 
    p.id,
    p.name,
    p.description,
    p.price
FROM 
    products p
WHERE 
    p.slug = ?;  -- Replace '?' with the actual product slug

-- To prevent SQL injection, use prepared statements
-- Example using PDO (PHP Data Objects)
-- $stmt = $pdo->prepare("SELECT * FROM products WHERE slug = :slug");
-- $stmt->bindParam(':slug', $slug);
-- $stmt->execute();
-- $product_info = $stmt->fetch();

-- Error handling
-- Check if product is found
-- if (!$product_info) {
--     throw new Exception("Product not found");
-- }

-- Example usage
-- $slug = 'lavender-essential-oil';
-- try {
--     $stmt = $pdo->prepare("SELECT * FROM products WHERE slug = :slug");
--     $stmt->bindParam(':slug', $slug);
--     $stmt->execute();
--     $product_info = $stmt->fetch();
--     print_r($product_info);
-- } catch (Exception $e) {
--     echo "Error: " . $e->getMessage();
-- }
```
