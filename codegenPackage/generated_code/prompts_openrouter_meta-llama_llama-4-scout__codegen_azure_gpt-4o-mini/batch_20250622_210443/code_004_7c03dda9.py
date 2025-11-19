"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: Design a database schema for storing information about a football team like cdjuangrande, including tables for team history, players, sponsors, and contact details.
Generated: DETERMINISTIC_7c03dda9c7dbba56
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about a football team

-- Create a table for storing team information
CREATE TABLE Teams (
    team_id SERIAL PRIMARY KEY,          -- Unique identifier for each team
    team_name VARCHAR(100) NOT NULL,    -- Name of the team
    founded_year INT,                    -- Year the team was founded
    stadium_name VARCHAR(100),           -- Name of the team's stadium
    capacity INT,                        -- Seating capacity of the stadium
    contact_email VARCHAR(100) UNIQUE,   -- Contact email for the team
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing player information
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY,        -- Unique identifier for each player
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE, -- Foreign key referencing Teams
    player_name VARCHAR(100) NOT NULL,  -- Name of the player
    position VARCHAR(50),                -- Position of the player (e.g., Forward, Defender)
    date_of_birth DATE,                  -- Date of birth of the player
    nationality VARCHAR(50),             -- Nationality of the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing team history
CREATE TABLE TeamHistory (
    history_id SERIAL PRIMARY KEY,       -- Unique identifier for each history record
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE, -- Foreign key referencing Teams
    year INT NOT NULL,                   -- Year of the historical record
    achievement VARCHAR(255),            -- Description of the achievement (e.g., championships won)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing sponsor information
CREATE TABLE Sponsors (
    sponsor_id SERIAL PRIMARY KEY,       -- Unique identifier for each sponsor
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE, -- Foreign key referencing Teams
    sponsor_name VARCHAR(100) NOT NULL,  -- Name of the sponsor
    sponsorship_amount DECIMAL(10, 2),   -- Amount of sponsorship
    start_date DATE,                     -- Start date of the sponsorship
    end_date DATE,                       -- End date of the sponsorship
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing contact details
CREATE TABLE ContactDetails (
    contact_id SERIAL PRIMARY KEY,       -- Unique identifier for each contact record
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE, -- Foreign key referencing Teams
    contact_type VARCHAR(50) NOT NULL,   -- Type of contact (e.g., Phone, Email)
    contact_value VARCHAR(100) NOT NULL,  -- Value of the contact (e.g., phone number or email address)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Ensure that all tables are created successfully
COMMIT;
```
