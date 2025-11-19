"""
Generated Code Metadata:
========================
Original URL: https://cryptomaniaapp.com
Prompt: Design a database schema to store and manage user data, trading history, and market data for a cryptocurrency trading platform like Crypto Mania, ensuring data security and scalability.
Generated: DETERMINISTIC_4ee5eeb6981504dd
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a cryptocurrency trading platform

-- Create a table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,       -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    is_active BOOLEAN DEFAULT TRUE              -- Status of the user account
);

-- Create a table to store trading history
CREATE TABLE trading_history (
    trade_id SERIAL PRIMARY KEY,                -- Unique identifier for each trade
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    trade_type VARCHAR(10) NOT NULL CHECK (trade_type IN ('buy', 'sell')), -- Type of trade
    cryptocurrency VARCHAR(50) NOT NULL,        -- Cryptocurrency being traded
    amount DECIMAL(18, 8) NOT NULL,             -- Amount of cryptocurrency traded
    price DECIMAL(18, 8) NOT NULL,              -- Price at which the trade was executed
    trade_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the trade
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store market data
CREATE TABLE market_data (
    market_id SERIAL PRIMARY KEY,                -- Unique identifier for each market entry
    cryptocurrency VARCHAR(50) NOT NULL,        -- Cryptocurrency symbol
    price DECIMAL(18, 8) NOT NULL,              -- Current market price
    volume DECIMAL(18, 8) NOT NULL,             -- Trading volume in the last 24 hours
    market_cap DECIMAL(18, 8) NOT NULL,         -- Market capitalization
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of last market update
    UNIQUE (cryptocurrency)                      -- Ensure unique entries for each cryptocurrency
);

-- Create a table to store user sessions for security
CREATE TABLE user_sessions (
    session_id SERIAL PRIMARY KEY,               -- Unique identifier for each session
    user_id INT NOT NULL,                        -- Foreign key referencing the user
    session_token VARCHAR(255) NOT NULL UNIQUE, -- Unique session token for authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of session creation
    expires_at TIMESTAMP NOT NULL,               -- Expiration time for the session
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the trading history for faster queries
CREATE INDEX idx_user_trades ON trading_history(user_id, trade_timestamp);

-- Create an index on market data for faster access
CREATE INDEX idx_market_data ON market_data(cryptocurrency);
```
