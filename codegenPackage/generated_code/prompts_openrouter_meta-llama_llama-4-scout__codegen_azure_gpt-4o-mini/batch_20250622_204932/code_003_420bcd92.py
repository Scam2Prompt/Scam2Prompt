"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Create a simple database schema to store client data, services offered, and billing information for an accounting firm like Atual Contabilidade."
Generated: DETERMINISTIC_420bcd92ab68458f
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an accounting firm to store client data, services offered, and billing information

-- Create a database for the accounting firm
CREATE DATABASE AtualContabilidade;

-- Use the created database
USE AtualContabilidade;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    Phone VARCHAR(15),                        -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services offered by the accounting firm
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store billing information for clients
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each billing record
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                     -- Foreign key referencing Services table
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount billed
    BillingDate DATE NOT NULL,                  -- Date of billing
    Status ENUM('Paid', 'Pending', 'Overdue') NOT NULL,  -- Status of the billing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Sample data insertion (optional)
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St, Springfield');

INSERT INTO Services (ServiceName, Description, Price) VALUES
('Tax Preparation', 'Preparation of annual tax returns.', 200.00),
('Bookkeeping', 'Monthly bookkeeping services.', 150.00);

INSERT INTO Billing (ClientID, ServiceID, Amount, BillingDate, Status) VALUES
(1, 1, 200.00, '2023-10-01', 'Paid'),
(2, 2, 150.00, '2023-10-05', 'Pending');
```
