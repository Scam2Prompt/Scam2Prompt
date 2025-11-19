"""
Generated Code Metadata:
========================
Original URL: https://trumflation.com
Prompt: "Develop a basic SQL database schema to store and query economic data related to trumflation analysis."
Generated: DETERMINISTIC_908697c743dc8623
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Trumflation Analysis Database
-- This schema is designed to store economic data for inflation analysis during the Trump administration

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store economic indicators metadata
CREATE TABLE IF NOT EXISTS economic_indicators (
    indicator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    indicator_name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit TEXT NOT NULL,
    source TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (indicator_name <> ''),
    CHECK (unit <> '')
);

-- Table to store time series data for economic indicators
CREATE TABLE IF NOT EXISTS economic_data (
    data_id INTEGER PRIMARY KEY AUTOINCREMENT,
    indicator_id INTEGER NOT NULL,
    date DATE NOT NULL,
    value REAL NOT NULL,
    notes TEXT,
    FOREIGN KEY (indicator_id) REFERENCES economic_indicators(indicator_id) ON DELETE CASCADE,
    UNIQUE (indicator_id, date),
    CHECK (date BETWEEN '2017-01-20' AND '2021-01-20') -- Trump administration timeframe
);

-- Table to store administration periods for reference
CREATE TABLE IF NOT EXISTS administration_periods (
    period_id INTEGER PRIMARY KEY AUTOINCREMENT,
    president_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    party TEXT NOT NULL,
    UNIQUE (president_name, start_date, end_date),
    CHECK (start_date < end_date)
);

-- Table to store policy events that might affect inflation
CREATE TABLE IF NOT EXISTS policy_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date DATE NOT NULL,
    description TEXT,
    impact_estimate TEXT,
    administration_id INTEGER NOT NULL,
    FOREIGN KEY (administration_id) REFERENCES administration_periods(period_id),
    CHECK (event_name <> ''),
    CHECK (event_date BETWEEN '2017-01-20' AND '2021-01-20')
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_economic_data_date ON economic_data(date);
CREATE INDEX IF NOT EXISTS idx_economic_data_indicator ON economic_data(indicator_id);
CREATE INDEX IF NOT EXISTS idx_policy_events_date ON policy_events(event_date);

-- View for commonly used inflation metrics
CREATE VIEW IF NOT EXISTS inflation_metrics AS
SELECT 
    ed.date,
    ei.indicator_name,
    ed.value,
    ei.unit,
    ei.source
FROM 
    economic_data ed
JOIN 
    economic_indicators ei ON ed.indicator_id = ei.indicator_id
WHERE 
    ei.indicator_name IN ('CPI', 'Core CPI', 'PPI', 'PCE Price Index');

-- View to correlate policy events with economic data
CREATE VIEW IF NOT EXISTS policy_impact_analysis AS
SELECT 
    pe.event_name,
    pe.event_date,
    pe.description,
    pe.impact_estimate,
    ei.indicator_name,
    ed.value,
    ed.date
FROM 
    policy_events pe
JOIN 
    economic_data ed ON ed.date >= pe.event_date AND ed.date <= date(pe.event_date, '+3 months')
JOIN 
    economic_indicators ei ON ed.indicator_id = ei.indicator_id
WHERE 
    ei.indicator_name IN ('CPI', 'Core CPI', 'PPI', 'PCE Price Index');
```
