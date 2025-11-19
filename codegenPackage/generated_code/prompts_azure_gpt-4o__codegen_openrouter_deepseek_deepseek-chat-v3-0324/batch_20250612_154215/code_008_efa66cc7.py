"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Generate a database schema to store information about esports tournaments, participants, sponsors, and apparel designs, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_efa66cc7498ce3bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ace Pro Sports Technologies esports tournaments

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tournaments table
CREATE TABLE tournaments (
    tournament_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(100),
    prize_pool DECIMAL(15, 2),
    game_title VARCHAR(50) NOT NULL,
    max_participants INTEGER,
    registration_deadline TIMESTAMP WITH TIME ZONE,
    rules TEXT,
    status VARCHAR(20) NOT NULL CHECK (status IN ('upcoming', 'ongoing', 'completed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Participants table
CREATE TABLE participants (
    participant_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tournament_id UUID NOT NULL REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    team_name VARCHAR(100) NOT NULL,
    team_logo_url VARCHAR(255),
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20),
    country VARCHAR(50),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('registered', 'approved', 'rejected', 'withdrawn')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Team members table
CREATE TABLE team_members (
    member_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    participant_id UUID NOT NULL REFERENCES participants(participant_id) ON DELETE CASCADE,
    full_name VARCHAR(100) NOT NULL,
    game_username VARCHAR(50) NOT NULL,
    role VARCHAR(50),
    is_captain BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sponsors table
CREATE TABLE sponsors (
    sponsor_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    logo_url VARCHAR(255),
    website_url VARCHAR(255),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tournament sponsors junction table
CREATE TABLE tournament_sponsors (
    tournament_id UUID NOT NULL REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    sponsor_id UUID NOT NULL REFERENCES sponsors(sponsor_id) ON DELETE CASCADE,
    sponsorship_level VARCHAR(50) NOT NULL,
    contribution DECIMAL(15, 2),
    PRIMARY KEY (tournament_id, sponsor_id)
);

-- Apparel designs table
CREATE TABLE apparel_designs (
    design_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url VARCHAR(255) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tournament apparel junction table
CREATE TABLE tournament_apparel (
    tournament_id UUID NOT NULL REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    design_id UUID NOT NULL REFERENCES apparel_designs(design_id) ON DELETE CASCADE,
    custom_price DECIMAL(10, 2),
    is_featured BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (tournament_id, design_id)
);

-- Matches table
CREATE TABLE matches (
    match_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tournament_id UUID NOT NULL REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    round_number INTEGER NOT NULL,
    match_number INTEGER NOT NULL,
    scheduled_time TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    winner_id UUID REFERENCES participants(participant_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Match participants junction table
CREATE TABLE match_participants (
    match_id UUID NOT NULL REFERENCES matches(match_id) ON DELETE CASCADE,
    participant_id UUID NOT NULL REFERENCES participants(participant_id) ON DELETE CASCADE,
    score INTEGER,
    is_home BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (match_id, participant_id)
);

-- Results table
CREATE TABLE results (
    result_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tournament_id UUID NOT NULL REFERENCES tournaments(tournament_id) ON DELETE CASCADE,
    participant_id UUID NOT NULL REFERENCES participants(participant_id) ON DELETE CASCADE,
    final_position INTEGER NOT NULL,
    prize_money DECIMAL(15, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_tournaments_timestamp
BEFORE UPDATE ON tournaments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_participants_timestamp
BEFORE UPDATE ON participants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_team_members_timestamp
BEFORE UPDATE ON team_members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_sponsors_timestamp
BEFORE UPDATE ON sponsors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_apparel_designs_timestamp
BEFORE UPDATE ON apparel_designs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_matches_timestamp
BEFORE UPDATE ON matches
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
