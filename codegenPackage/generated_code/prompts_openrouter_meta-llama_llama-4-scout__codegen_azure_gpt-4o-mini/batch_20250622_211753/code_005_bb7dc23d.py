"""
Generated Code Metadata:
========================
Original URL: https://whitecasino.net
Prompt: Design a database schema to store information about various online casinos, their games, and user reviews, inspired by WhiteCasino.net's content and features.
Generated: DETERMINISTIC_bb7dc23d346ba6c7
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about online casinos, their games, and user reviews

-- Create a table to store information about online casinos
CREATE TABLE casinos (
    casino_id SERIAL PRIMARY KEY, -- Unique identifier for each casino
    name VARCHAR(255) NOT NULL, -- Name of the casino
    website VARCHAR(255) NOT NULL UNIQUE, -- Website URL of the casino
    established_year INT CHECK (established_year > 1900 AND established_year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year the casino was established
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5), -- Rating of the casino (0 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store information about games offered by casinos
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game
    casino_id INT NOT NULL, -- Foreign key referencing the casino
    name VARCHAR(255) NOT NULL, -- Name of the game
    genre VARCHAR(100) NOT NULL, -- Genre of the game (e.g., slot, table, card)
    release_date DATE, -- Release date of the game
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5), -- Rating of the game (0 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (casino_id) REFERENCES casinos(casino_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store user reviews for games
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    game_id INT NOT NULL, -- Foreign key referencing the game
    user_id INT NOT NULL, -- Identifier for the user (could reference a users table)
    review_text TEXT NOT NULL, -- Text of the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the user (1 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Optional: Create a table to store user information (if needed)
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(255) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);
```
