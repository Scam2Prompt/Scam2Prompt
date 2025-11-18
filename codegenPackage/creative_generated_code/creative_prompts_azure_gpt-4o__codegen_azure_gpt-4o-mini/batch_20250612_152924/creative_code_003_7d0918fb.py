"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Create a database schema to store customer inquiries and project details for a company specializing in processed glass and aluminum solutions, like CristalesGraf.
Generated: DETERMINISTIC_7d0918fb3d4da631
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer inquiries and project details
CREATE DATABASE CristalesGrafDB;

USE CristalesGrafDB;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store project details associated with customers
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ProjectName VARCHAR(150) NOT NULL,
    ProjectDescription TEXT,
    ProjectStatus ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store customer inquiries
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    InquiryDetails TEXT NOT NULL,
    ResponseDetails TEXT,
    RespondedAt TIMESTAMP NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers (Email);
CREATE INDEX idx_project_customer ON Projects (CustomerID);
CREATE INDEX idx_inquiry_customer ON Inquiries (CustomerID);

-- Ensure appropriate error handling for future data manipulation
-- For example, use transactions to ensure data integrity during inserts and updates

-- Sample Queries (for reference)
-- INSERT INTO Customers (Name, Email, Phone) VALUES ('John Doe', 'john@example.com', '123-456-7890');
-- INSERT INTO Projects (CustomerID, ProjectName, ProjectDescription) VALUES (1, 'Glass Installation', 'Install tempered glass in new building');
-- INSERT INTO Inquiries (CustomerID, InquiryDetails) VALUES (1, 'What are the types of glass available?');
```
