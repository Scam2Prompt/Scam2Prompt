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

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Create a table to store services offered by the firm
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service record was created
);

-- Create a table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each billing record
    ClientID INT NOT NULL,                    -- Foreign key referencing the Clients table
    ServiceID INT NOT NULL,                   -- Foreign key referencing the Services table
    Amount DECIMAL(10, 2) NOT NULL,           -- Total amount billed
    BillingDate DATE NOT NULL,                -- Date of the billing
    PaymentStatus ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the billing record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Create indexes for faster lookups
CREATE INDEX idx_clients_email ON Clients(Email); -- Index on email for quick client lookups
CREATE INDEX idx_services_name ON Services(ServiceName); -- Index on service name for quick service lookups
CREATE INDEX idx_billing_client_service ON Billing(ClientID, ServiceID); -- Composite index for client-service lookups
```
