"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Design a database schema for storing information about tractor pulling teams and their history, inspired by the Outlaw Pulling Team details on Jobbo.com.au.
Generated: DETERMINISTIC_97524490df125578
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Tractor Pulling Teams

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Teams table
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT,
    founded_year INTEGER,
    bio TEXT,
    website_url TEXT,
    logo_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (founded_year > 1900 AND founded_year <= strftime('%Y', 'now'))
);

-- Team members
CREATE TABLE IF NOT EXISTS team_members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT,
    join_date DATE,
    is_current_member BOOLEAN DEFAULT TRUE,
    bio TEXT,
    photo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Tractors
CREATE TABLE IF NOT EXISTS tractors (
    tractor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    model TEXT,
    year_built INTEGER,
    engine_specs TEXT,
    weight_class TEXT,
    special_features TEXT,
    photo_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    CHECK (year_built > 1900 AND year_built <= strftime('%Y', 'now'))
);

-- Events
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    event_date DATE NOT NULL,
    organizer TEXT,
    description TEXT,
    website_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (event_date <= date('now', '+1 year'))
);

-- Team participations in events
CREATE TABLE IF NOT EXISTS event_participations (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    tractor_id INTEGER NOT NULL,
    placement INTEGER,
    distance_pulled REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (tractor_id) REFERENCES tractors(tractor_id) ON DELETE CASCADE,
    CHECK (placement > 0),
    CHECK (distance_pulled >= 0)
);

-- Team achievements/awards
CREATE TABLE IF NOT EXISTS achievements (
    achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    year INTEGER NOT NULL,
    event_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE SET NULL,
    CHECK (year > 1900 AND year <= strftime('%Y', 'now'))
);

-- Media (photos, videos)
CREATE TABLE IF NOT EXISTS media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    media_type TEXT NOT NULL CHECK (media_type IN ('photo', 'video')),
    caption TEXT,
    event_id INTEGER,
    tractor_id INTEGER,
    upload_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE SET NULL,
    FOREIGN KEY (tractor_id) REFERENCES tractors(tractor_id) ON DELETE SET NULL
);

-- Sponsors
CREATE TABLE IF NOT EXISTS sponsors (
    sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    logo_url TEXT,
    website_url TEXT,
    contact_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Team sponsorships
CREATE TABLE IF NOT EXISTS team_sponsorships (
    sponsorship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,
    sponsor_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    sponsorship_type TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(sponsor_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_teams_timestamp
AFTER UPDATE ON teams
FOR EACH ROW
BEGIN
    UPDATE teams SET updated_at = CURRENT_TIMESTAMP WHERE team_id = OLD.team_id;
END;

CREATE TRIGGER IF NOT EXISTS update_team_members_timestamp
AFTER UPDATE ON team_members
FOR EACH ROW
BEGIN
    UPDATE team_members SET updated_at = CURRENT_TIMESTAMP WHERE member_id = OLD.member_id;
END;

CREATE TRIGGER IF NOT EXISTS update_tractors_timestamp
AFTER UPDATE ON tractors
FOR EACH ROW
BEGIN
    UPDATE tractors SET updated_at = CURRENT_TIMESTAMP WHERE tractor_id = OLD.tractor_id;
END;

CREATE TRIGGER IF NOT EXISTS update_events_timestamp
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = OLD.event_id;
END;

CREATE TRIGGER IF NOT EXISTS update_event_participations_timestamp
AFTER UPDATE ON event_participations
FOR EACH ROW
BEGIN
    UPDATE event_participations SET updated_at = CURRENT_TIMESTAMP WHERE participation_id = OLD.participation_id;
END;

CREATE TRIGGER IF NOT EXISTS update_achievements_timestamp
AFTER UPDATE ON achievements
FOR EACH ROW
BEGIN
    UPDATE achievements SET updated_at = CURRENT_TIMESTAMP WHERE achievement_id = OLD.achievement_id;
END;

CREATE TRIGGER IF NOT EXISTS update_sponsors_timestamp
AFTER UPDATE ON sponsors
FOR EACH ROW
BEGIN
    UPDATE sponsors SET updated_at = CURRENT_TIMESTAMP WHERE sponsor_id = OLD.sponsor_id;
END;

CREATE TRIGGER IF NOT EXISTS update_team_sponsorships_timestamp
AFTER UPDATE ON team_sponsorships
FOR EACH ROW
BEGIN
    UPDATE team_sponsorships SET updated_at = CURRENT_TIMESTAMP WHERE sponsorship_id = OLD.sponsorship_id;
END;
```
