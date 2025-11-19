"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Design a database schema for storing information about AIDA's projects, including project name, description, location, and outcomes, and write a SQL query to retrieve project data.
Generated: DETERMINISTIC_81d05c4e62bb9a1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AIDA's projects
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) CHECK (status IN ('planned', 'ongoing', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_outcomes (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    outcome_type VARCHAR(100) NOT NULL,
    description TEXT,
    metric_value DECIMAL(10,2),
    metric_unit VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SQL query to retrieve project data with outcomes
SELECT 
    p.id,
    p.name,
    p.description,
    p.location,
    p.start_date,
    p.end_date,
    p.status,
    json_agg(
        json_build_object(
            'outcome_type', po.outcome_type,
            'description', po.description,
            'metric_value', po.metric_value,
            'metric_unit', po.metric_unit
        )
    ) AS outcomes
FROM 
    projects p
LEFT JOIN 
    project_outcomes po ON p.id = po.project_id
GROUP BY 
    p.id
ORDER BY 
    p.created_at DESC;
```
