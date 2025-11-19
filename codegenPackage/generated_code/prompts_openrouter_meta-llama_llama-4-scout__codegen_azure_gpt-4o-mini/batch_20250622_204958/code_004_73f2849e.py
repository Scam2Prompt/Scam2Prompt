"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Write a SQL query to manage customer information and job history for a handyman service provider like Handyfix.
Generated: DETERMINISTIC_73f2849ea7d4dbe5
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the handyman service provider
CREATE DATABASE Handyfix;

-- Use the newly created database
USE Handyfix;

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Phone VARCHAR(15),                        -- Customer's phone number
    Address VARCHAR(255),                      -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store job history
CREATE TABLE JobHistory (
    JobID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each job
    CustomerID INT NOT NULL,                   -- Foreign key referencing the customer
    JobDescription VARCHAR(255) NOT NULL,      -- Description of the job
    JobStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the job
    JobDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the job was scheduled
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert a new customer into the Customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, Anytown, USA');

-- Insert a new job into the JobHistory table for the newly added customer
INSERT INTO JobHistory (CustomerID, JobDescription, JobStatus)
VALUES (LAST_INSERT_ID(), 'Fix leaky faucet', 'Pending');

-- Query to retrieve all customers and their job history
SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Email,
    c.Phone,
    c.Address,
    j.JobID,
    j.JobDescription,
    j.JobStatus,
    j.JobDate
FROM 
    Customers c
LEFT JOIN 
    JobHistory j ON c.CustomerID = j.CustomerID
ORDER BY 
    c.CustomerID, j.JobDate;

-- Error handling can be implemented in application code that executes these queries
-- Ensure to handle potential exceptions such as duplicate entries, foreign key violations, etc.
```
