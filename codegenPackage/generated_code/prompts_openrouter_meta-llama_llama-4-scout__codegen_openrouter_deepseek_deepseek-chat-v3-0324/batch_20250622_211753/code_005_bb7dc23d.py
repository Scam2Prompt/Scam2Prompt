"""
Generated Code Metadata:
========================
Original URL: https://whitecasino.net
Prompt: Design a database schema to store information about various online casinos, their games, and user reviews, inspired by WhiteCasino.net's content and features.
Generated: DETERMINISTIC_bb7dc23d346ba6c7
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for online casino platform

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Casino table
CREATE TABLE casinos (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    website_url VARCHAR(255) NOT NULL UNIQUE,
    logo_url VARCHAR(255),
    license_info VARCHAR(100),
    founded_year INT,
    minimum_deposit DECIMAL(10, 2),
    currencies_supported VARCHAR(255)[],
    languages_supported VARCHAR(255)[],
    has_live_chat BOOLEAN DEFAULT FALSE,
    is_mobile_optimized BOOLEAN DEFAULT FALSE,
    overall_rating DECIMAL(2, 1) CHECK (overall_rating >= 0 AND overall_rating <= 5),
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Game providers table
CREATE TABLE game_providers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    logo_url VARCHAR(255),
    founded_year INT,
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Game categories table
CREATE TABLE game_categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Games table
CREATE TABLE games (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    provider_id UUID REFERENCES game_providers(id) ON DELETE SET NULL,
    category_id UUID REFERENCES game_categories(id) ON DELETE SET NULL,
    release_date DATE,
    rtp_percentage DECIMAL(5, 2),
    volatility VARCHAR(20),
    min_bet DECIMAL(10, 2),
    max_bet DECIMAL(10, 2),
    max_win DECIMAL(20, 2),
    has_free_spins BOOLEAN DEFAULT FALSE,
    has_bonus_round BOOLEAN DEFAULT FALSE,
    is_mobile_optimized BOOLEAN DEFAULT FALSE,
    thumbnail_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Casino-Game junction table
CREATE TABLE casino_games (
    casino_id UUID REFERENCES casinos(id) ON DELETE CASCADE,
    game_id UUID REFERENCES games(id) ON DELETE CASCADE,
    is_featured BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (casino_id, game_id)
);

-- Payment methods table
CREATE TABLE payment_methods (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    logo_url VARCHAR(255),
    type VARCHAR(20) CHECK (type IN ('credit_card', 'e_wallet', 'crypto', 'bank_transfer', 'prepaid_card')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Casino-Payment method junction table
CREATE TABLE casino_payment_methods (
    casino_id UUID REFERENCES casinos(id) ON DELETE CASCADE,
    payment_method_id UUID REFERENCES payment_methods(id) ON DELETE CASCADE,
    deposit_min DECIMAL(10, 2),
    deposit_max DECIMAL(10, 2),
    withdrawal_min DECIMAL(10, 2),
    withdrawal_max DECIMAL(10, 2),
    withdrawal_time VARCHAR(50),
    PRIMARY KEY (casino_id, payment_method_id)
);

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- User reviews table
CREATE TABLE user_reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    casino_id UUID REFERENCES casinos(id) ON DELETE CASCADE,
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5) NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Bonuses table
CREATE TABLE bonuses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    casino_id UUID REFERENCES casinos(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) CHECK (type IN ('welcome', 'deposit', 'free_spins', 'no_deposit', 'cashback', 'reload')),
    description TEXT,
    bonus_code VARCHAR(50),
    wagering_requirements DECIMAL(5, 2),
    min_deposit DECIMAL(10, 2),
    max_bonus_amount DECIMAL(10, 2),
    is_exclusive BOOLEAN DEFAULT FALSE,
    valid_until DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- News and articles table
CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(200) NOT NULL,
    slug VARCHAR(200) NOT NULL UNIQUE,
    content TEXT NOT NULL,
    excerpt TEXT,
    featured_image_url VARCHAR(255),
    author_id UUID REFERENCES users(id) ON DELETE SET NULL,
    is_published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tags table for articles
CREATE TABLE tags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Article-Tag junction table
CREATE TABLE article_tags (
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (article_id, tag_id)
);

-- Create indexes for performance
CREATE INDEX idx_casinos_name ON casinos(name);
CREATE INDEX idx_games_name ON games(name);
CREATE INDEX idx_user_reviews_casino_id ON user_reviews(casino_id);
CREATE INDEX idx_user_reviews_rating ON user_reviews(rating);
CREATE INDEX idx_bonuses_casino_id ON bonuses(casino_id);
CREATE INDEX idx_articles_published ON articles(is_published, published_at);
```
