"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create a SQL query to manage and retrieve listings of franchises for sale, including details like price, location, and industry.
Generated: DETERMINISTIC_c6d2a8e5e8de488b
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for franchises
CREATE TABLE Industries (
    IndustryID INT AUTO_INCREMENT,
    IndustryName VARCHAR(255) NOT NULL,
    PRIMARY KEY (IndustryID)
);

CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PRIMARY KEY (LocationID)
);

CREATE TABLE Franchises (
    FranchiseID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    IndustryID INT NOT NULL,
    LocationID INT NOT NULL,
    Description TEXT,
    PRIMARY KEY (FranchiseID),
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- Insert sample data into tables
INSERT INTO Industries (IndustryID, IndustryName)
VALUES 
(1, 'Food'),
(2, 'Retail'),
(3, 'Service');

INSERT INTO Locations (LocationID, City, State, Country)
VALUES 
(1, 'New York City', 'New York', 'USA'),
(2, 'Los Angeles', 'California', 'USA'),
(3, 'Chicago', 'Illinois', 'USA');

INSERT INTO Franchises (FranchiseID, Name, Price, IndustryID, LocationID, Description)
VALUES 
(1, 'Pizza Hut', 100000.00, 1, 1, 'Fast food franchise'),
(2, 'McDonald\'s', 500000.00, 1, 2, 'Fast food franchise'),
(3, '7-Eleven', 200000.00, 2, 3, 'Convenience store franchise'),
(4, 'Sally\'s Beauty', 30000.00, 2, 1, 'Beauty products franchise'),
(5, 'Molly Maid', 40000.00, 3, 2, 'Cleaning services franchise');

-- SQL query to retrieve franchise listings
DELIMITER $$

CREATE PROCEDURE GetFranchiseListings(
    IN industryFilter INT,
    IN locationFilter INT,
    IN minPriceFilter DECIMAL(10, 2),
    IN maxPriceFilter DECIMAL(10, 2)
)
BEGIN
    SELECT 
        f.FranchiseID,
        f.Name,
        f.Price,
        i.IndustryName,
        l.City,
        l.State,
        l.Country,
        f.Description
    FROM 
        Franchises f
    INNER JOIN 
        Industries i ON f.IndustryID = i.IndustryID
    INNER JOIN 
        Locations l ON f.LocationID = l.LocationID
    WHERE 
        (industryFilter IS NULL OR f.IndustryID = industryFilter)
        AND (locationFilter IS NULL OR f.LocationID = locationFilter)
        AND (minPriceFilter IS NULL OR f.Price >= minPriceFilter)
        AND (maxPriceFilter IS NULL OR f.Price <= maxPriceFilter);
END$$

DELIMITER ;

-- Example usage:
CALL GetFranchiseListings(NULL, NULL, NULL, NULL);

-- SQL query to add a new franchise listing
DELIMITER $$

CREATE PROCEDURE AddFranchiseListing(
    IN pName VARCHAR(255),
    IN pPrice DECIMAL(10, 2),
    IN pIndustryID INT,
    IN pLocationID INT,
    IN pDescription TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Industries WHERE IndustryID = pIndustryID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Industry does not exist';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Locations WHERE LocationID = pLocationID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Location does not exist';
    END IF;

    INSERT INTO Franchises (Name, Price, IndustryID, LocationID, Description)
    VALUES (pName, pPrice, pIndustryID, pLocationID, pDescription);
END$$

DELIMITER ;

-- Example usage:
CALL AddFranchiseListing('New Franchise', 150000.00, 1, 1, 'This is a new franchise listing');

-- SQL query to update an existing franchise listing
DELIMITER $$

CREATE PROCEDURE UpdateFranchiseListing(
    IN pFranchiseID INT,
    IN pName VARCHAR(255),
    IN pPrice DECIMAL(10, 2),
    IN pIndustryID INT,
    IN pLocationID INT,
    IN pDescription TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Franchises WHERE FranchiseID = pFranchiseID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Franchise does not exist';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Industries WHERE IndustryID = pIndustryID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Industry does not exist';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Locations WHERE LocationID = pLocationID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Location does not exist';
    END IF;

    UPDATE Franchises
    SET 
        Name = pName,
        Price = pPrice,
        IndustryID = pIndustryID,
        LocationID = pLocationID,
        Description = pDescription
    WHERE 
        FranchiseID = pFranchiseID;
END$$

DELIMITER ;

-- Example usage:
CALL UpdateFranchiseListing(1, 'Updated Franchise', 120000.00, 1, 1, 'This is an updated franchise listing');

-- SQL query to delete a franchise listing
DELIMITER $$

CREATE PROCEDURE DeleteFranchiseListing(
    IN pFranchiseID INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Franchises WHERE FranchiseID = pFranchiseID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Franchise does not exist';
    END IF;

    DELETE FROM Franchises
    WHERE 
        FranchiseID = pFranchiseID;
END$$

DELIMITER ;

-- Example usage:
CALL DeleteFranchiseListing(4);
```
