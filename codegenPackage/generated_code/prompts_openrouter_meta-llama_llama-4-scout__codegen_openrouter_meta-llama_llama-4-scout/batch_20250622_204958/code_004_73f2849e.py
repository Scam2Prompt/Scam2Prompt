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
-- Create a database for Handyfix
CREATE DATABASE HandyfixDB;

-- Use the Handyfix database
USE HandyfixDB;

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create a table for jobs
CREATE TABLE Jobs (
    JobID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    JobDate DATE NOT NULL,
    JobDescription VARCHAR(255) NOT NULL,
    JobStatus VARCHAR(50) NOT NULL DEFAULT 'Scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (JobID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create a table for job history
CREATE TABLE JobHistory (
    HistoryID INT AUTO_INCREMENT,
    JobID INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (HistoryID),
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID)
);

-- Create a trigger to update job history when job status changes
DELIMITER $$
CREATE TRIGGER UpdateJobHistory
AFTER UPDATE ON Jobs
FOR EACH ROW
BEGIN
    IF NEW.JobStatus != OLD.JobStatus THEN
        INSERT INTO JobHistory (JobID, Status)
        VALUES (NEW.JobID, NEW.JobStatus);
    END IF;
END$$
DELIMITER ;

-- Insert sample data into customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into jobs table
INSERT INTO Jobs (CustomerID, JobDate, JobDescription)
VALUES 
(1, '2024-09-16', 'Fix leaky faucet'),
(1, '2024-09-17', 'Unclog drain'),
(2, '2024-09-18', 'Repair broken toilet');

-- Update job status to trigger job history update
UPDATE Jobs
SET JobStatus = 'In Progress'
WHERE JobID = 1;

-- Retrieve customer information and job history
SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.Email,
    j.JobID,
    j.JobDate,
    j.JobDescription,
    j.JobStatus,
    jh.HistoryID,
    jh.Status AS HistoryStatus
FROM 
    Customers c
INNER JOIN 
    Jobs j ON c.CustomerID = j.CustomerID
LEFT JOIN 
    JobHistory jh ON j.JobID = jh.JobID
ORDER BY 
    c.CustomerID, j.JobID;
```
