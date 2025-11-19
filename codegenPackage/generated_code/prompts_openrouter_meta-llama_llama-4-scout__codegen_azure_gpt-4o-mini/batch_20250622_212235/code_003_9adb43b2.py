"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: "Design a community platform database schema to track NFT ownership and access levels, similar to The Park mentioned in Tim Cheese."
Generated: DETERMINISTIC_9adb43b2f9c4db87
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a community platform to track NFT ownership and access levels

-- Create a table to store users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store NFTs
CREATE TABLE NFTs (
    nft_id SERIAL PRIMARY KEY,            -- Unique identifier for each NFT
    name VARCHAR(100) NOT NULL,           -- Name of the NFT
    description TEXT,                     -- Description of the NFT
    creator_id INT NOT NULL,              -- User ID of the creator
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of NFT creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (creator_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to track NFT ownership
CREATE TABLE Ownership (
    ownership_id SERIAL PRIMARY KEY,      -- Unique identifier for each ownership record
    nft_id INT NOT NULL,                  -- NFT ID
    owner_id INT NOT NULL,                -- User ID of the owner
    acquired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of acquisition
    FOREIGN KEY (nft_id) REFERENCES NFTs(nft_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (owner_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (nft_id, owner_id)             -- Ensure a user can only own one instance of an NFT
);

-- Create a table to define access levels for NFTs
CREATE TABLE AccessLevels (
    access_level_id SERIAL PRIMARY KEY,   -- Unique identifier for each access level
    level_name VARCHAR(50) NOT NULL UNIQUE, -- Name of the access level (e.g., "Basic", "Premium")
    description TEXT                      -- Description of the access level
);

-- Create a table to link users to their access levels for specific NFTs
CREATE TABLE UserAccess (
    user_access_id SERIAL PRIMARY KEY,     -- Unique identifier for each user access record
    user_id INT NOT NULL,                  -- User ID
    nft_id INT NOT NULL,                   -- NFT ID
    access_level_id INT NOT NULL,          -- Access level ID
    granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of access level grant
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (nft_id) REFERENCES NFTs(nft_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (access_level_id) REFERENCES AccessLevels(access_level_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (user_id, nft_id)               -- Ensure a user can only have one access level per NFT
);

-- Create an index on the Ownership table for faster lookups
CREATE INDEX idx_nft_owner ON Ownership(nft_id, owner_id);

-- Create an index on the UserAccess table for faster lookups
CREATE INDEX idx_user_nft_access ON UserAccess(user_id, nft_id);
```
