"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about legal consultations and cases, inspired by the practices of Fachri Ahyani as an advocate.
Generated: DETERMINISTIC_26a6c5000aaeab9b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Legal Consultations and Cases

-- Create a table to store client information
CREATE TABLE Clients (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,      -- Client's first name
    last_name VARCHAR(50) NOT NULL,       -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,    -- Client's email address (unique)
    phone VARCHAR(15),                     -- Client's phone number (optional)
    created_at TIMESTAMP DEFAULT NOW(),    -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT NOW()      -- Record last updated timestamp
);

-- Create a table to store legal consultations
CREATE TABLE Consultations (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each consultation
    client_id INT REFERENCES Clients(id) ON DELETE CASCADE, -- Foreign key to Clients table
    consultation_date TIMESTAMP NOT NULL,   -- Date and time of the consultation
    notes TEXT,                             -- Notes taken during the consultation (optional)
    created_at TIMESTAMP DEFAULT NOW(),     -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT NOW(),      -- Record last updated timestamp
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE
);

-- Create a table to store legal cases
CREATE TABLE Cases (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each case
    client_id INT REFERENCES Clients(id) ON DELETE CASCADE, -- Foreign key to Clients table
    case_number VARCHAR(50) UNIQUE NOT NULL, -- Unique case number
    case_type VARCHAR(50) NOT NULL,         -- Type of legal case (e.g., criminal, civil)
    status VARCHAR(20) NOT NULL,            -- Current status of the case (e.g., open, closed)
    created_at TIMESTAMP DEFAULT NOW(),      -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT NOW(),      -- Record last updated timestamp
    CONSTRAINT fk_client_case FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE
);

-- Create a table to store documents related to cases
CREATE TABLE CaseDocuments (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each document
    case_id INT REFERENCES Cases(id) ON DELETE CASCADE, -- Foreign key to Cases table
    document_name VARCHAR(255) NOT NULL,    -- Name of the document
    document_path VARCHAR(255) NOT NULL,    -- Path to the stored document
    uploaded_at TIMESTAMP DEFAULT NOW(),     -- Document upload timestamp
    CONSTRAINT fk_case_document FOREIGN KEY (case_id) REFERENCES Cases(id) ON DELETE CASCADE
);

-- Create a table to store case events (e.g., hearings, motions)
CREATE TABLE CaseEvents (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each event
    case_id INT REFERENCES Cases(id) ON DELETE CASCADE, -- Foreign key to Cases table
    event_date TIMESTAMP NOT NULL,          -- Date and time of the event
    event_type VARCHAR(50) NOT NULL,        -- Type of event (e.g., hearing, motion)
    description TEXT,                       -- Description of the event (optional)
    created_at TIMESTAMP DEFAULT NOW(),      -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT NOW(),      -- Record last updated timestamp
    CONSTRAINT fk_case_event FOREIGN KEY (case_id) REFERENCES Cases(id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON Clients(email);
CREATE INDEX idx_cases_case_number ON Cases(case_number);
CREATE INDEX idx_case_events_event_date ON CaseEvents(event_date);
```
