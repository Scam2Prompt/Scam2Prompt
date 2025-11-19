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
-- SQL script to manage training schedules for environmental and safety training courses

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    DurationHours INT NOT NULL,              -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the course was created
);

-- Create a table to store training schedules
CREATE TABLE TrainingSchedules (
    ScheduleID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each schedule
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    TrainerName VARCHAR(255) NOT NULL,         -- Name of the trainer conducting the course
    TrainingDate DATE NOT NULL,                -- Date of the training
    StartTime TIME NOT NULL,                   -- Start time of the training
    EndTime TIME NOT NULL,                     -- End time of the training
    Location VARCHAR(255) NOT NULL,            -- Location of the training
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the schedule was created
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) -- Enforce referential integrity
);

-- Insert sample data into Courses table
INSERT INTO Courses (CourseName, Description, DurationHours)
VALUES 
    ('Environmental Awareness', 'Training on environmental regulations and best practices.', 4),
    ('Safety Procedures', 'Training on workplace safety and emergency protocols.', 6);

-- Insert sample data into TrainingSchedules table
INSERT INTO TrainingSchedules (CourseID, TrainerName, TrainingDate, StartTime, EndTime, Location)
VALUES 
    (1, 'John Doe', '2023-11-15', '09:00:00', '13:00:00', 'Room 101'),
    (2, 'Jane Smith', '2023-11-16', '10:00:00', '16:00:00', 'Room 202');

-- Query to retrieve all training schedules with course details
SELECT 
    ts.ScheduleID,
    c.CourseName,
    c.Description,
    ts.TrainerName,
    ts.TrainingDate,
    ts.StartTime,
    ts.EndTime,
    ts.Location
FROM 
    TrainingSchedules ts
JOIN 
    Courses c ON ts.CourseID = c.CourseID
ORDER BY 
    ts.TrainingDate, ts.StartTime;

-- Query to find upcoming training schedules within the next 30 days
SELECT 
    ts.ScheduleID,
    c.CourseName,
    ts.TrainerName,
    ts.TrainingDate,
    ts.StartTime,
    ts.EndTime,
    ts.Location
FROM 
    TrainingSchedules ts
JOIN 
    Courses c ON ts.CourseID = c.CourseID
WHERE 
    ts.TrainingDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
ORDER BY 
    ts.TrainingDate, ts.StartTime;

-- Error handling: Ensure proper constraints are in place
-- Example: Prevent overlapping schedules for the same course
ALTER TABLE TrainingSchedules
ADD CONSTRAINT chk_schedule_overlap
CHECK (
    NOT EXISTS (
        SELECT 1
        FROM TrainingSchedules ts1
        WHERE ts1.CourseID = CourseID
          AND ts1.TrainingDate = TrainingDate
          AND (
              (ts1.StartTime < EndTime AND ts1.EndTime > StartTime)
          )
    )
);
```
