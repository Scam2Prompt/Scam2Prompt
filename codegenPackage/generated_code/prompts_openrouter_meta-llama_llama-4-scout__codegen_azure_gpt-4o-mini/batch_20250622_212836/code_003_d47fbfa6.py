"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Create a SQL query to manage inventory for a store selling motores diesel, rocadeiras a gasolina, and other equipment."
Generated: DETERMINISTIC_d47fbfa63ac02937
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory for a store selling diesel motors, gasoline brush cutters, and other equipment

-- Create a table to store inventory items
CREATE TABLE Inventory (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each item
    ItemName VARCHAR(255) NOT NULL,         -- Name of the item
    ItemType ENUM('Diesel Motor', 'Gasoline Brush Cutter', 'Other Equipment') NOT NULL,  -- Type of the item
    Quantity INT NOT NULL DEFAULT 0,         -- Quantity of the item in stock
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Insert sample data into the Inventory table
INSERT INTO Inventory (ItemName, ItemType, Quantity, Price) VALUES
('Diesel Motor 1', 'Diesel Motor', 10, 1500.00),
('Gasoline Brush Cutter 1', 'Gasoline Brush Cutter', 5, 300.00),
('Other Equipment 1', 'Other Equipment', 20, 100.00);

-- Function to update the quantity of an item
DELIMITER //
CREATE PROCEDURE UpdateItemQuantity(
    IN p_ItemID INT,
    IN p_Quantity INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
        SELECT 'Error occurred while updating item quantity.' AS ErrorMessage;
    END;

    START TRANSACTION;

    -- Update the quantity of the specified item
    UPDATE Inventory
    SET Quantity = Quantity + p_Quantity
    WHERE ItemID = p_ItemID;

    COMMIT;
END //
DELIMITER ;

-- Function to retrieve the current inventory
CREATE PROCEDURE GetInventory()
BEGIN
    SELECT * FROM Inventory;
END;

-- Function to delete an item from the inventory
DELIMITER //
CREATE PROCEDURE DeleteItem(
    IN p_ItemID INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
        SELECT 'Error occurred while deleting item.' AS ErrorMessage;
    END;

    START TRANSACTION;

    -- Delete the specified item from the inventory
    DELETE FROM Inventory
    WHERE ItemID = p_ItemID;

    COMMIT;
END //
DELIMITER ;

-- Example usage of the procedures
-- CALL UpdateItemQuantity(1, 5);  -- Add 5 to the quantity of the item with ItemID 1
-- CALL GetInventory();              -- Retrieve the current inventory
-- CALL DeleteItem(2);               -- Delete the item with ItemID 2
```
