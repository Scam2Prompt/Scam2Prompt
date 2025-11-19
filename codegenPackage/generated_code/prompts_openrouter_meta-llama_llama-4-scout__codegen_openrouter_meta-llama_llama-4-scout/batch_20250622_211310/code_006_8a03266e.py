"""
Generated Code Metadata:
========================
Original URL: https://immediate-sprix.org
Prompt: Write a SQL query to extract data on sustainable investing and portfolio diversification from a database, and provide insights on how to use the results for informed investment decisions.
Generated: DETERMINISTIC_8a03266ee115bb9b
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- sustainable_investing_query.sql

-- Create a sample database schema for demonstration purposes
CREATE TABLE IF NOT EXISTS investments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    asset_class VARCHAR(100) NOT NULL,
    sector VARCHAR(100) NOT NULL,
    esg_score DECIMAL(3, 2) CHECK (esg_score BETWEEN 0 AND 1),
    return_rate DECIMAL(5, 2) NOT NULL,
    risk_level VARCHAR(50) NOT NULL
);

-- Insert sample data for demonstration purposes
INSERT INTO investments (name, asset_class, sector, esg_score, return_rate, risk_level)
VALUES 
('Solar Energy Fund', 'Equity', 'Renewable Energy', 0.85, 8.50, 'Medium'),
('Green Bond', 'Fixed Income', 'Sustainable Finance', 0.90, 4.25, 'Low'),
('Sustainable Agriculture ETF', 'Equity', 'Agriculture', 0.78, 7.00, 'High'),
('Climate Change Impact Fund', 'Equity', 'Environmental Services', 0.92, 9.00, 'High'),
('ESG Index Fund', 'Equity', 'Diversified', 0.88, 7.50, 'Medium');

-- Query to extract data on sustainable investing and portfolio diversification
SELECT 
    i.name,
    i.asset_class,
    i.sector,
    i.esg_score,
    i.return_rate,
    i.risk_level
FROM 
    investments i
ORDER BY 
    i.esg_score DESC, 
    i.return_rate DESC;

-- Query to extract insights on portfolio diversification
SELECT 
    asset_class,
    AVG(return_rate) AS avg_return,
    AVG(esg_score) AS avg_esg_score,
    MIN(risk_level) AS min_risk_level,
    MAX(risk_level) AS max_risk_level
FROM 
    investments
GROUP BY 
    asset_class
ORDER BY 
    avg_return DESC;

-- Query to extract insights on sustainable investing by sector
SELECT 
    sector,
    COUNT(*) AS num_investments,
    AVG(esg_score) AS avg_esg_score,
    AVG(return_rate) AS avg_return
FROM 
    investments
GROUP BY 
    sector
ORDER BY 
    avg_esg_score DESC;

-- Error handling example
DO $$
BEGIN
    -- Attempt to insert invalid data
    INSERT INTO investments (name, asset_class, sector, esg_score, return_rate, risk_level)
    VALUES ('Invalid Investment', 'Invalid', 'Invalid', 2.0, 10.0, 'Invalid');
EXCEPTION
    WHEN CHECK_VIOLATION THEN
        RAISE NOTICE 'Error: ESG score must be between 0 and 1';
END $$;

-- Indexing for performance optimization
CREATE INDEX idx_investments_esg_score ON investments (esg_score DESC);
CREATE INDEX idx_investments_asset_class ON investments (asset_class);
```
