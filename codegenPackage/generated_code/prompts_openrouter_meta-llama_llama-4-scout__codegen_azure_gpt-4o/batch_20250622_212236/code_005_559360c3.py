"""
Generated Code Metadata:
========================
Original URL: https://www.cooperativadetasabajacl.com
Prompt: "Write a SQL query to manage loan accounts, including loan amount, interest rate, repayment term, and customer information, for a Chilean financial cooperative."
Generated: DETERMINISTIC_559360c3b88d1ed4
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store loan account information
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each loan
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    LoanAmount DECIMAL(15, 2) NOT NULL,        -- Total loan amount
    InterestRate DECIMAL(5, 2) NOT NULL,       -- Interest rate for the loan
    RepaymentTerm INT NOT NULL,                -- Repayment term in months
    StartDate DATE NOT NULL,                   -- Loan start date
    EndDate DATE NOT NULL,                     -- Loan end date
    Status ENUM('Active', 'Closed', 'Defaulted') DEFAULT 'Active', -- Loan status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Enforce relationship with Customers table
);

-- Insert sample data into Customers table
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
VALUES 
('Juan', 'Perez', 'juan.perez@example.cl', '+56912345678', 'Santiago, Chile'),
('Maria', 'Gonzalez', 'maria.gonzalez@example.cl', '+56987654321', 'Valparaiso, Chile');

-- Insert sample data into Loans table
INSERT INTO Loans (CustomerID, LoanAmount, InterestRate, RepaymentTerm, StartDate, EndDate, Status)
VALUES 
(1, 5000000.00, 3.5, 36, '2023-01-01', '2025-12-31', 'Active'),
(2, 3000000.00, 4.0, 24, '2023-06-01', '2025-05-31', 'Active');

-- Query to retrieve all loan accounts with customer information
SELECT 
    L.LoanID,
    C.FirstName,
    C.LastName,
    C.Email,
    L.LoanAmount,
    L.InterestRate,
    L.RepaymentTerm,
    L.StartDate,
    L.EndDate,
    L.Status
FROM 
    Loans L
JOIN 
    Customers C
ON 
    L.CustomerID = C.CustomerID
ORDER BY 
    L.StartDate DESC; -- Order loans by start date, most recent first

-- Query to calculate the total interest for a specific loan
SELECT 
    LoanID,
    LoanAmount,
    InterestRate,
    RepaymentTerm,
    (LoanAmount * (InterestRate / 100) * (RepaymentTerm / 12)) AS TotalInterest
FROM 
    Loans
WHERE 
    LoanID = 1; -- Replace with the desired LoanID

-- Query to update the status of a loan
UPDATE Loans
SET Status = 'Closed'
WHERE LoanID = 1; -- Replace with the desired LoanID

-- Query to delete a loan record (use with caution)
DELETE FROM Loans
WHERE LoanID = 2; -- Replace with the desired LoanID
```
