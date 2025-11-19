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
-- SQL script to manage a database of clients, invoices, and factoring transactions

-- Create a table for clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Unique email for client contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for invoices
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each invoice
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    InvoiceDate DATE NOT NULL,                 -- Date of the invoice
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount of the invoice
    Status ENUM('Pending', 'Paid', 'Cancelled') DEFAULT 'Pending', -- Status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures data consistency
);

-- Create a table for factoring transactions
CREATE TABLE FactoringTransactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    InvoiceID INT NOT NULL,                        -- Foreign key referencing Invoices
    TransactionDate DATE NOT NULL,                 -- Date of the transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount of the transaction
    Fee DECIMAL(10, 2) NOT NULL,                  -- Fee charged for factoring
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the transaction was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE -- Ensures data consistency
);

-- Example of inserting a new client
INSERT INTO Clients (ClientName, ContactEmail) 
VALUES ('Acme Corp', 'contact@acmecorp.com');

-- Example of inserting a new invoice for a client
INSERT INTO Invoices (ClientID, InvoiceDate, Amount) 
VALUES (1, '2023-10-01', 1500.00);

-- Example of inserting a new factoring transaction for an invoice
INSERT INTO FactoringTransactions (InvoiceID, TransactionDate, Amount, Fee) 
VALUES (1, '2023-10-02', 1500.00, 50.00);

-- Error handling example for inserting a new client
BEGIN;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback in case of error
        ROLLBACK;
        SELECT 'Error occurred while inserting client';
    END;

    INSERT INTO Clients (ClientName, ContactEmail) 
    VALUES ('Beta LLC', 'contact@betallc.com');
COMMIT;

-- Query to retrieve all clients with their invoices and factoring transactions
SELECT 
    c.ClientID,
    c.ClientName,
    i.InvoiceID,
    i.InvoiceDate,
    i.Amount AS InvoiceAmount,
    i.Status AS InvoiceStatus,
    ft.TransactionID,
    ft.TransactionDate,
    ft.Amount AS TransactionAmount,
    ft.Fee AS TransactionFee
FROM 
    Clients c
LEFT JOIN 
    Invoices i ON c.ClientID = i.ClientID
LEFT JOIN 
    FactoringTransactions ft ON i.InvoiceID = ft.InvoiceID
ORDER BY 
    c.ClientID, i.InvoiceDate;
```
