"""
Generated Code Metadata:
========================
Original URL: https://grampreico.com
Prompt: Design a database schema to store information about the various games, game providers, and user transactions on the nagoya168 platform, and suggest a suitable database management system.
Generated: DETERMINISTIC_f9ce761db6c4be5e
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for the Nagoya168 platform

-- Use PostgreSQL as the database management system
CREATE DATABASE nagoya168;

-- Connect to the nagoya168 database
\c nagoya168;

-- Table to store information about game providers
CREATE TABLE game_providers (
    provider_id SERIAL PRIMARY KEY, -- Unique identifier for each provider
    provider_name VARCHAR(255) NOT NULL, -- Name of the game provider
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the provider was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about games
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game
    game_name VARCHAR(255) NOT NULL, -- Name of the game
    provider_id INT NOT NULL, -- Foreign key referencing the game provider
    genre VARCHAR(100), -- Genre of the game
    release_date DATE, -- Release date of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for the user
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store user transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL, -- Foreign key referencing the user
    game_id INT NOT NULL, -- Foreign key referencing the game
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the transaction occurred
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    status VARCHAR(50) NOT NULL, -- Status of the transaction (e.g., 'completed', 'pending', 'failed')
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_game_provider ON games(provider_id);
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_transaction_user ON transactions(user_id);
CREATE INDEX idx_transaction_game ON transactions(game_id);
```
