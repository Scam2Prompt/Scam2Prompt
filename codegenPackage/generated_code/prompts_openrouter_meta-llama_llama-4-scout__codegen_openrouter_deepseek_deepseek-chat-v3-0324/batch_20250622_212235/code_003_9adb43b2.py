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
-- Database schema for NFT-based community platform

-- Users table to store community members
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile_image_url VARCHAR(255),
    bio TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE
);

-- NFT collections table
CREATE TABLE nft_collections (
    collection_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    contract_address VARCHAR(42) NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- NFTs table
CREATE TABLE nfts (
    nft_id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES nft_collections(collection_id) ON DELETE CASCADE,
    token_id VARCHAR(100) NOT NULL,
    metadata_url VARCHAR(255),
    image_url VARCHAR(255),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(collection_id, token_id)
);

-- NFT ownership tracking
CREATE TABLE nft_ownership (
    ownership_id SERIAL PRIMARY KEY,
    nft_id INTEGER REFERENCES nfts(nft_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    acquired_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    sold_at TIMESTAMP WITH TIME ZONE,
    current_owner BOOLEAN DEFAULT TRUE,
    transaction_hash VARCHAR(66),
    UNIQUE(nft_id, user_id, current_owner) WHERE current_owner = TRUE
);

-- Access levels/groups
CREATE TABLE access_levels (
    level_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- NFT to access level mapping
CREATE TABLE nft_access_mapping (
    mapping_id SERIAL PRIMARY KEY,
    nft_id INTEGER REFERENCES nfts(nft_id) ON DELETE CASCADE,
    level_id INTEGER REFERENCES access_levels(level_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(nft_id, level_id)
);

-- User access tracking
CREATE TABLE user_access (
    access_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    level_id INTEGER REFERENCES access_levels(level_id) ON DELETE CASCADE,
    granted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    granted_by INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    UNIQUE(user_id, level_id) WHERE is_active = TRUE
);

-- Community spaces/areas
CREATE TABLE community_spaces (
    space_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    required_level_id INTEGER REFERENCES access_levels(level_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Activity log for user actions
CREATE TABLE activity_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    action_type VARCHAR(50) NOT NULL,
    target_type VARCHAR(50),
    target_id INTEGER,
    details JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_nft_ownership_user ON nft_ownership(user_id);
CREATE INDEX idx_nft_ownership_nft ON nft_ownership(nft_id);
CREATE INDEX idx_user_access_user ON user_access(user_id);
CREATE INDEX idx_user_access_level ON user_access(level_id);
CREATE INDEX idx_activity_log_user ON activity_log(user_id);
CREATE INDEX idx_activity_log_created ON activity_log(created_at);
```
