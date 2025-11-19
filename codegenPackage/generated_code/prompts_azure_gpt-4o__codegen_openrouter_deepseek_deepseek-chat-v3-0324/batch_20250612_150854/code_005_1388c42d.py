"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Develop a database schema for storing user profiles, preferences, matched firms, and investment education progress for a platform like Juros Xyro.
Generated: DETERMINISTIC_1388c42dc25cb613
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Juros Xyro platform

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store basic profile information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE
);

-- User preferences for investment matching
CREATE TABLE user_preferences (
    preference_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    risk_tolerance VARCHAR(50) CHECK (risk_tolerance IN ('low', 'medium', 'high')),
    investment_horizon VARCHAR(50) CHECK (investment_horizon IN ('short', 'medium', 'long')),
    preferred_investment_types VARCHAR(255)[],
    minimum_investment_amount DECIMAL(15, 2),
    maximum_investment_amount DECIMAL(15, 2),
    preferred_industries VARCHAR(255)[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id)
);

-- Financial firms table
CREATE TABLE financial_firms (
    firm_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    logo_url VARCHAR(255),
    website_url VARCHAR(255),
    risk_profile VARCHAR(50) CHECK (risk_profile IN ('low', 'medium', 'high')),
    minimum_investment DECIMAL(15, 2),
    investment_types VARCHAR(255)[],
    industries_served VARCHAR(255)[],
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User matched firms
CREATE TABLE user_matched_firms (
    match_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    firm_id UUID NOT NULL REFERENCES financial_firms(firm_id) ON DELETE CASCADE,
    match_score DECIMAL(5, 2) NOT NULL,
    match_reasons TEXT[],
    is_favorite BOOLEAN DEFAULT FALSE,
    viewed_at TIMESTAMP WITH TIME ZONE,
    contacted_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, firm_id)
);

-- Investment education modules
CREATE TABLE education_modules (
    module_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    content_url VARCHAR(255),
    duration_minutes INTEGER,
    difficulty_level VARCHAR(50) CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User education progress
CREATE TABLE user_education_progress (
    progress_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    module_id UUID NOT NULL REFERENCES education_modules(module_id) ON DELETE CASCADE,
    completion_status VARCHAR(50) CHECK (completion_status IN ('not_started', 'in_progress', 'completed')),
    progress_percentage INTEGER DEFAULT 0,
    last_accessed_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, module_id)
);

-- Audit log for user activities
CREATE TABLE user_activity_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    activity_type VARCHAR(100) NOT NULL,
    activity_details JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id);
CREATE INDEX idx_user_matched_firms_user_id ON user_matched_firms(user_id);
CREATE INDEX idx_user_matched_firms_firm_id ON user_matched_firms(firm_id);
CREATE INDEX idx_user_education_progress_user_id ON user_education_progress(user_id);
CREATE INDEX idx_user_education_progress_module_id ON user_education_progress(module_id);
CREATE INDEX idx_user_activity_logs_user_id ON user_activity_logs(user_id);
CREATE INDEX idx_user_activity_logs_created_at ON user_activity_logs(created_at);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update updated_at
CREATE TRIGGER update_users_modtime
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_user_preferences_modtime
BEFORE UPDATE ON user_preferences
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_financial_firms_modtime
BEFORE UPDATE ON financial_firms
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_user_matched_firms_modtime
BEFORE UPDATE ON user_matched_firms
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_education_modules_modtime
BEFORE UPDATE ON education_modules
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_user_education_progress_modtime
BEFORE UPDATE ON user_education_progress
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```
