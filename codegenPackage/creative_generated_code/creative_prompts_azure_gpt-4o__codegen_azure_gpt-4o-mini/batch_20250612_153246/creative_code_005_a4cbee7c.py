"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Create a database schema for storing customer inquiries, project details, and feedback, tailored to the services offered by "The Fence Guys" (fences, decks, pergolas).
Generated: DETERMINISTIC_a4cbee7caf2a7c9b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer inquiries, project details, and feedback
-- for "The Fence Guys" (fences, decks, pergolas)

-- Create the database
CREATE DATABASE TheFenceGuys;

-- Use the created database
USE TheFenceGuys;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email (must be unique)
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store inquiries made by customers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                     -- Foreign key linked to Customers table
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the inquiry
    InquiryType ENUM('Fence', 'Deck', 'Pergola') NOT NULL, -- Type of inquiry
    Description TEXT,                            -- Detailed description of the inquiry
    Status ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each project
    CustomerID INT NOT NULL,                      -- Foreign key linked to Customers table
    ProjectType ENUM('Fence', 'Deck', 'Pergola') NOT NULL, -- Type of project
    ProjectDescription TEXT,                      -- Description of the project
    StartDate DATE,                              -- Start date of the project
    EndDate DATE,                                -- End date of the project
    Status ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started', -- Current project status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store feedback from customers
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each feedback
    CustomerID INT NOT NULL,                      -- Foreign key linked to Customers table
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of feedback submission
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating out of 5
    Comments TEXT,                                -- Comments provided by the customer
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Ensure proper indexing for performance on frequently queried fields
CREATE INDEX idx_inquiry_customer ON Inquiries(CustomerID);
CREATE INDEX idx_project_customer ON Projects(CustomerID);
CREATE INDEX idx_feedback_customer ON Feedback(CustomerID);
```
