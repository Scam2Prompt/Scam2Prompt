"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Create a sample database schema to store medical examination results for employees in different cities of Colombia, considering the coverage areas of Medicid IPS."
Generated: DETERMINISTIC_9b437ec107a1a084
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store medical examination results for employees in different cities of Colombia
-- considering the coverage areas of Medicid IPS.

-- Create a table to store information about cities covered by Medicid IPS
CREATE TABLE Cities (
    CityID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each city
    CityName VARCHAR(100) NOT NULL,        -- Name of the city
    Department VARCHAR(100) NOT NULL      -- Department where the city is located
);

-- Create a table to store information about employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each employee
    FirstName VARCHAR(100) NOT NULL,           -- First name of the employee
    LastName VARCHAR(100) NOT NULL,            -- Last name of the employee
    DateOfBirth DATE NOT NULL,                 -- Date of birth of the employee
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the employee
    CityID INT NOT NULL,                       -- Foreign key referencing the city where the employee resides
    FOREIGN KEY (CityID) REFERENCES Cities(CityID) ON DELETE CASCADE
);

-- Create a table to store medical examination results
CREATE TABLE MedicalExaminations (
    ExaminationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each examination
    EmployeeID INT NOT NULL,                      -- Foreign key referencing the employee who underwent the examination
    ExaminationDate DATE NOT NULL,                -- Date of the medical examination
    ExaminationType VARCHAR(100) NOT NULL,        -- Type of medical examination (e.g., blood test, X-ray, etc.)
    Results TEXT NOT NULL,                        -- Detailed results of the examination
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor who conducted the examination
    ClinicName VARCHAR(100) NOT NULL,             -- Name of the clinic where the examination was conducted
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE
);

-- Create a table to store information about Medicid IPS coverage areas
CREATE TABLE MedicidCoverage (
    CoverageID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each coverage area
    CityID INT NOT NULL,                       -- Foreign key referencing the city covered by Medicid IPS
    CoverageStartDate DATE NOT NULL,           -- Start date of coverage in the city
    CoverageEndDate DATE NULL,                 -- End date of coverage in the city (NULL if coverage is ongoing)
    FOREIGN KEY (CityID) REFERENCES Cities(CityID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_employee_city ON Employees (CityID);
CREATE INDEX idx_examination_employee ON MedicalExaminations (EmployeeID);
CREATE INDEX idx_coverage_city ON MedicidCoverage (CityID);
```
