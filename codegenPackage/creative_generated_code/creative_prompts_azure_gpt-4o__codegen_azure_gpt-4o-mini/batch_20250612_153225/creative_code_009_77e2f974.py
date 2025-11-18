"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Suggest a database schema for storing architectural project data, inspired by the Études Architect application’s functionality described on lojaoficial.cloud.
Generated: DETERMINISTIC_77e2f974dcdc95dd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Architectural Project Data

-- Table to store information about architectural projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,             -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,       -- Name of the project
    project_description TEXT,                   -- Description of the project
    start_date DATE NOT NULL,                   -- Start date of the project
    end_date DATE,                              -- End date of the project (NULL if ongoing)
    client_id INT REFERENCES Clients(client_id), -- Foreign key referencing the Clients table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,               -- Unique identifier for each client
    client_name VARCHAR(255) NOT NULL,         -- Client's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Client's contact email (must be unique)
    phone_number VARCHAR(15),                   -- Client's contact phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store architects involved in projects
CREATE TABLE Architects (
    architect_id SERIAL PRIMARY KEY,            -- Unique identifier for each architect
    architect_name VARCHAR(255) NOT NULL,      -- Architect's name
    bio TEXT,                                   -- Brief biography of the architect
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Architect's contact email (must be unique)
    phone_number VARCHAR(15),                   -- Architect's contact phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to associate architects with projects
CREATE TABLE Project_Architects (
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key referencing Projects
    architect_id INT REFERENCES Architects(architect_id) ON DELETE CASCADE, -- Foreign key referencing Architects
    PRIMARY KEY (project_id, architect_id)             -- Composite primary key
);

-- Table to store project phases (design, construction, etc.)
CREATE TABLE Project_Phases (
    phase_id SERIAL PRIMARY KEY,                -- Unique identifier for each project phase
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key referencing Projects
    phase_name VARCHAR(255) NOT NULL,           -- Name of the project phase
    phase_description TEXT,                      -- Description of the project phase
    start_date DATE NOT NULL,                   -- Start date of the phase
    end_date DATE,                              -- End date of the phase (NULL if ongoing)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store project documents (drawings, reports, etc.)
CREATE TABLE Project_Documents (
    document_id SERIAL PRIMARY KEY,             -- Unique identifier for each document
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key referencing Projects
    document_name VARCHAR(255) NOT NULL,        -- Name of the document
    document_type VARCHAR(100) NOT NULL,        -- Type of the document (e.g., drawing, report)
    document_path VARCHAR(500) NOT NULL,        -- File path to the document
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store reviews or feedback for projects
CREATE TABLE Project_Reviews (
    review_id SERIAL PRIMARY KEY,                -- Unique identifier for each review
    project_id INT REFERENCES Projects(project_id) ON DELETE CASCADE, -- Foreign key referencing Projects
    reviewer_name VARCHAR(255) NOT NULL,        -- Name of the reviewer
    review_text TEXT NOT NULL,                   -- Text of the review
    rating INT CHECK (rating BETWEEN 1 AND 5),  -- Rating score (1 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);
```
