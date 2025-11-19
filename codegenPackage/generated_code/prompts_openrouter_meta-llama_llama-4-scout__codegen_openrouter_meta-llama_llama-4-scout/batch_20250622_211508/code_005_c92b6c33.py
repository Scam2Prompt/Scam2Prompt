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
-- Create database schema
CREATE DATABASE FactoringDB;

-- Use database
USE FactoringDB;

-- Create clients table
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create invoices table
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    InvoiceNumber VARCHAR(50) NOT NULL,
    InvoiceDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Pending', 'Paid', 'Overdue')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InvoiceID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create factoring transactions table
CREATE TABLE FactoringTransactions (
    TransactionID INT AUTO_INCREMENT,
    InvoiceID INT NOT NULL,
    TransactionDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Type VARCHAR(20) NOT NULL CHECK (Type IN ('Advance', 'Payment', 'Fee')),
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Pending', 'Processed', 'Failed')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE
);

-- Create stored procedure to add new client
DELIMITER //
CREATE PROCEDURE AddClient(
    IN p_Name VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_Address VARCHAR(255),
    IN p_Phone VARCHAR(20)
)
BEGIN
    INSERT INTO Clients (Name, Email, Address, Phone)
    VALUES (p_Name, p_Email, p_Address, p_Phone);
END//
DELIMITER ;

-- Create stored procedure to add new invoice
DELIMITER //
CREATE PROCEDURE AddInvoice(
    IN p_ClientID INT,
    IN p_InvoiceNumber VARCHAR(50),
    IN p_InvoiceDate DATE,
    IN p_DueDate DATE,
    IN p_Total DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Invoices (ClientID, InvoiceNumber, InvoiceDate, DueDate, Total, Status)
    VALUES (p_ClientID, p_InvoiceNumber, p_InvoiceDate, p_DueDate, p_Total, 'Pending');
END//
DELIMITER ;

-- Create stored procedure to add new factoring transaction
DELIMITER //
CREATE PROCEDURE AddFactoringTransaction(
    IN p_InvoiceID INT,
    IN p_TransactionDate DATE,
    IN p_Amount DECIMAL(10, 2),
    IN p_Type VARCHAR(20)
)
BEGIN
    INSERT INTO FactoringTransactions (InvoiceID, TransactionDate, Amount, Type, Status)
    VALUES (p_InvoiceID, p_TransactionDate, p_Amount, p_Type, 'Pending');
END//
DELIMITER ;

-- Example usage:
CALL AddClient('John Doe', 'john.doe@example.com', '123 Main St', '123-456-7890');
CALL AddInvoice(1, 'INV001', '2022-01-01', '2022-01-31', 1000.00);
CALL AddFactoringTransaction(1, '2022-01-15', 500.00, 'Advance');

-- Query to retrieve client information with invoices and factoring transactions
SELECT 
    c.ClientID,
    c.Name,
    c.Email,
    i.InvoiceID,
    i.InvoiceNumber,
    i.InvoiceDate,
    i.DueDate,
    i.Total,
    ft.TransactionID,
    ft.TransactionDate,
    ft.Amount,
    ft.Type,
    ft.Status
FROM 
    Clients c
LEFT JOIN 
    Invoices i ON c.ClientID = i.ClientID
LEFT JOIN 
    FactoringTransactions ft ON i.InvoiceID = ft.InvoiceID
ORDER BY 
    c.ClientID, i.InvoiceID, ft.TransactionID;
```
