"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Develop a database schema to store information about the IGEOG selection processes, including candidate lists, results, and timelines for various "Editais."
Generated: DETERMINISTIC_75feafd5a596b796
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for IGEOG selection processes

-- Create a table to store information about Editais
CREATE TABLE Editais (
    edital_id SERIAL PRIMARY KEY, -- Unique identifier for each edital
    title VARCHAR(255) NOT NULL, -- Title of the edital
    description TEXT, -- Description of the edital
    publication_date DATE NOT NULL, -- Date when the edital was published
    deadline DATE NOT NULL, -- Deadline for applications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store candidate information
CREATE TABLE Candidates (
    candidate_id SERIAL PRIMARY KEY, -- Unique identifier for each candidate
    edital_id INT NOT NULL, -- Foreign key referencing the Editais table
    name VARCHAR(255) NOT NULL, -- Candidate's name
    email VARCHAR(255) UNIQUE NOT NULL, -- Candidate's email (must be unique)
    phone VARCHAR(20), -- Candidate's phone number
    application_date DATE NOT NULL, -- Date when the candidate applied
    status VARCHAR(50) DEFAULT 'Pending', -- Status of the application (e.g., Pending, Approved, Rejected)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (edital_id) REFERENCES Editais(edital_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store results of the selection process
CREATE TABLE Results (
    result_id SERIAL PRIMARY KEY, -- Unique identifier for each result entry
    edital_id INT NOT NULL, -- Foreign key referencing the Editais table
    candidate_id INT NOT NULL, -- Foreign key referencing the Candidates table
    score DECIMAL(5, 2) NOT NULL, -- Score obtained by the candidate
    result_status VARCHAR(50) NOT NULL, -- Result status (e.g., Approved, Disqualified)
    announcement_date DATE NOT NULL, -- Date when the results were announced
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (edital_id) REFERENCES Editais(edital_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (candidate_id) REFERENCES Candidates(candidate_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store timelines for each edital
CREATE TABLE Timelines (
    timeline_id SERIAL PRIMARY KEY, -- Unique identifier for each timeline entry
    edital_id INT NOT NULL, -- Foreign key referencing the Editais table
    event_description VARCHAR(255) NOT NULL, -- Description of the event
    event_date DATE NOT NULL, -- Date of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (edital_id) REFERENCES Editais(edital_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_candidates_edital ON Candidates(edital_id);
CREATE INDEX idx_results_edital ON Results(edital_id);
CREATE INDEX idx_results_candidate ON Results(candidate_id);
CREATE INDEX idx_timelines_edital ON Timelines(edital_id);
```
