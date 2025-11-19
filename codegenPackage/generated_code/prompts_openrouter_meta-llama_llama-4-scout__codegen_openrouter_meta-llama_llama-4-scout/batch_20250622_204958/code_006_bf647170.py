"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Design a database schema for storing handyman job details, customer information, and service areas, similar to Handyfix's operations.
Generated: DETERMINISTIC_bf6471700bb3ec16
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for handyman job details, customer information, and service areas

-- Create database
CREATE DATABASE Handyfix;

-- Use database
USE Handyfix;

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for handymen
CREATE TABLE Handymen (
    HandymanID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (HandymanID)
);

-- Create table for service areas
CREATE TABLE ServiceAreas (
    ServiceAreaID INT AUTO_INCREMENT,
    HandymanID INT NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceAreaID),
    FOREIGN KEY (HandymanID) REFERENCES Handymen(HandymanID)
);

-- Create table for jobs
CREATE TABLE Jobs (
    JobID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    HandymanID INT,
    JobType VARCHAR(100) NOT NULL,
    JobDescription TEXT,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    ScheduledDate DATE,
    ScheduledTime TIME,
    JobStatus VARCHAR(50) NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (JobID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (HandymanID) REFERENCES Handymen(HandymanID)
);

-- Create table for job history
CREATE TABLE JobHistory (
    JobHistoryID INT AUTO_INCREMENT,
    JobID INT NOT NULL,
    HandymanID INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (JobHistoryID),
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
    FOREIGN KEY (HandymanID) REFERENCES Handymen(HandymanID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    JobID INT NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID)
);

-- Create table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    JobID INT NOT NULL,
    CustomerID INT NOT NULL,
    HandymanID INT NOT NULL,
    Rating TINYINT NOT NULL,
    Review TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (HandymanID) REFERENCES Handymen(HandymanID)
);
```

```sql
-- Example usage:

-- Insert a new customer
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');

-- Insert a new handyman
INSERT INTO Handymen (FirstName, LastName, Email, Phone)
VALUES ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

-- Insert a new service area
INSERT INTO ServiceAreas (HandymanID, City, State, ZipCode)
VALUES (1, 'Anytown', 'CA', '12345');

-- Insert a new job
INSERT INTO Jobs (CustomerID, HandymanID, JobType, JobDescription, Address, City, State, ZipCode)
VALUES (1, 1, 'Plumbing', 'Fix leaky faucet', '123 Main St', 'Anytown', 'CA', '12345');

-- Get all jobs for a customer
SELECT * FROM Jobs WHERE CustomerID = 1;

-- Get all jobs for a handyman
SELECT * FROM Jobs WHERE HandymanID = 1;
```
