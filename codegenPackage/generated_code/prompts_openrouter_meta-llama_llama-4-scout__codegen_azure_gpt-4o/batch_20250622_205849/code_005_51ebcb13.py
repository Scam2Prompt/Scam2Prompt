"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Design a database schema for a medical laboratory technology application, inspired by RSP Bharat's Diploma in Medical Laboratory Technology (DMLT) course."
Generated: DETERMINISTIC_51ebcb13fe077b40
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Medical Laboratory Technology Application

-- Table: Users
-- Stores information about users (students, staff, administrators)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Role ENUM('Student', 'Staff', 'Admin') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Courses
-- Stores information about courses offered in the DMLT program
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    DurationWeeks INT NOT NULL,              -- Duration of the course in weeks
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of course creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Enrollments
-- Tracks which users are enrolled in which courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Status of enrollment
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete
);

-- Table: Tests
-- Stores information about medical tests available in the laboratory
CREATE TABLE Tests (
    TestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each test
    TestName VARCHAR(100) NOT NULL,        -- Name of the test
    Description TEXT,                      -- Description of the test
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the test
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of test creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: TestResults
-- Stores results of medical tests conducted for users
CREATE TABLE TestResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each test result
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    TestID INT NOT NULL,                     -- Foreign key referencing Tests table
    ResultData TEXT NOT NULL,                -- Data/results of the test
    TestDate DATE NOT NULL,                  -- Date the test was conducted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (TestID) REFERENCES Tests(TestID) ON DELETE CASCADE -- Cascade delete
);

-- Table: StaffAssignments
-- Tracks which staff members are assigned to which tests
CREATE TABLE StaffAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    StaffID INT NOT NULL,                        -- Foreign key referencing Users table (staff role)
    TestID INT NOT NULL,                         -- Foreign key referencing Tests table
    AssignmentDate DATE NOT NULL,                -- Date of assignment
    FOREIGN KEY (StaffID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (TestID) REFERENCES Tests(TestID) ON DELETE CASCADE -- Cascade delete
);

-- Table: Notifications
-- Stores notifications for users
CREATE TABLE Notifications (
    NotificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each notification
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    Message TEXT NOT NULL,                         -- Notification message
    IsRead BOOLEAN DEFAULT FALSE,                 -- Whether the notification has been read
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of notification creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes and Constraints
-- Adding indexes for faster queries
CREATE INDEX idx_user_email ON Users(Email);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_test_name ON Tests(TestName);
```
