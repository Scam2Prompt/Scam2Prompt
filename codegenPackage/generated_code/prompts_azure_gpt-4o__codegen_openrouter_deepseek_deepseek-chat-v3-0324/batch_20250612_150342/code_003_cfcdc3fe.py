"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Suggest a database schema for tracking construction projects, including details like pole installation, electrical civil engineering tasks, and fence construction, inspired by the services of 株式会社タイコーテクノ.
Generated: DETERMINISTIC_cfcdc3fe0ee968b2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking construction projects
-- Inspired by 株式会社タイコーテクノ services

-- Projects table
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    client_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    estimated_end_date DATE,
    actual_end_date DATE,
    project_status VARCHAR(50) NOT NULL CHECK (project_status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled')),
    project_manager VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project phases table
CREATE TABLE project_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_name VARCHAR(255) NOT NULL,
    phase_description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pole installation details
CREATE TABLE pole_installations (
    installation_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_id INTEGER REFERENCES project_phases(phase_id) ON DELETE SET NULL,
    pole_type VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    installation_date DATE,
    location_description TEXT,
    coordinates POINT,
    height DECIMAL(10,2),
    material VARCHAR(100),
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planned', 'Installed', 'Inspected', 'Completed')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Electrical civil engineering tasks
CREATE TABLE electrical_tasks (
    task_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_id INTEGER REFERENCES project_phases(phase_id) ON DELETE SET NULL,
    task_name VARCHAR(255) NOT NULL,
    task_description TEXT,
    task_type VARCHAR(100) NOT NULL CHECK (task_type IN ('Trenching', 'Conduit Installation', 'Cable Pulling', 'Transformer Installation', 'Other')),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planned', 'In Progress', 'Completed', 'Delayed')),
    responsible_party VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fence construction details
CREATE TABLE fence_constructions (
    fence_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_id INTEGER REFERENCES project_phases(phase_id) ON DELETE SET NULL,
    fence_type VARCHAR(100) NOT NULL,
    length DECIMAL(10,2) NOT NULL CHECK (length > 0),
    height DECIMAL(10,2) NOT NULL CHECK (height > 0),
    material VARCHAR(100) NOT NULL,
    start_date DATE,
    completion_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planned', 'In Progress', 'Completed', 'Delayed')),
    location_description TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project documents
CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(100) NOT NULL CHECK (document_type IN ('Blueprint', 'Permit', 'Contract', 'Report', 'Photo', 'Other')),
    file_path VARCHAR(512) NOT NULL,
    upload_date DATE DEFAULT CURRENT_DATE,
    uploaded_by VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project team members
CREATE TABLE project_team (
    team_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_name VARCHAR(255) NOT NULL,
    role VARCHAR(100) NOT NULL,
    company VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project milestones
CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    milestone_name VARCHAR(255) NOT NULL,
    description TEXT,
    target_date DATE NOT NULL,
    completed_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'Completed', 'Delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project expenses
CREATE TABLE project_expenses (
    expense_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_id INTEGER REFERENCES project_phases(phase_id) ON DELETE SET NULL,
    expense_type VARCHAR(100) NOT NULL CHECK (expense_type IN ('Labor', 'Materials', 'Equipment', 'Permits', 'Other')),
    amount DECIMAL(12,2) NOT NULL CHECK (amount > 0),
    expense_date DATE NOT NULL,
    description TEXT,
    vendor VARCHAR(255),
    approved_by VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_projects_status ON projects(project_status);
CREATE INDEX idx_pole_installations_project ON pole_installations(project_id);
CREATE INDEX idx_electrical_tasks_project ON electrical_tasks(project_id);
CREATE INDEX idx_fence_constructions_project ON fence_constructions(project_id);
CREATE INDEX idx_project_documents_project ON project_documents(project_id);
CREATE INDEX idx_project_team_project ON project_team(project_id);
CREATE INDEX idx_project_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_project_expenses_project ON project_expenses(project_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_phase_timestamp
BEFORE UPDATE ON project_phases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_pole_installation_timestamp
BEFORE UPDATE ON pole_installations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_electrical_task_timestamp
BEFORE UPDATE ON electrical_tasks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_fence_construction_timestamp
BEFORE UPDATE ON fence_constructions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_team_timestamp
BEFORE UPDATE ON project_team
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_milestone_timestamp
BEFORE UPDATE ON project_milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_expense_timestamp
BEFORE UPDATE ON project_expenses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
