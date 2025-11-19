"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Develop a database schema for managing garment production details, including uniform types, accessories, and client information, based on Real Garment's "All In One" service model.
Generated: DETERMINISTIC_e3c92f1e566c6dda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing garment production details

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS UniformTypes;
DROP TABLE IF EXISTS Accessories;
DROP TABLE IF EXISTS ProductionOrders;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactPerson VARCHAR(255),                -- Name of the contact person
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the client
    Phone VARCHAR(20),                         -- Phone number of the client
    Address TEXT,                              -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store uniform types
CREATE TABLE UniformTypes (
    UniformTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each uniform type
    TypeName VARCHAR(255) NOT NULL,                -- Name of the uniform type
    Description TEXT,                               -- Description of the uniform type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the uniform type was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store accessories
CREATE TABLE Accessories (
    AccessoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each accessory
    AccessoryName VARCHAR(255) NOT NULL,         -- Name of the accessory
    Description TEXT,                             -- Description of the accessory
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the accessory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the accessory was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store production orders
CREATE TABLE ProductionOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each production order
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    UniformTypeID INT NOT NULL,                  -- Foreign key referencing UniformTypes
    AccessoryID INT,                             -- Foreign key referencing Accessories (optional)
    Quantity INT NOT NULL,                       -- Quantity of uniforms ordered
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the order was placed
    Status ENUM('Pending', 'In Production', 'Completed', 'Cancelled') DEFAULT 'Pending',  -- Status of the order
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (UniformTypeID) REFERENCES UniformTypes(UniformTypeID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (AccessoryID) REFERENCES Accessories(AccessoryID) ON DELETE SET NULL  -- Optional accessory
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_uniform_type_name ON UniformTypes(TypeName);
CREATE INDEX idx_accessory_name ON Accessories(AccessoryName);
CREATE INDEX idx_order_status ON ProductionOrders(Status);
```
