"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Design a database schema for an online auction platform like Abilia Trading, including tables for users, auctions, bids, and payments."
Generated: DETERMINISTIC_884a7cedf9d9e319
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online auction platform

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store auction details
CREATE TABLE Auctions (
    auction_id SERIAL PRIMARY KEY,        -- Unique identifier for each auction
    user_id INT NOT NULL,                 -- Foreign key referencing the user who created the auction
    title VARCHAR(100) NOT NULL,          -- Title of the auction item
    description TEXT NOT NULL,             -- Detailed description of the auction item
    starting_price DECIMAL(10, 2) NOT NULL, -- Starting price for the auction
    reserve_price DECIMAL(10, 2),         -- Optional reserve price for the auction
    start_time TIMESTAMP NOT NULL,        -- Start time of the auction
    end_time TIMESTAMP NOT NULL,          -- End time of the auction
    status VARCHAR(20) DEFAULT 'active',  -- Status of the auction (active, completed, cancelled)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Auction creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure user deletion cascades
);

-- Table to store bids placed on auctions
CREATE TABLE Bids (
    bid_id SERIAL PRIMARY KEY,            -- Unique identifier for each bid
    auction_id INT NOT NULL,              -- Foreign key referencing the auction
    user_id INT NOT NULL,                 -- Foreign key referencing the user who placed the bid
    bid_amount DECIMAL(10, 2) NOT NULL,   -- Amount of the bid
    bid_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time when the bid was placed
    FOREIGN KEY (auction_id) REFERENCES Auctions(auction_id) ON DELETE CASCADE, -- Ensure auction deletion cascades
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure user deletion cascades
    CHECK (bid_amount > 0)                -- Ensure bid amount is positive
);

-- Table to store payment transactions
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,        -- Unique identifier for each payment
    user_id INT NOT NULL,                 -- Foreign key referencing the user making the payment
    auction_id INT NOT NULL,              -- Foreign key referencing the auction for which the payment is made
    amount DECIMAL(10, 2) NOT NULL,       -- Amount of the payment
    payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time when the payment was made
    payment_status VARCHAR(20) DEFAULT 'pending', -- Status of the payment (pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure user deletion cascades
    FOREIGN KEY (auction_id) REFERENCES Auctions(auction_id) ON DELETE CASCADE -- Ensure auction deletion cascades
);
```
