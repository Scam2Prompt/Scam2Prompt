"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Construct a database schema for managing information on various types of construction projects, including underground and engineering works, as highlighted by URANPRES.
Generated: DETERMINISTIC_b249174bea685afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction project management
-- Supports underground and engineering works as per URANPRES requirements

CREATE TABLE project_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_underground BOOLEAN DEFAULT FALSE,
    is_engineering BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    project_code VARCHAR(50) UNIQUE NOT NULL,
    type_id INTEGER REFERENCES project_types(type_id),
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    current_spending DECIMAL(15, 2),
    status VARCHAR(50) CHECK (status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled')),
    location GEOMETRY(Point, 4326),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_name VARCHAR(100) NOT NULL,
    sequence_number INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Delayed')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_phase_sequence UNIQUE (project_id, sequence_number)
);

CREATE TABLE engineering_specs (
    spec_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    spec_name VARCHAR(200) NOT NULL,
    spec_value TEXT NOT NULL,
    unit VARCHAR(50),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE underground_works (
    work_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    depth DECIMAL(10, 2) NOT NULL,
    length DECIMAL(10, 2) NOT NULL,
    soil_type VARCHAR(100),
    rock_type VARCHAR(100),
    groundwater_level DECIMAL(10, 2),
    safety_measures TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(200) NOT NULL,
    document_type VARCHAR(100) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    created_by VARCHAR(100)
);

CREATE TABLE project_team (
    team_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_name VARCHAR(200) NOT NULL,
    role VARCHAR(100) NOT NULL,
    organization VARCHAR(200),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(50),
    is_primary_contact BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    milestone_name VARCHAR(200) NOT NULL,
    target_date DATE NOT NULL,
    completed_date DATE,
    status VARCHAR(50) CHECK (status IN ('Pending', 'Achieved', 'Delayed', 'Cancelled')),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_projects_type ON projects(type_id);
CREATE INDEX idx_project_phases_project ON project_phases(project_id);
CREATE INDEX idx_engineering_specs_project ON engineering_specs(project_id);
CREATE INDEX idx_underground_works_project ON underground_works(project_id);
CREATE INDEX idx_project_documents_project ON project_documents(project_id);
CREATE INDEX idx_project_team_project ON project_team(project_id);
CREATE INDEX idx_project_milestones_project ON project_milestones(project_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_project_types_timestamp
BEFORE UPDATE ON project_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_phases_timestamp
BEFORE UPDATE ON project_phases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_engineering_specs_timestamp
BEFORE UPDATE ON engineering_specs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_underground_works_timestamp
BEFORE UPDATE ON underground_works
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_team_timestamp
BEFORE UPDATE ON project_team
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_milestones_timestamp
BEFORE UPDATE ON project_milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
