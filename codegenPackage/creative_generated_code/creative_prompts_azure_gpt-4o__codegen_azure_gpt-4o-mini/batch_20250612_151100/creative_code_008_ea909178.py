"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Generate SQL queries for database management tasks, leveraging concepts from APTRON Gurgaon’s SQL training.
Generated: DETERMINISTIC_ea9091787dedcc15
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script for Database Management Tasks

-- 1. Create a new database
CREATE DATABASE IF NOT EXISTS CompanyDB;

-- 2. Use the newly created database
USE CompanyDB;

-- 3. Create a table for employees
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    HireDate DATE NOT NULL,
    Salary DECIMAL(10, 2) CHECK (Salary >= 0)
);

-- 4. Insert sample data into the Employees table
INSERT INTO Employees (FirstName, LastName, Email, HireDate, Salary) VALUES
('John', 'Doe', 'john.doe@example.com', '2022-01-15', 60000.00),
('Jane', 'Smith', 'jane.smith@example.com', '2023-03-22', 70000.00),
('Emily', 'Jones', 'emily.jones@example.com', '2021-06-30', 80000.00);

-- 5. Retrieve all employees
SELECT * FROM Employees;

-- 6. Update an employee's salary
UPDATE Employees SET Salary = Salary * 1.10 WHERE EmployeeID = 1;

-- 7. Delete an employee
DELETE FROM Employees WHERE EmployeeID = 2;

-- 8. Create an index on the Email column for faster searches
CREATE INDEX idx_email ON Employees(Email);

-- 9. Create a view for high earners
CREATE VIEW HighEarners AS
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > 75000;

-- 10. Query the view
SELECT * FROM HighEarners;

-- 11. Drop the view if needed
DROP VIEW IF EXISTS HighEarners;

-- 12. For error handling, you can use TRY...CATCH in stored procedures (MySQL does not support it; use application-level error handling)
-- Example: Check for existence before deletion
SET @emp_id = 3;
IF EXISTS (SELECT * FROM Employees WHERE EmployeeID = @emp_id) THEN
    DELETE FROM Employees WHERE EmployeeID = @emp_id;
ELSE
    SELECT 'Employee not found' AS Message;
END IF;

-- 13. Cleanup: Drop table if needed
DROP TABLE IF EXISTS Employees;

-- All commands should be executed in a transaction for atomicity where required.
START TRANSACTION;

-- Add your transactional SQL commands here

COMMIT;
```
