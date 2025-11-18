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
-- SQL script to create a database schema for storing patient information, medical orders, and test results
-- Following best practices for naming conventions, normalization, and data integrity

-- Create a table for storing patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,             -- Patient's last name
    DateOfBirth DATE NOT NULL,                 -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                 -- Optional contact number for the patient
    Email VARCHAR(100),                        -- Optional email address of the patient
    Address TEXT                               -- Optional address field
);

-- Create a table for storing medical orders
CREATE TABLE MedicalOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each medical order
    PatientID INT NOT NULL,                    -- Foreign key to associate order with a patient
    OrderDate DATETIME NOT NULL,               -- Date and time when the order was created
    DoctorName VARCHAR(100),                   -- Name of the doctor who issued the order
    Notes TEXT,                                -- Additional notes for the order
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) -- Ensures referential integrity
);

-- Create a table for storing test results
CREATE TABLE TestResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each test result
    OrderID INT NOT NULL,                      -- Foreign key to associate the result with a medical order
    TestName ENUM('TGO', 'TGP', 'Colesterol Total', 'VIH') NOT NULL, -- Name of the test
    ResultValue DECIMAL(10, 2),                -- Numeric value for the test result
    Unit VARCHAR(20),                          -- Unit of measurement for the result (e.g., mg/dL, IU/L)
    ResultDate DATETIME NOT NULL,              -- Date and time when the test result was recorded
    Notes TEXT,                                -- Optional notes or observations about the test result
    FOREIGN KEY (OrderID) REFERENCES MedicalOrders(OrderID) -- Ensures referential integrity
);

-- Additional constraints and indices for optimization and data integrity
CREATE INDEX idx_patient_last_name ON Patients(LastName); -- Index for faster patient searches by last name
CREATE INDEX idx_order_date ON MedicalOrders(OrderDate);  -- Index for faster retrieval of orders by date
CREATE INDEX idx_test_result_date ON TestResults(ResultDate); -- Index for faster retrieval of test results by date
```
