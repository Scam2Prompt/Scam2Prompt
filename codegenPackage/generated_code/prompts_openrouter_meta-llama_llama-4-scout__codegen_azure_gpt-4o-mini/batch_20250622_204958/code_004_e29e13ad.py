"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: "Create a simple database schema to store information about environmental testing samples, including sample matrix, turnaround time, and rush charges, inspired by A&B Labs' services."
Generated: DETERMINISTIC_e29e13adc1926784
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing environmental testing samples
CREATE DATABASE EnvironmentalTesting;

USE EnvironmentalTesting;

-- Table to store information about sample matrices
CREATE TABLE SampleMatrix (
    MatrixID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each sample matrix
    MatrixName VARCHAR(100) NOT NULL,         -- Name of the sample matrix (e.g., Water, Soil)
    Description TEXT,                          -- Description of the sample matrix
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about testing samples
CREATE TABLE TestingSamples (
    SampleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each testing sample
    SampleName VARCHAR(100) NOT NULL,          -- Name of the testing sample
    MatrixID INT NOT NULL,                      -- Foreign key referencing SampleMatrix
    TurnaroundTime INT NOT NULL,                -- Turnaround time in hours
    RushCharge DECIMAL(10, 2) DEFAULT 0.00,    -- Rush charge for expedited testing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (MatrixID) REFERENCES SampleMatrix(MatrixID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion for SampleMatrix
INSERT INTO SampleMatrix (MatrixName, Description) VALUES
('Water', 'Testing for various contaminants in water samples.'),
('Soil', 'Analysis of soil samples for pollutants and nutrients.'),
('Air', 'Testing air samples for particulate matter and gases.');

-- Sample data insertion for TestingSamples
INSERT INTO TestingSamples (SampleName, MatrixID, TurnaroundTime, RushCharge) VALUES
('Water Quality Test', 1, 48, 150.00),
('Soil Nutrient Test', 2, 72, 200.00),
('Air Quality Test', 3, 24, 100.00);
```
