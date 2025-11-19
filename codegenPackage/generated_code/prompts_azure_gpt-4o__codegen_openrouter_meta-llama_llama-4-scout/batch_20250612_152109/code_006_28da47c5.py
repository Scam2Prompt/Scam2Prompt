"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Create a database schema for managing financial accountability indicators, inspired by the SAKIP system described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_28da47c57021c905
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- financial_accountability_indicators_schema.sql

-- Create database schema for managing financial accountability indicators
CREATE SCHEMA financial_accountability_indicators;
SET search_path TO financial_accountability_indicators;

-- Create table for indicators
CREATE TABLE indicators (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for indicator categories
CREATE TABLE indicator_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create many-to-many relationship table for indicators and categories
CREATE TABLE indicator_category_mappings (
    indicator_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (indicator_id, category_id),
    FOREIGN KEY (indicator_id) REFERENCES indicators(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES indicator_categories(id) ON DELETE CASCADE
);

-- Create table for indicator values
CREATE TABLE indicator_values (
    id SERIAL PRIMARY KEY,
    indicator_id INTEGER NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    year INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (indicator_id) REFERENCES indicators(id) ON DELETE CASCADE
);

-- Create table for indicator targets
CREATE TABLE indicator_targets (
    id SERIAL PRIMARY KEY,
    indicator_id INTEGER NOT NULL,
    target DECIMAL(10, 2) NOT NULL,
    year INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (indicator_id) REFERENCES indicators(id) ON DELETE CASCADE
);

-- Create table for data sources
CREATE TABLE data_sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for indicator data sources
CREATE TABLE indicator_data_sources (
    indicator_id INTEGER NOT NULL,
    data_source_id INTEGER NOT NULL,
    PRIMARY KEY (indicator_id, data_source_id),
    FOREIGN KEY (indicator_id) REFERENCES indicators(id) ON DELETE CASCADE,
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_indicators_name ON indicators (name);
CREATE INDEX idx_indicator_categories_name ON indicator_categories (name);
CREATE INDEX idx_indicator_values_indicator_id ON indicator_values (indicator_id);
CREATE INDEX idx_indicator_targets_indicator_id ON indicator_targets (indicator_id);
CREATE INDEX idx_indicator_data_sources_indicator_id ON indicator_data_sources (indicator_id);
CREATE INDEX idx_indicator_data_sources_data_source_id ON indicator_data_sources (data_source_id);

-- Create views for simplified querying
CREATE VIEW indicator_details AS
SELECT 
    i.id,
    i.name,
    i.description,
    ic.name AS category_name,
    iv.value,
    iv.year,
    it.target,
    ds.name AS data_source_name
FROM 
    indicators i
LEFT JOIN 
    indicator_category_mappings icm ON i.id = icm.indicator_id
LEFT JOIN 
    indicator_categories ic ON icm.category_id = ic.id
LEFT JOIN 
    indicator_values iv ON i.id = iv.indicator_id
LEFT JOIN 
    indicator_targets it ON i.id = it.indicator_id AND iv.year = it.year
LEFT JOIN 
    indicator_data_sources ids ON i.id = ids.indicator_id
LEFT JOIN 
    data_sources ds ON ids.data_source_id = ds.id;
```

```sql
-- Example usage:
-- Insert sample data
INSERT INTO indicators (name, description) 
VALUES ('Indicator 1', 'This is indicator 1');

INSERT INTO indicator_categories (name, description) 
VALUES ('Category 1', 'This is category 1');

INSERT INTO indicator_category_mappings (indicator_id, category_id) 
VALUES (1, 1);

INSERT INTO indicator_values (indicator_id, value, year) 
VALUES (1, 100.00, 2022);

INSERT INTO indicator_targets (indicator_id, target, year) 
VALUES (1, 120.00, 2022);

INSERT INTO data_sources (name, description) 
VALUES ('Data Source 1', 'This is data source 1');

INSERT INTO indicator_data_sources (indicator_id, data_source_id) 
VALUES (1, 1);

-- Query indicator details
SELECT * FROM indicator_details;
```
