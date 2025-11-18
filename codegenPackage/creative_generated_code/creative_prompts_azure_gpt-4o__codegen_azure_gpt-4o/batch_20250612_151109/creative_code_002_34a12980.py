"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a database schema in SQL to store furniture product information from "moveisonlinepelotasbraz," including columns for product name, price range, category (e.g., "Sala," "Quarto"), and availability.
Generated: DETERMINISTIC_34a129806760b415
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing furniture product information
-- from "moveisonlinepelotasbraz"

-- Ensure the database exists before creating the table
CREATE DATABASE IF NOT EXISTS MoveisOnlinePelotasBraz;

-- Switch to the newly created database
USE MoveisOnlinePelotasBraz;

-- Create the table to store furniture product information
CREATE TABLE FurnitureProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the furniture product
    PriceRange VARCHAR(50) NOT NULL,          -- Price range (e.g., "Low", "Medium", "High")
    Category ENUM('Sala', 'Quarto', 'Cozinha', 'Banheiro', 'Outros') NOT NULL, -- Furniture category
    Availability BOOLEAN NOT NULL DEFAULT TRUE, -- Indicates whether the product is available (true/false)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Add an index to ProductName for faster searches by product name
CREATE INDEX idx_ProductName ON FurnitureProducts(ProductName);

-- Add an index to Category for faster searches by category
CREATE INDEX idx_Category ON FurnitureProducts(Category);

-- Add an index to Availability for faster filtering on availability status
CREATE INDEX idx_Availability ON FurnitureProducts(Availability);
```
