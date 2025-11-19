"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Create a database schema for an online slot platform that includes game providers such as Pragmatic Play, Habanero, Joker123, PGSoft, and Spadegaming, as listed on ANGKA805.
Generated: DETERMINISTIC_c9b43a0940a09e01
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online slot platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS GameProviders;
DROP TABLE IF EXISTS Games;

-- Table to store game providers
CREATE TABLE GameProviders (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each provider
    provider_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the game provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the provider was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store games
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,  -- Name of the game
    provider_id INT NOT NULL,  -- Foreign key referencing the game provider
    release_date DATE,  -- Release date of the game
    RTP DECIMAL(5, 2),  -- Return to Player percentage
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (provider_id) REFERENCES GameProviders(provider_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Insert initial game providers
INSERT INTO GameProviders (provider_name) VALUES
('Pragmatic Play'),
('Habanero'),
('Joker123'),
('PGSoft'),
('Spadegaming');

-- Example of inserting a game (uncomment to use)
-- INSERT INTO Games (game_name, provider_id, release_date, RTP) VALUES
-- ('Great Rhino', 1, '2018-05-01', 96.71),
-- ('Wild Fruits', 2, '2019-06-15', 95.00),
-- ('Dragon Tiger', 3, '2020-01-10', 97.00),
-- ('Medusa II', 4, '2019-03-20', 96.50),
-- ('Jungle Delight', 5, '2021-07-30', 95.50);
```
