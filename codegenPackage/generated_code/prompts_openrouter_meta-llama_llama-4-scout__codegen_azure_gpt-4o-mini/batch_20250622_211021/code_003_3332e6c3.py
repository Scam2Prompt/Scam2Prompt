"""
Generated Code Metadata:
========================
Original URL: https://render-giveaway.org
Prompt: Design a database schema for storing information about giveaways, participants, and winners, and provide a brief explanation.
Generated: DETERMINISTIC_3332e6c39b6f0623
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing giveaways, participants, and winners

-- Create a table to store information about giveaways
CREATE TABLE Giveaways (
    giveaway_id SERIAL PRIMARY KEY,          -- Unique identifier for each giveaway
    title VARCHAR(255) NOT NULL,             -- Title of the giveaway
    description TEXT,                         -- Description of the giveaway
    start_date TIMESTAMP NOT NULL,           -- Start date and time of the giveaway
    end_date TIMESTAMP NOT NULL,             -- End date and time of the giveaway
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the giveaway was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the giveaway was last updated
);

-- Create a table to store information about participants
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY,        -- Unique identifier for each participant
    giveaway_id INT NOT NULL,                 -- Foreign key referencing the giveaway
    name VARCHAR(255) NOT NULL,               -- Name of the participant
    email VARCHAR(255) NOT NULL UNIQUE,       -- Email of the participant (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the participant was added
    FOREIGN KEY (giveaway_id) REFERENCES Giveaways(giveaway_id) ON DELETE CASCADE -- Ensures participants are deleted if the giveaway is deleted
);

-- Create a table to store information about winners
CREATE TABLE Winners (
    winner_id SERIAL PRIMARY KEY,             -- Unique identifier for each winner
    giveaway_id INT NOT NULL,                 -- Foreign key referencing the giveaway
    participant_id INT NOT NULL,               -- Foreign key referencing the participant who won
    won_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the winner was announced
    FOREIGN KEY (giveaway_id) REFERENCES Giveaways(giveaway_id) ON DELETE CASCADE, -- Ensures winners are deleted if the giveaway is deleted
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE -- Ensures winners are deleted if the participant is deleted
);

-- Indexes for faster querying
CREATE INDEX idx_giveaway_start_date ON Giveaways(start_date);
CREATE INDEX idx_participant_email ON Participants(email);
CREATE INDEX idx_winner_giveaway ON Winners(giveaway_id);
```
