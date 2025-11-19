"""
Generated Code Metadata:
========================
Original URL: https://renovada.org.br
Prompt: Develop a donation tracking system using SQL that can handle transactions like tithes and offerings for a church, inspired by Renovada’s approach to contributions.
Generated: DETERMINISTIC_10035c4697100275
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the donation tracking system
CREATE DATABASE DonationTracking;

-- Use the newly created database
USE DonationTracking;

-- Table to store information about donors
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store different types of contributions
CREATE TABLE ContributionTypes (
    ContributionTypeID INT AUTO_INCREMENT PRIMARY KEY,
    TypeName VARCHAR(50) NOT NULL,
    Description TEXT
);

-- Table to store contributions made by donors
CREATE TABLE Contributions (
    ContributionID INT AUTO_INCREMENT PRIMARY KEY,
    DonorID INT NOT NULL,
    ContributionTypeID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL CHECK (Amount > 0),
    ContributionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE,
    FOREIGN KEY (ContributionTypeID) REFERENCES ContributionTypes(ContributionTypeID) ON DELETE CASCADE
);

-- Insert default contribution types
INSERT INTO ContributionTypes (TypeName, Description) VALUES
('Tithe', 'A tenth of a person’s income, given to the church.'),
('Offering', 'Any additional contribution beyond the tithe.');

-- Function to add a new donor
DELIMITER //
CREATE PROCEDURE AddDonor(
    IN p_FirstName VARCHAR(50),
    IN p_LastName VARCHAR(50),
    IN p_Email VARCHAR(100),
    IN p_Phone VARCHAR(15)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
    END;

    START TRANSACTION;
    INSERT INTO Donors (FirstName, LastName, Email, Phone) 
    VALUES (p_FirstName, p_LastName, p_Email, p_Phone);
    COMMIT;
END //
DELIMITER ;

-- Function to record a contribution
DELIMITER //
CREATE PROCEDURE RecordContribution(
    IN p_DonorID INT,
    IN p_ContributionTypeID INT,
    IN p_Amount DECIMAL(10, 2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle any SQL exceptions
        ROLLBACK;
    END;

    START TRANSACTION;
    INSERT INTO Contributions (DonorID, ContributionTypeID, Amount) 
    VALUES (p_DonorID, p_ContributionTypeID, p_Amount);
    COMMIT;
END //
DELIMITER ;

-- Function to retrieve total contributions by donor
DELIMITER //
CREATE FUNCTION GetTotalContributions(p_DonorID INT) 
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total DECIMAL(10, 2);
    SELECT COALESCE(SUM(Amount), 0) INTO total 
    FROM Contributions 
    WHERE DonorID = p_DonorID;
    RETURN total;
END //
DELIMITER ;

-- Function to retrieve contributions by type
DELIMITER //
CREATE FUNCTION GetContributionsByType(p_ContributionTypeID INT) 
RETURNS TABLE (DonorID INT, Amount DECIMAL(10, 2), ContributionDate TIMESTAMP)
BEGIN
    RETURN (
        SELECT DonorID, Amount, ContributionDate 
        FROM Contributions 
        WHERE ContributionTypeID = p_ContributionTypeID
    );
END //
DELIMITER ;

-- Example usage of the procedures
-- CALL AddDonor('John', 'Doe', 'john.doe@example.com', '123-456-7890');
-- CALL RecordContribution(1, 1, 100.00);
-- SELECT GetTotalContributions(1);
-- SELECT * FROM GetContributionsByType(1);
```
