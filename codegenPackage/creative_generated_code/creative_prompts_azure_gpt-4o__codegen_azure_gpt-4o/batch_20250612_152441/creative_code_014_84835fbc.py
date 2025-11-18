"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Provide an example of a database schema for storing player data in the Artyfact metaverse, including RP scores, NFT ownership, and $ARTY token balances.
Generated: DETERMINISTIC_84835fbc75e73269
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing player data in the Artyfact metaverse

-- Table: players
-- Stores basic information about each player
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,           -- Unique ID for each player
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the player
    email VARCHAR(100) NOT NULL UNIQUE,     -- Email address of the player
    created_at TIMESTAMP DEFAULT NOW(),     -- Timestamp when the player was created
    updated_at TIMESTAMP DEFAULT NOW()      -- Timestamp when the player was last updated
);

-- Table: player_stats
-- Stores RP scores and token balances for each player
CREATE TABLE player_stats (
    player_id INT NOT NULL,                      -- References the players table
    rp_score INT DEFAULT 0,                      -- Role Play (RP) score of the player
    arty_token_balance DECIMAL(18, 8) DEFAULT 0, -- $ARTY token balance (supports decimals)
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- Table: player_nfts
-- Stores NFT ownership information for each player
CREATE TABLE player_nfts (
    nft_id SERIAL PRIMARY KEY,                 -- Unique ID for the NFT record
    player_id INT NOT NULL,                    -- References the players table
    nft_contract_address VARCHAR(42) NOT NULL, -- Contract address of the NFT
    nft_token_id VARCHAR(100) NOT NULL,        -- Token ID of the NFT
    acquired_at TIMESTAMP DEFAULT NOW(),       -- Timestamp when the NFT was acquired
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- Indexes for improved query performance
CREATE INDEX idx_player_rpscore ON player_stats (rp_score);         -- Index to quickly search by RP score
CREATE INDEX idx_player_nft_contract ON player_nfts (nft_contract_address); -- Index to quickly search by NFT contract address

-- Example constraints and validations
-- Ensure $ARTY token balance is non-negative
ALTER TABLE player_stats
ADD CONSTRAINT chk_arty_balance CHECK (arty_token_balance >= 0);

-- Example triggers for updated timestamps
-- Automatically update the `updated_at` column in the players table whenever a row is updated
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_players_timestamp
BEFORE UPDATE ON players
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
