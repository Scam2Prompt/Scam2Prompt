"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Create a database schema for storing customer inquiries, project details, and feedback, tailored to the services offered by "The Fence Guys" (fences, decks, pergolas).
Generated: DETERMINISTIC_a4cbee7caf2a7c9b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for "The Fence Guys" to store customer inquiries, project details, and feedback

-- Create a database
CREATE DATABASE TheFenceGuys;

-- Use the created database
USE TheFenceGuys;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store inquiries from customers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the inquiry
    ServiceType ENUM('Fence', 'Deck', 'Pergola') NOT NULL, -- Type of service requested
    Description TEXT NOT NULL,                   -- Description of the inquiry
    Status ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    InquiryID INT NOT NULL,                       -- Foreign key referencing Inquiries
    ProjectStartDate DATE NOT NULL,              -- Start date of the project
    ProjectEndDate DATE,                         -- End date of the project (nullable)
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the project
    Status ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started', -- Current status of the project
    FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback from customers
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each feedback entry
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    Comments TEXT,                                 -- Additional comments from the customer
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_inquiry_status ON Inquiries(Status);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_feedback_rating ON Feedback(Rating);
```
