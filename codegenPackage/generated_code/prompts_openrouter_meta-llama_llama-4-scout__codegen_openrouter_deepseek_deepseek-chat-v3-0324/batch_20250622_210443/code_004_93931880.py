"""
Generated Code Metadata:
========================
Original URL: https://wahdigi.com
Prompt: "Design a database schema for storing client information, marketing campaigns, and performance metrics for a digital marketing agency like Wahdigi."
Generated: DETERMINISTIC_93931880be940105
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Wahdigi digital marketing agency

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(255) NOT NULL,
    industry VARCHAR(100),
    website VARCHAR(255),
    contact_person VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(50),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(50),
    date_added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'prospect')),
    notes TEXT,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Campaign types reference table
CREATE TABLE campaign_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Campaigns table
CREATE TABLE campaigns (
    campaign_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    type_id INTEGER REFERENCES campaign_types(type_id),
    campaign_name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(15, 2),
    target_audience TEXT,
    status VARCHAR(20) CHECK (status IN ('planned', 'active', 'paused', 'completed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Campaign platforms table (e.g., Facebook, Google Ads, etc.)
CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    platform_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Campaign platform assignments
CREATE TABLE campaign_platforms (
    campaign_id UUID NOT NULL REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    platform_id INTEGER NOT NULL REFERENCES platforms(platform_id),
    budget_allocation DECIMAL(5, 2) CHECK (budget_allocation BETWEEN 0 AND 100),
    platform_campaign_id VARCHAR(255), -- External campaign ID from the platform
    PRIMARY KEY (campaign_id, platform_id)
);

-- Performance metrics table
CREATE TABLE performance_metrics (
    metric_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    campaign_id UUID NOT NULL REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    platform_id INTEGER NOT NULL REFERENCES platforms(platform_id),
    date DATE NOT NULL,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER,
    spend DECIMAL(15, 2),
    revenue DECIMAL(15, 2),
    ctr DECIMAL(5, 2), -- Click-through rate
    cpc DECIMAL(10, 2), -- Cost per click
    cpa DECIMAL(10, 2), -- Cost per acquisition
    roas DECIMAL(10, 2), -- Return on ad spend
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id, platform_id) REFERENCES campaign_platforms(campaign_id, platform_id),
    CONSTRAINT positive_values CHECK (
        impressions >= 0 AND
        clicks >= 0 AND
        conversions >= 0 AND
        spend >= 0 AND
        revenue >= 0
    )
);

-- Content assets table (ads, creatives, landing pages)
CREATE TABLE content_assets (
    asset_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    campaign_id UUID NOT NULL REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    asset_name VARCHAR(255) NOT NULL,
    asset_type VARCHAR(50) CHECK (asset_type IN ('image', 'video', 'text', 'landing_page', 'other')),
    platform_id INTEGER REFERENCES platforms(platform_id),
    url TEXT,
    thumbnail_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Team members table
CREATE TABLE team_members (
    member_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(50),
    role VARCHAR(100),
    department VARCHAR(100),
    hire_date DATE,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'on_leave')),
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Campaign team assignments
CREATE TABLE campaign_team (
    campaign_id UUID NOT NULL REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    member_id UUID NOT NULL REFERENCES team_members(member_id) ON DELETE CASCADE,
    role VARCHAR(100),
    PRIMARY KEY (campaign_id, member_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_campaigns_client ON campaigns(client_id);
CREATE INDEX idx_campaigns_status ON campaigns(status);
CREATE INDEX idx_performance_campaign_date ON performance_metrics(campaign_id, date);
CREATE INDEX idx_performance_platform_date ON performance_metrics(platform_id, date);
CREATE INDEX idx_content_assets_campaign ON content_assets(campaign_id);

-- Create function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for automatic timestamp updates
CREATE TRIGGER update_campaign_timestamp
BEFORE UPDATE ON campaigns
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_performance_timestamp
BEFORE UPDATE ON performance_metrics
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_content_timestamp
BEFORE UPDATE ON content_assets
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
