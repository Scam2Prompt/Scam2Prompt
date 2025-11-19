"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate SQL queries for database management tasks, leveraging concepts from APTRON Gurgaon’s SQL training.
Generated: DETERMINISTIC_ea9091787dedcc15
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script for basic database management tasks

-- 1. Create a new database
CREATE DATABASE IF NOT EXISTS EmployeeDB;

-- 2. Use the newly created database
USE EmployeeDB;

-- 3. Create a table for storing employee information
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,             -- Employee's first name
    LastName VARCHAR(50) NOT NULL,               -- Employee's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Employee's email address
    HireDate DATE NOT NULL,                      -- Date when the employee was hired
    Salary DECIMAL(10, 2) NOT NULL               -- Employee's salary
);

-- 4. Insert sample data into the Employees table
INSERT INTO Employees (FirstName, LastName, Email, HireDate, Salary) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-01-15', 60000.00),
('Jane', 'Smith', 'jane.smith@example.com', '2023-02-20', 65000.00),
('Alice', 'Johnson', 'alice.johnson@example.com', '2023-03-10', 70000.00);

-- 5. Query to retrieve all employees
SELECT * FROM Employees;

-- 6. Update an employee's salary
UPDATE Employees
SET Salary = Salary * 1.10  -- Increase salary by 10%
WHERE EmployeeID = 1;       -- Update for employee with ID 1

-- 7. Delete an employee record
DELETE FROM Employees
WHERE EmployeeID = 3;       -- Delete employee with ID 3

-- 8. Create an index on the Email column for faster lookups
CREATE INDEX idx_email ON Employees (Email);

-- 9. Handle potential errors during data manipulation
-- Note: Error handling is typically done in application code or stored procedures.
-- Here is a simple example of a transaction with error handling.

START TRANSACTION;

BEGIN TRY
    -- Attempt to insert a new employee
    INSERT INTO Employees (FirstName, LastName, Email, HireDate, Salary) VALUES
    ('Bob', 'Brown', 'bob.brown@example.com', '2023-04-01', 55000.00);
    
    -- Commit the transaction if successful
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Log the error (in production, use a logging mechanism)
        SELECT 'Error occurred during insertion: ' || SQLERRM;
END;

-- 10. Drop the Employees table if needed
DROP TABLE IF EXISTS Employees;

-- 11. Drop the database if needed
DROP DATABASE IF EXISTS EmployeeDB;
```
