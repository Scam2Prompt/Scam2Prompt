"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Develop a database schema to store information about the IGEOG selection processes, including candidate lists, results, and timelines for various "Editais."
Generated: DETERMINISTIC_75feafd5a596b796
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store information about the IGEOG selection processes.
-- This schema includes tables for "Editais," candidates, results, and timelines.

-- Create the table for "Editais" (selection processes).
CREATE TABLE Editais (
    edital_id SERIAL PRIMARY KEY,           -- Unique identifier for each edital
    title VARCHAR(255) NOT NULL,            -- Title/name of the edital
    description TEXT,                       -- Brief description of the edital
    start_date DATE NOT NULL,               -- Start date of the edital
    end_date DATE NOT NULL,                 -- End date of the edital
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for when the edital was created
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for the last update
    CONSTRAINT date_check CHECK (end_date >= start_date) -- Ensure end_date is not before start_date
);

-- Create the table for candidates.
CREATE TABLE Candidates (
    candidate_id SERIAL PRIMARY KEY,        -- Unique identifier for each candidate
    edital_id INT NOT NULL,                 -- Foreign key linking to the related edital
    full_name VARCHAR(255) NOT NULL,        -- Full name of the candidate
    email VARCHAR(255) NOT NULL UNIQUE,     -- Email address of the candidate
    phone_number VARCHAR(20),               -- Phone number of the candidate
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for when the candidate was added
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for the last update
    CONSTRAINT fk_edital_candidates FOREIGN KEY (edital_id) REFERENCES Editais (edital_id) ON DELETE CASCADE
);

-- Create the table for results (status of candidates in the selection process).
CREATE TABLE Results (
    result_id SERIAL PRIMARY KEY,           -- Unique identifier for each result record
    candidate_id INT NOT NULL,              -- Foreign key linking to the related candidate
    edital_id INT NOT NULL,                 -- Foreign key linking to the related edital
    status VARCHAR(50) NOT NULL,            -- Status of the candidate (e.g., "Approved", "Rejected", "Under Review")
    notes TEXT,                             -- Additional notes regarding the result
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for when the result was created
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for the last update
    CONSTRAINT fk_candidate_results FOREIGN KEY (candidate_id) REFERENCES Candidates (candidate_id) ON DELETE CASCADE,
    CONSTRAINT fk_edital_results FOREIGN KEY (edital_id) REFERENCES Editais (edital_id) ON DELETE CASCADE
);

-- Create the table for timelines (key dates or events in the edital process).
CREATE TABLE Timelines (
    timeline_id SERIAL PRIMARY KEY,         -- Unique identifier for each timeline entry
    edital_id INT NOT NULL,                 -- Foreign key linking to the related edital
    event_name VARCHAR(255) NOT NULL,       -- Name of the event (e.g., "Application Deadline", "Results Announcement")
    event_date DATE NOT NULL,               -- Date of the event
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for when the timeline entry was created
    updated_at TIMESTAMP DEFAULT NOW(),     -- Timestamp for the last update
    CONSTRAINT fk_edital_timelines FOREIGN KEY (edital_id) REFERENCES Editais (edital_id) ON DELETE CASCADE
);

-- Indexes for optimization.
CREATE INDEX idx_edital_start_date ON Editais (start_date);
CREATE INDEX idx_candidate_email ON Candidates (email);
CREATE INDEX idx_result_status ON Results (status);
CREATE INDEX idx_timeline_event_date ON Timelines (event_date);
```
