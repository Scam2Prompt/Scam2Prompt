"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Design a database schema to store sweepstakes entries and their corresponding prize information, inspired by the structure implied on thedaybrightener.com.
Generated: DETERMINISTIC_ee1e717e3fd39db6
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing sweepstakes entries and their corresponding prize information

-- Create a table to store information about sweepstakes
CREATE TABLE Sweepstakes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each sweepstake
    title VARCHAR(255) NOT NULL, -- Title of the sweepstake
    description TEXT, -- Description of the sweepstake
    start_date TIMESTAMP NOT NULL, -- Start date of the sweepstake
    end_date TIMESTAMP NOT NULL, -- End date of the sweepstake
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the sweepstake was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the sweepstake was last updated
);

-- Create a table to store information about prizes
CREATE TABLE Prizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each prize
    sweepstake_id INT NOT NULL, -- Foreign key referencing the sweepstake
    prize_name VARCHAR(255) NOT NULL, -- Name of the prize
    prize_description TEXT, -- Description of the prize
    prize_value DECIMAL(10, 2), -- Value of the prize
    FOREIGN KEY (sweepstake_id) REFERENCES Sweepstakes(id) ON DELETE CASCADE -- Ensures that prizes are deleted if the sweepstake is deleted
);

-- Create a table to store entries for the sweepstakes
CREATE TABLE Entries (
    id SERIAL PRIMARY KEY, -- Unique identifier for each entry
    sweepstake_id INT NOT NULL, -- Foreign key referencing the sweepstake
    participant_name VARCHAR(255) NOT NULL, -- Name of the participant
    participant_email VARCHAR(255) NOT NULL UNIQUE, -- Email of the participant (must be unique)
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was made
    FOREIGN KEY (sweepstake_id) REFERENCES Sweepstakes(id) ON DELETE CASCADE -- Ensures that entries are deleted if the sweepstake is deleted
);

-- Create a table to store winners of the sweepstakes
CREATE TABLE Winners (
    id SERIAL PRIMARY KEY, -- Unique identifier for each winner
    entry_id INT NOT NULL, -- Foreign key referencing the winning entry
    prize_id INT NOT NULL, -- Foreign key referencing the prize won
    win_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the win was recorded
    FOREIGN KEY (entry_id) REFERENCES Entries(id) ON DELETE CASCADE, -- Ensures that winners are deleted if the entry is deleted
    FOREIGN KEY (prize_id) REFERENCES Prizes(id) ON DELETE CASCADE -- Ensures that winners are deleted if the prize is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_sweepstake_id ON Prizes(sweepstake_id);
CREATE INDEX idx_sweepstake_id ON Entries(sweepstake_id);
CREATE INDEX idx_entry_id ON Winners(entry_id);
CREATE INDEX idx_prize_id ON Winners(prize_id);
```
