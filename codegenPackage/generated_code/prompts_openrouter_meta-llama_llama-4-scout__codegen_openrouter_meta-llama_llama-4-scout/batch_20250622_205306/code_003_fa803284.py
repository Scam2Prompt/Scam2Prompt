"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Design a database schema to store information about unique jewelry pieces, including details about gemstones, metals, and certifications like GIA and HRD.
Generated: DETERMINISTIC_fa803284b5af9318
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing jewelry information
CREATE DATABASE JewelryDB;

-- Use the JewelryDB database
USE JewelryDB;

-- Create a table for metals
CREATE TABLE Metals (
  MetalID INT AUTO_INCREMENT,
  MetalType VARCHAR(50) NOT NULL,
  MetalDescription TEXT,
  PRIMARY KEY (MetalID)
);

-- Create a table for gemstones
CREATE TABLE Gemstones (
  GemstoneID INT AUTO_INCREMENT,
  GemstoneType VARCHAR(100) NOT NULL,
  GemstoneDescription TEXT,
  CaratWeight DECIMAL(10, 2),
  Cut VARCHAR(50),
  Color VARCHAR(50),
  Clarity VARCHAR(50),
  PRIMARY KEY (GemstoneID)
);

-- Create a table for certifications
CREATE TABLE Certifications (
  CertificationID INT AUTO_INCREMENT,
  CertificationName VARCHAR(100) NOT NULL,
  CertificationDescription TEXT,
  PRIMARY KEY (CertificationID)
);

-- Create a table for jewelry pieces
CREATE TABLE JewelryPieces (
  JewelryPieceID INT AUTO_INCREMENT,
  PieceName VARCHAR(200) NOT NULL,
  PieceDescription TEXT,
  MetalID INT,
  FOREIGN KEY (MetalID) REFERENCES Metals(MetalID),
  PRIMARY KEY (JewelryPieceID)
);

-- Create a many-to-many relationship table for jewelry pieces and gemstones
CREATE TABLE JewelryPieceGemstones (
  JewelryPieceID INT,
  GemstoneID INT,
  PRIMARY KEY (JewelryPieceID, GemstoneID),
  FOREIGN KEY (JewelryPieceID) REFERENCES JewelryPieces(JewelryPieceID),
  FOREIGN KEY (GemstoneID) REFERENCES Gemstones(GemstoneID)
);

-- Create a table for jewelry piece certifications
CREATE TABLE JewelryPieceCertifications (
  JewelryPieceID INT,
  CertificationID INT,
  CertificateNumber VARCHAR(100),
  PRIMARY KEY (JewelryPieceID, CertificationID),
  FOREIGN KEY (JewelryPieceID) REFERENCES JewelryPieces(JewelryPieceID),
  FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID)
);

-- Insert sample data into the Metals table
INSERT INTO Metals (MetalType, MetalDescription)
VALUES 
('Gold', '18k Gold'),
('Silver', 'Sterling Silver'),
('Platinum', '950 Platinum');

-- Insert sample data into the Gemstones table
INSERT INTO Gemstones (GemstoneType, GemstoneDescription, CaratWeight, Cut, Color, Clarity)
VALUES 
('Diamond', 'Round Brilliant Diamond', 1.00, 'Round', 'D', 'Flawless'),
('Ruby', 'Burma Ruby', NULL, NULL, NULL, NULL),
('Sapphire', 'Ceylon Sapphire', NULL, NULL, NULL, NULL);

-- Insert sample data into the Certifications table
INSERT INTO Certifications (CertificationName, CertificationDescription)
VALUES 
('GIA', 'Gemological Institute of America'),
('HRD', 'Hoge Raad voor Diamant');

-- Insert sample data into the JewelryPieces table
INSERT INTO JewelryPieces (PieceName, PieceDescription, MetalID)
VALUES 
('Diamond Ring', '18k Gold Diamond Ring', 1),
('Ruby Necklace', 'Silver Ruby Necklace', 2),
('Sapphire Earrings', 'Platinum Sapphire Earrings', 3);

-- Insert sample data into the JewelryPieceGemstones table
INSERT INTO JewelryPieceGemstones (JewelryPieceID, GemstoneID)
VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insert sample data into the JewelryPieceCertifications table
INSERT INTO JewelryPieceCertifications (JewelryPieceID, CertificationID, CertificateNumber)
VALUES 
(1, 1, 'GIA12345'),
(2, 2, 'HRD67890'),
(3, 1, 'GIA34567');
```
