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
-- SQL Database Schema for Managing Orders, Clients, and Printing Services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS VinylTypes;
DROP TABLE IF EXISTS PrintingTechniques;
DROP TABLE IF EXISTS ProductPrices;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email (must be unique)
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store vinyl types
CREATE TABLE VinylTypes (
    VinylTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each vinyl type
    TypeName VARCHAR(50) NOT NULL,              -- Name of the vinyl type
    Description TEXT,                            -- Description of the vinyl type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the vinyl type was added
);

-- Table to store printing techniques
CREATE TABLE PrintingTechniques (
    TechniqueID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each printing technique
    TechniqueName VARCHAR(50) NOT NULL,          -- Name of the printing technique
    Description TEXT,                             -- Description of the printing technique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the technique was added
);

-- Table to store product prices
CREATE TABLE ProductPrices (
    PriceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each price entry
    VinylTypeID INT NOT NULL,                    -- Foreign key referencing VinylTypes
    TechniqueID INT NOT NULL,                    -- Foreign key referencing PrintingTechniques
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the price was added
    FOREIGN KEY (VinylTypeID) REFERENCES VinylTypes(VinylTypeID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TechniqueID) REFERENCES PrintingTechniques(TechniqueID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    VinylTypeID INT NOT NULL,                    -- Foreign key referencing VinylTypes
    TechniqueID INT NOT NULL,                    -- Foreign key referencing PrintingTechniques
    Quantity INT NOT NULL,                       -- Quantity of items ordered
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (VinylTypeID) REFERENCES VinylTypes(VinylTypeID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (TechniqueID) REFERENCES PrintingTechniques(TechniqueID) ON DELETE CASCADE -- Ensures referential integrity
);
```
