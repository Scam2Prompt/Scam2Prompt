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

-- Drop existing tables if they exist to avoid conflicts during recreation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS UniformTypes;
DROP TABLE IF EXISTS Accessories;
DROP TABLE IF EXISTS GarmentOrders;

-- Table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    ClientName VARCHAR(100) NOT NULL, -- Name of the client
    ContactPerson VARCHAR(100), -- Contact person for the client
    PhoneNumber VARCHAR(15), -- Phone number of the client
    Email VARCHAR(100) UNIQUE, -- Email address of the client
    Address TEXT, -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table for storing uniform types
CREATE TABLE UniformTypes (
    UniformID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each uniform type
    UniformName VARCHAR(100) NOT NULL, -- Name of the uniform type
    Description TEXT, -- Description of the uniform
    Price DECIMAL(10, 2) NOT NULL, -- Price of the uniform
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table for storing accessories
CREATE TABLE Accessories (
    AccessoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each accessory
    AccessoryName VARCHAR(100) NOT NULL, -- Name of the accessory
    Description TEXT, -- Description of the accessory
    Price DECIMAL(10, 2) NOT NULL, -- Price of the accessory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table for managing garment orders, linking clients to uniform types and accessories
CREATE TABLE GarmentOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    ClientID INT NOT NULL, -- Foreign key referencing Clients table
    UniformID INT NOT NULL, -- Foreign key referencing UniformTypes table
    AccessoryID INT, -- Foreign key referencing Accessories table (nullable)
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of garments ordered
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was placed
    Status ENUM('Pending', 'In Production', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (UniformID) REFERENCES UniformTypes(UniformID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AccessoryID) REFERENCES Accessories(AccessoryID) ON DELETE SET NULL -- Allow accessory to be optional
);

-- Sample data insertion for testing purposes (uncomment if needed)
-- INSERT INTO Clients (ClientName, ContactPerson, PhoneNumber, Email, Address) VALUES
-- ('Real Garment Co.', 'John Doe', '123-456-7890', 'john@realgarment.com', '123 Main St, City, Country');

-- INSERT INTO UniformTypes (UniformName, Description, Price) VALUES
-- ('Casual Uniform', 'Comfortable and stylish casual uniform.', 29.99);

-- INSERT INTO Accessories (AccessoryName, Description, Price) VALUES
-- ('Belt', 'Standard belt for the uniform.', 9.99);

-- INSERT INTO GarmentOrders (ClientID, UniformID, AccessoryID, Quantity, Status) VALUES
-- (1, 1, 1, 100, 'Pending');
```
