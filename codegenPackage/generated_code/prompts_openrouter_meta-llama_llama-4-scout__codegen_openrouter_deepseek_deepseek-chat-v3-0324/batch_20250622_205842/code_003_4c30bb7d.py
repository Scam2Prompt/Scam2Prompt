"""
Generated Code Metadata:
========================
Original URL: https://delta-tlkslkla.pages.dev
Prompt: "Design a database schema for a trading platform that includes tables for users, trades, campaigns, and delta points."
Generated: DETERMINISTIC_4c30bb7da28c086b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a trading platform

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    account_balance DECIMAL(18, 2) DEFAULT 0.00,
    account_status VARCHAR(20) DEFAULT 'active' CHECK (account_status IN ('active', 'suspended', 'closed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Campaigns table to store marketing campaigns
CREATE TABLE campaigns (
    campaign_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'paused', 'completed', 'cancelled')),
    budget DECIMAL(18, 2),
    created_by INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date > start_date)
);

-- Delta points table to track user points/credits
CREATE TABLE delta_points (
    point_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    campaign_id INTEGER REFERENCES campaigns(campaign_id) ON DELETE SET NULL,
    points DECIMAL(18, 2) NOT NULL,
    points_type VARCHAR(20) CHECK (points_type IN ('credit', 'debit')),
    description TEXT,
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'expired', 'cancelled'))
);

-- Trades table to record trading transactions
CREATE TABLE trades (
    trade_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    asset_symbol VARCHAR(10) NOT NULL,
    trade_type VARCHAR(4) NOT NULL CHECK (trade_type IN ('BUY', 'SELL')),
    quantity DECIMAL(18, 8) NOT NULL,
    price_per_unit DECIMAL(18, 2) NOT NULL,
    total_amount DECIMAL(18, 2) NOT NULL,
    commission DECIMAL(18, 2) DEFAULT 0.00,
    net_amount DECIMAL(18, 2) NOT NULL,
    trade_status VARCHAR(20) DEFAULT 'executed' CHECK (trade_status IN ('pending', 'executed', 'cancelled', 'failed')),
    execution_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    campaign_id INTEGER REFERENCES campaigns(campaign_id) ON DELETE SET NULL,
    notes TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_delta_points_user_id ON delta_points(user_id);
CREATE INDEX idx_delta_points_campaign_id ON delta_points(campaign_id);
CREATE INDEX idx_trades_user_id ON trades(user_id);
CREATE INDEX idx_trades_asset_symbol ON trades(asset_symbol);
CREATE INDEX idx_trades_execution_time ON trades(execution_time);
CREATE INDEX idx_campaigns_status ON campaigns(status);
```
