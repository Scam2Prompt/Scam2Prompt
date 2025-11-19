"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a database schema to store and manage data for over 30,000 completed projects, as highlighted on the Bismillah Traders website.
Generated: DETERMINISTIC_6863719769651f14
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Bismillah Traders project management system
-- Designed to efficiently store and manage over 30,000 completed projects

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE project_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE SET NULL,
    category_id INTEGER REFERENCES project_categories(category_id) ON DELETE SET NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE,
    completion_date DATE NOT NULL,
    budget DECIMAL(15, 2),
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('completed', 'archived')),
    location VARCHAR(200),
    project_manager VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (completion_date >= start_date)
);

CREATE TABLE project_photos (
    photo_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    photo_url TEXT NOT NULL,
    caption VARCHAR(200),
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_url TEXT NOT NULL,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(50),
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_testimonials (
    testimonial_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    client_name VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    rating SMALLINT CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE project_tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_tag_mapping (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES project_tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, tag_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_projects_completion_date ON projects(completion_date);
CREATE INDEX idx_project_photos ON project_photos(project_id);
CREATE INDEX idx_project_documents ON project_documents(project_id);
CREATE INDEX idx_project_testimonials ON project_testimonials(project_id);
CREATE INDEX idx_project_tag_mapping ON project_tag_mapping(project_id, tag_id);

-- Function to automatically update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- View for project summaries
CREATE VIEW project_summaries AS
SELECT 
    p.project_id,
    p.title,
    c.name AS client_name,
    pc.name AS category,
    p.start_date,
    p.completion_date,
    p.budget,
    p.location,
    (SELECT COUNT(*) FROM project_photos WHERE project_id = p.project_id) AS photo_count,
    (SELECT COUNT(*) FROM project_testimonials WHERE project_id = p.project_id AND is_approved = TRUE) AS testimonial_count
FROM 
    projects p
LEFT JOIN 
    clients c ON p.client_id = c.client_id
LEFT JOIN 
    project_categories pc ON p.category_id = pc.category_id;
```
