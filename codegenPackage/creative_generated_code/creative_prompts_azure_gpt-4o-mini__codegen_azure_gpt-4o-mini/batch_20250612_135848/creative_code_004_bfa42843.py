"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buforddental.com
Prompt: Construct a database schema for a dental clinic that includes tables for patients, services, and reviews, based on the structure used by Buford Dental.
Generated: DETERMINISTIC_bfa42843abfded17
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for a dental clinic
-- Includes tables for Patients, Services, and Reviews

-- Create database
CREATE DATABASE DentalClinic;

-- Use the created database
USE DentalClinic;

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL, -- First name of the patient
    LastName VARCHAR(50) NOT NULL, -- Last name of the patient
    DateOfBirth DATE NOT NULL, -- Date of birth of the patient
    PhoneNumber VARCHAR(15) NOT NULL, -- Contact number for the patient
    Email VARCHAR(100) NOT NULL UNIQUE, -- Email address of the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered by the clinic
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL, -- Name of the service
    Description TEXT, -- Description of the service
    Price DECIMAL(10, 2) NOT NULL, -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store reviews from patients about their services
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    PatientID INT NOT NULL, -- Foreign key to link reviews to patients
    ServiceID INT NOT NULL, -- Foreign key to link reviews to services
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the patient (1 to 5)
    Comment TEXT, -- Optional comment from the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Review creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Review update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure integrity of patient data
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure integrity of service data
);

-- Indexes for efficient querying
CREATE INDEX idx_patient_email ON Patients (Email);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_review_patient_service ON Reviews (PatientID, ServiceID);
```
