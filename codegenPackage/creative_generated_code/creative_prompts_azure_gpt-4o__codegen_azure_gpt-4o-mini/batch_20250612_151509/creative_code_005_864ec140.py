"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitmixr.biz
Prompt: Create a database schema for managing slot game providers, player accounts, and transaction records for a site like KONTAN88.
Generated: DETERMINISTIC_864ec140be5fd960
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database creation
CREATE DATABASE SlotGameDB;

-- Use the created database
USE SlotGameDB;

-- Table for managing slot game providers
CREATE TABLE GameProviders (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each provider
    provider_name VARCHAR(255) NOT NULL,         -- Name of the game provider
    contact_email VARCHAR(255),                   -- Contact email for the provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for managing player accounts
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for the player
    password_hash VARCHAR(255) NOT NULL,          -- Hashed password for security
    email VARCHAR(255) NOT NULL UNIQUE,           -- Unique email for player account
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP NULL,                     -- Timestamp of the last login
    status ENUM('active', 'inactive', 'banned') DEFAULT 'active' -- Player status
);

-- Table for managing transaction records
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    player_id INT NOT NULL,                         -- Foreign key to Players table
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,                -- Transaction amount
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction date
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Index for quick lookup on Transactions by player_id
CREATE INDEX idx_player_id ON Transactions(player_id);

-- Sample Insert into GameProviders
INSERT INTO GameProviders (provider_name, contact_email) VALUES
('Provider A', 'contact@providera.com'),
('Provider B', 'support@providerb.com');

-- Sample Insert into Players
INSERT INTO Players (username, password_hash, email) VALUES
('player1', 'hashed_password_1', 'player1@example.com'),
('player2', 'hashed_password_2', 'player2@example.com');

-- Sample Insert into Transactions
INSERT INTO Transactions (player_id, transaction_type, amount) VALUES
(1, 'deposit', 100.00),
(1, 'withdrawal', 50.00),
(2, 'deposit', 200.00);
```
