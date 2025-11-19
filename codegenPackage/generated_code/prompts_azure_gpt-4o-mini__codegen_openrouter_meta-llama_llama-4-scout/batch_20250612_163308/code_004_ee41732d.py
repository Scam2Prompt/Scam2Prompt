"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Design a database schema for storing information about various types of pebbles, including their source, quality certification, and usage recommendations.
Generated: DETERMINISTIC_ee41732df0941c81
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- pebble_schema.sql

-- Create a database for storing pebble information
CREATE DATABASE PebbleDatabase;

-- Use the PebbleDatabase
USE PebbleDatabase;

-- Create a table for pebble sources
CREATE TABLE Sources (
  SourceID INT AUTO_INCREMENT,
  SourceName VARCHAR(255) NOT NULL,
  SourceDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (SourceID)
);

-- Create a table for quality certifications
CREATE TABLE Certifications (
  CertificationID INT AUTO_INCREMENT,
  CertificationName VARCHAR(255) NOT NULL,
  CertificationDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (CertificationID)
);

-- Create a table for pebble types
CREATE TABLE PebbleTypes (
  PebbleTypeID INT AUTO_INCREMENT,
  PebbleTypeName VARCHAR(255) NOT NULL,
  PebbleTypeDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PebbleTypeID)
);

-- Create a table for pebble information
CREATE TABLE Pebbles (
  PebbleID INT AUTO_INCREMENT,
  PebbleTypeID INT NOT NULL,
  SourceID INT NOT NULL,
  CertificationID INT,
  PebbleName VARCHAR(255) NOT NULL,
  PebbleDescription TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (PebbleID),
  FOREIGN KEY (PebbleTypeID) REFERENCES PebbleTypes(PebbleTypeID),
  FOREIGN KEY (SourceID) REFERENCES Sources(SourceID),
  FOREIGN KEY (CertificationID) REFERENCES Certifications(CertificationID)
);

-- Create a table for usage recommendations
CREATE TABLE UsageRecommendations (
  RecommendationID INT AUTO_INCREMENT,
  PebbleID INT NOT NULL,
  RecommendationText TEXT NOT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (RecommendationID),
  FOREIGN KEY (PebbleID) REFERENCES Pebbles(PebbleID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Pebbles_PebbleTypeID ON Pebbles (PebbleTypeID);
CREATE INDEX idx_Pebbles_SourceID ON Pebbles (SourceID);
CREATE INDEX idx_Pebbles_CertificationID ON Pebbles (CertificationID);
CREATE INDEX idx_UsageRecommendations_PebbleID ON UsageRecommendations (PebbleID);

-- Example data insertion
INSERT INTO Sources (SourceName, SourceDescription)
VALUES ('River Source', 'Pebbles collected from a river'),
       ('Beach Source', 'Pebbles collected from a beach');

INSERT INTO Certifications (CertificationName, CertificationDescription)
VALUES ('Quality Certified', 'Pebbles meet quality standards'),
       ('Eco-Friendly Certified', 'Pebbles are eco-friendly');

INSERT INTO PebbleTypes (PebbleTypeName, PebbleTypeDescription)
VALUES ('Rock', 'A type of rock'),
       ('Stone', 'A type of stone');

INSERT INTO Pebbles (PebbleTypeID, SourceID, CertificationID, PebbleName, PebbleDescription)
VALUES (1, 1, 1, 'River Rock', 'A rock from the river'),
       (2, 2, 2, 'Beach Stone', 'A stone from the beach');

INSERT INTO UsageRecommendations (PebbleID, RecommendationText)
VALUES (1, 'Use for decoration'),
       (2, 'Use for construction');
```
