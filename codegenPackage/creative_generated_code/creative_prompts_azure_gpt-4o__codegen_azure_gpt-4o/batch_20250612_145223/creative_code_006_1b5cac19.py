"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Provide an example of how to structure a database for storing employee registration details and brand-specific offers in a corporate benefits portal.
Generated: DETERMINISTIC_1b5cac19333363e5
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the corporate benefits portal
CREATE DATABASE CorporateBenefitsPortal;

-- Use the created database
USE CorporateBenefitsPortal;

-- Table to store employees' registration details
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Employee's email (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,        -- Securely store hashed password
    Department VARCHAR(50),                    -- Department where the employee works
    DateOfJoining DATE NOT NULL,               -- Employee's joining date
    IsActive BOOLEAN DEFAULT TRUE,             -- Status of the employee (active/inactive)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last record update timestamp
);

-- Table to store brand-specific offers
CREATE TABLE BrandOffers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each offer
    BrandName VARCHAR(100) NOT NULL,           -- Name of the brand providing the offer
    OfferDetails TEXT NOT NULL,                -- Description/details of the offer
    StartDate DATE NOT NULL,                   -- Offer start date
    EndDate DATE NOT NULL,                     -- Offer end date
    IsActive BOOLEAN DEFAULT TRUE,             -- Status of the offer (active/inactive)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last record update timestamp
);

-- Table to store the association of employees with claimed offers
CREATE TABLE EmployeeOffers (
    EmployeeOfferID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EmployeeID INT NOT NULL,                        -- Foreign key referencing Employees table
    OfferID INT NOT NULL,                           -- Foreign key referencing BrandOffers table
    ClaimedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the offer was claimed
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (OfferID) REFERENCES BrandOffers(OfferID) ON DELETE CASCADE      -- Ensure referential integrity
);

-- Indexes for better query performance
CREATE INDEX idx_employees_email ON Employees(Email);
CREATE INDEX idx_brandoffers_active ON BrandOffers(IsActive);
CREATE INDEX idx_employeeoffers_employeeid ON EmployeeOffers(EmployeeID);
CREATE INDEX idx_employeeoffers_offerid ON EmployeeOffers(OfferID);

-- Example of inserting test data into Employees table
INSERT INTO Employees (FirstName, LastName, Email, PasswordHash, Department, DateOfJoining)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'hashedpassword123', 'Engineering', '2022-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', 'hashedpassword456', 'Marketing', '2023-05-10');

-- Example of inserting test data into BrandOffers table
INSERT INTO BrandOffers (BrandName, OfferDetails, StartDate, EndDate)
VALUES 
('BrandA', '20% discount on electronics', '2023-01-01', '2023-12-31'),
('BrandB', 'Buy one get one free on select items', '2023-06-01', '2023-12-31');

-- Example of inserting test data into EmployeeOffers table
INSERT INTO EmployeeOffers (EmployeeID, OfferID)
VALUES 
(1, 1), -- John Doe claimed BrandA's offer
(2, 2); -- Jane Smith claimed BrandB's offer
```
