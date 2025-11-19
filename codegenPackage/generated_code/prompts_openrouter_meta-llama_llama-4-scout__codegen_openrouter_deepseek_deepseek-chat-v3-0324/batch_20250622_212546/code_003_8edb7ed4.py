"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Design a database schema to store user information, membership levels, and earning percentages for a platform like bonaeac.com.
Generated: DETERMINISTIC_8edb7ed45a307af9
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user management and membership levels

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    date_of_birth DATE,
    profile_picture_url VARCHAR(255),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR(100),
    verification_expiry TIMESTAMP WITH TIME ZONE
);

-- Membership levels table
CREATE TABLE membership_levels (
    level_id SERIAL PRIMARY KEY,
    level_name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    monthly_price DECIMAL(10, 2) NOT NULL,
    annual_price DECIMAL(10, 2),
    benefits TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User membership information
CREATE TABLE user_memberships (
    membership_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    level_id INTEGER NOT NULL REFERENCES membership_levels(level_id),
    start_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    payment_method VARCHAR(50),
    auto_renew BOOLEAN DEFAULT FALSE,
    last_payment_date TIMESTAMP WITH TIME ZONE,
    next_payment_date TIMESTAMP WITH TIME ZONE,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date > start_date)
);

-- Earning percentages for different membership levels
CREATE TABLE earning_percentages (
    percentage_id SERIAL PRIMARY KEY,
    level_id INTEGER NOT NULL REFERENCES membership_levels(level_id),
    percentage DECIMAL(5, 2) NOT NULL,
    min_threshold DECIMAL(10, 2),
    max_threshold DECIMAL(10, 2),
    effective_from TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    effective_to TIMESTAMP WITH TIME ZONE,
    created_by INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_percentage CHECK (percentage > 0 AND percentage <= 100),
    CONSTRAINT valid_threshold CHECK (
        (min_threshold IS NULL AND max_threshold IS NULL) OR
        (min_threshold IS NOT NULL AND max_threshold IS NULL) OR
        (min_threshold IS NOT NULL AND max_threshold IS NOT NULL AND max_threshold > min_threshold)
    ),
    CONSTRAINT valid_dates CHECK (effective_to IS NULL OR effective_to > effective_from)
);

-- User earnings tracking
CREATE TABLE user_earnings (
    earning_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    percentage_id INTEGER NOT NULL REFERENCES earning_percentages(percentage_id),
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    reference_id VARCHAR(100),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'processed', 'failed', 'cancelled')),
    notes TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_user_memberships_user_id ON user_memberships(user_id);
CREATE INDEX idx_user_memberships_level_id ON user_memberships(level_id);
CREATE INDEX idx_user_earnings_user_id ON user_earnings(user_id);
CREATE INDEX idx_user_earnings_percentage_id ON user_earnings(percentage_id);
CREATE INDEX idx_user_earnings_status ON user_earnings(status);
```
