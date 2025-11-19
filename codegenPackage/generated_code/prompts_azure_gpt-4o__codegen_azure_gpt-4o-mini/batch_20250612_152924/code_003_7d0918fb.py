"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Create a database schema to store customer inquiries and project details for a company specializing in processed glass and aluminum solutions, like CristalesGraf.
Generated: DETERMINISTIC_7d0918fb3d4da631
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer inquiries and project details
CREATE DATABASE CristalesGrafDB;

USE CristalesGrafDB;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                  -- Customer's name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    ProjectName VARCHAR(100) NOT NULL,          -- Name of the project
    Description TEXT,                            -- Description of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the project was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer inquiries
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    Subject VARCHAR(255) NOT NULL,               -- Subject of the inquiry
    Message TEXT NOT NULL,                        -- Detailed message of the inquiry
    Status ENUM('New', 'In Progress', 'Resolved', 'Closed') NOT NULL DEFAULT 'New', -- Current status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_project_customer ON Projects(CustomerID);
CREATE INDEX idx_inquiry_customer ON Inquiries(CustomerID);
```
