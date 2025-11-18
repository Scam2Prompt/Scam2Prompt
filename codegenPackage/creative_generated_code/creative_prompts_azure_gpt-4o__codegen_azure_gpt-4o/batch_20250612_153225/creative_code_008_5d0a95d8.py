"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Generate SQL queries to manage inventory for Travis Scott merchandise, including updating stock levels for "Utopia Merch Hoodies" after a purchase.
Generated: DETERMINISTIC_5d0a95d8b64baa36
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create table for Travis Scott merchandise inventory
CREATE TABLE MerchandiseInventory (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the merchandise item
    StockLevel INT NOT NULL,                  -- Quantity of the item available in stock
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the merchandise item
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Insert initial stock levels for merchandise items
INSERT INTO MerchandiseInventory (ProductName, StockLevel, Price)
VALUES
('Utopia Merch Hoodie', 100, 79.99),  -- Example stock setup for hoodies
('Utopia Merch T-Shirt', 200, 39.99),
('Utopia Merch Cap', 150, 29.99);

-- Update stock levels after a purchase
-- Assume a user purchases 5 "Utopia Merch Hoodies"
DECLARE @PurchaseQuantity INT = 5; -- Number of hoodies purchased

-- Check if sufficient stock is available before updating
-- This ensures stock level is not reduced below 0
UPDATE MerchandiseInventory
SET StockLevel = StockLevel - @PurchaseQuantity
WHERE ProductName = 'Utopia Merch Hoodie'
  AND StockLevel >= @PurchaseQuantity;

-- Optional: Query to confirm the updated stock level
SELECT ProductName, StockLevel
FROM MerchandiseInventory
WHERE ProductName = 'Utopia Merch Hoodie';

-- Handle insufficient stock scenario
-- If the stock level is less than the purchase quantity, the above update will not execute.
-- You can handle this in your application layer or include additional SQL logic for error reporting.

-- Example: Check for low stock warning
SELECT ProductName, StockLevel
FROM MerchandiseInventory
WHERE StockLevel < 10; -- Notify admins if stock is below a specific threshold
```
