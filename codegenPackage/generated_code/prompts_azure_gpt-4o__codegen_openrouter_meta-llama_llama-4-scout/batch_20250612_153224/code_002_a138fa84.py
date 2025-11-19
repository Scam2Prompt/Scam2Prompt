"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Create a database schema for storing hair transplant results, including fields for graft count, cost, session duration, and before-and-after images, based on the services offered by Auqual Hair Services.
Generated: DETERMINISTIC_a138fa84546d24a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing hair transplant results
CREATE DATABASE HairTransplantDB;

-- Use the created database
USE HairTransplantDB;

-- Create a table for hair transplant services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table for hair transplant sessions
CREATE TABLE Sessions (
    SessionID INT AUTO_INCREMENT,
    ServiceID INT NOT NULL,
    PatientName VARCHAR(255) NOT NULL,
    GraftCount INT NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    SessionDuration INT NOT NULL,  -- in minutes
    BeforeImage BLOB,
    AfterImage BLOB,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SessionID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table for session outcomes
CREATE TABLE SessionOutcomes (
    OutcomeID INT AUTO_INCREMENT,
    SessionID INT NOT NULL,
    OutcomeDescription TEXT,
    SatisfactionRating TINYINT NOT NULL CHECK (SatisfactionRating BETWEEN 1 AND 5),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OutcomeID),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

-- Create a table for complications
CREATE TABLE Complications (
    ComplicationID INT AUTO_INCREMENT,
    SessionID INT NOT NULL,
    ComplicationDescription TEXT,
    Severity VARCHAR(50) NOT NULL CHECK (Severity IN ('Mild', 'Moderate', 'Severe')),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ComplicationID),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);

-- Insert sample services
INSERT INTO Services (ServiceName, Description)
VALUES 
('Hair Transplant', 'Hair transplant surgery'),
('Hair Restoration', 'Hair restoration treatment'),
('Scalp Micropigmentation', 'Scalp micropigmentation treatment');

-- Example usage:
DELIMITER //
CREATE PROCEDURE GetSessionDetails(IN sessionId INT)
BEGIN
    SELECT 
        s.SessionID,
        s.PatientName,
        s.GraftCount,
        s.Cost,
        s.SessionDuration,
        s.BeforeImage,
        s.AfterImage,
        so.OutcomeDescription,
        so.SatisfactionRating
    FROM 
        Sessions s
    LEFT JOIN 
        SessionOutcomes so ON s.SessionID = so.SessionID
    WHERE 
        s.SessionID = sessionId;
END//
DELIMITER ;

-- Call the stored procedure
CALL GetSessionDetails(1);
```
