"""
Generated Code Metadata:
========================
Original URL: https://muskgiveaway.vercel.app
Prompt: Design a basic database schema to store information about cryptocurrency giveaways, including participant details, distributed amounts of various cryptocurrencies (BTC, ETH, DOGE), and transaction IDs, based on the context provided.
Generated: DETERMINISTIC_eb4c713ee346109b
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for cryptocurrency giveaways
CREATE DATABASE CryptoGiveaways;

-- Use the newly created database
USE CryptoGiveaways;

-- Table to store participant details
CREATE TABLE Participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,                      -- Name of the participant
    email VARCHAR(255) NOT NULL UNIQUE,              -- Email of the participant (must be unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of when the participant was added
);

-- Table to store cryptocurrency giveaways
CREATE TABLE Giveaways (
    giveaway_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each giveaway
    giveaway_name VARCHAR(100) NOT NULL,             -- Name of the giveaway
    total_amount_btc DECIMAL(18, 8) DEFAULT 0.0,     -- Total amount of Bitcoin distributed
    total_amount_eth DECIMAL(18, 8) DEFAULT 0.0,     -- Total amount of Ethereum distributed
    total_amount_doge DECIMAL(18, 8) DEFAULT 0.0,    -- Total amount of Dogecoin distributed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Timestamp of when the giveaway was created
);

-- Table to link participants to giveaways and record distributed amounts
CREATE TABLE GiveawayParticipants (
    id INT AUTO_INCREMENT PRIMARY KEY,                -- Unique identifier for each record
    giveaway_id INT NOT NULL,                         -- Foreign key referencing the giveaway
    participant_id INT NOT NULL,                      -- Foreign key referencing the participant
    amount_btc DECIMAL(18, 8) DEFAULT 0.0,           -- Amount of Bitcoin distributed to the participant
    amount_eth DECIMAL(18, 8) DEFAULT 0.0,           -- Amount of Ethereum distributed to the participant
    amount_doge DECIMAL(18, 8) DEFAULT 0.0,          -- Amount of Dogecoin distributed to the participant
    transaction_id VARCHAR(255) NOT NULL,            -- Transaction ID for the distribution
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the record was created
    FOREIGN KEY (giveaway_id) REFERENCES Giveaways(giveaway_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for faster querying
CREATE INDEX idx_giveaway ON GiveawayParticipants(giveaway_id);
CREATE INDEX idx_participant ON GiveawayParticipants(participant_id);
```
