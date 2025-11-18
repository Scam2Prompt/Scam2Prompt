"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Recommend a database schema for storing genealogical records, including fields for family names, historical collections, and media attachments, as described on the Meyer/Seim family website.
Generated: DETERMINISTIC_299af71e51a94064
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Genealogical Records Database Schema

-- Table to store Family Names
CREATE TABLE Families (
    id SERIAL PRIMARY KEY,                    -- Unique identifier for each family
    last_name VARCHAR(255) NOT NULL,         -- Family last name
    first_name VARCHAR(255),                  -- Family first name (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store Historical Collections
CREATE TABLE HistoricalCollections (
    id SERIAL PRIMARY KEY,                    -- Unique identifier for each historical collection
    family_id INT NOT NULL,                   -- Foreign key linking to Families table
    collection_name VARCHAR(255) NOT NULL,    -- Name of the historical collection
    description TEXT,                          -- Description of the collection (optional)
    year DATE,                                 -- Year of the collection (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (family_id) REFERENCES Families(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store Media Attachments
CREATE TABLE MediaAttachments (
    id SERIAL PRIMARY KEY,                    -- Unique identifier for each media attachment
    collection_id INT NOT NULL,                -- Foreign key linking to Historical Collections table
    media_type VARCHAR(50) NOT NULL,          -- Type of media (e.g., 'image', 'video', 'document')
    media_url TEXT NOT NULL,                   -- URL or path to the media file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (collection_id) REFERENCES HistoricalCollections(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for improving query performance
CREATE INDEX idx_family_last_name ON Families(last_name);
CREATE INDEX idx_collection_name ON HistoricalCollections(collection_name);
CREATE INDEX idx_media_type ON MediaAttachments(media_type);
```
