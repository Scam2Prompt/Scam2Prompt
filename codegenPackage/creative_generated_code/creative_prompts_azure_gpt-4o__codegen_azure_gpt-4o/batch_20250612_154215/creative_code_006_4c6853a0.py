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
-- SQL schema to manage client information and invoice data for a factoring service

-- Create a table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(255) NOT NULL,          -- Full name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Unique email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    RUT VARCHAR(20) NOT NULL UNIQUE,         -- Unique Chilean RUT (tax identification)
    Address VARCHAR(255),                    -- Physical address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Create a table to store invoice data
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    ClientID INT NOT NULL,                    -- Foreign key linking to the Clients table
    InvoiceNumber VARCHAR(50) NOT NULL UNIQUE, -- Unique invoice number
    IssueDate DATE NOT NULL,                  -- Date when the invoice was issued
    DueDate DATE NOT NULL,                    -- Date when the invoice is due
    Amount DECIMAL(18, 2) NOT NULL,           -- Invoice amount in local currency
    Status ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending', -- Status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the invoice record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update

    -- Foreign key constraint to ensure ClientID exists in Clients table
    CONSTRAINT FK_Client FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create an index for faster lookups on RUT in the Clients table
CREATE INDEX IDX_RUT ON Clients(RUT);

-- Create an index for faster lookups on InvoiceNumber in the Invoices table
CREATE INDEX IDX_InvoiceNumber ON Invoices(InvoiceNumber);

-- Create a table for storing factoring transactions
CREATE TABLE FactoringTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    InvoiceID INT NOT NULL,                       -- Foreign key linking to the Invoices table
    ClientID INT NOT NULL,                        -- Foreign key linking to the Clients table
    AdvanceAmount DECIMAL(18, 2) NOT NULL,        -- Amount advanced to the client under factoring
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    Notes TEXT,                                   -- Notes or descriptions relevant to the transaction

    -- Foreign key constraints
    CONSTRAINT FK_Invoice FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
    CONSTRAINT FK_FactoringClient FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Add error handling for invalid RUT format using a stored procedure (optional)

-- This schema is designed to handle client and invoice data related to factoring operations.
-- Ensure database connection pooling and application-layer validation for production use.
```
