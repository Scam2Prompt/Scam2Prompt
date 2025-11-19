"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Design a database schema to store information about non-profit organizations, including their mission, vision, values, and programs, and write a SQL query to retrieve the data.
Generated: DETERMINISTIC_ed611e1bfd0f56f4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for non-profit organizations
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    founded_date DATE,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE missions (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    statement TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE visions (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    statement TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE values (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE programs (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SQL query to retrieve organization data with all related information
SELECT 
    o.id AS org_id,
    o.name AS org_name,
    o.description AS org_description,
    o.website_url,
    o.founded_date,
    o.tax_id,
    m.statement AS mission_statement,
    v.statement AS vision_statement,
    val.name AS value_name,
    val.description AS value_description,
    p.name AS program_name,
    p.description AS program_description,
    p.start_date AS program_start,
    p.end_date AS program_end,
    p.is_active AS program_active
FROM 
    organizations o
LEFT JOIN 
    missions m ON o.id = m.organization_id
LEFT JOIN 
    visions v ON o.id = v.organization_id
LEFT JOIN 
    values val ON o.id = val.organization_id
LEFT JOIN 
    programs p ON o.id = p.organization_id
WHERE 
    o.id = :organization_id
ORDER BY 
    val.name, p.name;
```
