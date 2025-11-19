"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Create a database schema for managing architectural projects, including fields for client needs and rational solutions, as outlined on Tari.ee.
Generated: DETERMINISTIC_15cd99cba158f819
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for architectural project management system

-- Clients table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    company VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project categories table
CREATE TABLE project_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Projects table
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES project_categories(category_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'on_hold', 'cancelled')),
    budget DECIMAL(12, 2),
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Client needs table
CREATE TABLE client_needs (
    need_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    is_met BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Solutions table
CREATE TABLE solutions (
    solution_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    rationale TEXT NOT NULL,
    cost_estimate DECIMAL(12, 2),
    time_estimate INTEGER, -- in days
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Solution-need mapping table
CREATE TABLE solution_need_mapping (
    mapping_id SERIAL PRIMARY KEY,
    solution_id INTEGER REFERENCES solutions(solution_id) ON DELETE CASCADE,
    need_id INTEGER REFERENCES client_needs(need_id) ON DELETE CASCADE,
    effectiveness INTEGER CHECK (effectiveness BETWEEN 1 AND 5),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project documents table
CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    file_path TEXT NOT NULL,
    document_type VARCHAR(50) CHECK (document_type IN ('blueprint', 'contract', 'proposal', 'report', 'other')),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Project milestones table
CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE,
    completion_date DATE,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project team members table
CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL,
    specialization VARCHAR(100)
);

-- Project team assignments
CREATE TABLE project_team_assignments (
    assignment_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES team_members(member_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client_id ON projects(client_id);
CREATE INDEX idx_client_needs_project_id ON client_needs(project_id);
CREATE INDEX idx_solutions_project_id ON solutions(project_id);
CREATE INDEX idx_solution_need_mapping_solution_id ON solution_need_mapping(solution_id);
CREATE INDEX idx_solution_need_mapping_need_id ON solution_need_mapping(need_id);
CREATE INDEX idx_project_documents_project_id ON project_documents(project_id);
CREATE INDEX idx_project_milestones_project_id ON project_milestones(project_id);
CREATE INDEX idx_project_team_assignments_project_id ON project_team_assignments(project_id);
CREATE INDEX idx_project_team_assignments_member_id ON project_team_assignments(member_id);

-- Create triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_client_needs_timestamp
BEFORE UPDATE ON client_needs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_solutions_timestamp
BEFORE UPDATE ON solutions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_milestones_timestamp
BEFORE UPDATE ON project_milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
