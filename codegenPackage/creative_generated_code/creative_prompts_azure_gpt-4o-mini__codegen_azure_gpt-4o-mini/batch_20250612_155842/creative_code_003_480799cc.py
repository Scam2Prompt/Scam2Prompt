"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Create a sample database schema for managing esports tournaments, including tables for participants, sponsors, and event details as utilized by Ace Pro.
Generated: DETERMINISTIC_480799cc53d43ba7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing esports tournaments

-- Drop the database if it exists (for easy re-creation during development)
DROP DATABASE IF EXISTS esports_tournament_management;

-- Create a new database for the esports tournament management system
CREATE DATABASE esports_tournament_management;
USE esports_tournament_management;

-- Table to store participant details
CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,                    -- Name of the participant
    gamer_tag VARCHAR(50) NOT NULL UNIQUE,         -- Unique gaming tag for the participant
    email VARCHAR(100) NOT NULL UNIQUE,            -- Email of the participant
    phone VARCHAR(15),                             -- Contact number of the participant
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    status ENUM('active', 'inactive') DEFAULT 'active' -- Status of the participant
);

-- Table to store sponsor details
CREATE TABLE sponsors (
    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each sponsor
    name VARCHAR(100) NOT NULL,                     -- Name of the sponsor
    contact_person VARCHAR(100),                    -- Contact person at the sponsoring company
    email VARCHAR(100) NOT NULL UNIQUE,             -- Email for communication
    phone VARCHAR(15),                              -- Contact number of the sponsor
    sponsorship_amount DECIMAL(10, 2) NOT NULL,    -- Amount sponsored
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Date when the sponsor joined
);

-- Table to store event details
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,              -- Name of the esports event
    event_date DATETIME NOT NULL,                   -- Date and time of the event
    location VARCHAR(150) NOT NULL,                 -- Location of the event
    prize_pool DECIMAL(10, 2) NOT NULL,            -- Total prize pool for the event
    max_participants INT NOT NULL,                  -- Maximum number of participants
    status ENUM('upcoming', 'ongoing', 'completed') DEFAULT 'upcoming' -- Status of the event
);

-- Table to manage the relationship between participants and events
CREATE TABLE event_participants (
    event_id INT NOT NULL,                          -- Identifier for the event
    participant_id INT NOT NULL,                    -- Identifier for the participant
    PRIMARY KEY (event_id, participant_id),        -- Composite primary key
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,  -- Foreign key reference to events
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE -- Foreign key reference to participants
);

-- Table to manage sponsorships for events
CREATE TABLE event_sponsors (
    event_id INT NOT NULL,                          -- Identifier for the event
    sponsor_id INT NOT NULL,                        -- Identifier for the sponsor
    PRIMARY KEY (event_id, sponsor_id),            -- Composite primary key
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,  -- Foreign key reference to events
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(sponsor_id) ON DELETE CASCADE -- Foreign key reference to sponsors
);

-- Sample data insertion (optional)
-- INSERT INTO participants (name, gamer_tag, email, phone) VALUES ('John Doe', 'Gamer123', 'john@example.com', '1234567890');
-- INSERT INTO sponsors (name, contact_person, email, phone, sponsorship_amount) VALUES ('Tech Corp', 'Alice Smith', 'alice@techcorp.com', '1234567890', 5000.00);
-- INSERT INTO events (event_name, event_date, location, prize_pool, max_participants) VALUES ('Championship 2024', '2024-06-15 10:00:00', 'Los Angeles', 10000.00, 100);

-- Note: To run this schema, ensure you have the necessary permissions and a compatible SQL environment such as MySQL or MariaDB.
```
