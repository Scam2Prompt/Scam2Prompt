"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Design a database schema in MySQL for storing user entries, referral data, and wallet connection details for the ScapesMania giveaway system.
Generated: DETERMINISTIC_ca3049f76184644a
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for ScapesMania Giveaway System
-- This schema includes tables for user entries, referral data, and wallet connection details

-- Drop the database if it exists (for development purposes)
DROP DATABASE IF EXISTS ScapesMania;
CREATE DATABASE ScapesMania;
USE ScapesMania;

-- Table to store user details
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,        -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email for communication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Table to store user entries for giveaways
CREATE TABLE UserEntries (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each entry
    user_id INT NOT NULL,                          -- Foreign key referencing Users table
    giveaway_id INT NOT NULL,                      -- Identifier for the associated giveaway
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the entry
    FOREIGN KEY (user_id) REFERENCES Users(user_id) -- Establish foreign key relationship
);

-- Table to store referral data
CREATE TABLE Referrals (
    referral_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each referral record
    user_id INT NOT NULL,                          -- Foreign key referencing the user who made the referral
    referred_email VARCHAR(100) NOT NULL,         -- Email of the referred user
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the referral
    FOREIGN KEY (user_id) REFERENCES Users(user_id) -- Establish foreign key relationship
);

-- Table to store wallet connection details
CREATE TABLE WalletConnections (
    wallet_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each wallet connection
    user_id INT NOT NULL,                          -- Foreign key referencing Users table
    wallet_address VARCHAR(255) NOT NULL UNIQUE,   -- Unique wallet address for the user
    connection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the wallet was connected
    FOREIGN KEY (user_id) REFERENCES Users(user_id) -- Establish foreign key relationship
);

-- Sample insertion of data into Users table (for testing)
INSERT INTO Users (username, email) VALUES 
('exampleUser1', 'user1@example.com'),
('exampleUser2', 'user2@example.com');

-- Sample insertion of data into UserEntries table (for testing)
INSERT INTO UserEntries (user_id, giveaway_id) VALUES 
(1, 101),
(2, 102);

-- Sample insertion of data into Referrals table (for testing)
INSERT INTO Referrals (user_id, referred_email) VALUES 
(1, 'referral@example.com');

-- Sample insertion of data into WalletConnections table (for testing)
INSERT INTO WalletConnections (user_id, wallet_address) VALUES 
(1, '0x123456789ABCDEF123456789ABCDEF1234567890'),
(2, '0x0987654321FEDCBA0987654321FEDCBA09876543');

-- End of SQL script
```
