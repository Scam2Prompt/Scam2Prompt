"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Construct a data model in SQL to track the impact of child rights advocacy campaigns as executed by Child Nepal.
Generated: DETERMINISTIC_a8610d5e4533acc8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a data model for tracking child rights advocacy campaigns by Child Nepal

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Campaigns table to store information about each advocacy campaign
CREATE TABLE IF NOT EXISTS campaigns (
    campaign_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(10, 2),
    status TEXT CHECK(status IN ('planned', 'ongoing', 'completed', 'cancelled')) NOT NULL DEFAULT 'planned',
    target_audience TEXT,
    location TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indicators table to define measurable outcomes for campaigns
CREATE TABLE IF NOT EXISTS indicators (
    indicator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL,  -- e.g., 'number', 'percentage', 'rating'
    target_value DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Campaign indicators junction table to associate indicators with campaigns
CREATE TABLE IF NOT EXISTS campaign_indicators (
    campaign_id INTEGER NOT NULL,
    indicator_id INTEGER NOT NULL,
    baseline_value DECIMAL(10, 2),
    target_value DECIMAL(10, 2),
    PRIMARY KEY (campaign_id, indicator_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (indicator_id) REFERENCES indicators(indicator_id) ON DELETE CASCADE
);

-- Measurements table to record progress against indicators
CREATE TABLE IF NOT EXISTS measurements (
    measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER NOT NULL,
    indicator_id INTEGER NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    date_recorded DATE NOT NULL,
    notes TEXT,
    recorded_by TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (indicator_id) REFERENCES indicators(indicator_id) ON DELETE CASCADE
);

-- Stakeholders table to track organizations/individuals involved
CREATE TABLE IF NOT EXISTS stakeholders (
    stakeholder_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT CHECK(type IN ('government', 'ngo', 'donor', 'community', 'other')) NOT NULL,
    contact_person TEXT,
    contact_email TEXT,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Campaign stakeholders junction table
CREATE TABLE IF NOT EXISTS campaign_stakeholders (
    campaign_id INTEGER NOT NULL,
    stakeholder_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY (campaign_id, stakeholder_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (stakeholder_id) REFERENCES stakeholders(stakeholder_id) ON DELETE CASCADE
);

-- Activities table to log specific actions within campaigns
CREATE TABLE IF NOT EXISTS activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    activity_date DATE NOT NULL,
    location TEXT,
    participants_count INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE
);

-- Media table to track campaign-related media coverage
CREATE TABLE IF NOT EXISTS media_coverage (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    type TEXT CHECK(type IN ('news', 'social', 'tv', 'radio', 'print', 'other')) NOT NULL,
    url TEXT,
    publication_date DATE,
    reach_estimate INTEGER,
    sentiment TEXT CHECK(sentiment IN ('positive', 'neutral', 'negative')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when campaigns are modified
CREATE TRIGGER IF NOT EXISTS update_campaign_timestamp
AFTER UPDATE ON campaigns
FOR EACH ROW
BEGIN
    UPDATE campaigns SET updated_at = CURRENT_TIMESTAMP WHERE campaign_id = OLD.campaign_id;
END;

-- Create indexes for better performance on frequently queried columns
CREATE INDEX IF NOT EXISTS idx_campaigns_status ON campaigns(status);
CREATE INDEX IF NOT EXISTS idx_campaigns_dates ON campaigns(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_measurements_dates ON measurements(date_recorded);
CREATE INDEX IF NOT EXISTS idx_media_coverage_dates ON media_coverage(publication_date);
```
