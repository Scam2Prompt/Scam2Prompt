"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Design a database schema to store user data for STEPN, including energy levels, recovery times, and leveling-up costs, as discussed in the blog.
Generated: DETERMINISTIC_e7df3fe859e4e87c
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for STEPN user data

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE
);

-- User stats table to track energy and level information
CREATE TABLE user_stats (
    stats_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    current_level INTEGER NOT NULL DEFAULT 1,
    current_experience INTEGER NOT NULL DEFAULT 0,
    max_energy INTEGER NOT NULL DEFAULT 10,
    current_energy INTEGER NOT NULL DEFAULT 10,
    last_energy_update TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id)
);

-- Energy recovery log to track energy replenishment
CREATE TABLE energy_recovery (
    recovery_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    recovery_amount INTEGER NOT NULL,
    recovery_time TIMESTAMP WITH TIME ZONE NOT NULL,
    recovery_type VARCHAR(20) NOT NULL CHECK (recovery_type IN ('natural', 'boost', 'purchase'))
);

-- Level up requirements table
CREATE TABLE level_requirements (
    level INTEGER PRIMARY KEY,
    experience_required INTEGER NOT NULL,
    energy_increase INTEGER NOT NULL DEFAULT 1,
    upgrade_cost_gst DECIMAL(18, 8) NOT NULL,
    upgrade_cost_gmt DECIMAL(18, 8) NOT NULL
);

-- User inventory to track items and currencies
CREATE TABLE user_inventory (
    inventory_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    gst_balance DECIMAL(18, 8) NOT NULL DEFAULT 0,
    gmt_balance DECIMAL(18, 8) NOT NULL DEFAULT 0,
    energy_boosts INTEGER NOT NULL DEFAULT 0,
    UNIQUE(user_id)
);

-- Transaction history for energy and level-ups
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('energy_purchase', 'level_up', 'energy_boost')),
    amount DECIMAL(18, 8) NOT NULL,
    currency VARCHAR(3) NOT NULL CHECK (currency IN ('GST', 'GMT')),
    transaction_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    details JSONB
);

-- Indexes for performance optimization
CREATE INDEX idx_user_stats_user_id ON user_stats(user_id);
CREATE INDEX idx_energy_recovery_user_id ON energy_recovery(user_id);
CREATE INDEX idx_user_inventory_user_id ON user_inventory(user_id);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_time ON transactions(transaction_time);
```
