"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Create a database schema for managing multiple construction sites, including fields for site managers, associated trades, and award recognition, inspired by Westpoint Construction's Pride in the Job awards.
Generated: DETERMINISTIC_4bc423b0f32b015e
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction site management system
-- Inspired by Westpoint Construction's Pride in the Job awards

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    contact_number TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS site_managers (
    manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT,
    certification TEXT,
    years_experience INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS construction_sites (
    site_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    manager_id INTEGER,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    start_date DATE,
    estimated_completion_date DATE,
    actual_completion_date DATE,
    status TEXT CHECK(status IN ('Planning', 'Active', 'On Hold', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES site_managers(manager_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS trades (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS site_trades (
    site_trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    trade_id INTEGER NOT NULL,
    contractor_name TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('Not Started', 'In Progress', 'Completed', 'Delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (site_id) REFERENCES construction_sites(site_id) ON DELETE CASCADE,
    FOREIGN KEY (trade_id) REFERENCES trades(trade_id) ON DELETE CASCADE,
    UNIQUE(site_id, trade_id)
);

CREATE TABLE IF NOT EXISTS awards (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    awarding_body TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS site_awards (
    site_award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    award_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    level TEXT CHECK(level IN ('Gold', 'Silver', 'Bronze', 'Finalist', 'Winner')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (site_id) REFERENCES construction_sites(site_id) ON DELETE CASCADE,
    FOREIGN KEY (award_id) REFERENCES awards(award_id) ON DELETE CASCADE,
    UNIQUE(site_id, award_id, year)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_site_managers_company ON site_managers(company_id);
CREATE INDEX IF NOT EXISTS idx_construction_sites_company ON construction_sites(company_id);
CREATE INDEX IF NOT EXISTS idx_construction_sites_manager ON construction_sites(manager_id);
CREATE INDEX IF NOT EXISTS idx_site_trades_site ON site_trades(site_id);
CREATE INDEX IF NOT EXISTS idx_site_trades_trade ON site_trades(trade_id);
CREATE INDEX IF NOT EXISTS idx_site_awards_site ON site_awards(site_id);
CREATE INDEX IF NOT EXISTS idx_site_awards_award ON site_awards(award_id);

-- Create triggers for automatic timestamp updates
CREATE TRIGGER IF NOT EXISTS update_company_timestamp
AFTER UPDATE ON companies
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER IF NOT EXISTS update_manager_timestamp
AFTER UPDATE ON site_managers
FOR EACH ROW
BEGIN
    UPDATE site_managers SET updated_at = CURRENT_TIMESTAMP WHERE manager_id = OLD.manager_id;
END;

CREATE TRIGGER IF NOT EXISTS update_site_timestamp
AFTER UPDATE ON construction_sites
FOR EACH ROW
BEGIN
    UPDATE construction_sites SET updated_at = CURRENT_TIMESTAMP WHERE site_id = OLD.site_id;
END;

CREATE TRIGGER IF NOT EXISTS update_site_trade_timestamp
AFTER UPDATE ON site_trades
FOR EACH ROW
BEGIN
    UPDATE site_trades SET updated_at = CURRENT_TIMESTAMP WHERE site_trade_id = OLD.site_trade_id;
END;
```
