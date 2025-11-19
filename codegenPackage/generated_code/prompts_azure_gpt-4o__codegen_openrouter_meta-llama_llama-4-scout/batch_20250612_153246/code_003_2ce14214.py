"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a SQL query to manage a database of dealers participating in the Sundance Spas Retail Advantage program, including columns for company name, location, showroom status, and training attendance.
Generated: DETERMINISTIC_2ce1421438ffb6cf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Sundance Spas Retail Advantage program
CREATE DATABASE SundanceSpasRetailAdvantage;

-- Use the SundanceSpasRetailAdvantage database
USE SundanceSpasRetailAdvantage;

-- Create a table to store dealer information
CREATE TABLE Dealers (
    DealerID INT AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    ShowroomStatus ENUM('Active', 'Inactive') DEFAULT 'Active',
    TrainingAttendance BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (DealerID)
);

-- Create a table to store training sessions
CREATE TABLE TrainingSessions (
    TrainingSessionID INT AUTO_INCREMENT,
    TrainingDate DATE NOT NULL,
    TrainingLocation VARCHAR(255) NOT NULL,
    PRIMARY KEY (TrainingSessionID)
);

-- Create a junction table to store dealer training attendance
CREATE TABLE DealerTrainingAttendance (
    DealerID INT NOT NULL,
    TrainingSessionID INT NOT NULL,
    AttendanceStatus BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (DealerID, TrainingSessionID),
    FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID),
    FOREIGN KEY (TrainingSessionID) REFERENCES TrainingSessions(TrainingSessionID)
);

-- Insert a new dealer into the Dealers table
DELIMITER //
CREATE PROCEDURE InsertDealer(
    IN companyName VARCHAR(255),
    IN location VARCHAR(255),
    IN showroomStatus ENUM('Active', 'Inactive'),
    IN trainingAttendance BOOLEAN
)
BEGIN
    INSERT INTO Dealers (CompanyName, Location, ShowroomStatus, TrainingAttendance)
    VALUES (companyName, location, showroomStatus, trainingAttendance);
END//
DELIMITER ;

-- Update an existing dealer's information in the Dealers table
DELIMITER //
CREATE PROCEDURE UpdateDealer(
    IN dealerID INT,
    IN companyName VARCHAR(255),
    IN location VARCHAR(255),
    IN showroomStatus ENUM('Active', 'Inactive'),
    IN trainingAttendance BOOLEAN
)
BEGIN
    UPDATE Dealers
    SET CompanyName = companyName,
        Location = location,
        ShowroomStatus = showroomStatus,
        TrainingAttendance = trainingAttendance
    WHERE DealerID = dealerID;
END//
DELIMITER ;

-- Delete a dealer from the Dealers table
DELIMITER //
CREATE PROCEDURE DeleteDealer(
    IN dealerID INT
)
BEGIN
    DELETE FROM Dealers
    WHERE DealerID = dealerID;
END//
DELIMITER ;

-- Mark a dealer as attended a training session
DELIMITER //
CREATE PROCEDURE MarkTrainingAttendance(
    IN dealerID INT,
    IN trainingSessionID INT,
    IN attendanceStatus BOOLEAN
)
BEGIN
    UPDATE DealerTrainingAttendance
    SET AttendanceStatus = attendanceStatus
    WHERE DealerID = dealerID AND TrainingSessionID = trainingSessionID;
END//
DELIMITER ;

-- Retrieve all dealers with their showroom status and training attendance
DELIMITER //
CREATE PROCEDURE GetAllDealers()
BEGIN
    SELECT 
        D.DealerID,
        D.CompanyName,
        D.Location,
        D.ShowroomStatus,
        COALESCE(DTA.AttendanceStatus, FALSE) AS TrainingAttendance
    FROM 
        Dealers D
    LEFT JOIN 
        DealerTrainingAttendance DTA ON D.DealerID = DTA.DealerID;
END//
DELIMITER ;
```
