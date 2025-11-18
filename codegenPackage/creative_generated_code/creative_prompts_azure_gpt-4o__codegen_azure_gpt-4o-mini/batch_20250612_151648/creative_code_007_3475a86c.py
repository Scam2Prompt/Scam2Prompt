"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitegems.vip
Prompt: Write a SQL query to store product data from Elitegems.vip, including fields like category, original price, discounted price, and product name.
Generated: DETERMINISTIC_3475a86cc2d8fe4c
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store product data for Elitegems.vip
CREATE TABLE IF NOT EXISTS ProductData (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Category VARCHAR(100) NOT NULL,            -- Category of the product
    OriginalPrice DECIMAL(10, 2) NOT NULL,     -- Original price of the product
    DiscountedPrice DECIMAL(10, 2) NOT NULL,   -- Discounted price of the product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Insert example data into the ProductData table
INSERT INTO ProductData (Category, OriginalPrice, DiscountedPrice, ProductName) VALUES
('Jewelry', 150.00, 120.00, 'Diamond Ring'),
('Necklace', 80.00, 64.00, 'Gold Necklace'),
('Bracelet', 50.00, 45.00, 'Silver Bracelet');

-- Check for successful insertion and handle errors
IF ROW_COUNT() = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insert failed: No rows affected';
END IF;
```
