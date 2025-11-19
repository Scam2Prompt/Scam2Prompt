"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Design a database schema for storing information about various types of pebbles, including their source, quality certification, and usage recommendations.
Generated: DETERMINISTIC_ee41732df0941c81
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Pebble Information Management

-- Create the table for storing pebble types
CREATE TABLE PebbleTypes (
    PebbleTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pebble type
    Name VARCHAR(100) NOT NULL,                  -- Name of the pebble type (e.g., Granite, Basalt, etc.)
    Description TEXT                             -- Description of the pebble type
);

-- Create the table for storing pebble sources
CREATE TABLE PebbleSources (
    SourceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each source
    Name VARCHAR(100) NOT NULL,                  -- Name of the source (e.g., River, Quarry, etc.)
    Location VARCHAR(255) NOT NULL,              -- Location of the source
    ContactDetails VARCHAR(255),                 -- Optional contact details for the source
    Notes TEXT                                   -- Additional notes about the source
);

-- Create the table for storing quality certifications
CREATE TABLE QualityCertifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    Name VARCHAR(100) NOT NULL,                     -- Name of the certification (e.g., ISO 9001, ASTM standards, etc.)
    IssuingAuthority VARCHAR(100) NOT NULL,         -- Issuing authority for the certification
    ValidFrom DATE NOT NULL,                        -- Start date of certification validity
    ValidUntil DATE,                                -- End date of certification validity (nullable for indefinite certifications)
    Notes TEXT                                      -- Additional notes
);

-- Create the table for storing usage recommendations
CREATE TABLE UsageRecommendations (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recommendation
    PebbleTypeID INT NOT NULL,                        -- Foreign key linking to PebbleTypes table
    RecommendedUsage VARCHAR(255) NOT NULL,           -- Recommended usage scenario (e.g., Landscaping, Aquarium, etc.)
    Notes TEXT,                                       -- Additional notes on usage
    FOREIGN KEY (PebbleTypeID) REFERENCES PebbleTypes(PebbleTypeID) -- Ensure pebble type exists
);

-- Create the table for associating pebbles with their sources and certifications
CREATE TABLE PebbleDetails (
    PebbleDetailID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each pebble detail record
    PebbleTypeID INT NOT NULL,                      -- Foreign key linking to PebbleTypes table
    SourceID INT NOT NULL,                          -- Foreign key linking to PebbleSources table
    CertificationID INT,                            -- Foreign key linking to QualityCertifications table
    FOREIGN KEY (PebbleTypeID) REFERENCES PebbleTypes(PebbleTypeID), -- Ensure pebble type exists
    FOREIGN KEY (SourceID) REFERENCES PebbleSources(SourceID),       -- Ensure source exists
    FOREIGN KEY (CertificationID) REFERENCES QualityCertifications(CertificationID) -- Ensure certification exists
);

-- Insert example data (optional, for testing purposes)
INSERT INTO PebbleTypes (Name, Description)
VALUES ('Granite', 'A durable and versatile pebble used in construction and landscaping.');

INSERT INTO PebbleSources (Name, Location, ContactDetails, Notes)
VALUES ('Rock Quarry', '123 Quarry Lane, Boulder City', 'contact@rockquarry.com', 'Produces high-quality granite pebbles.');

INSERT INTO QualityCertifications (Name, IssuingAuthority, ValidFrom, ValidUntil, Notes)
VALUES ('ISO 9001', 'International Standards Organization', '2023-01-01', '2025-12-31', 'Certified for high-quality and consistent production.');

INSERT INTO UsageRecommendations (PebbleTypeID, RecommendedUsage, Notes)
VALUES (1, 'Landscaping', 'Ideal for garden paths and decorative borders.');

INSERT INTO PebbleDetails (PebbleTypeID, SourceID, CertificationID)
VALUES (1, 1, 1);

-- End of schema definition
```
