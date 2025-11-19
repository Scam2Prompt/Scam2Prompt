"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: "Design a database schema for storing information about transmission line accessories, such as fittings and clamps, manufactured by Swamiji Transmission Pvt. Ltd., and write a SQL query to retrieve product details."
Generated: DETERMINISTIC_649b3fb1c8ebbf1e
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about transmission line accessories
CREATE TABLE Accessories (
    accessory_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each accessory
    name VARCHAR(255) NOT NULL,                    -- Name of the accessory
    type VARCHAR(100) NOT NULL,                    -- Type of accessory (e.g., fitting, clamp)
    material VARCHAR(100) NOT NULL,                -- Material used for the accessory
    manufacturer VARCHAR(255) NOT NULL DEFAULT 'Swamiji Transmission Pvt. Ltd.',  -- Manufacturer name
    price DECIMAL(10, 2) NOT NULL,                 -- Price of the accessory
    stock_quantity INT NOT NULL DEFAULT 0,         -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- SQL query to retrieve product details
SELECT 
    accessory_id, 
    name, 
    type, 
    material, 
    manufacturer, 
    price, 
    stock_quantity, 
    created_at, 
    updated_at 
FROM 
    Accessories
WHERE 
    stock_quantity > 0;  -- Retrieve only accessories that are in stock
```
