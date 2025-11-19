"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: "Design a database schema for storing NFT metadata and tournament results for a platform like Mojo Melee."
Generated: DETERMINISTIC_efced602b4fd6e16
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for NFT metadata and tournament results

-- Users table to store player information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    wallet_address VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- NFT collections table
CREATE TABLE collections (
    collection_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    contract_address VARCHAR(100) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- NFT metadata table
CREATE TABLE nfts (
    nft_id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections(collection_id) ON DELETE CASCADE,
    token_id VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url VARCHAR(255) NOT NULL,
    animation_url VARCHAR(255),
    external_url VARCHAR(255),
    attributes JSONB,
    rarity_score DECIMAL(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(collection_id, token_id)
);

-- User NFT ownership table
CREATE TABLE user_nfts (
    user_nft_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    nft_id INTEGER REFERENCES nfts(nft_id) ON DELETE CASCADE,
    acquired_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, nft_id)
);

-- Tournament table
CREATE TABLE tournaments (
    tournament_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    entry_fee DECIMAL(10, 2) DEFAULT 0,
    prize_pool DECIMAL(10, 2) DEFAULT 0,
    max_participants INTEGER,
    status VARCHAR(20) NOT NULL DEFAULT 'upcoming',
    CHECK (end_time > start_time),
    CHECK (status IN ('upcoming', 'ongoing', 'completed', 'cancelled'))
);

-- Tournament participants
CREATE TABLE tournament_participants (
    participant_id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    registered_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tournament_id, user_id)
);

-- Tournament matches
CREATE TABLE tournament_matches (
    match_id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    round_number INTEGER NOT NULL,
    player1_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    player2_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    winner_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'scheduled',
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    CHECK (end_time IS NULL OR end_time > start_time)
);

-- Tournament results
CREATE TABLE tournament_results (
    result_id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    prize_amount DECIMAL(10, 2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tournament_id, user_id),
    CHECK (position > 0)
);

-- NFT usage in tournaments
CREATE TABLE tournament_nft_usage (
    usage_id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    match_id INTEGER REFERENCES tournament_matches(match_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    nft_id INTEGER REFERENCES nfts(nft_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_nfts_collection_id ON nfts(collection_id);
CREATE INDEX idx_user_nfts_user_id ON user_nfts(user_id);
CREATE INDEX idx_user_nfts_nft_id ON user_nfts(nft_id);
CREATE INDEX idx_tournament_participants_tournament_id ON tournament_participants(tournament_id);
CREATE INDEX idx_tournament_participants_user_id ON tournament_participants(user_id);
CREATE INDEX idx_tournament_matches_tournament_id ON tournament_matches(tournament_id);
CREATE INDEX idx_tournament_matches_player1_id ON tournament_matches(player1_id);
CREATE INDEX idx_tournament_matches_player2_id ON tournament_matches(player2_id);
CREATE INDEX idx_tournament_matches_winner_id ON tournament_matches(winner_id);
CREATE INDEX idx_tournament_results_tournament_id ON tournament_results(tournament_id);
CREATE INDEX idx_tournament_results_user_id ON tournament_results(user_id);
CREATE INDEX idx_tournament_nft_usage_tournament_id ON tournament_nft_usage(tournament_id);
CREATE INDEX idx_tournament_nft_usage_match_id ON tournament_nft_usage(match_id);
CREATE INDEX idx_tournament_nft_usage_user_id ON tournament_nft_usage(user_id);
CREATE INDEX idx_tournament_nft_usage_nft_id ON tournament_nft_usage(nft_id);
```
