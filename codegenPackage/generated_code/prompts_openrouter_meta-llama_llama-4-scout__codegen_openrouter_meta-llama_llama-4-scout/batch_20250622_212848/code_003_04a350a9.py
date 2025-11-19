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
-- Create a database for beauty products
CREATE DATABASE BeautyProducts;

-- Use the BeautyProducts database
USE BeautyProducts;

-- Create a table for beauty products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductType ENUM('nail_enamel', 'lipstick', 'foundation', 'mascara') NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create a table for nail enamels with specific details
CREATE TABLE NailEnamels (
    NailEnamelID INT AUTO_INCREMENT,
    ProductID INT,
    ShadeName VARCHAR(255) NOT NULL,
    FinishType ENUM('matte', 'glossy', 'metallic') NOT NULL,
    Longevity VARCHAR(50) NOT NULL,
    PRIMARY KEY (NailEnamelID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Insert sample data into Products table
INSERT INTO Products (ProductName, ProductType, Price, Description)
VALUES 
("Up to 7 Days Shine & Color Nail Enamel", 'nail_enamel', 12.99, "Long-lasting nail enamel with vibrant colors"),
("Luxe Lipstick", 'lipstick', 19.99, "Moisturizing lipstick with rich pigmentation"),
("Flawless Foundation", 'foundation', 29.99, "Oil-control foundation with SPF 30"),
("Volume Mascara", 'mascara', 14.99, "Lengthening and volumizing mascara");

-- Insert sample data into NailEnamels table
INSERT INTO NailEnamels (ProductID, ShadeName, FinishType, Longevity)
VALUES 
(1, "Ruby Red", 'glossy', "Up to 7 days"),
(1, "Midnight Blue", 'matte', "Up to 10 days");

-- Create a view to retrieve nail enamel information with product details
CREATE VIEW NailEnamelDetails AS
SELECT 
    p.ProductName,
    p.Price,
    ne.ShadeName,
    ne.FinishType,
    ne.Longevity
FROM 
    Products p
JOIN 
    NailEnamels ne ON p.ProductID = ne.ProductID;

-- Retrieve nail enamel details
SELECT * FROM NailEnamelDetails;
```
