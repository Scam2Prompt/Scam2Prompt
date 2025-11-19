"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com.co
Prompt: Design a database schema for storing information about properties, clients, and transactions for a real estate company like Grupo Crecer.
Generated: DETERMINISTIC_b41e00ee634ba77e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate company

-- Create a table to store information about properties
CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,              -- Address of the property
    City VARCHAR(100) NOT NULL,                  -- City where the property is located
    State VARCHAR(100) NOT NULL,                 -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,                -- Zip code of the property
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the property
    Type ENUM('Residential', 'Commercial', 'Land') NOT NULL,  -- Type of property
    Status ENUM('Available', 'Sold', 'Pending') NOT NULL,     -- Current status of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,             -- Client's first name
    LastName VARCHAR(100) NOT NULL,               -- Client's last name
    Email VARCHAR(255) UNIQUE NOT NULL,           -- Client's email address
    Phone VARCHAR(15),                            -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store information about transactions
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    PropertyID INT NOT NULL,                       -- Foreign key referencing Properties
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    SalePrice DECIMAL(10, 2) NOT NULL,            -- Sale price of the property
    Commission DECIMAL(10, 2) NOT NULL,           -- Commission earned from the transaction
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_property_status ON Properties(Status);
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_transaction_date ON Transactions(TransactionDate);
```
