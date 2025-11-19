"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Create a database schema for managing various poker game types (e.g., Texas Hold'em, Omaha, Seven Card Stud) as listed on DominoBet.
Generated: DETERMINISTIC_90333ca7d17bac53
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing poker game types
-- Supports Texas Hold'em, Omaha, Seven Card Stud, and other variants

-- Table for storing poker game types
CREATE TABLE poker_game_types (
    game_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    max_players SMALLINT NOT NULL CHECK (max_players > 1),
    min_players SMALLINT NOT NULL CHECK (min_players >= 2),
    community_cards BOOLEAN NOT NULL,
    hole_cards_count SMALLINT NOT NULL CHECK (hole_cards_count >= 0),
    betting_structure VARCHAR(20) NOT NULL CHECK (betting_structure IN ('limit', 'pot-limit', 'no-limit')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table for storing game type specific rules
CREATE TABLE game_type_rules (
    rule_id SERIAL PRIMARY KEY,
    game_type_id INTEGER NOT NULL REFERENCES poker_game_types(game_type_id),
    rule_name VARCHAR(100) NOT NULL,
    rule_description TEXT NOT NULL,
    rule_order SMALLINT NOT NULL,
    UNIQUE (game_type_id, rule_name)
);

-- Table for storing blind structures
CREATE TABLE blind_structures (
    blind_structure_id SERIAL PRIMARY KEY,
    game_type_id INTEGER NOT NULL REFERENCES poker_game_types(game_type_id),
    level_name VARCHAR(50) NOT NULL,
    small_blind DECIMAL(10,2) NOT NULL CHECK (small_blind > 0),
    big_blind DECIMAL(10,2) NOT NULL CHECK (big_blind > small_blind),
    ante DECIMAL(10,2) DEFAULT 0 CHECK (ante >= 0),
    duration_minutes INTEGER CHECK (duration_minutes > 0),
    is_default BOOLEAN DEFAULT FALSE,
    UNIQUE (game_type_id, level_name)
);

-- Table for storing available poker tables
CREATE TABLE poker_tables (
    table_id SERIAL PRIMARY KEY,
    game_type_id INTEGER NOT NULL REFERENCES poker_game_types(game_type_id),
    table_name VARCHAR(100) NOT NULL UNIQUE,
    max_players SMALLINT NOT NULL,
    current_players SMALLINT DEFAULT 0 CHECK (current_players >= 0 AND current_players <= max_players),
    blind_structure_id INTEGER REFERENCES blind_structures(blind_structure_id),
    min_buy_in DECIMAL(10,2) NOT NULL CHECK (min_buy_in > 0),
    max_buy_in DECIMAL(10,2) NOT NULL CHECK (max_buy_in >= min_buy_in),
    status VARCHAR(20) NOT NULL CHECK (status IN ('waiting', 'active', 'paused', 'closed')) DEFAULT 'waiting',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing hand histories
CREATE TABLE hand_histories (
    hand_id BIGSERIAL PRIMARY KEY,
    table_id INTEGER NOT NULL REFERENCES poker_tables(table_id),
    game_type_id INTEGER NOT NULL REFERENCES poker_game_types(game_type_id),
    hand_number BIGINT NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    button_position SMALLINT NOT NULL CHECK (button_position >= 0),
    small_blind DECIMAL(10,2) NOT NULL,
    big_blind DECIMAL(10,2) NOT NULL,
    ante DECIMAL(10,2) DEFAULT 0,
    winning_hands JSONB,
    rake DECIMAL(10,2) DEFAULT 0 CHECK (rake >= 0),
    UNIQUE (table_id, hand_number)
);

-- Table for storing player actions in each hand
CREATE TABLE hand_actions (
    action_id BIGSERIAL PRIMARY KEY,
    hand_id BIGINT NOT NULL REFERENCES hand_histories(hand_id),
    player_id INTEGER NOT NULL,
    street VARCHAR(20) NOT NULL CHECK (street IN ('preflop', 'flop', 'turn', 'river', 'showdown')),
    action_type VARCHAR(20) NOT NULL CHECK (action_type IN ('fold', 'check', 'call', 'bet', 'raise', 'all-in')),
    amount DECIMAL(10,2) DEFAULT 0 CHECK (amount >= 0),
    action_order SMALLINT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_game_type_name ON poker_game_types(name);
CREATE INDEX idx_blind_structure_game_type ON blind_structures(game_type_id);
CREATE INDEX idx_tables_game_type ON poker_tables(game_type_id);
CREATE INDEX idx_hand_history_table ON hand_histories(table_id);
CREATE INDEX idx_hand_actions_hand ON hand_actions(hand_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_poker_game_types_timestamp
BEFORE UPDATE ON poker_game_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_poker_tables_timestamp
BEFORE UPDATE ON poker_tables
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
