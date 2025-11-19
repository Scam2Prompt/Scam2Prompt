"""
Generated Code Metadata:
========================
Original URL: https://duchessgarden.sn
Prompt: Design a simple database schema to store information about beauty products, including nail enamels with specific names like "Up to 7 Days Shine & Color Nail Enamel" and their corresponding prices.
Generated: DETERMINISTIC_04a350a903696a40
Batch ID: 20250622_212848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about beauty products, including nail enamels

-- Create a table to store beauty products
CREATE TABLE BeautyProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    ProductType VARCHAR(100) NOT NULL,        -- Type of the product (e.g., Nail Enamel, Lipstick, etc.)
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert sample data for nail enamels
INSERT INTO BeautyProducts (ProductName, ProductType, Price)
VALUES 
    ('Up to 7 Days Shine & Color Nail Enamel', 'Nail Enamel', 9.99),
    ('Glossy Finish Nail Enamel', 'Nail Enamel', 7.49),
    ('Matte Finish Nail Enamel', 'Nail Enamel', 8.99);

-- Query to retrieve all nail enamels
SELECT * FROM BeautyProducts
WHERE ProductType = 'Nail Enamel';

-- Error handling: Ensure proper constraints
-- Example: Prevent negative prices
ALTER TABLE BeautyProducts
ADD CONSTRAINT chk_price_positive CHECK (Price >= 0);
```
