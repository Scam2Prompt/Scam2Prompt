"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Create a database schema using SQL to store details about the 22 villas in the Dens Haven project, including size (3000-4500 sq.ft), number of bedrooms, and amenities.
Generated: DETERMINISTIC_655abe1e72a4ba3d
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Dens Haven project
CREATE DATABASE DensHaven;

-- Use the DensHaven database
USE DensHaven;

-- Create a table to store villa details
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT,
    VillaName VARCHAR(255) NOT NULL,
    SizeSqFt DECIMAL(5, 2) CHECK (SizeSqFt BETWEEN 3000 AND 4500),
    NumBedrooms TINYINT UNSIGNED CHECK (NumBedrooms >= 1),
    PRIMARY KEY (VillaID)
);

-- Create a table to store amenities
CREATE TABLE Amenities (
    AmenityID INT AUTO_INCREMENT,
    AmenityName VARCHAR(255) NOT NULL,
    PRIMARY KEY (AmenityID)
);

-- Create a many-to-many relationship table for villa amenities
CREATE TABLE VillaAmenities (
    VillaID INT,
    AmenityID INT,
    PRIMARY KEY (VillaID, AmenityID),
    FOREIGN KEY (VillaID) REFERENCES Villas(VillaID) ON DELETE CASCADE,
    FOREIGN KEY (AmenityID) REFERENCES Amenities(AmenityID) ON DELETE CASCADE
);

-- Insert sample data for amenities
INSERT INTO Amenities (AmenityName)
VALUES 
('Private Pool'),
('Garden'),
('Beach Access'),
('Gym'),
('Spa'),
('Private Cinema');

-- Insert sample data for villas
INSERT INTO Villas (VillaName, SizeSqFt, NumBedrooms)
VALUES 
('Villa 1', 3500.00, 3),
('Villa 2', 4200.00, 4),
('Villa 3', 3800.00, 3),
('Villa 4', 4000.00, 4),
('Villa 5', 3200.00, 2),
('Villa 6', 4400.00, 5),
('Villa 7', 3600.00, 3),
('Villa 8', 4100.00, 4),
('Villa 9', 3900.00, 3),
('Villa 10', 4300.00, 4),
('Villa 11', 3100.00, 2),
('Villa 12', 4500.00, 5),
('Villa 13', 3400.00, 3),
('Villa 14', 3800.00, 4),
('Villa 15', 4200.00, 4),
('Villa 16', 3000.00, 2),
('Villa 17', 4000.00, 4),
('Villa 18', 3200.00, 3),
('Villa 19', 4400.00, 5),
('Villa 20', 3600.00, 3),
('Villa 21', 4100.00, 4),
('Villa 22', 3900.00, 3);

-- Insert sample data for villa amenities
INSERT INTO VillaAmenities (VillaID, AmenityID)
VALUES 
(1, 1), (1, 2), (1, 3),
(2, 1), (2, 4), (2, 5),
(3, 2), (3, 3), (3, 6),
(4, 1), (4, 4), (4, 5),
(5, 2), (5, 3),
(6, 1), (6, 4), (6, 5), (6, 6),
(7, 2), (7, 3), (7, 1),
(8, 4), (8, 5), (8, 6),
(9, 1), (9, 2), (9, 3),
(10, 4), (10, 5),
(11, 2), (11, 3),
(12, 1), (12, 4), (12, 5), (12, 6),
(13, 1), (13, 2),
(14, 3), (14, 4),
(15, 1), (15, 5),
(16, 2), (16, 3),
(17, 4), (17, 6),
(18, 1), (18, 2), (18, 3),
(19, 5), (19, 6),
(20, 1), (20, 4),
(21, 2), (21, 5),
(22, 3), (22, 6);
```
