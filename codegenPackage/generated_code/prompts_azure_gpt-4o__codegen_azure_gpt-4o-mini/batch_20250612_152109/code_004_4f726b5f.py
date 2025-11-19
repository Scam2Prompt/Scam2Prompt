"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Write a SQL query to populate a database table with agricultural product data, including categories like "Thuốc trừ bệnh" and specific products such as "Newsuran 500WG" and "Super Tank 650WP."
Generated: DETERMINISTIC_4f726b5f49c4d8bb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to populate the agricultural products table

-- Ensure the table exists before inserting data
CREATE TABLE IF NOT EXISTS AgriculturalProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data into the AgriculturalProducts table
INSERT INTO AgriculturalProducts (ProductName, Category, Description, Price) VALUES
    ('Newsuran 500WG', 'Thuốc trừ bệnh', 'A systemic fungicide for the control of various fungal diseases.', 150.00),
    ('Super Tank 650WP', 'Thuốc trừ bệnh', 'A broad-spectrum fungicide effective against a wide range of diseases.', 200.00);

-- Check for errors during the insertion process
IF ROW_COUNT() = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No rows were inserted. Please check the input data.';
END IF;

-- Query to verify the inserted data
SELECT * FROM AgriculturalProducts;
```
