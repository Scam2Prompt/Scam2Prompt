"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Create a SQL query to manage inventory levels for pet supplies, including products like "Tapete Higiênico Premium Chalesco", with varying quantities and prices.
Generated: DETERMINISTIC_f89e2eb32ceb38a4
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory levels for pet supplies

-- Create a table to store product information
CREATE TABLE IF NOT EXISTS Inventory (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Quantity INT NOT NULL DEFAULT 0,            -- Quantity of the product in stock
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert a new product into the inventory
INSERT INTO Inventory (ProductName, Quantity, Price)
VALUES ('Tapete Higiênico Premium Chalesco', 100, 29.99)
ON DUPLICATE KEY UPDATE 
    Quantity = Quantity + VALUES(Quantity),  -- Update quantity if product already exists
    Price = VALUES(Price);                    -- Update price if product already exists

-- Function to update the inventory for a specific product
DELIMITER //

CREATE PROCEDURE UpdateInventory(
    IN p_ProductID INT,
    IN p_Quantity INT,
    IN p_Price DECIMAL(10, 2)
)
BEGIN
    -- Check if the product exists
    IF EXISTS (SELECT 1 FROM Inventory WHERE ProductID = p_ProductID) THEN
        -- Update the product's quantity and price
        UPDATE Inventory
        SET Quantity = Quantity + p_Quantity,  -- Adjust quantity
            Price = p_Price                     -- Update price
        WHERE ProductID = p_ProductID;
    ELSE
        -- Raise an error if the product does not exist
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found in inventory';
    END IF;
END //

DELIMITER ;

-- Example of calling the UpdateInventory procedure
CALL UpdateInventory(1, 50, 30.99);  -- Update product with ID 1, adding 50 units and changing price to 30.99

-- Query to retrieve current inventory levels
SELECT * FROM Inventory;

-- Query to delete a product from the inventory
DELETE FROM Inventory WHERE ProductID = 1;  -- Replace 1 with the actual ProductID to delete
```
