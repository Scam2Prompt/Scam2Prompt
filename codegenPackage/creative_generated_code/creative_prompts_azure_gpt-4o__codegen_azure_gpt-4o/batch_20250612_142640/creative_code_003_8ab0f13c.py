"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Create a database schema for managing award nominations and winners based on the structure described in MN SWAP's award nomination information.
Generated: DETERMINISTIC_8ab0f13c8c464f78
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing award nominations and winners

-- Table to store information about awards
CREATE TABLE awards (
    award_id SERIAL PRIMARY KEY,          -- Unique identifier for each award
    name VARCHAR(255) NOT NULL,           -- Name of the award
    description TEXT,                     -- Description of the award
    year INT NOT NULL,                    -- Year the award is given
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the award entry was created
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp when the award entry was last updated
);

-- Table to store nominees for awards
CREATE TABLE nominees (
    nominee_id SERIAL PRIMARY KEY,        -- Unique identifier for each nominee
    name VARCHAR(255) NOT NULL,           -- Name of the nominee (individual/group)
    description TEXT,                     -- Description of the nominee's work or achievements
    email VARCHAR(255) UNIQUE,            -- Contact email for the nominee
    phone_number VARCHAR(50),             -- Contact phone number for the nominee
    submitted_by VARCHAR(255),            -- Name of the person who submitted the nomination
    award_id INT NOT NULL,                -- Foreign key referencing the award
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the nominee was created
    updated_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the nominee was last updated
    CONSTRAINT fk_award
        FOREIGN KEY (award_id)
        REFERENCES awards (award_id)
        ON DELETE CASCADE                 -- Delete nominees if their award is deleted
);

-- Table to store winners for awards
CREATE TABLE winners (
    winner_id SERIAL PRIMARY KEY,         -- Unique identifier for each winner
    nominee_id INT NOT NULL,              -- Foreign key referencing the nominee
    award_id INT NOT NULL,                -- Foreign key referencing the award
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the winner entry was created
    updated_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the winner entry was last updated
    CONSTRAINT fk_nominee
        FOREIGN KEY (nominee_id)
        REFERENCES nominees (nominee_id)
        ON DELETE CASCADE,                -- Delete winner entry if nominee is deleted
    CONSTRAINT fk_award_in_winner
        FOREIGN KEY (award_id)
        REFERENCES awards (award_id)
        ON DELETE CASCADE,                -- Delete winner entry if award is deleted
    CONSTRAINT unique_winner_per_award
        UNIQUE (award_id, nominee_id)     -- Ensure a single nominee can only win one award
);

-- Indexes for improving query performance
CREATE INDEX idx_awards_year ON awards(year);               -- Index for faster querying of awards by year
CREATE INDEX idx_nominees_award ON nominees(award_id);      -- Index for faster querying of nominees by award
CREATE INDEX idx_winners_award ON winners(award_id);        -- Index for faster querying of winners by award
```
