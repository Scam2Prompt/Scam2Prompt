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
-- School Management System Database Schema

-- Table: Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Address TEXT,                             -- Student's address
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    Class VARCHAR(20) NOT NULL                -- Class/Grade the student is enrolled in
);

-- Table: Staff
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,           -- Staff's first name
    LastName VARCHAR(50) NOT NULL,            -- Staff's last name
    DateOfBirth DATE NOT NULL,                -- Staff's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the staff member
    Address TEXT,                             -- Staff's address
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    HireDate DATE NOT NULL,                   -- Date of hiring
    Position VARCHAR(50) NOT NULL,            -- Job position/title
    Salary DECIMAL(10, 2) NOT NULL            -- Monthly salary
);

-- Table: FeeCollection
CREATE TABLE FeeCollection (
    FeeID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each fee transaction
    StudentID INT NOT NULL,                   -- Foreign key referencing Students table
    Amount DECIMAL(10, 2) NOT NULL,           -- Fee amount collected
    PaymentDate DATE NOT NULL,                -- Date of payment
    PaymentMethod ENUM('Cash', 'Card', 'Online') NOT NULL, -- Payment method
    Remarks TEXT,                             -- Additional remarks or notes
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Establish relationship with Students table
);

-- Indexes for optimization
CREATE INDEX idx_students_class ON Students(Class); -- Index for faster queries on class
CREATE INDEX idx_staff_position ON Staff(Position); -- Index for faster queries on position
CREATE INDEX idx_fee_student ON FeeCollection(StudentID); -- Index for faster queries on student fees

-- Error handling and constraints
-- Ensure email addresses are unique for both Students and Staff
ALTER TABLE Students ADD CONSTRAINT unique_student_email UNIQUE (Email);
ALTER TABLE Staff ADD CONSTRAINT unique_staff_email UNIQUE (Email);

-- Ensure fee amount is positive
ALTER TABLE FeeCollection ADD CONSTRAINT check_fee_amount CHECK (Amount > 0);
```
