"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Suggest a suitable database schema for storing patient information, test results, and doctor's orders for a clinical laboratory with services like LabVida's.
Generated: DETERMINISTIC_6ee9ed85f35d8fc7
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the clinical laboratory
CREATE DATABASE ClinicalLab;

-- Use the ClinicalLab database
USE ClinicalLab;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table for doctors
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    MedicalLicenseNumber VARCHAR(50) UNIQUE NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DoctorID)
);

-- Create a table for test types
CREATE TABLE TestTypes (
    TestTypeID INT AUTO_INCREMENT,
    TestName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestTypeID)
);

-- Create a table for test results
CREATE TABLE TestResults (
    TestResultID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    TestTypeID INT NOT NULL,
    TestDate DATE NOT NULL,
    Result VARCHAR(255) NOT NULL,
    ReferenceRange VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestResultID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID)
);

-- Create a table for doctor's orders
CREATE TABLE DoctorsOrders (
    OrderID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TestTypeID INT NOT NULL,
    SpecialInstructions TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (TestTypeID) REFERENCES TestTypes(TestTypeID)
);

-- Create a table for lab staff
CREATE TABLE LabStaff (
    StaffID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Role ENUM('Lab Technician', 'Lab Manager', 'Medical Laboratory Scientist') NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (StaffID)
);

-- Create a table for test status
CREATE TABLE TestStatus (
    TestStatusID INT AUTO_INCREMENT,
    TestResultID INT NOT NULL,
    StaffID INT NOT NULL,
    Status ENUM('Pending', 'In Progress', 'Completed', 'Verified') NOT NULL,
    Comments TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TestStatusID),
    FOREIGN KEY (TestResultID) REFERENCES TestResults(TestResultID),
    FOREIGN KEY (StaffID) REFERENCES LabStaff(StaffID)
);

-- Example insert statements
INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, Address, Phone, Email)
VALUES ('John', 'Doe', '1990-01-01', 'Male', '123 Main St', '123-456-7890', 'john.doe@example.com');

INSERT INTO Doctors (FirstName, LastName, MedicalLicenseNumber, Address, Phone, Email)
VALUES ('Jane', 'Smith', 'MD12345', '456 Elm St', '987-654-3210', 'jane.smith@example.com');

INSERT INTO TestTypes (TestName, Description)
VALUES ('Complete Blood Count', 'Measures various components of blood');

INSERT INTO TestResults (PatientID, TestTypeID, TestDate, Result, ReferenceRange)
VALUES (1, 1, '2022-01-01', 'Normal', '4.32-5.72 million cells/μL');

INSERT INTO DoctorsOrders (PatientID, DoctorID, OrderDate, TestTypeID, SpecialInstructions)
VALUES (1, 1, '2022-01-01', 1, 'Fasting required');

INSERT INTO LabStaff (FirstName, LastName, Role, Address, Phone, Email)
VALUES ('Bob', 'Johnson', 'Lab Technician', '789 Oak St', '555-123-4567', 'bob.johnson@example.com');

INSERT INTO TestStatus (TestResultID, StaffID, Status, Comments)
VALUES (1, 1, 'Completed', 'Result verified by lab manager');
```
