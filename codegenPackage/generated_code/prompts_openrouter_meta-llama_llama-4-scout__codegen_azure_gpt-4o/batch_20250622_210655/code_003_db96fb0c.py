"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Design a database schema to store information about courses, students, and certifications for an educational institution like Geta Consulenze. Provide the schema in SQL format."
Generated: DETERMINISTIC_db96fb0cd9e09c05
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an educational institution to store information about courses, students, and certifications

-- Create a table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE,                         -- Date of birth of the student
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time of registration
);

-- Create a table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    DurationInHours INT NOT NULL,            -- Duration of the course in hours
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time when the course was created
);

-- Create a table to store information about certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    CertificationName VARCHAR(100) NOT NULL,        -- Name of the certification
    IssuedBy VARCHAR(100) NOT NULL,                 -- Organization or entity issuing the certification
    ValidityInYears INT,                            -- Validity period of the certification in years
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Date and time when the certification was created
);

-- Create a table to store the relationship between students and courses (enrollments)
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Status of the enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table to store the relationship between students and certifications
CREATE TABLE StudentCertifications (
    StudentCertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student certification
    StudentID INT NOT NULL,                                -- Foreign key referencing Students table
    CertificationID INT NOT NULL,                         -- Foreign key referencing Certifications table
    DateIssued DATE NOT NULL,                             -- Date when the certification was issued
    ExpiryDate DATE,                                      -- Expiry date of the certification (if applicable)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_email ON Students(Email); -- Index on email for faster lookups
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index on course name for faster lookups
CREATE INDEX idx_certification_name ON Certifications(CertificationName); -- Index on certification name for faster lookups
```
