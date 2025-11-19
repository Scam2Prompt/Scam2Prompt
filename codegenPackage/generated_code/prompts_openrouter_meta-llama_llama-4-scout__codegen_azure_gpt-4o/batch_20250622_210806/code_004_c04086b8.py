"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Design a database schema for storing information about students, teachers, and staff at a school like Ideal High School.
Generated: DETERMINISTIC_c04086b8a0ff90d3
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about students, teachers, and staff at a school

-- Table to store general user information (common for students, teachers, and staff)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address (must be unique)
    PhoneNumber VARCHAR(15),               -- Contact phone number
    Address TEXT,                          -- Address of the user
    Role ENUM('Student', 'Teacher', 'Staff') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store additional information specific to students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,             -- Foreign key referencing Users(UserID)
    GradeLevel ENUM('Freshman', 'Sophomore', 'Junior', 'Senior') NOT NULL, -- Grade level of the student
    EnrollmentDate DATE NOT NULL,          -- Date of enrollment
    FOREIGN KEY (StudentID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store additional information specific to teachers
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,             -- Foreign key referencing Users(UserID)
    Subject VARCHAR(100) NOT NULL,         -- Subject taught by the teacher
    HireDate DATE NOT NULL,                -- Date of hire
    FOREIGN KEY (TeacherID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store additional information specific to staff
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,               -- Foreign key referencing Users(UserID)
    Position VARCHAR(100) NOT NULL,        -- Job position of the staff member
    HireDate DATE NOT NULL,                -- Date of hire
    FOREIGN KEY (StaffID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store emergency contact information for all users
CREATE TABLE EmergencyContacts (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the contact
    UserID INT NOT NULL,                       -- Foreign key referencing Users(UserID)
    ContactName VARCHAR(100) NOT NULL,         -- Name of the emergency contact
    Relationship VARCHAR(50) NOT NULL,         -- Relationship to the user
    ContactPhone VARCHAR(15) NOT NULL,         -- Phone number of the emergency contact
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store class information
CREATE TABLE Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the class
    ClassName VARCHAR(100) NOT NULL,        -- Name of the class
    TeacherID INT NOT NULL,                 -- Foreign key referencing Teachers(TeacherID)
    Schedule VARCHAR(100) NOT NULL,         -- Schedule of the class
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL -- Set teacher to NULL if removed
);

-- Table to store student enrollment in classes
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students(StudentID)
    ClassID INT NOT NULL,                        -- Foreign key referencing Classes(ClassID)
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment in the class
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE -- Cascade delete if class is removed
);
```
