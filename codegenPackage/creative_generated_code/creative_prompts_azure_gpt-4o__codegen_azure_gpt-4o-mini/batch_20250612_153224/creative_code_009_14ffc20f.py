"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Create a database schema for storing property information, title transaction details, and client communication logs, tailored to the services offered by Superior Title Montana.
Generated: DETERMINISTIC_14ffc20f30ddc9e5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing property information, title transaction details,
-- and client communication logs for Superior Title Montana.

-- Create a database for the application
CREATE DATABASE SuperiorTitleMontana;

-- Use the created database
USE SuperiorTitleMontana;

-- Table for storing property information
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,               -- Property address
    City VARCHAR(100) NOT NULL,                   -- City where the property is located
    State VARCHAR(100) NOT NULL,                  -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL,                 -- Zip code of the property
    OwnerName VARCHAR(255) NOT NULL,              -- Name of the property owner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing title transaction details
CREATE TABLE TitleTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    PropertyID INT,                                 -- Foreign key referring to Properties table
    TransactionDate DATE NOT NULL,                 -- Date of the transaction
    TransactionAmount DECIMAL(10, 2) NOT NULL,    -- Amount of the transaction
    TransactionType ENUM('Sale', 'Refinance', 'Other') NOT NULL, -- Type of transaction
    ClientID INT,                                  -- Foreign key referring to Clients table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,              -- Client's first name
    LastName VARCHAR(100) NOT NULL,                -- Client's last name
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Client's email address (unique)
    PhoneNumber VARCHAR(20) NOT NULL,             -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing communication logs
CREATE TABLE CommunicationLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each communication log
    ClientID INT,                                  -- Foreign key referring to Clients table
    CommunicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of communication
    CommunicationType ENUM('Email', 'Phone', 'In-Person', 'Other') NOT NULL, -- Type of communication
    Notes TEXT,                                    -- Notes from the communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Indexes for better performance on commonly queried fields
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_transaction_date ON TitleTransactions(TransactionDate);
CREATE INDEX idx_property_address ON Properties(Address);
```
