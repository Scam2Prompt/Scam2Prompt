"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Design a database schema to store information about various stone products, including Premium Pennsylvania Bluestone, Treads, Steps, and Boulders, and their respective suppliers.
Generated: DETERMINISTIC_3f518451611763e2
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- stone_products_schema.sql

-- Create a database schema to store information about stone products and their suppliers

CREATE TABLE Suppliers (
  SupplierID INT AUTO_INCREMENT,
  SupplierName VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(100) UNIQUE NOT NULL,
  PRIMARY KEY (SupplierID)
);

CREATE TABLE StoneProducts (
  ProductID INT AUTO_INCREMENT,
  ProductName VARCHAR(255) NOT NULL,
  ProductDescription TEXT,
  UnitPrice DECIMAL(10, 2) NOT NULL,
  UnitOfMeasurement VARCHAR(20) NOT NULL,
  PRIMARY KEY (ProductID)
);

CREATE TABLE ProductSuppliers (
  ProductID INT NOT NULL,
  SupplierID INT NOT NULL,
  PRIMARY KEY (ProductID, SupplierID),
  FOREIGN KEY (ProductID) REFERENCES StoneProducts(ProductID),
  FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

CREATE TABLE ProductVariants (
  VariantID INT AUTO_INCREMENT,
  ProductID INT NOT NULL,
  VariantName VARCHAR(255) NOT NULL,
  VariantDescription TEXT,
  PRIMARY KEY (VariantID),
  FOREIGN KEY (ProductID) REFERENCES StoneProducts(ProductID)
);

CREATE TABLE ProductVariantDetails (
  VariantID INT NOT NULL,
  Thickness DECIMAL(10, 2) NOT NULL,
  Length DECIMAL(10, 2) NOT NULL,
  Width DECIMAL(10, 2) NOT NULL,
  Weight DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (VariantID),
  FOREIGN KEY (VariantID) REFERENCES ProductVariants(VariantID)
);

-- Insert sample data
INSERT INTO Suppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES
  ('Acme Stone', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'info@acmestone.com'),
  ('Stone Masters', '456 Elm St', 'Chicago', 'IL', 'USA', '60601', '987-654-3210', 'info@stonemasters.com');

INSERT INTO StoneProducts (ProductName, ProductDescription, UnitPrice, UnitOfMeasurement)
VALUES
  ('Premium Pennsylvania Bluestone', 'High-quality bluestone from Pennsylvania', 10.00, 'sqft'),
  ('Treads', 'Stone treads for stairways', 50.00, 'each'),
  ('Steps', 'Stone steps for outdoor use', 75.00, 'each'),
  ('Boulders', 'Large stones for landscaping', 200.00, 'each');

INSERT INTO ProductSuppliers (ProductID, SupplierID)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (3, 2),
  (4, 1);

INSERT INTO ProductVariants (ProductID, VariantName, VariantDescription)
VALUES
  (1, 'Bluestone Pavers', 'Bluestone pavers for patios and walkways'),
  (1, 'Bluestone Flagstone', 'Bluestone flagstone for outdoor flooring'),
  (2, 'Tread - 12 inches wide', '12-inch wide stone treads'),
  (3, 'Step - 6 inches high', '6-inch high stone steps'),
  (4, 'Boulder - 2-3 tons', 'Large boulders for landscaping');

INSERT INTO ProductVariantDetails (VariantID, Thickness, Length, Width, Weight)
VALUES
  (1, 1.5, 12.0, 12.0, 50.0),
  (2, 1.0, 24.0, 24.0, 100.0),
  (3, 2.0, 12.0, 12.0, 75.0),
  (4, 6.0, 36.0, 12.0, 200.0),
  (5, 48.0, 48.0, 24.0, 4000.0);
```
