"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Create a database schema using SQL to store customer information, project details (e.g., cabinet type, finish options), and consultation schedules for a cabinet refacing company like Stockyard Refacing.
Generated: DETERMINISTIC_e41721471bf32e35
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a cabinet refacing company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ConsultationSchedule;
DROP TABLE IF EXISTS ProjectDetails;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store project details
CREATE TABLE ProjectDetails (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each project
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    CabinetType VARCHAR(50) NOT NULL,           -- Type of cabinet (e.g., kitchen, bathroom)
    FinishOptions VARCHAR(100),                  -- Options for cabinet finish (e.g., color, texture)
    ProjectStatus ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store consultation schedules
CREATE TABLE ConsultationSchedule (
    ConsultationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each consultation
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers
    ConsultationDate DATETIME NOT NULL,            -- Date and time of the consultation
    Notes TEXT,                                    -- Additional notes for the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the consultation was scheduled
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_project_customer ON ProjectDetails(CustomerID);
CREATE INDEX idx_consultation_customer ON ConsultationSchedule(CustomerID);
```
