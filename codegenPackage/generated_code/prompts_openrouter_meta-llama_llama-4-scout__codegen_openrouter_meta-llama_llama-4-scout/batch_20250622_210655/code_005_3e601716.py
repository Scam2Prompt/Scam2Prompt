"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Create a SQL database schema for storing patient reviews and ratings for a dental clinic, inspired by the types of evaluations collected on the Móricz Dental website.
Generated: DETERMINISTIC_3e6017169932faeb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the dental clinic
CREATE DATABASE DentalClinicReviews;

-- Use the database
USE DentalClinicReviews;

-- Create a table for patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PatientID)
);

-- Create a table for dentists
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Specialty VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (DentistID)
);

-- Create a table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DentistID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    ReviewText TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID) ON DELETE CASCADE
);

-- Create a table for review responses
CREATE TABLE ReviewResponses (
    ResponseID INT AUTO_INCREMENT,
    ReviewID INT NOT NULL,
    ResponseText TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ResponseID),
    FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID) ON DELETE CASCADE
);

-- Create an index on PatientID and DentistID in Reviews table
CREATE INDEX idx_PatientID ON Reviews (PatientID);
CREATE INDEX idx_DentistID ON Reviews (DentistID);

-- Create a view to get the average rating for each dentist
CREATE VIEW DentistRatings AS
SELECT 
    D.DentistID,
    D.FirstName,
    D.LastName,
    AVG(R.Rating) AS AverageRating
FROM 
    Dentists D
JOIN 
    Reviews R ON D.DentistID = R.DentistID
GROUP BY 
    D.DentistID, D.FirstName, D.LastName;

-- Stored procedure to add a new review
DELIMITER //
CREATE PROCEDURE AddReview(
    IN p_PatientID INT,
    IN p_DentistID INT,
    IN p_Rating TINYINT,
    IN p_ReviewText TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Patients WHERE PatientID = p_PatientID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Patient not found';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Dentists WHERE DentistID = p_DentistID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Dentist not found';
    END IF;

    IF p_Rating NOT BETWEEN 1 AND 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Rating must be between 1 and 5';
    END IF;

    INSERT INTO Reviews (PatientID, DentistID, Rating, ReviewText)
    VALUES (p_PatientID, p_DentistID, p_Rating, p_ReviewText);
END//
DELIMITER ;
```
