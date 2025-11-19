"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Design a database schema to store information about construction projects, clients, and team members for a design-build and turnkey construction services company, and provide an example of how to query the database."
Generated: DETERMINISTIC_040da88968a618df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction management system

-- Clients table
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'on_hold', 'completed', 'cancelled')),
    project_type VARCHAR(50) CHECK (project_type IN ('design-build', 'turnkey', 'other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Team members table
CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES team_members(member_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    hours_allocated INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(project_id, member_id)
);

-- Project phases table
CREATE TABLE project_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('not_started', 'in_progress', 'completed', 'delayed')),
    budget DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Documents table
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    uploaded_by INTEGER REFERENCES team_members(member_id),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    version VARCHAR(20)
);

-- Example queries

-- Get all active projects with client information
SELECT 
    p.project_id,
    p.name AS project_name,
    p.status,
    p.start_date,
    p.end_date,
    c.name AS client_name,
    c.contact_person,
    c.email AS client_email
FROM 
    projects p
JOIN 
    clients c ON p.client_id = c.client_id
WHERE 
    p.status NOT IN ('completed', 'cancelled')
ORDER BY 
    p.start_date DESC;

-- Get team members assigned to a specific project
SELECT 
    tm.member_id,
    tm.first_name,
    tm.last_name,
    tm.role AS member_role,
    pa.role AS project_role,
    pa.start_date,
    pa.end_date
FROM 
    team_members tm
JOIN 
    project_assignments pa ON tm.member_id = pa.member_id
WHERE 
    pa.project_id = :project_id
ORDER BY 
    tm.last_name;

-- Get project phases with budget information
SELECT 
    ph.phase_id,
    ph.name,
    ph.start_date,
    ph.end_date,
    ph.status,
    ph.budget,
    (ph.budget / NULLIF(p.budget, 0)) * 100 AS budget_percentage
FROM 
    project_phases ph
JOIN 
    projects p ON ph.project_id = p.project_id
WHERE 
    ph.project_id = :project_id
ORDER BY 
    ph.start_date;

-- Get documents for a project
SELECT 
    d.document_id,
    d.name,
    d.type,
    d.upload_date,
    CONCAT(tm.first_name, ' ', tm.last_name) AS uploaded_by,
    d.description
FROM 
    documents d
LEFT JOIN 
    team_members tm ON d.uploaded_by = tm.member_id
WHERE 
    d.project_id = :project_id
ORDER BY 
    d.upload_date DESC;
```
