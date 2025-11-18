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
-- Database schema for storing customer inquiries and project details.

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the customer
    FullName VARCHAR(100) NOT NULL,            -- Customer's full name
    Email VARCHAR(150) UNIQUE NOT NULL,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CompanyName VARCHAR(100),                  -- Name of the customer's company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the entry was last updated
);

-- Create a table to store inquiries from customers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the inquiry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the customer
    InquiryType ENUM('Glass', 'Aluminum', 'Other') NOT NULL, -- Type of inquiry (processed glass, aluminum solutions, etc.)
    InquiryDetails TEXT NOT NULL,              -- Detailed description of the inquiry
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the inquiry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inquiry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the inquiry was last updated
    CONSTRAINT FK_Customer_Inquiry FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create a table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the project
    InquiryID INT NOT NULL,                    -- Foreign key referencing the inquiry
    ProjectName VARCHAR(100) NOT NULL,         -- Name of the project
    Description TEXT,                          -- Description of the project
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date
    Budget DECIMAL(15, 2),                     -- Budget allocated for the project
    Status ENUM('Not Started', 'Active', 'Completed', 'On Hold', 'Cancelled') DEFAULT 'Not Started', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the project was last updated
    CONSTRAINT FK_Inquiry_Project FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID) ON DELETE CASCADE
);

-- Create indexes to improve query performance
CREATE INDEX IDX_Customers_Email ON Customers(Email); -- Index on email for faster lookups
CREATE INDEX IDX_Inquiries_Status ON Inquiries(Status); -- Index on status for faster filtering
CREATE INDEX IDX_Projects_Status ON Projects(Status); -- Index on project status for faster filtering
```
