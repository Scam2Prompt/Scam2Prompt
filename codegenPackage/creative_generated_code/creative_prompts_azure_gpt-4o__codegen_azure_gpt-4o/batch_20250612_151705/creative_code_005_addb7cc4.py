"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Create a database schema for managing content monetization features, including "Pay to View," "Memberships," and "Tips," as outlined on Lyvely.
Generated: DETERMINISTIC_addb7cc4a1c2ee92
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Content Monetization Features

-- Users table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,            -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for secure storage
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of the last update
);

-- Content table to store information about content
CREATE TABLE Content (
    content_id SERIAL PRIMARY KEY,         -- Unique identifier for each content item
    user_id INT REFERENCES Users(user_id), -- ID of the creator/user
    title VARCHAR(255) NOT NULL,           -- Title of the content
    description TEXT,                      -- Description of the content
    content_url TEXT NOT NULL,             -- URL or path to the content
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of content creation
    updated_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of the last update
    monetization_type VARCHAR(50) CHECK (monetization_type IN ('PayToView', 'Membership', 'Tips')) NOT NULL
);

-- Pay to View table to store pricing information for "pay-to-view" content
CREATE TABLE PayToView (
    ptv_id SERIAL PRIMARY KEY,             -- Unique identifier for pay-to-view pricing
    content_id INT REFERENCES Content(content_id), -- Associated content ID
    price DECIMAL(10, 2) NOT NULL,         -- Price to access the content
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of price creation
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of the last update
);

-- Memberships table to store subscription plans for users
CREATE TABLE Memberships (
    membership_id SERIAL PRIMARY KEY,      -- Unique identifier for membership plan
    user_id INT REFERENCES Users(user_id), -- User offering the membership
    name VARCHAR(50) NOT NULL,             -- Name of the membership plan
    description TEXT,                      -- Description of the membership plan
    price DECIMAL(10, 2) NOT NULL,         -- Monthly price for the subscription
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of membership creation
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of the last update
);

-- Tips table to store tips given to a user or for content
CREATE TABLE Tips (
    tip_id SERIAL PRIMARY KEY,             -- Unique identifier for each tip
    sender_user_id INT REFERENCES Users(user_id), -- User sending the tip
    receiver_user_id INT REFERENCES Users(user_id), -- User receiving the tip
    content_id INT REFERENCES Content(content_id), -- Optional: Associated content ID
    amount DECIMAL(10, 2) NOT NULL,        -- Tip amount
    message TEXT,                          -- Optional message from the sender
    created_at TIMESTAMP DEFAULT NOW()     -- Timestamp of the tip transaction
);

-- Transactions table to store all monetization transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    user_id INT REFERENCES Users(user_id), -- User making the payment
    monetization_type VARCHAR(50) CHECK (monetization_type IN ('PayToView', 'Membership', 'Tips')) NOT NULL, -- Type of monetization
    related_id INT,                        -- ID of the related monetization (e.g., ptv_id, membership_id, or tip_id)
    amount DECIMAL(10, 2) NOT NULL,        -- Transaction amount
    transaction_status VARCHAR(50) CHECK (transaction_status IN ('Pending', 'Completed', 'Failed')) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp of the transaction
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp of the last update
);

-- Error handling: Ensure referential integrity constraints and logical data constraints
-- Example: User cannot tip themselves
-- Example: Prices must be positive
-- These constraints can be further enforced through application-layer logic or triggers.
```
