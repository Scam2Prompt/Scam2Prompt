"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Create a database schema in SQL to store lottery results for multiple regions (e.g., Singapore, Sydney, and Qatar) with fields for date, region, and winning numbers, inspired by the 4DLOVER website's results section.
Generated: DETERMINISTIC_05858ec501e551ee
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing lottery results
CREATE DATABASE LotteryResults;

-- Use the LotteryResults database
USE LotteryResults;

-- Create a table for regions
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT,
    RegionName VARCHAR(255) NOT NULL,
    PRIMARY KEY (RegionID),
    UNIQUE KEY (RegionName)
);

-- Create a table for lottery results
CREATE TABLE LotteryResults (
    ResultID INT AUTO_INCREMENT,
    Date DATE NOT NULL,
    RegionID INT NOT NULL,
    FirstPrize VARCHAR(10) NOT NULL,
    SecondPrize VARCHAR(10) NOT NULL,
    ThirdPrize VARCHAR(10) NOT NULL,
    SpecialPrize VARCHAR(10) NOT NULL,
    PRIMARY KEY (ResultID),
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID)
);

-- Create a table for 4D winning numbers
CREATE TABLE FourDWinningNumbers (
    WinningNumberID INT AUTO_INCREMENT,
    ResultID INT NOT NULL,
    FirstDigit VARCHAR(1) NOT NULL,
    SecondDigit VARCHAR(1) NOT NULL,
    ThirdDigit VARCHAR(1) NOT NULL,
    FourthDigit VARCHAR(1) NOT NULL,
    PRIMARY KEY (WinningNumberID),
    FOREIGN KEY (ResultID) REFERENCES LotteryResults(ResultID)
);

-- Insert sample regions
INSERT INTO Regions (RegionName)
VALUES 
('Singapore'),
('Sydney'),
('Qatar');

-- Example usage: Inserting a lottery result
DELIMITER //
CREATE PROCEDURE InsertLotteryResult(
    IN pDate DATE,
    IN pRegionName VARCHAR(255),
    IN pFirstPrize VARCHAR(10),
    IN pSecondPrize VARCHAR(10),
    IN pThirdPrize VARCHAR(10),
    IN pSpecialPrize VARCHAR(10),
    IN pFirstDigit VARCHAR(1),
    IN pSecondDigit VARCHAR(1),
    IN pThirdDigit VARCHAR(1),
    IN pFourthDigit VARCHAR(1)
)
BEGIN
    DECLARE regionID INT;
    DECLARE resultID INT;

    -- Get the region ID
    SELECT RegionID INTO regionID
    FROM Regions
    WHERE RegionName = pRegionName;

    IF regionID IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Region not found';
    END IF;

    -- Insert lottery result
    INSERT INTO LotteryResults (Date, RegionID, FirstPrize, SecondPrize, ThirdPrize, SpecialPrize)
    VALUES (pDate, regionID, pFirstPrize, pSecondPrize, pThirdPrize, pSpecialPrize);

    -- Get the result ID
    SET resultID = LAST_INSERT_ID();

    -- Insert 4D winning numbers
    INSERT INTO FourDWinningNumbers (ResultID, FirstDigit, SecondDigit, ThirdDigit, FourthDigit)
    VALUES (resultID, pFirstDigit, pSecondDigit, pThirdDigit, pFourthDigit);
END//
DELIMITER ;

-- Example usage
CALL InsertLotteryResult(
    '2022-01-01',
    'Singapore',
    '1234',
    '5678',
    '9012',
    '1111',
    '1',
    '2',
    '3',
    '4'
);
```
