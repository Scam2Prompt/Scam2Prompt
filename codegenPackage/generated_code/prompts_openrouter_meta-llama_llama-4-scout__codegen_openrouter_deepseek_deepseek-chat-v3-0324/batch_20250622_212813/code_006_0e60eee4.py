"""
Generated Code Metadata:
========================
Original URL: https://hypersteakin.site
Prompt: Design a database schema to store information about gaming startups, indie developers, and their projects, as featured in the HyperSteakin Startup Showcase.
Generated: DETERMINISTIC_0e60eee438d857e8
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for HyperSteakin Startup Showcase

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing gaming startups
CREATE TABLE startups (
    startup_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    founded_date DATE,
    website_url TEXT,
    logo_url TEXT,
    country TEXT,
    city TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing indie developers
CREATE TABLE developers (
    developer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    bio TEXT,
    email TEXT UNIQUE NOT NULL,
    twitter_handle TEXT,
    linkedin_url TEXT,
    portfolio_url TEXT,
    country TEXT,
    city TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for developer-startup relationships
CREATE TABLE developer_startup (
    developer_id INTEGER NOT NULL,
    startup_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    join_date DATE,
    is_current BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (developer_id, startup_id),
    FOREIGN KEY (developer_id) REFERENCES developers(developer_id) ON DELETE CASCADE,
    FOREIGN KEY (startup_id) REFERENCES startups(startup_id) ON DELETE CASCADE
);

-- Table for storing game projects
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    startup_id INTEGER,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    genre TEXT NOT NULL,
    platform TEXT NOT NULL,
    release_date DATE,
    website_url TEXT,
    trailer_url TEXT,
    status TEXT CHECK(status IN ('Concept', 'Development', 'Alpha', 'Beta', 'Released', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (startup_id) REFERENCES startups(startup_id) ON DELETE SET NULL
);

-- Table for storing project media (screenshots, artwork, etc.)
CREATE TABLE project_media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    media_type TEXT CHECK(media_type IN ('Screenshot', 'Artwork', 'Logo', 'Video')),
    caption TEXT,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table for storing showcase features
CREATE TABLE showcases (
    showcase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for projects featured in showcases
CREATE TABLE showcase_projects (
    showcase_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    featured_order INTEGER NOT NULL,
    notes TEXT,
    PRIMARY KEY (showcase_id, project_id),
    FOREIGN KEY (showcase_id) REFERENCES showcases(showcase_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table for storing press mentions/articles
CREATE TABLE press_mentions (
    mention_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    startup_id INTEGER,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    source TEXT NOT NULL,
    publish_date DATE,
    excerpt TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL,
    FOREIGN KEY (startup_id) REFERENCES startups(startup_id) ON DELETE SET NULL
);

-- Trigger to update timestamps on row updates
CREATE TRIGGER update_timestamps
AFTER UPDATE ON startups
FOR EACH ROW
BEGIN
    UPDATE startups SET updated_at = CURRENT_TIMESTAMP WHERE startup_id = OLD.startup_id;
END;

CREATE TRIGGER update_timestamps_dev
AFTER UPDATE ON developers
FOR EACH ROW
BEGIN
    UPDATE developers SET updated_at = CURRENT_TIMESTAMP WHERE developer_id = OLD.developer_id;
END;

CREATE TRIGGER update_timestamps_proj
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_startup_name ON startups(name);
CREATE INDEX idx_developer_name ON developers(last_name, first_name);
CREATE INDEX idx_project_name ON projects(name);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_project_startup ON projects(startup_id);
CREATE INDEX idx_showcase_date ON showcases(event_date);
```
