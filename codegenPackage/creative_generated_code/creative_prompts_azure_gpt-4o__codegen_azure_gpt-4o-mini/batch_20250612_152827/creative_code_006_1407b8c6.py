"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Create a database schema for storing patient information, medical orders, and test results for a clinical laboratory, including fields for tests like "TGO," "TGP," "colesterol total," and "VIH."
Generated: DETERMINISTIC_1407b8c68e0e475a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a clinical laboratory to store patient information,
-- medical orders, and test results.

CREATE DATABASE ClinicalLaboratory;

USE ClinicalLaboratory;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,                -- Patient's first name
    LastName VARCHAR(50) NOT NULL,                  -- Patient's last name
    DateOfBirth DATE NOT NULL,                      -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                        -- Patient's phone number
    Email VARCHAR(100) UNIQUE,                      -- Patient's email address
    Address VARCHAR(255),                           -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when the patient record was created
);

-- Table to store medical orders
CREATE TABLE MedicalOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each medical order
    PatientID INT NOT NULL,                         -- Reference to the patient
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the order
    PhysicianName VARCHAR(100) NOT NULL,           -- Name of the physician who placed the order
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) -- Foreign key constraint
);

-- Table to store test results
CREATE TABLE TestResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each test result
    OrderID INT NOT NULL,                           -- Reference to the medical order
    TGO DECIMAL(5,2),                              -- Test result for TGO
    TGP DECIMAL(5,2),                              -- Test result for TGP
    CholesterolTotal DECIMAL(5,2),                 -- Test result for cholesterol total
    VIH ENUM('Positive', 'Negative') NOT NULL,     -- Test result for VIH
    ResultDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the test result
    FOREIGN KEY (OrderID) REFERENCES MedicalOrders(OrderID) -- Foreign key constraint
);

-- Sample error handling can be implemented in application code when performing CRUD operations on these tables.
-- Ensure to handle exceptions and rollback transactions where necessary in real-world applications.
```
