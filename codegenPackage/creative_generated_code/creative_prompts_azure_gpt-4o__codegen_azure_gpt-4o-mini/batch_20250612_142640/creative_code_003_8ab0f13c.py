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
-- Database Schema for Managing Award Nominations and Winners

-- Create a table for storing information about the awards
CREATE TABLE awards (
    award_id SERIAL PRIMARY KEY, -- Unique identifier for each award
    award_name VARCHAR(100) NOT NULL, -- Name of the award
    award_description TEXT, -- Description of the award
    award_year INT NOT NULL CHECK (award_year > 2000) -- Year the award is given, must be after 2000
);

-- Create a table for storing nominees
CREATE TABLE nominees (
    nominee_id SERIAL PRIMARY KEY, -- Unique identifier for each nominee
    nominee_name VARCHAR(100) NOT NULL, -- Name of the nominee
    nominee_email VARCHAR(100) UNIQUE NOT NULL, -- Email of the nominee (must be unique)
    nominee_bio TEXT -- Short biography of the nominee
);

-- Create a table for storing nomination details
CREATE TABLE nominations (
    nomination_id SERIAL PRIMARY KEY, -- Unique identifier for each nomination
    award_id INT NOT NULL REFERENCES awards(award_id) ON DELETE CASCADE, -- Foreign key to awards
    nominee_id INT NOT NULL REFERENCES nominees(nominee_id) ON DELETE CASCADE, -- Foreign key to nominees
    nomination_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the nomination
    nomination_reason TEXT, -- Reason for the nomination
    UNIQUE (award_id, nominee_id) -- Ensures a nominee can only be nominated once for an award
);

-- Create a table for storing winners
CREATE TABLE winners (
    winner_id SERIAL PRIMARY KEY, -- Unique identifier for each winner
    nomination_id INT NOT NULL REFERENCES nominations(nomination_id) ON DELETE CASCADE, -- Foreign key to nominations
    win_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the award was won
    special_recognition TEXT -- Any special recognition details
);

-- Indexes can be added for better performance on commonly queried fields
CREATE INDEX idx_award_year ON awards(award_year);
CREATE INDEX idx_nominee_name ON nominees(nominee_name);
CREATE INDEX idx_nomination_date ON nominations(nomination_date);

-- Example data insertion (commented out for initial setup)
-- INSERT INTO awards (award_name, award_description, award_year) VALUES ('Best Innovator', 'Award for the best innovator of the year', 2023);
-- INSERT INTO nominees (nominee_name, nominee_email, nominee_bio) VALUES ('Jane Doe', 'jane.doe@example.com', 'Innovator in technology.');
-- INSERT INTO nominations (award_id, nominee_id, nomination_reason) VALUES (1, 1, 'For outstanding innovation in tech.');
-- INSERT INTO winners (nomination_id) VALUES (1);

-- Use proper error handling in application logic when interacting with these tables.
```
