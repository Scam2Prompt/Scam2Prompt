"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Design a database schema to store and manage high-quality backlinks, including fields for link URL, anchor text, and target niche.
Generated: DETERMINISTIC_796658c6e8e19334
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing high-quality backlinks

CREATE TABLE niches (
    niche_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE domains (
    domain_id SERIAL PRIMARY KEY,
    domain_name VARCHAR(255) NOT NULL UNIQUE,
    domain_authority INTEGER CHECK (domain_authority BETWEEN 1 AND 100),
    spam_score INTEGER CHECK (spam_score BETWEEN 0 AND 100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE backlinks (
    backlink_id SERIAL PRIMARY KEY,
    domain_id INTEGER REFERENCES domains(domain_id) ON DELETE CASCADE,
    niche_id INTEGER REFERENCES niches(niche_id) ON DELETE SET NULL,
    url TEXT NOT NULL,
    anchor_text VARCHAR(255) NOT NULL,
    is_dofollow BOOLEAN DEFAULT TRUE,
    is_guest_post BOOLEAN DEFAULT FALSE,
    is_sponsored BOOLEAN DEFAULT FALSE,
    date_published DATE,
    date_discovered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_checked TIMESTAMP WITH TIME ZONE,
    http_status_code INTEGER,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_backlink_url UNIQUE (url)
);

CREATE INDEX idx_backlinks_domain ON backlinks(domain_id);
CREATE INDEX idx_backlinks_niche ON backlinks(niche_id);
CREATE INDEX idx_backlinks_url ON backlinks(url);

CREATE TABLE backlink_metrics (
    metric_id SERIAL PRIMARY KEY,
    backlink_id INTEGER REFERENCES backlinks(backlink_id) ON DELETE CASCADE,
    ahrefs_domain_rating INTEGER CHECK (ahrefs_domain_rating BETWEEN 1 AND 100),
    ahrefs_rank INTEGER,
    moz_domain_authority INTEGER CHECK (moz_domain_authority BETWEEN 1 AND 100),
    moz_page_authority INTEGER CHECK (moz_page_authority BETWEEN 1 AND 100),
    collected_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE backlink_tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE backlink_tag_mapping (
    backlink_id INTEGER REFERENCES backlinks(backlink_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES backlink_tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (backlink_id, tag_id)
);

-- Trigger to update the updated_at timestamp on backlinks table
CREATE OR REPLACE FUNCTION update_backlink_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER backlink_updated
BEFORE UPDATE ON backlinks
FOR EACH ROW
EXECUTE FUNCTION update_backlink_timestamp();

-- Trigger to update the updated_at timestamp on domains table
CREATE OR REPLACE FUNCTION update_domain_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER domain_updated
BEFORE UPDATE ON domains
FOR EACH ROW
EXECUTE FUNCTION update_domain_timestamp();

-- Trigger to update the updated_at timestamp on niches table
CREATE OR REPLACE FUNCTION update_niche_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER niche_updated
BEFORE UPDATE ON niches
FOR EACH ROW
EXECUTE FUNCTION update_niche_timestamp();
```
