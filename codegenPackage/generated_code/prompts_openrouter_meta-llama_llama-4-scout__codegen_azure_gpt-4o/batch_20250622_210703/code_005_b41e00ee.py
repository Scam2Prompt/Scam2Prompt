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
-- Database Schema for Real Estate Company

-- Table to store information about properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,             -- Full address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(20) NOT NULL,              -- Zip code of the property
    Type ENUM('Residential', 'Commercial', 'Land') NOT NULL, -- Type of property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    Status ENUM('Available', 'Sold', 'Pending') NOT NULL DEFAULT 'Available', -- Current status of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,           -- First name of the client
    LastName VARCHAR(100) NOT NULL,            -- Last name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the client
    PhoneNumber VARCHAR(20),                   -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    PropertyID INT NOT NULL,                      -- Foreign key referencing Properties table
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount
    Status ENUM('Completed', 'Pending', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the transaction was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete for property
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete for client
);

-- Indexes for optimizing queries
CREATE INDEX idx_properties_status ON Properties(Status);
CREATE INDEX idx_transactions_status ON Transactions(Status);
CREATE INDEX idx_clients_email ON Clients(Email);

-- Error handling and constraints
-- Ensure that transaction amount is positive
ALTER TABLE Transactions
ADD CONSTRAINT chk_transaction_amount CHECK (Amount > 0);

-- Ensure that property price is positive
ALTER TABLE Properties
ADD CONSTRAINT chk_property_price CHECK (Price > 0);
```
