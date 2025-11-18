"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkcs.org
Prompt: Suggest a database schema for storing information about Morahs and their placement options, as described by ZKCS.
Generated: DETERMINISTIC_cf022778168eb17c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about Morahs and their placement options

-- Table to store information about Morahs
CREATE TABLE Morahs (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each Morah
    name VARCHAR(100) NOT NULL,  -- Name of the Morah
    age INT CHECK (age >= 0),  -- Age of the Morah, must be non-negative
    specialization VARCHAR(100),  -- Specialization area of the Morah
    email VARCHAR(255) UNIQUE NOT NULL,  -- Email address of the Morah, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the Morah was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Table to store placement options for Morahs
CREATE TABLE PlacementOptions (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each placement option
    morah_id INT NOT NULL,  -- Foreign key referencing the Morah
    option_description TEXT NOT NULL,  -- Description of the placement option
    location VARCHAR(255),  -- Location where the placement is offered
    availability BOOLEAN DEFAULT TRUE,  -- Indicates if the placement option is currently available
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the option was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for the last update
    FOREIGN KEY (morah_id) REFERENCES Morahs(id) ON DELETE CASCADE  -- Establishing foreign key relationship
);

-- Table to store feedback for Morahs
CREATE TABLE Feedback (
    id SERIAL PRIMARY KEY,  -- Unique identifier for each feedback entry
    morah_id INT NOT NULL,  -- Foreign key referencing the Morah
    comments TEXT,  -- Comments about the Morah
    rating INT CHECK (rating BETWEEN 1 AND 5),  -- Rating for the Morah, must be between 1 and 5
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the feedback was submitted
    FOREIGN KEY (morah_id) REFERENCES Morahs(id) ON DELETE CASCADE  -- Establishing foreign key relationship
);

-- Index to optimize searches on Morah's email
CREATE INDEX idx_morah_email ON Morahs(email);

-- Index to optimize searches on placement option descriptions
CREATE INDEX idx_placement_desc ON PlacementOptions(option_description);
```
