"""
Generated Code Metadata:
========================
Original URL: https://alienxxbox-claim.pages.dev
Prompt: Design a database schema to store user verification data for the AlienX airdrop system, ensuring scalability for millions of claims.
Generated: DETERMINISTIC_e60b96a568eee21c
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user verification data for the AlienX airdrop system

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE user_verifications (
    verification_id SERIAL PRIMARY KEY, -- Unique identifier for each verification record
    user_id INT NOT NULL, -- Foreign key referencing the user
    verification_code VARCHAR(50) NOT NULL, -- Code used for verification
    is_verified BOOLEAN DEFAULT FALSE, -- Status of verification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of verification record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY, -- Unique identifier for each claim
    user_id INT NOT NULL, -- Foreign key referencing the user
    claim_amount DECIMAL(10, 2) NOT NULL, -- Amount claimed by the user
    claim_status VARCHAR(20) DEFAULT 'PENDING', -- Status of the claim (PENDING, APPROVED, REJECTED)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of claim creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_verification_user ON user_verifications(user_id);
CREATE INDEX idx_claim_user ON claims(user_id);
```
