"""
Generated Code Metadata:
========================
Original URL: https://adstar.network
Prompt: "Design a simple database schema for storing ad metadata, inspired by AdStar's data needs."
Generated: DETERMINISTIC_3295203316cb8720
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ad metadata storage

-- Users table to store information about advertisers
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    company_name VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Campaigns table to group related ads
CREATE TABLE campaigns (
    campaign_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    budget DECIMAL(15, 2),
    start_date TIMESTAMP WITH TIME ZONE,
    end_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'draft' CHECK (status IN ('draft', 'active', 'paused', 'completed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Ads table to store individual ad creatives
CREATE TABLE ads (
    ad_id SERIAL PRIMARY KEY,
    campaign_id INTEGER NOT NULL REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    creative_url VARCHAR(255) NOT NULL,
    destination_url VARCHAR(255) NOT NULL,
    bid_amount DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'active', 'paused')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Ad targeting criteria
CREATE TABLE ad_targeting (
    targeting_id SERIAL PRIMARY KEY,
    ad_id INTEGER NOT NULL REFERENCES ads(ad_id) ON DELETE CASCADE,
    age_min INTEGER CHECK (age_min >= 13),
    age_max INTEGER CHECK (age_max <= 100),
    gender VARCHAR(20) CHECK (gender IN ('male', 'female', 'all')),
    location VARCHAR(100),
    interests TEXT[],
    languages VARCHAR(3)[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Ad performance metrics
CREATE TABLE ad_metrics (
    metric_id SERIAL PRIMARY KEY,
    ad_id INTEGER NOT NULL REFERENCES ads(ad_id) ON DELETE CASCADE,
    date DATE NOT NULL,
    impressions INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    conversions INTEGER DEFAULT 0,
    spend DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (ad_id, date)
);

-- Ad approval history
CREATE TABLE ad_approvals (
    approval_id SERIAL PRIMARY KEY,
    ad_id INTEGER NOT NULL REFERENCES ads(ad_id) ON DELETE CASCADE,
    reviewer_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('approved', 'rejected')),
    feedback TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_campaigns_user ON campaigns(user_id);
CREATE INDEX idx_ads_campaign ON ads(campaign_id);
CREATE INDEX idx_ad_targeting ON ad_targeting(ad_id);
CREATE INDEX idx_ad_metrics ON ad_metrics(ad_id, date);
CREATE INDEX idx_ad_approvals ON ad_approvals(ad_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update timestamps
CREATE TRIGGER update_users_modtime
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_campaigns_modtime
BEFORE UPDATE ON campaigns
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_ads_modtime
BEFORE UPDATE ON ads
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```
