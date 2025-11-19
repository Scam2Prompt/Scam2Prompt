"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Create a database schema in SQL to store information about orthopedic products such as "Plantillas Ortopédicas," "Rodilleras," and "Colchones," including attributes like price, stock availability, and certification (ISO, CE, ISP).
Generated: DETERMINISTIC_f1d00030b8e94dc3
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for orthopedic products
CREATE DATABASE OrthopedicProducts;

-- Use the OrthopedicProducts database
USE OrthopedicProducts;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CategoryID)
);

-- Create a table for certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT,
    CertificationName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CertificationID)
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10, 2) NOT NULL,
    StockAvailability INT NOT NULL DEFAULT 0,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Create a table for product certifications
CREATE TABLE ProductCertifications (
    ProductID INT,
    CertificationID INT,
    PRIMARY KEY (ProductID, CertificationID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID)
);

-- Insert some sample data into ProductCategories
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
('Plantillas Ortopédicas', 'Orthopedic insoles'),
('Rodilleras', 'Knee supports'),
('Colchones', 'Orthopedic mattresses');

-- Insert some sample data into Certifications
INSERT INTO Certifications (CertificationName, Description)
VALUES 
('ISO', 'International Organization for Standardization'),
('CE', 'Conformité Européene'),
('ISP', 'Instituto de Seguridad y Protección');

-- Insert some sample data into Products
INSERT INTO Products (ProductName, CategoryID, Price, StockAvailability)
VALUES 
('Ortho Insole', 1, 50.00, 100),
('Knee Support', 2, 30.00, 50),
('Orthopedic Mattress', 3, 800.00, 20);

-- Insert some sample data into ProductCertifications
INSERT INTO ProductCertifications (ProductID, CertificationID)
VALUES 
(1, 1),
(1, 2),
(2, 2),
(3, 1),
(3, 3);
```
