"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stockyardrefacing.com
Prompt: Create a database schema using SQL to store customer information, project details (e.g., cabinet type, finish options), and consultation schedules for a cabinet refacing company like Stockyard Refacing.
Generated: DETERMINISTIC_e41721471bf32e35
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Cabinet Refacing Company

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address, must be unique
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's phone number
    Address VARCHAR(255),                      -- Customer's address
    City VARCHAR(50),                          -- Customer's city
    State VARCHAR(50),                         -- Customer's state
    ZipCode VARCHAR(10),                       -- Customer's ZIP code
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store project details
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    CabinetType VARCHAR(100) NOT NULL,         -- Type of cabinet (e.g., kitchen, bathroom)
    FinishOption VARCHAR(100),                 -- Finish option selected (e.g., matte, glossy)
    EstimatedCost DECIMAL(10, 2),              -- Estimated cost of the project
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date
    Status VARCHAR(50) DEFAULT 'Pending',      -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) 
    ON DELETE CASCADE                          -- Cascade delete when a customer is deleted
);

-- Create a table to store consultation schedules
CREATE TABLE Consultations (
    ConsultationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each consultation
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers table
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects table
    ConsultationDate DATETIME NOT NULL,            -- Date and time of the consultation
    Notes TEXT,                                    -- Notes or comments about the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    ON DELETE CASCADE,                             -- Cascade delete when a customer is deleted
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
    ON DELETE CASCADE                              -- Cascade delete when a project is deleted
);

-- Additional indexes for optimization
CREATE INDEX idx_Customers_Email ON Customers (Email); -- Index for faster lookups by email
CREATE INDEX idx_Projects_CustomerID ON Projects (CustomerID); -- Index for faster customer-project lookups
CREATE INDEX idx_Consultations_ConsultationDate ON Consultations (ConsultationDate); -- Index for faster consultation scheduling
```
