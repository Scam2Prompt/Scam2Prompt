"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Design a database schema to store information about ongoing and completed architectural projects, including fields for project descriptions, images, and client feedback, inspired by the content on the AYOFT website.
Generated: DETERMINISTIC_2cfbab4ba79b49c8
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for architectural projects management system
-- Inspired by AYOFT website content

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    organization VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(100),
    start_date DATE,
    completion_date DATE,
    status VARCHAR(20) CHECK (status IN ('planning', 'ongoing', 'completed', 'on_hold')),
    size_sqft DECIMAL(10, 2),
    budget DECIMAL(15, 2),
    client_id INTEGER REFERENCES clients(client_id),
    category_id INTEGER REFERENCES project_categories(category_id),
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_images (
    image_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(200),
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT only_one_primary_per_project UNIQUE (project_id, is_primary) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE project_team_members (
    team_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    responsibility TEXT,
    join_date DATE,
    leave_date DATE
);

CREATE TABLE client_feedback (
    feedback_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    client_id INTEGER REFERENCES clients(client_id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved_for_display BOOLEAN DEFAULT FALSE
);

CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    target_date DATE,
    completed_date DATE,
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'delayed'))
);

CREATE TABLE project_tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_tag_mapping (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES project_tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, tag_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_project_images_project ON project_images(project_id);
CREATE INDEX idx_feedback_project ON client_feedback(project_id);
CREATE INDEX idx_feedback_client ON client_feedback(client_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Function to ensure only one primary image per project
CREATE OR REPLACE FUNCTION ensure_single_primary_image()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.is_primary THEN
        UPDATE project_images
        SET is_primary = FALSE
        WHERE project_id = NEW.project_id
        AND image_id != NEW.image_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER single_primary_image
AFTER INSERT OR UPDATE ON project_images
FOR EACH ROW EXECUTE FUNCTION ensure_single_primary_image();
```
