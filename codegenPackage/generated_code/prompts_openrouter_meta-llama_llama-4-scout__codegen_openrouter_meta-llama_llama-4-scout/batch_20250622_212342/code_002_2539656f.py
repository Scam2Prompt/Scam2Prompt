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

-- Use the SmallBusiness database
USE SmallBusiness;

-- Create a table for income
CREATE TABLE Income (
    IncomeID INT AUTO_INCREMENT,
    Date DATE NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (IncomeID)
);

-- Create a table for expenses
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT,
    Date DATE NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ExpenseID)
);

-- Create a table for budget
CREATE TABLE Budget (
    BudgetID INT AUTO_INCREMENT,
    Category VARCHAR(100) NOT NULL,
    BudgetedAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (BudgetID)
);

-- Insert some sample data into the Income table
INSERT INTO Income (Date, Description, Amount)
VALUES 
('2022-01-01', 'Initial Investment', 10000.00),
('2022-01-15', 'Sales', 5000.00),
('2022-02-01', 'Sales', 6000.00);

-- Insert some sample data into the Expenses table
INSERT INTO Expenses (Date, Description, Category, Amount)
VALUES 
('2022-01-05', 'Rent', 'Fixed Expenses', 2000.00),
('2022-01-10', 'Utilities', 'Fixed Expenses', 150.00),
('2022-01-12', 'Office Supplies', 'Variable Expenses', 500.00);

-- Insert some sample data into the Budget table
INSERT INTO Budget (Category, BudgetedAmount)
VALUES 
('Fixed Expenses', 3000.00),
('Variable Expenses', 2000.00);

-- Procedure to add new income
DELIMITER //
CREATE PROCEDURE AddIncome(IN date DATE, IN description VARCHAR(255), IN amount DECIMAL(10, 2))
BEGIN
    INSERT INTO Income (Date, Description, Amount)
    VALUES (date, description, amount);
END//
DELIMITER ;

-- Procedure to add new expense
DELIMITER //
CREATE PROCEDURE AddExpense(IN date DATE, IN description VARCHAR(255), IN category VARCHAR(100), IN amount DECIMAL(10, 2))
BEGIN
    INSERT INTO Expenses (Date, Description, Category, Amount)
    VALUES (date, description, category, amount);
END//
DELIMITER ;

-- Procedure to get total income
DELIMITER //
CREATE PROCEDURE GetTotalIncome()
BEGIN
    SELECT SUM(Amount) AS TotalIncome
    FROM Income;
END//
DELIMITER ;

-- Procedure to get total expenses
DELIMITER //
CREATE PROCEDURE GetTotalExpenses()
BEGIN
    SELECT SUM(Amount) AS TotalExpenses
    FROM Expenses;
END//
DELIMITER ;

-- Procedure to get total expenses by category
DELIMITER //
CREATE PROCEDURE GetTotalExpensesByCategory(IN category VARCHAR(100))
BEGIN
    SELECT SUM(Amount) AS TotalExpenses
    FROM Expenses
    WHERE Category = category;
END//
DELIMITER ;

-- Procedure to get budget vs actual expenses
DELIMITER //
CREATE PROCEDURE GetBudgetVsActualExpenses()
BEGIN
    SELECT 
        b.Category,
        b.BudgetedAmount,
        COALESCE(SUM(e.Amount), 0) AS ActualExpenses
    FROM 
        Budget b
    LEFT JOIN 
        Expenses e ON b.Category = e.Category
    GROUP BY 
        b.Category, b.BudgetedAmount;
END//
DELIMITER ;

-- Call procedures to test
CALL AddIncome('2022-03-01', 'New Sales', 7000.00);
CALL AddExpense('2022-03-05', 'New Office Supplies', 'Variable Expenses', 800.00);
CALL GetTotalIncome();
CALL GetTotalExpenses();
CALL GetTotalExpensesByCategory('Variable Expenses');
CALL GetBudgetVsActualExpenses();
```
