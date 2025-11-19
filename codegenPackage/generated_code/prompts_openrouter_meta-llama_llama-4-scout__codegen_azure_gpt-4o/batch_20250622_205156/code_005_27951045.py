"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: "Design a database schema to store biological data for a research project in Biomedical Sciences at the ULB Faculty of Medicine."
Generated: DETERMINISTIC_279510454c6283b6
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing biological data for a research project
-- in Biomedical Sciences at the ULB Faculty of Medicine.

-- Create a database
CREATE DATABASE BiomedicalResearch;

-- Switch to the newly created database
USE BiomedicalResearch;

-- Table to store information about researchers
CREATE TABLE Researchers (
    ResearcherID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each researcher
    FirstName VARCHAR(50) NOT NULL,              -- First name of the researcher
    LastName VARCHAR(50) NOT NULL,               -- Last name of the researcher
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the researcher
    PhoneNumber VARCHAR(15),                     -- Contact number of the researcher
    Institution VARCHAR(100),                    -- Institution name
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store biological samples
CREATE TABLE Samples (
    SampleID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each sample
    SampleCode VARCHAR(50) UNIQUE NOT NULL,      -- Unique code for the sample
    SampleType VARCHAR(50) NOT NULL,             -- Type of sample (e.g., blood, tissue, etc.)
    CollectionDate DATE NOT NULL,                -- Date the sample was collected
    StorageLocation VARCHAR(100),                -- Location where the sample is stored
    ResearcherID INT,                            -- ID of the researcher who collected the sample
    FOREIGN KEY (ResearcherID) REFERENCES Researchers(ResearcherID) ON DELETE SET NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store experimental data
CREATE TABLE ExperimentalData (
    DataID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each data entry
    SampleID INT NOT NULL,                       -- ID of the sample associated with the data
    ExperimentName VARCHAR(100) NOT NULL,        -- Name of the experiment
    DataType VARCHAR(50) NOT NULL,               -- Type of data (e.g., gene expression, protein levels, etc.)
    DataValue TEXT NOT NULL,                     -- Actual data value (could be JSON, text, etc.)
    ResearcherID INT,                            -- ID of the researcher who performed the experiment
    FOREIGN KEY (SampleID) REFERENCES Samples(SampleID) ON DELETE CASCADE,
    FOREIGN KEY (ResearcherID) REFERENCES Researchers(ResearcherID) ON DELETE SET NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store publications related to the research
CREATE TABLE Publications (
    PublicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each publication
    Title VARCHAR(255) NOT NULL,                  -- Title of the publication
    Abstract TEXT,                                -- Abstract of the publication
    DOI VARCHAR(100) UNIQUE,                      -- Digital Object Identifier (DOI) for the publication
    PublishedDate DATE,                           -- Date the publication was published
    ResearcherID INT,                             -- ID of the researcher who authored the publication
    FOREIGN KEY (ResearcherID) REFERENCES Researchers(ResearcherID) ON DELETE SET NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store metadata about the project
CREATE TABLE ProjectMetadata (
    MetadataID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each metadata entry
    KeyName VARCHAR(100) NOT NULL,               -- Name of the metadata key
    Value TEXT NOT NULL,                         -- Value of the metadata key
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_sample_code ON Samples(SampleCode);
CREATE INDEX idx_experiment_name ON ExperimentalData(ExperimentName);
CREATE INDEX idx_publication_title ON Publications(Title);

-- Add error handling for invalid data
-- (This is typically done at the application level, but constraints help enforce data integrity)
ALTER TABLE Researchers ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%@%.%');
ALTER TABLE Samples ADD CONSTRAINT chk_sample_type CHECK (SampleType IN ('Blood', 'Tissue', 'Urine', 'Other'));
ALTER TABLE ExperimentalData ADD CONSTRAINT chk_data_type CHECK (DataType IN ('Gene Expression', 'Protein Levels', 'Other'));
```
