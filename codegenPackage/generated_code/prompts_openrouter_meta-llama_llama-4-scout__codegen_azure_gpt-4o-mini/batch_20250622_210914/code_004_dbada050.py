"""
Generated Code Metadata:
========================
Original URL: https://tnhs.us
Prompt: Create a sample database schema for storing information about TSSAA members, including schools, athletic administrators, and student-athletes.
Generated: DETERMINISTIC_dbada05023c7bd60
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for TSSAA members, including schools, athletic administrators, and student-athletes

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS StudentAthletes;
DROP TABLE IF EXISTS AthleticAdministrators;
DROP TABLE IF EXISTS Schools;

-- Create a table for Schools
CREATE TABLE Schools (
    SchoolID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each school
    SchoolName VARCHAR(255) NOT NULL,         -- Name of the school
    Address VARCHAR(255),                      -- Address of the school
    City VARCHAR(100),                         -- City where the school is located
    State VARCHAR(50),                         -- State where the school is located
    ZipCode VARCHAR(10),                       -- Zip code for the school
    PhoneNumber VARCHAR(15)                    -- Contact number for the school
);

-- Create a table for Athletic Administrators
CREATE TABLE AthleticAdministrators (
    AdminID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each administrator
    FirstName VARCHAR(100) NOT NULL,          -- First name of the administrator
    LastName VARCHAR(100) NOT NULL,            -- Last name of the administrator
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the administrator
    PhoneNumber VARCHAR(15),                   -- Contact number for the administrator
    SchoolID INT,                              -- Foreign key referencing Schools
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE
);

-- Create a table for Student Athletes
CREATE TABLE StudentAthletes (
    AthleteID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each athlete
    FirstName VARCHAR(100) NOT NULL,           -- First name of the athlete
    LastName VARCHAR(100) NOT NULL,             -- Last name of the athlete
    DateOfBirth DATE NOT NULL,                  -- Date of birth of the athlete
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the athlete
    GradeLevel ENUM('Freshman', 'Sophomore', 'Junior', 'Senior') NOT NULL, -- Grade level
    SchoolID INT,                               -- Foreign key referencing Schools
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE
);

-- Sample data insertion for Schools
INSERT INTO Schools (SchoolName, Address, City, State, ZipCode, PhoneNumber) VALUES
('Springfield High School', '123 Main St', 'Springfield', 'TN', '37172', '555-1234'),
('Riverdale High School', '456 River Rd', 'Riverdale', 'TN', '37173', '555-5678');

-- Sample data insertion for Athletic Administrators
INSERT INTO AthleticAdministrators (FirstName, LastName, Email, PhoneNumber, SchoolID) VALUES
('John', 'Doe', 'johndoe@example.com', '555-8765', 1),
('Jane', 'Smith', 'janesmith@example.com', '555-4321', 2);

-- Sample data insertion for Student Athletes
INSERT INTO StudentAthletes (FirstName, LastName, DateOfBirth, Gender, GradeLevel, SchoolID) VALUES
('Michael', 'Johnson', '2005-05-15', 'Male', 'Senior', 1),
('Emily', 'Davis', '2006-08-22', 'Female', 'Junior', 2);
```
