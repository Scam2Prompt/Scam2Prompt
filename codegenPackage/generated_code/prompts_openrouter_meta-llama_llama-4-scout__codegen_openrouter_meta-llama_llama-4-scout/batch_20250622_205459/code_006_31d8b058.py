"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write a SQL query to manage training schedules for environmental and safety training courses offered by iSi Environmental.
Generated: DETERMINISTIC_31d8b0589cf79e5e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing training schedules

-- Create table for courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT,
    CourseName VARCHAR(255) NOT NULL,
    CourseDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CourseID)
);

-- Create table for trainers
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT,
    TrainerName VARCHAR(255) NOT NULL,
    TrainerEmail VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TrainerID)
);

-- Create table for training schedules
CREATE TABLE TrainingSchedules (
    ScheduleID INT AUTO_INCREMENT,
    CourseID INT NOT NULL,
    TrainerID INT NOT NULL,
    ScheduleDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    Location VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ScheduleID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID)
);

-- Create table for attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT,
    ScheduleID INT NOT NULL,
    AttendeeName VARCHAR(255) NOT NULL,
    AttendeeEmail VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AttendeeID),
    FOREIGN KEY (ScheduleID) REFERENCES TrainingSchedules(ScheduleID)
);

-- Insert sample data
INSERT INTO Courses (CourseName, CourseDescription)
VALUES 
('Environmental Safety Training', 'Training on environmental safety procedures'),
('Hazardous Materials Handling', 'Training on handling hazardous materials');

INSERT INTO Trainers (TrainerName, TrainerEmail)
VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');

INSERT INTO TrainingSchedules (CourseID, TrainerID, ScheduleDate, StartTime, EndTime, Location)
VALUES 
(1, 1, '2024-09-17', '09:00:00', '12:00:00', 'Conference Room'),
(2, 2, '2024-09-18', '10:00:00', '13:00:00', 'Training Room');

INSERT INTO Attendees (ScheduleID, AttendeeName, AttendeeEmail)
VALUES 
(1, 'Bob Johnson', 'bob.johnson@example.com'),
(1, 'Alice Brown', 'alice.brown@example.com'),
(2, 'Mike Davis', 'mike.davis@example.com');

-- Query to retrieve all training schedules
SELECT 
    ts.ScheduleID,
    c.CourseName,
    t.TrainerName,
    ts.ScheduleDate,
    ts.StartTime,
    ts.EndTime,
    ts.Location
FROM 
    TrainingSchedules ts
INNER JOIN 
    Courses c ON ts.CourseID = c.CourseID
INNER JOIN 
    Trainers t ON ts.TrainerID = t.TrainerID;

-- Query to retrieve attendees for a specific schedule
SELECT 
    a.AttendeeID,
    a.AttendeeName,
    a.AttendeeEmail
FROM 
    Attendees a
WHERE 
    a.ScheduleID = 1;

-- Stored procedure to add new training schedule
DELIMITER //
CREATE PROCEDURE AddTrainingSchedule(
    IN p_CourseID INT,
    IN p_TrainerID INT,
    IN p_ScheduleDate DATE,
    IN p_StartTime TIME,
    IN p_EndTime TIME,
    IN p_Location VARCHAR(255)
)
BEGIN
    INSERT INTO TrainingSchedules (CourseID, TrainerID, ScheduleDate, StartTime, EndTime, Location)
    VALUES (p_CourseID, p_TrainerID, p_ScheduleDate, p_StartTime, p_EndTime, p_Location);
END//
DELIMITER ;

-- Stored procedure to add new attendee
DELIMITER //
CREATE PROCEDURE AddAttendee(
    IN p_ScheduleID INT,
    IN p_AttendeeName VARCHAR(255),
    IN p_AttendeeEmail VARCHAR(255)
)
BEGIN
    INSERT INTO Attendees (ScheduleID, AttendeeName, AttendeeEmail)
    VALUES (p_ScheduleID, p_AttendeeName, p_AttendeeEmail);
END//
DELIMITER ;
```
