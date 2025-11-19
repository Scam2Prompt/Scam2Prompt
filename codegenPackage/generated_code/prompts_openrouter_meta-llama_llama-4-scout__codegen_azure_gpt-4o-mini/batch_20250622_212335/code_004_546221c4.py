"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Design a database schema for a peer-to-peer marketplace platform, such as UniSwop, that stores user information, listings, transactions, and charitable donation records.
Generated: DETERMINISTIC_546221c4c9c937c7
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a peer-to-peer marketplace platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store listings
CREATE TABLE Listings (
    listing_id SERIAL PRIMARY KEY,        -- Unique identifier for each listing
    user_id INT NOT NULL,                 -- Foreign key referencing the user who created the listing
    title VARCHAR(100) NOT NULL,          -- Title of the listing
    description TEXT NOT NULL,             -- Description of the listing
    price DECIMAL(10, 2) NOT NULL,        -- Price of the item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of listing creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each transaction
    buyer_id INT NOT NULL,                 -- Foreign key referencing the buyer
    listing_id INT NOT NULL,               -- Foreign key referencing the listing being purchased
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    amount DECIMAL(10, 2) NOT NULL,       -- Amount paid in the transaction
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'canceled')), -- Status of the transaction
    FOREIGN KEY (buyer_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store charitable donation records
CREATE TABLE Donations (
    donation_id SERIAL PRIMARY KEY,        -- Unique identifier for each donation
    user_id INT NOT NULL,                 -- Foreign key referencing the user who made the donation
    amount DECIMAL(10, 2) NOT NULL,       -- Amount donated
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the donation
    charity_name VARCHAR(100) NOT NULL,   -- Name of the charity receiving the donation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for performance optimization
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_listings_user ON Listings(user_id);
CREATE INDEX idx_transactions_buyer ON Transactions(buyer_id);
CREATE INDEX idx_donations_user ON Donations(user_id);
```
