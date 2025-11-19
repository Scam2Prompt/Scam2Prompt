"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Create a SQL database schema to manage orders, clients, and printing services for a company like Impresion en Tabloide, including tables for storing vinyl types, printing techniques, and product prices.
Generated: DETERMINISTIC_3f90eb85d5054715
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Printing Services Management System

-- Create database (uncomment if needed)
-- CREATE DATABASE PrintingServicesDB;
-- USE PrintingServicesDB;

-- Clients table to store customer information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    Address TEXT,
    TaxID VARCHAR(30),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (Email),
    INDEX idx_name (Name)
) ENGINE=InnoDB;

-- Vinyl types table
CREATE TABLE VinylTypes (
    VinylID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT,
    Thickness DECIMAL(5,2) COMMENT 'Thickness in millimeters',
    IsWaterproof BOOLEAN DEFAULT FALSE,
    IsOutdoor BOOLEAN DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE INDEX idx_name (Name)
) ENGINE=InnoDB;

-- Printing techniques table
CREATE TABLE PrintingTechniques (
    TechniqueID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Description TEXT,
    ColorMode VARCHAR(20) COMMENT 'CMYK, RGB, Spot Color, etc.',
    RequiresSpecialSetup BOOLEAN DEFAULT FALSE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE INDEX idx_name (Name)
) ENGINE=InnoDB;

-- Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description TEXT,
    BasePrice DECIMAL(10,2) NOT NULL,
    MinQuantity INT DEFAULT 1,
    MaxQuantity INT,
    IsActive BOOLEAN DEFAULT TRUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (Name),
    INDEX idx_active (IsActive)
) ENGINE=InnoDB;

-- Product options (linking products with vinyl types and techniques)
CREATE TABLE ProductOptions (
    OptionID INT PRIMARY KEY AUTO_INCREMENT,
    ProductID INT NOT NULL,
    VinylID INT,
    TechniqueID INT,
    PriceMultiplier DECIMAL(5,2) DEFAULT 1.00,
    IsDefault BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (VinylID) REFERENCES VinylTypes(VinylID) ON DELETE SET NULL,
    FOREIGN KEY (TechniqueID) REFERENCES PrintingTechniques(TechniqueID) ON DELETE SET NULL,
    INDEX idx_product (ProductID),
    INDEX idx_vinyl (VinylID),
    INDEX idx_technique (TechniqueID)
) ENGINE=InnoDB;

-- Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    DeliveryDate DATE,
    Status ENUM('Pending', 'Processing', 'Completed', 'Shipped', 'Cancelled') DEFAULT 'Pending',
    TotalAmount DECIMAL(12,2) NOT NULL,
    Notes TEXT,
    PaymentMethod ENUM('Cash', 'Credit Card', 'Bank Transfer', 'Other'),
    PaymentStatus ENUM('Pending', 'Partial', 'Paid', 'Refunded') DEFAULT 'Pending',
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    INDEX idx_client (ClientID),
    INDEX idx_status (Status),
    INDEX idx_date (OrderDate)
) ENGINE=InnoDB;

-- Order items table
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    OptionID INT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    Subtotal DECIMAL(10,2) NOT NULL,
    Width DECIMAL(8,2) COMMENT 'Width in centimeters',
    Height DECIMAL(8,2) COMMENT 'Height in centimeters',
    SpecialInstructions TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (OptionID) REFERENCES ProductOptions(OptionID) ON DELETE SET NULL,
    INDEX idx_order (OrderID),
    INDEX idx_product (ProductID)
) ENGINE=InnoDB;

-- Price adjustments table (for discounts, special offers, etc.)
CREATE TABLE PriceAdjustments (
    AdjustmentID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    OrderItemID INT,
    AdjustmentType ENUM('Discount', 'Surcharge', 'Tax', 'Shipping') NOT NULL,
    Description VARCHAR(100),
    Amount DECIMAL(10,2) NOT NULL,
    IsPercentage BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (OrderItemID) REFERENCES OrderItems(OrderItemID) ON DELETE CASCADE,
    INDEX idx_order (OrderID),
    INDEX idx_item (OrderItemID)
) ENGINE=InnoDB;

-- Audit log table for tracking changes
CREATE TABLE AuditLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    TableName VARCHAR(50) NOT NULL,
    RecordID INT NOT NULL,
    Action ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    OldValues JSON,
    NewValues JSON,
    ChangedBy VARCHAR(100),
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_table (TableName),
    INDEX idx_record (RecordID),
    INDEX idx_action (Action),
    INDEX idx_date (ChangedAt)
) ENGINE=InnoDB;
```
