"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Design a database schema to store information about different types of acrylic yarns, such as Grey Yarns, Dyed Yarns, and Milange Yarns."
Generated: DETERMINISTIC_5d10528d529c61cb
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for yarn information
CREATE DATABASE YarnDatabase;

-- Use the YarnDatabase
USE YarnDatabase;

-- Create a table for yarn types
CREATE TABLE YarnTypes (
    YarnTypeID INT AUTO_INCREMENT,
    YarnTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (YarnTypeID)
);

-- Create a table for yarn colors
CREATE TABLE YarnColors (
    ColorID INT AUTO_INCREMENT,
    ColorName VARCHAR(255) NOT NULL,
    HexCode VARCHAR(7),
    PRIMARY KEY (ColorID)
);

-- Create a table for yarn materials
CREATE TABLE YarnMaterials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(255) NOT NULL,
    PRIMARY KEY (MaterialID)
);

-- Create a table for yarns
CREATE TABLE Yarns (
    YarnID INT AUTO_INCREMENT,
    YarnTypeID INT NOT NULL,
    MaterialID INT NOT NULL,
    Weight DECIMAL(5,2) NOT NULL,
    FiberContent DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (YarnID),
    FOREIGN KEY (YarnTypeID) REFERENCES YarnTypes(YarnTypeID),
    FOREIGN KEY (MaterialID) REFERENCES YarnMaterials(MaterialID)
);

-- Create a table for yarn color variations
CREATE TABLE YarnColorVariations (
    YarnID INT NOT NULL,
    ColorID INT NOT NULL,
    PRIMARY KEY (YarnID, ColorID),
    FOREIGN KEY (YarnID) REFERENCES Yarns(YarnID),
    FOREIGN KEY (ColorID) REFERENCES YarnColors(ColorID)
);

-- Create a table for specific yarn products
CREATE TABLE YarnProducts (
    ProductID INT AUTO_INCREMENT,
    YarnID INT NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    StockQuantity INT NOT NULL,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (YarnID) REFERENCES Yarns(YarnID)
);

-- Insert some sample data
INSERT INTO YarnTypes (YarnTypeName, Description)
VALUES 
('Grey Yarns', 'Yarns with grey color'),
('Dyed Yarns', 'Yarns that are dyed'),
('Milange Yarns', 'Yarns with mixed colors');

INSERT INTO YarnColors (ColorName, HexCode)
VALUES 
('Grey', '#808080'),
('Blue', '#0000FF'),
('Red', '#FF0000');

INSERT INTO YarnMaterials (MaterialName)
VALUES 
('Acrylic'),
('Cotton'),
('Wool');

INSERT INTO Yarns (YarnTypeID, MaterialID, Weight, FiberContent)
VALUES 
(1, 1, 50.00, 100.00),
(2, 1, 100.00, 50.00),
(3, 1, 75.00, 75.00);

INSERT INTO YarnColorVariations (YarnID, ColorID)
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO YarnProducts (YarnID, ProductName, Price, StockQuantity)
VALUES 
(1, 'Grey Acrylic Yarn', 5.99, 100),
(2, 'Blue Dyed Yarn', 7.99, 50),
(3, 'Milange Acrylic Yarn', 9.99, 75);
```
