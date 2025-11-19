"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Design a database schema for storing information about puppetry groups, similar to Corporación El Cristal, including details about their history and projects.
Generated: DETERMINISTIC_bc94aeb256c3e8cf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for puppetry groups information system

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    founded_date DATE,
    country VARCHAR(50),
    city VARCHAR(50),
    website VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE group_history (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE,
    event_date DATE NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('planned', 'ongoing', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_media (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    media_type VARCHAR(20) CHECK (media_type IN ('image', 'video', 'document', 'audio')),
    url VARCHAR(255) NOT NULL,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    join_date DATE,
    leave_date DATE,
    is_current_member BOOLEAN DEFAULT TRUE,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE performances (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE,
    project_id INTEGER REFERENCES projects(id) ON DELETE SET NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    performance_date DATE NOT NULL,
    location VARCHAR(100),
    audience_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE group_tags (
    group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (group_id, tag_id)
);

CREATE TABLE project_tags (
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, tag_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_group_name ON groups(name);
CREATE INDEX idx_group_country ON groups(country);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_project_group ON projects(group_id);
CREATE INDEX idx_performance_date ON performances(performance_date);
CREATE INDEX idx_member_group ON members(group_id);
CREATE INDEX idx_member_current ON members(is_current_member);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_group_timestamp
BEFORE UPDATE ON groups
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_group_history_timestamp
BEFORE UPDATE ON group_history
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_member_timestamp
BEFORE UPDATE ON members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_performance_timestamp
BEFORE UPDATE ON performances
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
