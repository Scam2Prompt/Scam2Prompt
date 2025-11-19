"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Design a database schema to store information about Batıkent Tofaş Spor Klübü's fitness classes, trainers, and members, and write a SQL query to retrieve the class schedule for a specific day.
Generated: DETERMINISTIC_e4c45b65ed4092b5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Batıkent Tofaş Spor Klübü's fitness classes, trainers, and members

-- Table to store information about trainers
CREATE TABLE Trainers (
    TrainerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Specialty VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100) UNIQUE
);

-- Table to store information about members
CREATE TABLE Members (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    JoinDate DATE DEFAULT CURRENT_DATE
);

-- Table to store fitness classes
CREATE TABLE FitnessClasses (
    ClassID INT PRIMARY KEY AUTO_INCREMENT,
    ClassName VARCHAR(100) NOT NULL,
    TrainerID INT,
    ClassDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    Capacity INT,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

-- Table to store attendance records for members in classes
CREATE TABLE ClassAttendance (
    AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
    ClassID INT,
    MemberID INT,
    AttendanceDate DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (ClassID) REFERENCES FitnessClasses(ClassID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- SQL query to retrieve the class schedule for a specific day
-- Replace '2023-10-01' with the desired date to query
SELECT 
    fc.ClassName,
    t.FirstName AS TrainerFirstName,
    t.LastName AS TrainerLastName,
    fc.StartTime,
    fc.EndTime,
    fc.Capacity
FROM 
    FitnessClasses fc
JOIN 
    Trainers t ON fc.TrainerID = t.TrainerID
WHERE 
    fc.ClassDate = '2023-10-01'
ORDER BY 
    fc.StartTime;
```
