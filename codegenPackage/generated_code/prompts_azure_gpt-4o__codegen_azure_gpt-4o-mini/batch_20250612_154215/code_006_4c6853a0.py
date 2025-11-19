"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Create a database schema in SQL to manage client information, including RUT and invoice data, for a factoring service inspired by Adelanto.cl.
Generated: DETERMINISTIC_4c6853a098fa3d2c
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information and invoice data for a factoring service

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Invoices;
DROP TABLE IF EXISTS Clients;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID SERIAL PRIMARY KEY, -- Unique identifier for each client
    RUT VARCHAR(12) NOT NULL UNIQUE, -- RUT (Rol Único Tributario) of the client, must be unique
    Name VARCHAR(100) NOT NULL, -- Name of the client
    Email VARCHAR(100) NOT NULL, -- Email address of the client
    Phone VARCHAR(15), -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store invoice information
CREATE TABLE Invoices (
    InvoiceID SERIAL PRIMARY KEY, -- Unique identifier for each invoice
    ClientID INT NOT NULL, -- Foreign key referencing the Clients table
    InvoiceNumber VARCHAR(50) NOT NULL, -- Unique invoice number
    Amount DECIMAL(10, 2) NOT NULL, -- Amount of the invoice
    DueDate DATE NOT NULL, -- Due date for the invoice
    Status VARCHAR(20) NOT NULL DEFAULT 'Pending', -- Status of the invoice (e.g., Pending, Paid, Overdue)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_rut ON Clients(RUT);
CREATE INDEX idx_invoice_client ON Invoices(ClientID);
CREATE INDEX idx_invoice_status ON Invoices(Status);
```
