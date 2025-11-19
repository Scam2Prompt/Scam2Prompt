"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: Design a database schema for storing information about NFTs, user votes, and claims on a platform similar to Shibuya, ensuring efficient lookup and retrieval of user data.
Generated: DETERMINISTIC_6c3097f7f8bcd63f
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an NFT platform with user votes and claims

-- Table to store information about NFTs
CREATE TABLE nfts (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each NFT
    name VARCHAR(255) NOT NULL,                -- Name of the NFT
    description TEXT,                           -- Description of the NFT
    creator_id INT NOT NULL,                   -- User ID of the creator
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of NFT creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    UNIQUE (name)                              -- Ensure NFT names are unique
);

-- Table to store user information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for each user
    email VARCHAR(255) NOT NULL UNIQUE,       -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user registration
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store user votes on NFTs
CREATE TABLE nft_votes (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each vote
    nft_id INT NOT NULL,                       -- ID of the NFT being voted on
    user_id INT NOT NULL,                      -- ID of the user casting the vote
    vote_value INT CHECK (vote_value IN (1, -1)), -- Vote value: 1 for upvote, -1 for downvote
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the vote
    FOREIGN KEY (nft_id) REFERENCES nfts(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (nft_id, user_id)                  -- Ensure a user can only vote once per NFT
);

-- Table to store claims made by users on NFTs
CREATE TABLE nft_claims (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each claim
    nft_id INT NOT NULL,                       -- ID of the NFT being claimed
    user_id INT NOT NULL,                      -- ID of the user making the claim
    claim_reason TEXT NOT NULL,                -- Reason for the claim
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the claim
    FOREIGN KEY (nft_id) REFERENCES nfts(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for efficient lookup
CREATE INDEX idx_nft_votes_nft_id ON nft_votes(nft_id);
CREATE INDEX idx_nft_votes_user_id ON nft_votes(user_id);
CREATE INDEX idx_nft_claims_nft_id ON nft_claims(nft_id);
CREATE INDEX idx_nft_claims_user_id ON nft_claims(user_id);
```
