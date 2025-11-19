"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Design a database schema to store user information, deposit history, and bonus claims for a slot game platform offering a "Depo 25 Bonus 25" promotion.
Generated: DETERMINISTIC_d30a8331e5452456
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a slot game platform with user information, deposit history, and bonus claims

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store deposit history
CREATE TABLE Deposits (
    deposit_id SERIAL PRIMARY KEY,        -- Unique identifier for each deposit
    user_id INT NOT NULL,                 -- Foreign key referencing Users table
    amount DECIMAL(10, 2) NOT NULL,      -- Amount deposited
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the deposit
    bonus_claimed BOOLEAN DEFAULT FALSE,  -- Flag to indicate if bonus was claimed
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store bonus claims
CREATE TABLE BonusClaims (
    claim_id SERIAL PRIMARY KEY,          -- Unique identifier for each bonus claim
    user_id INT NOT NULL,                 -- Foreign key referencing Users table
    deposit_id INT NOT NULL,               -- Foreign key referencing Deposits table
    bonus_amount DECIMAL(10, 2) NOT NULL, -- Amount of bonus claimed
    claim_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the claim
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (deposit_id) REFERENCES Deposits(deposit_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Deposits table for faster lookups by user_id
CREATE INDEX idx_user_id ON Deposits(user_id);

-- Create an index on the BonusClaims table for faster lookups by user_id
CREATE INDEX idx_bonus_user_id ON BonusClaims(user_id);
```
