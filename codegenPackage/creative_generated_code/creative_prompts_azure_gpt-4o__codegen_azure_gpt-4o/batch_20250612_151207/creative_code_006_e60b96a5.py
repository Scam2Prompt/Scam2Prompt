"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alienxxbox-claim.pages.dev
Prompt: Design a database schema to store user verification data for the AlienX airdrop system, ensuring scalability for millions of claims.
Generated: DETERMINISTIC_e60b96a568eee21c
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user verification data for the AlienX airdrop system.

-- Table to store user details
CREATE TABLE Users (
    user_id BIGSERIAL PRIMARY KEY,                -- Unique identifier for each user
    wallet_address VARCHAR(255) NOT NULL UNIQUE, -- User's wallet address (unique for each user)
    email VARCHAR(255) NULL,                     -- Optional: User's email address
    phone_number VARCHAR(50) NULL,               -- Optional: User's phone number
    created_at TIMESTAMP DEFAULT NOW(),          -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT NOW()           -- Timestamp of last update
);

-- Table to store verification details
CREATE TABLE Verifications (
    verification_id BIGSERIAL PRIMARY KEY,       -- Unique identifier for each verification record
    user_id BIGINT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key linking to Users table
    status VARCHAR(50) NOT NULL,                -- Verification status (e.g., "pending", "verified", "failed")
    verification_code VARCHAR(255) NOT NULL,    -- Unique code for verification
    attempts INT DEFAULT 0,                     -- Number of verification attempts
    expires_at TIMESTAMP,                       -- Expiration timestamp for verification code
    created_at TIMESTAMP DEFAULT NOW(),         -- Timestamp of verification creation
    updated_at TIMESTAMP DEFAULT NOW()          -- Timestamp of last update
);

-- Table to store claims for the airdrop
CREATE TABLE Claims (
    claim_id BIGSERIAL PRIMARY KEY,             -- Unique identifier for each claim record
    user_id BIGINT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key linking to Users table
    claim_status VARCHAR(50) NOT NULL,         -- Claim status (e.g., "pending", "approved", "rejected")
    airdrop_id BIGINT NOT NULL,                -- Identifier for the specific airdrop
    claimed_at TIMESTAMP DEFAULT NOW(),        -- Timestamp of the claim attempt
    created_at TIMESTAMP DEFAULT NOW(),        -- Timestamp of claim creation
    updated_at TIMESTAMP DEFAULT NOW()         -- Timestamp of last update
);

-- Optimization: Indexes for fast lookup
CREATE INDEX idx_wallet_address ON Users(wallet_address); -- Index on wallet address for quick user lookup
CREATE INDEX idx_verification_status ON Verifications(status); -- Index on verification status
CREATE INDEX idx_claim_status ON Claims(claim_status); -- Index on claim status

-- Constraints for data integrity
ALTER TABLE Verifications ADD CONSTRAINT chk_status CHECK (status IN ('pending', 'verified', 'failed')); -- Ensure status is valid
ALTER TABLE Claims ADD CONSTRAINT chk_claim_status CHECK (claim_status IN ('pending', 'approved', 'rejected')); -- Ensure claim status is valid
```
