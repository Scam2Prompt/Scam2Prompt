"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Design a simple database schema for storing information about medical professionals, including details like name, specialty, and contact information, similar to what might be used by the team at Medizinisches Gutachteninstitut Döbeln.
Generated: DETERMINISTIC_4b18e45b2724dad9
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing medical professional information
CREATE DATABASE MedicalProfessionalsDB;

-- Use the created database
USE MedicalProfessionalsDB;

-- Create a table for medical specialties
CREATE TABLE MedicalSpecialties (
    SpecialtyID INT AUTO_INCREMENT,
    SpecialtyName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SpecialtyID)
);

-- Create a table for medical professionals
CREATE TABLE MedicalProfessionals (
    ProfessionalID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    SpecialtyID INT,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProfessionalID),
    FOREIGN KEY (SpecialtyID) REFERENCES MedicalSpecialties(SpecialtyID) ON DELETE SET NULL
);

-- Create a table for contact information
CREATE TABLE ContactInformation (
    ContactID INT AUTO_INCREMENT,
    ProfessionalID INT,
    ContactType ENUM('phone', 'email', 'address') NOT NULL,
    ContactValue VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ContactID),
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID) ON DELETE CASCADE
);

-- Insert sample data into MedicalSpecialties table
INSERT INTO MedicalSpecialties (SpecialtyName, Description)
VALUES 
('Cardiology', 'Deals with disorders of the heart and blood vessels'),
('Neurology', 'Deals with disorders of the brain and nervous system'),
('Oncology', 'Deals with the study and treatment of tumors');

-- Insert sample data into MedicalProfessionals table
INSERT INTO MedicalProfessionals (FirstName, LastName, SpecialtyID, Email, Phone, Address)
VALUES 
('John', 'Doe', 1, 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 2, 'jane.smith@example.com', '987-654-3210', '456 Elm St'),
('Bob', 'Johnson', 3, 'bob.johnson@example.com', '555-123-4567', '789 Oak St');

-- Insert sample data into ContactInformation table
INSERT INTO ContactInformation (ProfessionalID, ContactType, ContactValue)
VALUES 
(1, 'phone', '123-456-7890'),
(1, 'email', 'john.doe@example.com'),
(2, 'phone', '987-654-3210'),
(3, 'address', '789 Oak St');
```
