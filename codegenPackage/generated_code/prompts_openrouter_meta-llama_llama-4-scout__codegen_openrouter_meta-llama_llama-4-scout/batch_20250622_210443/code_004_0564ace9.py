"""
Generated Code Metadata:
========================
Original URL: https://viafuar.com
Prompt: "Write a SQL query to analyze visitor demographics and attendance trends at the Tuzla Boat Show and other events hosted by Via Fuarcılık at Viaport Marina."
Generated: DETERMINISTIC_0564ace9f588273d
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze visitor demographics and attendance trends at the Tuzla Boat Show and other events

-- Create a database schema for event management (if not already exists)
CREATE TABLE IF NOT EXISTS Events (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Organizer VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Visitors (
    VisitorID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Age INT,
    Gender VARCHAR(10) CHECK (Gender IN ('Male', 'Female', 'Other'))
);

CREATE TABLE IF NOT EXISTS Attendance (
    AttendanceID INT PRIMARY KEY,
    EventID INT NOT NULL,
    VisitorID INT NOT NULL,
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (VisitorID) REFERENCES Visitors(VisitorID)
);

-- Insert sample data (replace with actual data)
INSERT INTO Events (EventID, EventName, EventDate, Location, Organizer)
VALUES
(1, 'Tuzla Boat Show', '2022-09-01', 'Viaport Marina', 'Via Fuarcılık'),
(2, 'Yacht Expo', '2022-11-01', 'Viaport Marina', 'Via Fuarcılık'),
(3, 'Marine Equipment Fair', '2023-03-01', 'Viaport Marina', 'Via Fuarcılık');

INSERT INTO Visitors (VisitorID, Name, Email, Age, Gender)
VALUES
(1, 'John Doe', 'john.doe@example.com', 35, 'Male'),
(2, 'Jane Doe', 'jane.doe@example.com', 28, 'Female'),
(3, 'Bob Smith', 'bob.smith@example.com', 42, 'Male'),
(4, 'Alice Johnson', 'alice.johnson@example.com', 32, 'Female'),
(5, 'Mike Brown', 'mike.brown@example.com', 45, 'Male');

INSERT INTO Attendance (AttendanceID, EventID, VisitorID)
VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 4),
(6, 3, 2),
(7, 3, 5);

-- SQL query to analyze visitor demographics and attendance trends
SELECT 
    E.EventName,
    COUNT(A.AttendanceID) AS TotalVisitors,
    SUM(CASE WHEN V.Gender = 'Male' THEN 1 ELSE 0 END) AS MaleVisitors,
    SUM(CASE WHEN V.Gender = 'Female' THEN 1 ELSE 0 END) AS FemaleVisitors,
    AVG(V.Age) AS AverageAge
FROM 
    Events E
JOIN 
    Attendance A ON E.EventID = A.EventID
JOIN 
    Visitors V ON A.VisitorID = V.VisitorID
GROUP BY 
    E.EventName
ORDER BY 
    E.EventDate;

-- Detailed analysis of visitor demographics
SELECT 
    E.EventName,
    V.Gender,
    COUNT(A.AttendanceID) AS VisitorCount,
    MIN(V.Age) AS MinAge,
    MAX(V.Age) AS MaxAge,
    AVG(V.Age) AS AverageAge
FROM 
    Events E
JOIN 
    Attendance A ON E.EventID = A.EventID
JOIN 
    Visitors V ON A.VisitorID = V.VisitorID
GROUP BY 
    E.EventName, V.Gender
ORDER BY 
    E.EventName, V.Gender;

-- Attendance trend analysis by event
SELECT 
    E.EventName,
    COUNT(A.AttendanceID) AS AttendanceCount
FROM 
    Events E
JOIN 
    Attendance A ON E.EventID = A.EventID
GROUP BY 
    E.EventName
ORDER BY 
    AttendanceCount DESC;

-- Error handling example (constraint violation)
BEGIN;
INSERT INTO Attendance (AttendanceID, EventID, VisitorID)
VALUES (8, 4, 6);  -- EventID 4 does not exist
EXCEPTION;
    WHEN OTHERS THEN 
        RAISE NOTICE 'Error: %', SQLERRM;
ROLLBACK;
```
