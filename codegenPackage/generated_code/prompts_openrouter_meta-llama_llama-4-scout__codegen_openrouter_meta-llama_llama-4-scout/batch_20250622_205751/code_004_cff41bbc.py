"""
Generated Code Metadata:
========================
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Develop a simple database schema to store information about gourmet food products, including Foie Gras, with details such as origin, price, and certification (e.g., IGP Périgord).
Generated: DETERMINISTIC_cff41bbce2ec100b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for gourmet food products

CREATE DATABASE GourmetFoodDB;

USE GourmetFoodDB;

-- Create a table for food products
CREATE TABLE FoodProducts (
    ProductID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Origin VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Certification VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create a table for certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CertificationID)
);

-- Create a many-to-many relationship table for food products and certifications
CREATE TABLE ProductCertifications (
    ProductID INT NOT NULL,
    CertificationID INT NOT NULL,
    PRIMARY KEY (ProductID, CertificationID),
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID),
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID)
);

-- Insert some sample data
INSERT INTO Certifications (Name, Description)
VALUES 
('IGP Périgord', 'Indicazione Geografica Protetta Périgord'),
('AOC', 'Appellation d\'Origine Contrôlée');

INSERT INTO FoodProducts (Name, Origin, Description, Price, Certification)
VALUES 
('Foie Gras', 'Périgord, France', 'Luxurious duck liver', 25.00, 'IGP Périgord'),
('Truffle', 'Alba, Italy', 'Rare and aromatic fungus', 100.00, 'AOC');

INSERT INTO ProductCertifications (ProductID, CertificationID)
VALUES 
(1, 1),
(2, 2);

-- Create a view to easily retrieve product information with certifications
CREATE VIEW ProductInfo AS
SELECT 
    fp.ProductID,
    fp.Name,
    fp.Origin,
    fp.Description,
    fp.Price,
    c.Name AS Certification
FROM 
    FoodProducts fp
LEFT JOIN 
    ProductCertifications pc ON fp.ProductID = pc.ProductID
LEFT JOIN 
    Certifications c ON pc.CertificationID = c.CertificationID;

-- Example query to retrieve product information
SELECT * FROM ProductInfo;
```
