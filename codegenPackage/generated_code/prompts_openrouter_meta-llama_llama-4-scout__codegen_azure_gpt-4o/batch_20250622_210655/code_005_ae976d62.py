"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: "Design a database schema for a real estate brokerage platform in Senegal, including tables for properties, clients, and transactions."
Generated: DETERMINISTIC_ae976d62dee0de8a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate brokerage platform in Senegal

-- Table: Properties
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property
    Description TEXT,                          -- Detailed description of the property
    Address VARCHAR(255) NOT NULL,             -- Address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    PropertyType ENUM('House', 'Apartment', 'Land', 'Commercial') NOT NULL, -- Type of property
    Bedrooms INT,                              -- Number of bedrooms (if applicable)
    Bathrooms INT,                             -- Number of bathrooms (if applicable)
    Area DECIMAL(10, 2),                       -- Area of the property in square meters
    AvailabilityStatus ENUM('Available', 'Sold', 'Rented') DEFAULT 'Available', -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,           -- First name of the client
    LastName VARCHAR(100) NOT NULL,            -- Last name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the client
    PhoneNumber VARCHAR(20) NOT NULL,          -- Phone number of the client
    Address VARCHAR(255),                      -- Address of the client
    City VARCHAR(100),                         -- City of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    PropertyID INT NOT NULL,                      -- Foreign key referencing the Properties table
    ClientID INT NOT NULL,                        -- Foreign key referencing the Clients table
    TransactionType ENUM('Purchase', 'Rent') NOT NULL, -- Type of transaction
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Amount DECIMAL(15, 2) NOT NULL,               -- Amount involved in the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the transaction was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete for property
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete for client
);

-- Indexes for optimization
CREATE INDEX idx_properties_city ON Properties (City); -- Index for city in Properties table
CREATE INDEX idx_clients_city ON Clients (City);       -- Index for city in Clients table
CREATE INDEX idx_transactions_date ON Transactions (TransactionDate); -- Index for transaction date
```
