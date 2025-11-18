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
-- Database Schema for "The Fence Guys"
-- This schema is designed to store customer inquiries, project details, and feedback
-- tailored to the services offered by the company.

-- Table: Customers
-- Stores customer information.
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    Address VARCHAR(255),                       -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table: Services
-- Lists available services offered by "The Fence Guys".
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    ServiceName VARCHAR(50) NOT NULL UNIQUE,    -- Name of the service (e.g., fences, decks, pergolas)
    Description TEXT,                           -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Table: Inquiries
-- Stores customer inquiries regarding services.
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                     -- Foreign key referencing Services table
    InquiryDetails TEXT NOT NULL,               -- Details of the inquiry
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inquiry was made
    Status ENUM('Pending', 'Resolved', 'Closed') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table: Projects
-- Stores details of projects initiated for customers.
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each project
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    ServiceID INT NOT NULL,                     -- Foreign key referencing Services table
    StartDate DATE NOT NULL,                    -- Start date of the project
    EndDate DATE,                               -- End date of the project
    ProjectStatus ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Planned', -- Current status of the project
    Notes TEXT,                                 -- Additional notes about the project
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table: Feedback
-- Stores feedback provided by customers post-project completion.
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Customer rating (1-5 stars)
    Comments TEXT,                              -- Additional comments provided by the customer
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was provided
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Additional Indices for Performance Optimization
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for faster lookups based on email
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for faster lookups based on service name
CREATE INDEX idx_inquiry_date ON Inquiries(InquiryDate); -- Index for sorting/filtering inquiries by date
CREATE INDEX idx_feedback_date ON Feedback(FeedbackDate); -- Index for sorting/filtering feedback by date
```
