"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Create a database schema in SQL to manage client information, including RUT and invoice data, for a factoring service inspired by Adelanto.cl.
Generated: DETERMINISTIC_4c6853a098fa3d2c
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create the database schema for managing client information and invoice data

-- Drop existing tables if they exist to avoid conflicts during re-creation
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS Clients;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID SERIAL PRIMARY KEY,                      -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,                       -- Client's name
    RUT VARCHAR(12) UNIQUE NOT NULL,                  -- Client's RUT (Chilean tax identification number)
    Email VARCHAR(100) UNIQUE NOT NULL,               -- Client's email address
    Phone VARCHAR(15),                                -- Client's phone number
    Address VARCHAR(255),                             -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when client was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table to store invoice data associated with clients
CREATE TABLE Invoices (
    InvoiceID SERIAL PRIMARY KEY,                      -- Unique identifier for each invoice
    ClientID INT NOT NULL,                             -- Foreign key referencing Clients
    Amount DECIMAL(10, 2) NOT NULL,                   -- Invoice amount
    IssueDate DATE NOT NULL,                           -- Date when the invoice was issued
    DueDate DATE NOT NULL,                             -- Due date for the invoice payment
    Status VARCHAR(20) NOT NULL DEFAULT 'Pending',    -- Status of the invoice (e.g., Pending, Paid, Overdue)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure deletion of invoices if client is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_rut ON Clients(RUT);
CREATE INDEX idx_invoice_client ON Invoices(ClientID);
CREATE INDEX idx_invoice_status ON Invoices(Status);

-- Insert sample data for testing purposes
INSERT INTO Clients (Name, RUT, Email, Phone, Address) VALUES 
('Example Client', '12345678-9', 'client@example.com', '123456789', '123 Example St');

INSERT INTO Invoices (ClientID, Amount, IssueDate, DueDate) VALUES 
(1, 1500.00, '2023-01-01', '2023-01-31');

-- Note: Always ensure to sanitize input and validate RUT format in application logic.
```
