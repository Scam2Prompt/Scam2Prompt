"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: How can I create a database schema to manage documents for health product regulations and consultations as outlined by the หนองบัวลำภู health authorities?
Generated: DETERMINISTIC_fe34fafc2c8bca5d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing documents related to health product regulations and consultations
-- This schema is designed to be clean, efficient, and production-ready.

-- Create a table to store information about health product regulations
CREATE TABLE HealthProductRegulations (
    RegulationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each regulation
    Title VARCHAR(255) NOT NULL,                -- Title of the regulation
    Description TEXT,                           -- Detailed description of the regulation
    EffectiveDate DATE NOT NULL,                -- Date when the regulation becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about consultations
CREATE TABLE Consultations (
    ConsultationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each consultation
    RegulationID INT NOT NULL,                     -- Foreign key referencing HealthProductRegulations
    ConsultantName VARCHAR(255) NOT NULL,          -- Name of the consultant
    ConsultationDate DATE NOT NULL,                -- Date of the consultation
    Notes TEXT,                                    -- Notes or summary of the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (RegulationID) REFERENCES HealthProductRegulations(RegulationID) -- Enforce relationship
);

-- Create a table to store documents related to regulations and consultations
CREATE TABLE Documents (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    RegulationID INT,                          -- Foreign key referencing HealthProductRegulations
    ConsultationID INT,                        -- Foreign key referencing Consultations
    FileName VARCHAR(255) NOT NULL,            -- Name of the file
    FilePath VARCHAR(255) NOT NULL,            -- Path to the file on the server
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the document was uploaded
    FOREIGN KEY (RegulationID) REFERENCES HealthProductRegulations(RegulationID), -- Enforce relationship
    FOREIGN KEY (ConsultationID) REFERENCES Consultations(ConsultationID) -- Enforce relationship
);

-- Create indexes for faster querying
CREATE INDEX idx_regulation_id ON Consultations(RegulationID);
CREATE INDEX idx_document_regulation_id ON Documents(RegulationID);
CREATE INDEX idx_document_consultation_id ON Documents(ConsultationID);

-- Error handling and constraints
-- Ensure that the file path is unique to avoid duplicate uploads
ALTER TABLE Documents ADD CONSTRAINT unique_file_path UNIQUE (FilePath);

-- Ensure that the consultation date cannot be in the future
ALTER TABLE Consultations ADD CONSTRAINT chk_consultation_date CHECK (ConsultationDate <= CURDATE());

-- Ensure that the effective date of regulations cannot be in the past
ALTER TABLE HealthProductRegulations ADD CONSTRAINT chk_effective_date CHECK (EffectiveDate >= CURDATE());
```
