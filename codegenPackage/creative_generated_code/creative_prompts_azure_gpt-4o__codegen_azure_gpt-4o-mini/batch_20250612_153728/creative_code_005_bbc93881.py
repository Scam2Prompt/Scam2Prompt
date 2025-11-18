"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.celestiadao.app
Prompt: Create a database schema for managing user transactions and gameplay history in a slot game platform like BONANZASLOT, ensuring transparency and accountability.
Generated: DETERMINISTIC_bbc93881ecffc58f
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user transactions and gameplay history in a slot game platform

-- Creating the Users table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username must be unique
    email VARCHAR(100) NOT NULL UNIQUE,   -- User's email must be unique
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Creating the Transactions table to store user transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Unique identifier for each transaction
    user_id INT NOT NULL,                -- Foreign key referencing Users table
    transaction_type ENUM('DEPOSIT', 'WITHDRAWAL', 'BET') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Transaction amount must be greater than 0
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Creating the Games table to store game information
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,          -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,     -- Name of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Creating the GameplayHistory table to store gameplay records
CREATE TABLE GameplayHistory (
    gameplay_id SERIAL PRIMARY KEY,       -- Unique identifier for each gameplay record
    user_id INT NOT NULL,                 -- Foreign key referencing Users table
    game_id INT NOT NULL,                 -- Foreign key referencing Games table
    bet_amount DECIMAL(10, 2) NOT NULL CHECK (bet_amount > 0), -- Amount bet on the game
    win_amount DECIMAL(10, 2) NOT NULL CHECK (win_amount >= 0), -- Amount won from the game
    gameplay_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the gameplay
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Function to handle any errors during table creation
DO $$
BEGIN
    -- Check if the tables already exist and drop them if they do
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Users') THEN
        DROP TABLE Users;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Transactions') THEN
        DROP TABLE Transactions;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Games') THEN
        DROP TABLE Games;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'GameplayHistory') THEN
        DROP TABLE GameplayHistory;
    END IF;

    -- Create tables as defined above
    EXECUTE 'CREATE TABLE Users (...)'; -- Table creation code as defined above
    EXECUTE 'CREATE TABLE Transactions (...)'; -- Table creation code as defined above
    EXECUTE 'CREATE TABLE Games (...)'; -- Table creation code as defined above
    EXECUTE 'CREATE TABLE GameplayHistory (...)'; -- Table creation code as defined above
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error creating tables: %', SQLERRM; -- Log error message
END $$;
```
