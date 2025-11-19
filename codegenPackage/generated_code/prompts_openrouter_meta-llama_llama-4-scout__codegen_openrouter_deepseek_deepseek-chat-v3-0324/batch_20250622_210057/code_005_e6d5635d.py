"""
Generated Code Metadata:
========================
Original URL: https://purelywealth.com
Prompt: "Design a simple database schema for storing information on industries and portfolios in the finance sector."
Generated: DETERMINISTIC_e6d5635d6ebd1785
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for finance sector industries and portfolios

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create industries table
CREATE TABLE industries (
    industry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create portfolios table
CREATE TABLE portfolios (
    portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    risk_level TEXT CHECK(risk_level IN ('Low', 'Medium', 'High')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create junction table for industry-portfolio relationships
CREATE TABLE industry_portfolios (
    industry_id INTEGER NOT NULL,
    portfolio_id INTEGER NOT NULL,
    weight DECIMAL(5,2) CHECK(weight > 0 AND weight <= 100),
    PRIMARY KEY (industry_id, portfolio_id),
    FOREIGN KEY (industry_id) REFERENCES industries(industry_id) ON DELETE CASCADE,
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Create triggers to update timestamps
CREATE TRIGGER update_industry_timestamp
AFTER UPDATE ON industries
FOR EACH ROW
BEGIN
    UPDATE industries SET updated_at = CURRENT_TIMESTAMP WHERE industry_id = OLD.industry_id;
END;

CREATE TRIGGER update_portfolio_timestamp
AFTER UPDATE ON portfolios
FOR EACH ROW
BEGIN
    UPDATE portfolios SET updated_at = CURRENT_TIMESTAMP WHERE portfolio_id = OLD.portfolio_id;
END;

-- Create index for performance optimization
CREATE INDEX idx_industry_name ON industries(name);
CREATE INDEX idx_portfolio_name ON portfolios(name);
CREATE INDEX idx_industry_portfolio ON industry_portfolios(industry_id, portfolio_id);
```
