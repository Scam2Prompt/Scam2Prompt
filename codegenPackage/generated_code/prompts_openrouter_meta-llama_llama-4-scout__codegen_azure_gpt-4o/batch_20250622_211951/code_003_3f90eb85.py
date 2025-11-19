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
-- SQL Schema for managing orders, clients, and printing services

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,              -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    Phone VARCHAR(15),                       -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store vinyl types
CREATE TABLE VinylTypes (
    VinylID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each vinyl type
    Name VARCHAR(100) NOT NULL,              -- Name of the vinyl type
    Description TEXT,                        -- Description of the vinyl type
    PricePerUnit DECIMAL(10, 2) NOT NULL,    -- Price per unit of vinyl
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store printing techniques
CREATE TABLE PrintingTechniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each technique
    Name VARCHAR(100) NOT NULL,                 -- Name of the printing technique
    Description TEXT,                           -- Description of the technique
    PricePerUnit DECIMAL(10, 2) NOT NULL,       -- Price per unit for the technique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store products and their prices
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Description of the product
    BasePrice DECIMAL(10, 2) NOT NULL,         -- Base price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status VARCHAR(50) DEFAULT 'Pending',      -- Status of the order (e.g., Pending, Completed)
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store order details (items in the order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    VinylID INT,                                  -- Foreign key referencing VinylTypes table (optional)
    TechniqueID INT,                              -- Foreign key referencing PrintingTechniques table (optional)
    Quantity INT NOT NULL,                        -- Quantity of the product
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for this item
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (VinylID) REFERENCES VinylTypes(VinylID) ON DELETE SET NULL,
    FOREIGN KEY (TechniqueID) REFERENCES PrintingTechniques(TechniqueID) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_order_date ON Orders(OrderDate);
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_vinyl_name ON VinylTypes(Name);
CREATE INDEX idx_technique_name ON PrintingTechniques(Name);
```
