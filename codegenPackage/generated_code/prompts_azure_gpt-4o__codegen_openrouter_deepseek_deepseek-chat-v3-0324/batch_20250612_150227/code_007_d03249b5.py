"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Develop a database schema for tracking portfolio companies' growth and international expansion, considering Initia Capital's operational support and strategic guidance.
Generated: DETERMINISTIC_d03249b528142a73
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking portfolio companies' growth and international expansion
-- Designed for Initia Capital's operational support and strategic guidance

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Companies table - core information about portfolio companies
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    industry TEXT NOT NULL,
    founding_date DATE NOT NULL,
    headquarters_country TEXT NOT NULL,
    description TEXT,
    website_url TEXT,
    current_valuation REAL,
    initial_investment_date DATE NOT NULL,
    exit_date DATE,
    exit_type TEXT CHECK(exit_type IN ('IPO', 'Acquisition', 'Secondary Sale', NULL)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (exit_date IS NULL OR exit_date >= initial_investment_date)
);

-- Company financials table - track financial metrics over time
CREATE TABLE company_financials (
    financial_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    reporting_date DATE NOT NULL,
    revenue REAL NOT NULL CHECK(revenue >= 0),
    ebitda REAL,
    net_income REAL,
    cash_balance REAL CHECK(cash_balance >= 0),
    burn_rate REAL,
    employees INTEGER CHECK(employees >= 0),
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    UNIQUE (company_id, reporting_date)
);

-- International expansion tracking
CREATE TABLE international_expansion (
    expansion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    country_code TEXT NOT NULL,
    entry_date DATE NOT NULL,
    expansion_type TEXT NOT NULL CHECK(expansion_type IN ('Sales', 'Operations', 'Manufacturing', 'HQ')),
    fte_count INTEGER CHECK(fte_count >= 0),
    revenue_contribution REAL CHECK(revenue_contribution >= 0),
    status TEXT NOT NULL CHECK(status IN ('Planning', 'Active', 'Paused', 'Exited')),
    notes TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Operational support provided by Initia Capital
CREATE TABLE operational_support (
    support_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    support_date DATE NOT NULL,
    support_type TEXT NOT NULL CHECK(support_type IN ('Hiring', 'Strategy', 'Finance', 'Product', 'Marketing', 'Legal', 'International')),
    description TEXT NOT NULL,
    hours_spent REAL CHECK(hours_spent > 0),
    initia_team_member TEXT NOT NULL,
    impact_rating INTEGER CHECK(impact_rating BETWEEN 1 AND 5),
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    CHECK (follow_up_date IS NULL OR follow_up_date >= support_date)
);

-- Strategic milestones and objectives
CREATE TABLE strategic_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL CHECK(category IN ('Growth', 'International', 'Product', 'Funding', 'Operational')),
    target_date DATE NOT NULL,
    completion_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Not Started', 'In Progress', 'Completed', 'Delayed', 'Cancelled')),
    priority INTEGER CHECK(priority BETWEEN 1 AND 3),
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    CHECK (completion_date IS NULL OR completion_date >= target_date)
);

-- Funding rounds tracking
CREATE TABLE funding_rounds (
    round_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    round_date DATE NOT NULL,
    round_type TEXT NOT NULL CHECK(round_type IN ('Seed', 'Series A', 'Series B', 'Series C', 'Series D+', 'Bridge', 'Debt')),
    amount_raised REAL NOT NULL CHECK(amount_raised > 0),
    pre_money_valuation REAL CHECK(pre_money_valuation > 0),
    lead_investor TEXT,
    participants TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Key performance indicators (KPIs)
CREATE TABLE company_kpis (
    kpi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    kpi_date DATE NOT NULL,
    kpi_name TEXT NOT NULL CHECK(kpi_name IN ('ARR', 'CAC', 'LTV', 'Churn Rate', 'Gross Margin', 'NPS', 'Market Share')),
    kpi_value REAL NOT NULL,
    target_value REAL,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    UNIQUE (company_id, kpi_date, kpi_name)
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_company_timestamp
AFTER UPDATE ON companies
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_financials_timestamp
AFTER UPDATE ON company_financials
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_expansion_timestamp
AFTER UPDATE ON international_expansion
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_support_timestamp
AFTER UPDATE ON operational_support
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_milestones_timestamp
AFTER UPDATE ON strategic_milestones
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_funding_timestamp
AFTER UPDATE ON funding_rounds
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_kpis_timestamp
AFTER UPDATE ON company_kpis
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;
```
