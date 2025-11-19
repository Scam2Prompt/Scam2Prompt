"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Design a database schema to store information about investment education firms, their courses, and student registrations.
Generated: DETERMINISTIC_f8399a010210f242
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about investment education firms, their courses, and student registrations

-- Create a table to store information about investment education firms
CREATE TABLE InvestmentFirms (
    FirmID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each firm
    FirmName VARCHAR(255) NOT NULL,         -- Name of the investment education firm
    Address VARCHAR(255),                    -- Address of the firm
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Email VARCHAR(255) UNIQUE,               -- Contact email address
    Website VARCHAR(255)                     -- Website URL
);

-- Create a table to store information about courses offered by the firms
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    FirmID INT NOT NULL,                      -- Foreign key referencing the InvestmentFirms table
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                         -- Description of the course
    StartDate DATE,                          -- Start date of the course
    EndDate DATE,                            -- End date of the course
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the course
    FOREIGN KEY (FirmID) REFERENCES InvestmentFirms(FirmID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store information about student registrations for courses
CREATE TABLE StudentRegistrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each registration
    CourseID INT NOT NULL,                          -- Foreign key referencing the Courses table
    StudentName VARCHAR(255) NOT NULL,             -- Name of the student
    StudentEmail VARCHAR(255) NOT NULL,            -- Email of the student
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of registration
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_firm_name ON InvestmentFirms(FirmName);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_student_email ON StudentRegistrations(StudentEmail);
```
