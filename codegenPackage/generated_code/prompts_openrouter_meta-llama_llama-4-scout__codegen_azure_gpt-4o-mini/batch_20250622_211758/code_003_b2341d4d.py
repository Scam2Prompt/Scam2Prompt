"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Design a simple database schema to store information about wood products, including their applications, advantages, and treatment processes, similar to those described on the Trattar Madeiras website."
Generated: DETERMINISTIC_b2341d4da1332be3
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about wood products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS TreatmentProcesses;
DROP TABLE IF EXISTS Advantages;
DROP TABLE IF EXISTS Applications;
DROP TABLE IF EXISTS WoodProducts;

-- Table to store information about wood products
CREATE TABLE WoodProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each wood product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the wood product
    Description TEXT,                           -- Description of the wood product
    Species VARCHAR(50) NOT NULL,              -- Species of the wood used
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store applications of wood products
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each application
    ProductID INT NOT NULL,                        -- Foreign key referencing WoodProducts
    ApplicationDescription TEXT NOT NULL,          -- Description of the application
    FOREIGN KEY (ProductID) REFERENCES WoodProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store advantages of wood products
CREATE TABLE Advantages (
    AdvantageID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each advantage
    ProductID INT NOT NULL,                         -- Foreign key referencing WoodProducts
    AdvantageDescription TEXT NOT NULL,             -- Description of the advantage
    FOREIGN KEY (ProductID) REFERENCES WoodProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store treatment processes for wood products
CREATE TABLE TreatmentProcesses (
    TreatmentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each treatment process
    ProductID INT NOT NULL,                          -- Foreign key referencing WoodProducts
    TreatmentDescription TEXT NOT NULL,              -- Description of the treatment process
    FOREIGN KEY (ProductID) REFERENCES WoodProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion (optional)
INSERT INTO WoodProducts (ProductName, Description, Species) VALUES
('Oak', 'Strong and durable wood, ideal for furniture.', 'Quercus'),
('Pine', 'Lightweight wood, commonly used in construction.', 'Pinus');

INSERT INTO Applications (ProductID, ApplicationDescription) VALUES
(1, 'Used for making furniture and flooring.'),
(2, 'Commonly used in framing and paneling.');

INSERT INTO Advantages (ProductID, AdvantageDescription) VALUES
(1, 'Highly durable and resistant to wear.'),
(2, 'Cost-effective and easy to work with.');

INSERT INTO TreatmentProcesses (ProductID, TreatmentDescription) VALUES
(1, 'Kiln drying to reduce moisture content.'),
(2, 'Pressure treatment for enhanced durability.');
```
