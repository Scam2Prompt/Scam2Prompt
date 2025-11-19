"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Design a database schema for storing client information and project details for an experiential marketing agency with operations in Uganda, Mozambique, and South Africa."
Generated: DETERMINISTIC_0a652fce223dcbfa
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an experiential marketing agency
-- Supports operations in Uganda, Mozambique, and South Africa

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Countries table
CREATE TABLE countries (
    country_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    country_name VARCHAR(100) NOT NULL,
    country_code VARCHAR(3) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Cities table
CREATE TABLE cities (
    city_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    country_id UUID NOT NULL,
    city_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

-- Client categories table
CREATE TABLE client_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_name VARCHAR(255) NOT NULL,
    category_id UUID,
    contact_person VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city_id UUID,
    tax_id VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES client_categories(category_id) ON DELETE SET NULL,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE SET NULL,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Project statuses table
CREATE TABLE project_statuses (
    status_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_name VARCHAR(255) NOT NULL,
    client_id UUID NOT NULL,
    status_id UUID NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2),
    description TEXT,
    city_id UUID,
    country_id UUID,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES project_statuses(status_id) ON DELETE RESTRICT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE SET NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE SET NULL,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
);

-- Project documents table
CREATE TABLE project_documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project team members table
CREATE TABLE project_team_members (
    member_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL,
    member_name VARCHAR(255) NOT NULL,
    role VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    country_id UUID,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE SET NULL
);

-- Project milestones table
CREATE TABLE project_milestones (
    milestone_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL,
    milestone_name VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completion_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT valid_completion_date CHECK (
        (completed = FALSE AND completion_date IS NULL) OR
        (completed = TRUE AND completion_date IS NOT NULL)
    )
);

-- Project expenses table
CREATE TABLE project_expenses (
    expense_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL,
    expense_name VARCHAR(255) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    expense_date DATE NOT NULL,
    category VARCHAR(100) NOT NULL,
    description TEXT,
    receipt_path TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT positive_amount CHECK (amount > 0)
);

-- Create indexes for performance
CREATE INDEX idx_clients_city ON clients(city_id);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status_id);
CREATE INDEX idx_projects_city ON projects(city_id);
CREATE INDEX idx_project_documents_project ON project_documents(project_id);
CREATE INDEX idx_project_team_members_project ON project_team_members(project_id);
CREATE INDEX idx_project_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_project_expenses_project ON project_expenses(project_id);

-- Create trigger function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to all tables with updated_at field
DO $$
DECLARE
    t record;
BEGIN
    FOR t IN 
        SELECT table_name 
        FROM information_schema.columns 
        WHERE column_name = 'updated_at' 
        AND table_schema = 'public'
    LOOP
        EXECUTE format('CREATE TRIGGER update_timestamp
                        BEFORE UPDATE ON %I
                        FOR EACH ROW EXECUTE FUNCTION update_timestamp()', 
                        t.table_name);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Insert initial data for supported countries
INSERT INTO countries (country_name, country_code) VALUES
('Uganda', 'UG'),
('Mozambique', 'MZ'),
('South Africa', 'ZA');

-- Insert common project statuses
INSERT INTO project_statuses (status_name, description) VALUES
('Proposed', 'Project is in proposal stage'),
('Planning', 'Project is being planned'),
('Active', 'Project is currently active'),
('On Hold', 'Project is temporarily on hold'),
('Completed', 'Project has been completed'),
('Cancelled', 'Project was cancelled');
```
