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
-- Inspired by Him Saral's design principles

-- Create database
CREATE DATABASE SchoolManagementSystem;
USE SchoolManagementSystem;

-- Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Address TEXT NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    AdmissionDate DATE NOT NULL,
    ClassID INT,
    SectionID INT,
    Status ENUM('Active', 'Inactive', 'Graduated', 'Transferred') DEFAULT 'Active',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (ClassID),
    INDEX (SectionID)
);

-- Staff table
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Address TEXT NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Qualification VARCHAR(100) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    JoiningDate DATE NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    Status ENUM('Active', 'Inactive', 'Retired', 'Resigned') DEFAULT 'Active',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Classes table
CREATE TABLE Classes (
    ClassID INT PRIMARY KEY AUTO_INCREMENT,
    ClassName VARCHAR(50) NOT NULL,
    NumericValue INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Sections table
CREATE TABLE Sections (
    SectionID INT PRIMARY KEY AUTO_INCREMENT,
    SectionName VARCHAR(50) NOT NULL,
    ClassID INT NOT NULL,
    TeacherID INT,
    Capacity INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (TeacherID) REFERENCES Staff(StaffID),
    INDEX (ClassID),
    INDEX (TeacherID)
);

-- Subjects table
CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY AUTO_INCREMENT,
    SubjectName VARCHAR(100) NOT NULL,
    SubjectCode VARCHAR(20) NOT NULL,
    ClassID INT NOT NULL,
    TeacherID INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (TeacherID) REFERENCES Staff(StaffID),
    INDEX (ClassID),
    INDEX (TeacherID)
);

-- Fee structure table
CREATE TABLE FeeStructure (
    FeeStructureID INT PRIMARY KEY AUTO_INCREMENT,
    ClassID INT NOT NULL,
    FeeType VARCHAR(50) NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    Frequency ENUM('Monthly', 'Quarterly', 'Half-Yearly', 'Yearly') NOT NULL,
    EffectiveFrom DATE NOT NULL,
    EffectiveTo DATE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    INDEX (ClassID)
);

-- Fee collection table
CREATE TABLE FeeCollection (
    FeeCollectionID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT NOT NULL,
    FeeStructureID INT NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentMode ENUM('Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Online Payment') NOT NULL,
    TransactionReference VARCHAR(100),
    Status ENUM('Paid', 'Unpaid', 'Partial', 'Cancelled') DEFAULT 'Paid',
    CollectedBy INT NOT NULL,
    Remarks TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (FeeStructureID) REFERENCES FeeStructure(FeeStructureID),
    FOREIGN KEY (CollectedBy) REFERENCES Staff(StaffID),
    INDEX (StudentID),
    INDEX (FeeStructureID),
    INDEX (CollectedBy)
);

-- Attendance table
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT NOT NULL,
    Date DATE NOT NULL,
    Status ENUM('Present', 'Absent', 'Half Day', 'Leave') NOT NULL,
    Remarks TEXT,
    RecordedBy INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (RecordedBy) REFERENCES Staff(StaffID),
    INDEX (StudentID),
    INDEX (RecordedBy)
);

-- Exams table
CREATE TABLE Exams (
    ExamID INT PRIMARY KEY AUTO_INCREMENT,
    ExamName VARCHAR(100) NOT NULL,
    ClassID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    INDEX (ClassID)
);

-- Exam results table
CREATE TABLE ExamResults (
    ResultID INT PRIMARY KEY AUTO_INCREMENT,
    ExamID INT NOT NULL,
    StudentID INT NOT NULL,
    SubjectID INT NOT NULL,
    MarksObtained DECIMAL(5,2) NOT NULL,
    MaxMarks DECIMAL(5,2) NOT NULL,
    Grade VARCHAR(5),
    Remarks TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ExamID) REFERENCES Exams(ExamID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID),
    INDEX (ExamID),
    INDEX (StudentID),
    INDEX (SubjectID)
);

-- Add foreign keys to Students table
ALTER TABLE Students
ADD FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
ADD FOREIGN KEY (SectionID) REFERENCES Sections(SectionID);
```
