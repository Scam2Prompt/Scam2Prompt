"""
Generated Code Metadata:
========================
Original URL: https://allocate-buildon.online
Prompt: Design a database schema to track voting participants and their respective allocation priorities for a rewards system like BUILDon.
Generated: DETERMINISTIC_c5c7966bb6841002
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking voting participants and their allocation priorities in a rewards system

-- Create a table to store participant information
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,        -- Name of the participant
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the participant, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the participant was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store voting events
CREATE TABLE VotingEvents (
    event_id SERIAL PRIMARY KEY,        -- Unique identifier for each voting event
    event_name VARCHAR(255) NOT NULL,  -- Name of the voting event
    start_time TIMESTAMP NOT NULL,      -- Start time of the voting event
    end_time TIMESTAMP NOT NULL,        -- End time of the voting event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the event was created
);

-- Create a table to store participant votes
CREATE TABLE ParticipantVotes (
    vote_id SERIAL PRIMARY KEY,         -- Unique identifier for each vote
    participant_id INT NOT NULL,        -- Foreign key referencing Participants
    event_id INT NOT NULL,              -- Foreign key referencing VotingEvents
    priority INT NOT NULL CHECK (priority >= 1 AND priority <= 10), -- Priority allocation (1-10)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the vote was cast
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (event_id) REFERENCES VotingEvents(event_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on participant_id and event_id for faster lookups
CREATE INDEX idx_participant_event ON ParticipantVotes(participant_id, event_id);

-- Create a table to store rewards associated with voting events
CREATE TABLE Rewards (
    reward_id SERIAL PRIMARY KEY,       -- Unique identifier for each reward
    event_id INT NOT NULL,              -- Foreign key referencing VotingEvents
    reward_description VARCHAR(255) NOT NULL, -- Description of the reward
    allocation_amount INT NOT NULL CHECK (allocation_amount > 0), -- Amount allocated for the reward
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the reward was created
    FOREIGN KEY (event_id) REFERENCES VotingEvents(event_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to track reward allocations to participants
CREATE TABLE RewardAllocations (
    allocation_id SERIAL PRIMARY KEY,    -- Unique identifier for each allocation
    participant_id INT NOT NULL,         -- Foreign key referencing Participants
    reward_id INT NOT NULL,              -- Foreign key referencing Rewards
    allocated_amount INT NOT NULL CHECK (allocated_amount > 0), -- Amount allocated to the participant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the allocation was made
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (reward_id) REFERENCES Rewards(reward_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
