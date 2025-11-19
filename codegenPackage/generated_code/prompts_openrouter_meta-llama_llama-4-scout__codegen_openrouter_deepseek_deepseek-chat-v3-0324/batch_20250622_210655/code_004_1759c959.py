"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Create a simple database schema for managing projects, institutional support, and programs (e.g., NAPREDUJEM UZ PODRŠKU- MROSP, TEMELJNE SUSTAVNE PODRŠKE- NZZRCD) for an organization similar to Udruga Radost Ogulin.
Generated: DETERMINISTIC_1759c959a7ae57c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for project management system
-- Supports projects, institutional support programs, and related entities

CREATE TABLE institutions (
    institution_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(50) UNIQUE,
    description TEXT,
    institution_id INTEGER REFERENCES institutions(institution_id),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES project_categories(category_id),
    program_id INTEGER REFERENCES programs(program_id),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15,2),
    status VARCHAR(50) CHECK (status IN ('planned', 'active', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN DEFAULT FALSE,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    file_path VARCHAR(512) NOT NULL,
    file_type VARCHAR(50),
    file_size INTEGER,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE financial_records (
    record_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    amount DECIMAL(15,2) NOT NULL,
    transaction_date DATE NOT NULL,
    description TEXT,
    transaction_type VARCHAR(50) CHECK (transaction_type IN ('income', 'expense')),
    category VARCHAR(100),
    receipt_path VARCHAR(512),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    role VARCHAR(100),
    join_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_team (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES team_members(member_id) ON DELETE CASCADE,
    role VARCHAR(100),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (project_id, member_id)
);

-- Create indexes for better performance
CREATE INDEX idx_projects_program ON projects(program_id);
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_documents_project ON documents(project_id);
CREATE INDEX idx_financial_project ON financial_records(project_id);
CREATE INDEX idx_project_team_project ON project_team(project_id);
CREATE INDEX idx_project_team_member ON project_team(member_id);

-- Create triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_institutions_timestamp
BEFORE UPDATE ON institutions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_programs_timestamp
BEFORE UPDATE ON programs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_milestones_timestamp
BEFORE UPDATE ON project_milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_team_members_timestamp
BEFORE UPDATE ON team_members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
