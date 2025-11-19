"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Write a SQL query to manage a database of clients, invoices, and factoring transactions, ensuring data consistency and security."
Generated: DETERMINISTIC_c92b6c339cb6d552
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing clients, invoices, and factoring transactions
-- Ensure data consistency and security with proper constraints and indexing

-- Create the Clients table
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Client's name
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Client's email (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create the Invoices table
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each invoice
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients
    Amount DECIMAL(10, 2) NOT NULL,           -- Invoice amount
    DueDate DATE NOT NULL,                    -- Due date for the invoice
    Status ENUM('Pending', 'Paid', 'Factored') DEFAULT 'Pending', -- Invoice status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create the FactoringTransactions table
CREATE TABLE FactoringTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    InvoiceID INT NOT NULL,                       -- Foreign key referencing Invoices
    FactorAmount DECIMAL(10, 2) NOT NULL,         -- Amount factored
    FactorDate DATE NOT NULL,                     -- Date of factoring
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the transaction was created
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Add an index to optimize queries on frequently searched columns
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_invoice_status ON Invoices (Status);
CREATE INDEX idx_factoring_date ON FactoringTransactions (FactorDate);

-- Example query to retrieve all invoices for a specific client
SELECT 
    i.InvoiceID, 
    i.Amount, 
    i.DueDate, 
    i.Status, 
    c.Name AS ClientName, 
    c.Email AS ClientEmail
FROM 
    Invoices i
JOIN 
    Clients c ON i.ClientID = c.ClientID
WHERE 
    c.Email = 'example@example.com';

-- Example query to calculate the total factored amount for a specific client
SELECT 
    c.Name AS ClientName, 
    SUM(ft.FactorAmount) AS TotalFactoredAmount
FROM 
    FactoringTransactions ft
JOIN 
    Invoices i ON ft.InvoiceID = i.InvoiceID
JOIN 
    Clients c ON i.ClientID = c.ClientID
WHERE 
    c.ClientID = 1
GROUP BY 
    c.Name;

-- Example query to update the status of an invoice after factoring
UPDATE 
    Invoices
SET 
    Status = 'Factored'
WHERE 
    InvoiceID = 123 AND Status = 'Pending';

-- Example query to delete a client and cascade delete related invoices and transactions
DELETE FROM 
    Clients
WHERE 
    ClientID = 1;
```
