"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Design a database schema to store information about custom apparel orders, including details about fabric selection, fit, and printing services, for a company like Black Hill Sports."
Generated: DETERMINISTIC_97cf886da71bf85a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for custom apparel orders

CREATE DATABASE BlackHillSports;

USE BlackHillSports;

-- Define table for fabrics
CREATE TABLE Fabrics (
  FabricID INT AUTO_INCREMENT,
  FabricType VARCHAR(255) NOT NULL,
  FabricDescription TEXT,
  PRIMARY KEY (FabricID)
);

-- Define table for fits
CREATE TABLE Fits (
  FitID INT AUTO_INCREMENT,
  FitType VARCHAR(255) NOT NULL,
  FitDescription TEXT,
  PRIMARY KEY (FitID)
);

-- Define table for printing services
CREATE TABLE PrintingServices (
  PrintingServiceID INT AUTO_INCREMENT,
  PrintingServiceType VARCHAR(255) NOT NULL,
  PrintingServiceDescription TEXT,
  PRIMARY KEY (PrintingServiceID)
);

-- Define table for apparel items
CREATE TABLE ApparelItems (
  ApparelItemID INT AUTO_INCREMENT,
  ApparelItemName VARCHAR(255) NOT NULL,
  ApparelItemDescription TEXT,
  PRIMARY KEY (ApparelItemID)
);

-- Define table for orders
CREATE TABLE Orders (
  OrderID INT AUTO_INCREMENT,
  CustomerName VARCHAR(255) NOT NULL,
  OrderDate DATE NOT NULL,
  TotalCost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (OrderID)
);

-- Define table for order items
CREATE TABLE OrderItems (
  OrderItemID INT AUTO_INCREMENT,
  OrderID INT NOT NULL,
  ApparelItemID INT NOT NULL,
  FabricID INT NOT NULL,
  FitID INT NOT NULL,
  PrintingServiceID INT NOT NULL,
  Quantity INT NOT NULL,
  UnitCost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (OrderItemID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
  FOREIGN KEY (ApparelItemID) REFERENCES ApparelItems(ApparelItemID),
  FOREIGN KEY (FabricID) REFERENCES Fabrics(FabricID),
  FOREIGN KEY (FitID) REFERENCES Fits(FitID),
  FOREIGN KEY (PrintingServiceID) REFERENCES PrintingServices(PrintingServiceID)
);

-- Define table for order status
CREATE TABLE OrderStatus (
  OrderStatusID INT AUTO_INCREMENT,
  OrderID INT NOT NULL,
  Status VARCHAR(255) NOT NULL,
  UpdateDate DATE NOT NULL,
  PRIMARY KEY (OrderStatusID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert sample data
INSERT INTO Fabrics (FabricType, FabricDescription)
VALUES 
('Cotton', '100% cotton'),
('Polyester', '100% polyester'),
('Blended', '50% cotton, 50% polyester');

INSERT INTO Fits (FitType, FitDescription)
VALUES 
('Slim Fit', 'Slim fit for a modern look'),
('Regular Fit', 'Regular fit for a classic look'),
('Loose Fit', 'Loose fit for a relaxed look');

INSERT INTO PrintingServices (PrintingServiceType, PrintingServiceDescription)
VALUES 
('Screen Printing', 'Traditional screen printing'),
('Direct-to-Garment', 'High-resolution direct-to-garment printing'),
('Embroidery', 'Custom embroidery');

INSERT INTO ApparelItems (ApparelItemName, ApparelItemDescription)
VALUES 
('T-Shirt', 'Classic T-shirt'),
('Hoodie', 'Fleece-lined hoodie'),
('Hat', 'Adjustable hat');

INSERT INTO Orders (CustomerName, OrderDate, TotalCost)
VALUES 
('John Doe', '2022-01-01', 100.00),
('Jane Smith', '2022-01-15', 200.00);

INSERT INTO OrderItems (OrderID, ApparelItemID, FabricID, FitID, PrintingServiceID, Quantity, UnitCost)
VALUES 
(1, 1, 1, 1, 1, 10, 10.00),
(1, 2, 2, 2, 2, 5, 20.00),
(2, 3, 3, 3, 3, 20, 5.00);

INSERT INTO OrderStatus (OrderID, Status, UpdateDate)
VALUES 
(1, 'Placed', '2022-01-01'),
(1, 'Shipped', '2022-01-05'),
(2, 'Placed', '2022-01-15');
```
