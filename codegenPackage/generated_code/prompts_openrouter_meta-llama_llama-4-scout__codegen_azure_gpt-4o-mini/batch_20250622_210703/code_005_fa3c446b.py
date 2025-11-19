"""
Generated Code Metadata:
========================
Original URL: https://dextranslogistics.com
Prompt: "Write a SQL query to manage inventory across multiple warehouses in India, considering the services offered by Dextrans Logistics."
Generated: DETERMINISTIC_fa3c446b16b2a718
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage inventory across multiple warehouses in India for Dextrans Logistics

-- Create a table to store warehouse information
CREATE TABLE Warehouses (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT,
    WarehouseName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Capacity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to manage inventory across warehouses
CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    WarehouseID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity >= 0),
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Function to add a new product to the inventory
DELIMITER //
CREATE PROCEDURE AddProductToInventory(
    IN p_WarehouseID INT,
    IN p_ProductID INT,
    IN p_Quantity INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
        SELECT 'Error occurred while adding product to inventory' AS ErrorMessage;
    END;

    START TRANSACTION;

    -- Check if the warehouse and product exist
    IF (SELECT COUNT(*) FROM Warehouses WHERE WarehouseID = p_WarehouseID) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Warehouse does not exist';
    END IF;

    IF (SELECT COUNT(*) FROM Products WHERE ProductID = p_ProductID) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
    END IF;

    -- Insert or update the inventory
    INSERT INTO Inventory (WarehouseID, ProductID, Quantity)
    VALUES (p_WarehouseID, p_ProductID, p_Quantity)
    ON DUPLICATE KEY UPDATE Quantity = Quantity + p_Quantity;

    COMMIT;
END //
DELIMITER ;

-- Function to retrieve inventory details
CREATE PROCEDURE GetInventoryDetails()
BEGIN
    SELECT 
        w.WarehouseName,
        p.ProductName,
        i.Quantity,
        i.LastUpdated
    FROM 
        Inventory i
    JOIN 
        Warehouses w ON i.WarehouseID = w.WarehouseID
    JOIN 
        Products p ON i.ProductID = p.ProductID
    ORDER BY 
        w.WarehouseName, p.ProductName;
END;

-- Function to update inventory quantity
DELIMITER //
CREATE PROCEDURE UpdateInventoryQuantity(
    IN p_InventoryID INT,
    IN p_NewQuantity INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
        SELECT 'Error occurred while updating inventory quantity' AS ErrorMessage;
    END;

    START TRANSACTION;

    -- Update the inventory quantity
    UPDATE Inventory
    SET Quantity = p_NewQuantity
    WHERE InventoryID = p_InventoryID;

    COMMIT;
END //
DELIMITER ;

-- Function to delete a product from inventory
DELIMITER //
CREATE PROCEDURE DeleteProductFromInventory(
    IN p_InventoryID INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
        SELECT 'Error occurred while deleting product from inventory' AS ErrorMessage;
    END;

    START TRANSACTION;

    -- Delete the inventory record
    DELETE FROM Inventory
    WHERE InventoryID = p_InventoryID;

    COMMIT;
END //
DELIMITER ;
```
