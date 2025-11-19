"""
Generated Code Metadata:
========================
Original URL: https://www.precisaocontabil.com
Prompt: "Write a code snippet to track expenses and income in a small business using SQL."
Generated: DETERMINISTIC_2539656fb2377142
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the small business
CREATE DATABASE SmallBusiness;

-- Switch to the SmallBusiness database
USE SmallBusiness;

-- Create a table to track transactions (both income and expenses)
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    Description VARCHAR(255) NOT NULL,            -- Description of the transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount of the transaction (positive for income, negative for expenses)
    Category VARCHAR(100) NOT NULL,               -- Category of the transaction (e.g., "Sales", "Office Supplies", "Utilities")
    TransactionType ENUM('Income', 'Expense') NOT NULL -- Type of transaction (Income or Expense)
);

-- Insert sample data into the Transactions table
INSERT INTO Transactions (TransactionDate, Description, Amount, Category, TransactionType)
VALUES
    ('2023-10-01', 'Office Rent', -1200.00, 'Rent', 'Expense'),
    ('2023-10-02', 'Product Sale', 5000.00, 'Sales', 'Income'),
    ('2023-10-03', 'Electricity Bill', -300.00, 'Utilities', 'Expense'),
    ('2023-10-04', 'Consulting Service', 1500.00, 'Services', 'Income'),
    ('2023-10-05', 'Office Supplies', -200.00, 'Office Supplies', 'Expense');

-- Query to calculate total income, total expenses, and net balance
SELECT
    SUM(CASE WHEN TransactionType = 'Income' THEN Amount ELSE 0 END) AS TotalIncome, -- Total income
    SUM(CASE WHEN TransactionType = 'Expense' THEN Amount ELSE 0 END) AS TotalExpenses, -- Total expenses
    SUM(Amount) AS NetBalance -- Net balance (income - expenses)
FROM Transactions;

-- Query to view all transactions grouped by category
SELECT
    Category,
    SUM(Amount) AS TotalAmount,
    COUNT(*) AS TransactionCount
FROM Transactions
GROUP BY Category;

-- Query to view recent transactions (last 7 days)
SELECT *
FROM Transactions
WHERE TransactionDate >= CURDATE() - INTERVAL 7 DAY
ORDER BY TransactionDate DESC;

-- Add error handling for invalid data (example: negative income or positive expense)
-- This can be enforced using a CHECK constraint
ALTER TABLE Transactions
ADD CONSTRAINT chk_amount_valid
CHECK (
    (TransactionType = 'Income' AND Amount > 0) OR
    (TransactionType = 'Expense' AND Amount < 0)
);

-- Ensure the table is ready for production use
-- Indexing for faster queries (e.g., on TransactionDate and Category)
CREATE INDEX idx_transaction_date ON Transactions(TransactionDate);
CREATE INDEX idx_category ON Transactions(Category);
```
