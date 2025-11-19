"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Create a database schema for managing sports streaming subscriptions, giveaways, and user preferences, including features like extra channels and live game updates, as highlighted on Sportify.Club.
Generated: DETERMINISTIC_be59ef2df1474168
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Sportify.Club sports streaming platform

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Subscription plans table
CREATE TABLE subscription_plans (
    plan_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL,
    description TEXT,
    monthly_price DECIMAL(10, 2) NOT NULL,
    annual_price DECIMAL(10, 2),
    max_simultaneous_streams INTEGER DEFAULT 1,
    video_quality VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE
);

-- User subscriptions table
CREATE TABLE user_subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    plan_id INTEGER REFERENCES subscription_plans(plan_id),
    start_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP WITH TIME ZONE,
    auto_renew BOOLEAN DEFAULT TRUE,
    payment_method VARCHAR(50),
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'cancelled', 'paused', 'expired')),
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date > start_date)
);

-- Sports categories table
CREATE TABLE sports_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Channels table
CREATE TABLE channels (
    channel_id SERIAL PRIMARY KEY,
    channel_name VARCHAR(100) NOT NULL,
    description TEXT,
    logo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE
);

-- Channel availability by subscription plan
CREATE TABLE plan_channels (
    plan_id INTEGER REFERENCES subscription_plans(plan_id) ON DELETE CASCADE,
    channel_id INTEGER REFERENCES channels(channel_id) ON DELETE CASCADE,
    PRIMARY KEY (plan_id, channel_id)
);

-- Extra channels that can be added to subscriptions
CREATE TABLE extra_channels (
    extra_channel_id SERIAL PRIMARY KEY,
    channel_id INTEGER REFERENCES channels(channel_id),
    additional_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- User extra channels
CREATE TABLE user_extra_channels (
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    extra_channel_id INTEGER REFERENCES extra_channels(extra_channel_id) ON DELETE CASCADE,
    added_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, extra_channel_id)
);

-- Live events/games table
CREATE TABLE live_events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    category_id INTEGER REFERENCES sports_categories(category_id),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE,
    description TEXT,
    channel_id INTEGER REFERENCES channels(channel_id),
    is_live BOOLEAN DEFAULT FALSE,
    CONSTRAINT valid_event_times CHECK (end_time IS NULL OR end_time > start_time)
);

-- User preferences for notifications
CREATE TABLE user_preferences (
    user_id INTEGER PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
    receive_email_notifications BOOLEAN DEFAULT TRUE,
    receive_push_notifications BOOLEAN DEFAULT TRUE,
    preferred_sports INTEGER[] DEFAULT '{}',
    favorite_teams VARCHAR(100)[] DEFAULT '{}',
    language_preference VARCHAR(10) DEFAULT 'en',
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Game update preferences
CREATE TABLE game_update_preferences (
    preference_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES live_events(event_id) ON DELETE CASCADE,
    receive_score_updates BOOLEAN DEFAULT TRUE,
    receive_start_end_alerts BOOLEAN DEFAULT TRUE,
    receive_highlight_alerts BOOLEAN DEFAULT FALSE,
    UNIQUE (user_id, event_id)
);

-- Giveaways table
CREATE TABLE giveaways (
    giveaway_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    max_participants INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    prize_description TEXT NOT NULL,
    CONSTRAINT valid_giveaway_dates CHECK (end_date > start_date)
);

-- User participation in giveaways
CREATE TABLE user_giveaways (
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    giveaway_id INTEGER REFERENCES giveaways(giveaway_id) ON DELETE CASCADE,
    participation_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_winner BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (user_id, giveaway_id)
);

-- Payment history table
CREATE TABLE payment_history (
    payment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    subscription_id INTEGER REFERENCES user_subscriptions(subscription_id) ON DELETE SET NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    transaction_id VARCHAR(100),
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('pending', 'completed', 'failed', 'refunded'))
);

-- User watch history
CREATE TABLE watch_history (
    history_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES live_events(event_id) ON DELETE SET NULL,
    channel_id INTEGER REFERENCES channels(channel_id) ON DELETE SET NULL,
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    duration INTERVAL GENERATED ALWAYS AS (end_time - start_time) STORED
);

-- Create indexes for performance
CREATE INDEX idx_user_subscriptions_user_id ON user_subscriptions(user_id);
CREATE INDEX idx_user_subscriptions_plan_id ON user_subscriptions(plan_id);
CREATE INDEX idx_live_events_category_id ON live_events(category_id);
CREATE INDEX idx_live_events_channel_id ON live_events(channel_id);
CREATE INDEX idx_watch_history_user_id ON watch_history(user_id);
CREATE INDEX idx_watch_history_event_id ON watch_history(event_id);
```
