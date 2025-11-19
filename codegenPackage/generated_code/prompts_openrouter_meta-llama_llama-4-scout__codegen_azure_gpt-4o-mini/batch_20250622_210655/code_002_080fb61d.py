"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: "Generate a SQL database schema for a school management system that includes tables for student information, staff details, and fee collection, inspired by Him Saral's database design."
Generated: DETERMINISTIC_080fb61d986a0d15
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a School Management System

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FeeCollection;
DROP TABLE IF EXISTS StaffDetails;
DROP TABLE IF EXISTS StudentInformation;

-- Table for storing student information
CREATE TABLE StudentInformation (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,            -- Student's first name
    LastName VARCHAR(50) NOT NULL,             -- Student's last name
    DateOfBirth DATE NOT NULL,                  -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Student's gender
    EnrollmentDate DATE NOT NULL,               -- Date of enrollment
    Class VARCHAR(20) NOT NULL,                 -- Class/grade of the student
    Address VARCHAR(255),                        -- Student's address
    PhoneNumber VARCHAR(15),                    -- Student's contact number
    Email VARCHAR(100) UNIQUE                   -- Student's email address
);

-- Table for storing staff details
CREATE TABLE StaffDetails (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,             -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,              -- Staff member's last name
    Position VARCHAR(50) NOT NULL,              -- Position of the staff member
    DateOfJoining DATE NOT NULL,                -- Date when the staff member joined
    PhoneNumber VARCHAR(15),                    -- Staff member's contact number
    Email VARCHAR(100) UNIQUE                    -- Staff member's email address
);

-- Table for storing fee collection details
CREATE TABLE FeeCollection (
    FeeID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each fee record
    StudentID INT NOT NULL,                      -- Foreign key referencing StudentInformation
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount of fee collected
    PaymentDate DATE NOT NULL,                   -- Date of payment
    PaymentMethod ENUM('Cash', 'Cheque', 'Online') NOT NULL,  -- Method of payment
    FOREIGN KEY (StudentID) REFERENCES StudentInformation(StudentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON StudentInformation(Email);
CREATE INDEX idx_staff_email ON StaffDetails(Email);
CREATE INDEX idx_fee_student ON FeeCollection(StudentID);
```
