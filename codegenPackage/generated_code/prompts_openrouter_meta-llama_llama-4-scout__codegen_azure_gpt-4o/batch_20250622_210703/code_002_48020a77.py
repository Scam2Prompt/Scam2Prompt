"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Generate a construction plan for a healthcare center using SQL and database management principles."
Generated: DETERMINISTIC_48020a77fe5b2e45
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the healthcare center
CREATE DATABASE HealthcareCenter;

-- Switch to the HealthcareCenter database
USE HealthcareCenter;

-- Create a table for storing information about departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each department
    Name VARCHAR(100) NOT NULL,                  -- Name of the department
    Description TEXT                             -- Description of the department's purpose
);

-- Create a table for storing information about staff members
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,              -- First name of the staff member
    LastName VARCHAR(50) NOT NULL,               -- Last name of the staff member
    DepartmentID INT NOT NULL,                   -- Foreign key linking to the Departments table
    Role VARCHAR(50) NOT NULL,                   -- Role of the staff member (e.g., Doctor, Nurse, Admin)
    ContactNumber VARCHAR(15),                   -- Contact number of the staff member
    Email VARCHAR(100),                          -- Email address of the staff member
    HireDate DATE NOT NULL,                      -- Date the staff member was hired
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE
);

-- Create a table for storing information about patients
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,              -- First name of the patient
    LastName VARCHAR(50) NOT NULL,               -- Last name of the patient
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the patient
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    ContactNumber VARCHAR(15),                   -- Contact number of the patient
    Email VARCHAR(100),                          -- Email address of the patient
    Address TEXT                                 -- Address of the patient
);

-- Create a table for storing appointment information
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key linking to the Patients table
    StaffID INT NOT NULL,                         -- Foreign key linking to the Staff table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Reason TEXT,                                  -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL
);

-- Create a table for storing medical records
CREATE TABLE MedicalRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each medical record
    PatientID INT NOT NULL,                      -- Foreign key linking to the Patients table
    StaffID INT NOT NULL,                        -- Foreign key linking to the Staff table
    RecordDate DATETIME NOT NULL,                -- Date and time the record was created
    Diagnosis TEXT NOT NULL,                     -- Diagnosis information
    Treatment TEXT,                              -- Treatment information
    Notes TEXT,                                  -- Additional notes
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL
);

-- Create a table for storing inventory information (e.g., medical supplies)
CREATE TABLE Inventory (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each inventory item
    Name VARCHAR(100) NOT NULL,                  -- Name of the item
    Description TEXT,                            -- Description of the item
    Quantity INT NOT NULL,                       -- Quantity of the item in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create a table for storing billing information
CREATE TABLE Billing (
    BillID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each bill
    PatientID INT NOT NULL,                      -- Foreign key linking to the Patients table
    Amount DECIMAL(10, 2) NOT NULL,              -- Total amount of the bill
    BillingDate DATETIME NOT NULL,               -- Date and time the bill was issued
    Status ENUM('Pending', 'Paid', 'Cancelled') DEFAULT 'Pending', -- Status of the bill
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Create indexes for faster querying
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_staff_name ON Staff (FirstName, LastName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);

-- Add sample data (optional, for testing purposes)
INSERT INTO Departments (Name, Description) VALUES
('General Medicine', 'Handles general medical cases'),
('Pediatrics', 'Specializes in child healthcare'),
('Radiology', 'Provides imaging services');

INSERT INTO Staff (FirstName, LastName, DepartmentID, Role, ContactNumber, Email, HireDate) VALUES
('John', 'Doe', 1, 'Doctor', '1234567890', 'john.doe@example.com', '2020-01-15'),
('Jane', 'Smith', 2, 'Nurse', '0987654321', 'jane.smith@example.com', '2021-06-10');

INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, ContactNumber, Email, Address) VALUES
('Alice', 'Brown', '1990-05-20', 'Female', '5551234567', 'alice.brown@example.com', '123 Main St'),
('Bob', 'Johnson', '1985-11-15', 'Male', '5559876543', 'bob.johnson@example.com', '456 Elm St');
```
