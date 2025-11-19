"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Design a database schema for an esports management firm like Ace Pro Sports Technologies, including tables for teams, players, tournaments, and apparel orders.
Generated: DETERMINISTIC_ad36e2caa453dcca
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for esports management firm

-- Teams table
CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    organization VARCHAR(100) NOT NULL,
    founded_date DATE,
    coach VARCHAR(100),
    country VARCHAR(50),
    logo_url VARCHAR(255),
    social_media_links JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_team_name UNIQUE (team_name)
);

-- Players table
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams(team_id) ON DELETE SET NULL,
    gamer_tag VARCHAR(50) NOT NULL,
    real_name VARCHAR(100),
    date_of_birth DATE,
    country VARCHAR(50),
    main_role VARCHAR(50),
    join_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    social_media_links JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_gamer_tag UNIQUE (gamer_tag)
);

-- Games table
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    game_name VARCHAR(100) NOT NULL,
    developer VARCHAR(100),
    release_year INTEGER,
    genre VARCHAR(50),
    current_version VARCHAR(50),
    CONSTRAINT unique_game_name UNIQUE (game_name)
);

-- Tournaments table
CREATE TABLE tournaments (
    tournament_id SERIAL PRIMARY KEY,
    tournament_name VARCHAR(100) NOT NULL,
    game_id INTEGER REFERENCES games(game_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    prize_pool DECIMAL(12, 2),
    location VARCHAR(100),
    organizer VARCHAR(100),
    status VARCHAR(20) CHECK (status IN ('upcoming', 'ongoing', 'completed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date >= start_date)
);

-- Tournament participants (many-to-many relationship)
CREATE TABLE tournament_participants (
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    team_id INTEGER REFERENCES teams(team_id) ON DELETE CASCADE,
    placement INTEGER,
    prize_money DECIMAL(12, 2),
    PRIMARY KEY (tournament_id, team_id)
);

-- Matches table
CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    game_id INTEGER REFERENCES games(game_id) ON DELETE CASCADE,
    match_date TIMESTAMP WITH TIME ZONE NOT NULL,
    team1_id INTEGER REFERENCES teams(team_id) ON DELETE SET NULL,
    team2_id INTEGER REFERENCES teams(team_id) ON DELETE SET NULL,
    winner_id INTEGER REFERENCES teams(team_id) ON DELETE SET NULL,
    score_team1 INTEGER,
    score_team2 INTEGER,
    round_name VARCHAR(50),
    is_bo5 BOOLEAN DEFAULT FALSE,
    vod_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_teams CHECK (team1_id != team2_id)
);

-- Sponsors table
CREATE TABLE sponsors (
    sponsor_id SERIAL PRIMARY KEY,
    sponsor_name VARCHAR(100) NOT NULL,
    industry VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    logo_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Team sponsorships (many-to-many relationship)
CREATE TABLE team_sponsorships (
    team_id INTEGER REFERENCES teams(team_id) ON DELETE CASCADE,
    sponsor_id INTEGER REFERENCES sponsors(sponsor_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE,
    contract_value DECIMAL(12, 2),
    is_active BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (team_id, sponsor_id),
    CONSTRAINT valid_sponsorship_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Apparel products table
CREATE TABLE apparel_products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_type VARCHAR(50),
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    team_id INTEGER REFERENCES teams(team_id) ON DELETE CASCADE,
    image_url VARCHAR(255),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    shipping_address JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_email UNIQUE (email)
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE SET NULL,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(12, 2) NOT NULL,
    shipping_cost DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'processing' CHECK (status IN ('processing', 'shipped', 'delivered', 'cancelled')),
    tracking_number VARCHAR(100),
    shipping_address JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Order items table
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES apparel_products(product_id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    size VARCHAR(10),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_players_team_id ON players(team_id);
CREATE INDEX idx_tournaments_game_id ON tournaments(game_id);
CREATE INDEX idx_matches_tournament_id ON matches(tournament_id);
CREATE INDEX idx_matches_team1_id ON matches(team1_id);
CREATE INDEX idx_matches_team2_id ON matches(team2_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```
