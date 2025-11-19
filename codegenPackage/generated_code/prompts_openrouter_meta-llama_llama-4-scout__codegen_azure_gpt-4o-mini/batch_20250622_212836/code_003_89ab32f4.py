"""
Generated Code Metadata:
========================
Original URL: https://zelenina-hrbek.cz
Prompt: "Design a simple database schema for a company's contact information using MySQL."
Generated: DETERMINISTIC_89ab32f44e342678
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the company's contact information
CREATE DATABASE IF NOT EXISTS CompanyContacts;

-- Use the newly created database
USE CompanyContacts;

-- Create a table to store employee contact information
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,           -- Employee's first name
    LastName VARCHAR(50) NOT NULL,            -- Employee's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Employee's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    Department VARCHAR(50),                    -- Department where the employee works
    HireDate DATE NOT NULL,                    -- Date when the employee was hired
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store additional contact information for employees
CREATE TABLE IF NOT EXISTS EmployeeContacts (
    ContactID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each contact entry
    EmployeeID INT NOT NULL,                    -- Foreign key referencing Employees table
    ContactType ENUM('Personal', 'Work') NOT NULL, -- Type of contact (Personal or Work)
    ContactValue VARCHAR(100) NOT NULL,        -- Value of the contact (e.g., phone number, email)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Email column for faster lookups
CREATE INDEX idx_email ON Employees(Email);

-- Create an index on the EmployeeID column in EmployeeContacts for faster lookups
CREATE INDEX idx_employee_id ON EmployeeContacts(EmployeeID);
```
