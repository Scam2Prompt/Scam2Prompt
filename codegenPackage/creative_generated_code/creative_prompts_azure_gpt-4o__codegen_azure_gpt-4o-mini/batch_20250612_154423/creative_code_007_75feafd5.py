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
-- Database schema for storing information about the IGEOG selection processes

-- Drop existing tables if they exist for fresh creation
DROP TABLE IF EXISTS Editais CASCADE;
DROP TABLE IF EXISTS Candidates CASCADE;
DROP TABLE IF EXISTS Results CASCADE;
DROP TABLE IF EXISTS Timelines CASCADE;

-- Table to store information about each edital
CREATE TABLE Editais (
    edital_id SERIAL PRIMARY KEY,               -- Unique identifier for each edital
    edital_name VARCHAR(255) NOT NULL,         -- Name of the edital
    edital_description TEXT,                     -- Description of the edital
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the edital was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store candidates for each edital
CREATE TABLE Candidates (
    candidate_id SERIAL PRIMARY KEY,            -- Unique identifier for each candidate
    edital_id INT REFERENCES Editais(edital_id) ON DELETE CASCADE, -- Foreign key reference to Editais
    candidate_name VARCHAR(255) NOT NULL,      -- Name of the candidate
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the candidate applied
    status VARCHAR(50) NOT NULL DEFAULT 'pending' -- Status of the candidate (e.g., pending, approved, rejected)
);

-- Table to store results of the selection process for each edital
CREATE TABLE Results (
    result_id SERIAL PRIMARY KEY,               -- Unique identifier for each result
    edital_id INT REFERENCES Editais(edital_id) ON DELETE CASCADE, -- Foreign key reference to Editais
    candidate_id INT REFERENCES Candidates(candidate_id) ON DELETE CASCADE, -- Foreign key reference to Candidates
    result_status VARCHAR(50) NOT NULL,        -- Status of the result (e.g., approved, rejected)
    result_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date when the result was published
);

-- Table to store timelines for each edital
CREATE TABLE Timelines (
    timeline_id SERIAL PRIMARY KEY,             -- Unique identifier for each timeline entry
    edital_id INT REFERENCES Editais(edital_id) ON DELETE CASCADE, -- Foreign key reference to Editais
    event_name VARCHAR(255) NOT NULL,          -- Name of the timeline event
    event_date TIMESTAMP NOT NULL,              -- Date of the event
    description TEXT                             -- Description of the event
);

-- Add indexes for performance optimization
CREATE INDEX idx_candidates_edital_id ON Candidates(edital_id);
CREATE INDEX idx_results_edital_id ON Results(edital_id);
CREATE INDEX idx_timelines_edital_id ON Timelines(edital_id);
```
