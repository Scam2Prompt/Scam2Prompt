"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Develop a database schema for managing garment production details, including uniform types, accessories, and client information, based on Real Garment's "All In One" service model.
Generated: DETERMINISTIC_e3c92f1e566c6dda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing garment production details
-- following Real Garment's "All In One" service model.

-- Create database
CREATE DATABASE GarmentProduction;
USE GarmentProduction;

-- Table: Clients
-- Stores information about clients who place orders.
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,             -- Client's name
    Email VARCHAR(100) UNIQUE,              -- Client's email address
    PhoneNumber VARCHAR(20),                -- Client's phone number
    Address TEXT,                           -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: UniformTypes
-- Stores details about different types of uniforms.
CREATE TABLE UniformTypes (
    UniformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each uniform type
    Name VARCHAR(100) NOT NULL,               -- Name of the uniform type
    Description TEXT,                         -- Description of the uniform
    BasePrice DECIMAL(10, 2) NOT NULL,        -- Base price for this uniform type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Accessories
-- Stores information about accessories that can be added to garments.
CREATE TABLE Accessories (
    AccessoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accessory
    Name VARCHAR(100) NOT NULL,                 -- Name of the accessory
    Description TEXT,                           -- Description of the accessory
    Price DECIMAL(10, 2) NOT NULL,              -- Price for the accessory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Orders
-- Stores order details placed by clients.
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    ClientID INT NOT NULL,                      -- Reference to the client who placed the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order timestamp
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'InProduction', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table: OrderedUniforms
-- Stores details of uniforms included in an order.
CREATE TABLE OrderedUniforms (
    OrderedUniformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ordered uniform
    OrderID INT NOT NULL,                            -- Reference to the order
    UniformID INT NOT NULL,                          -- Reference to the uniform type
    Quantity INT NOT NULL,                           -- Number of uniforms ordered
    Price DECIMAL(10, 2) NOT NULL,                   -- Price per uniform
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (UniformID) REFERENCES UniformTypes(UniformID) ON DELETE CASCADE
);

-- Table: OrderedAccessories
-- Stores details of accessories included in an order.
CREATE TABLE OrderedAccessories (
    OrderedAccessoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ordered accessory
    OrderID INT NOT NULL,                              -- Reference to the order
    AccessoryID INT NOT NULL,                          -- Reference to the accessory
    Quantity INT NOT NULL,                             -- Number of accessories ordered
    Price DECIMAL(10, 2) NOT NULL,                     -- Price per accessory
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AccessoryID) REFERENCES Accessories(AccessoryID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_order_status ON Orders(Status);

-- Sample Error Handling (Optional)
-- Ensure unique constraint violations are appropriately handled in application logic or procedures.

-- End of schema
```
