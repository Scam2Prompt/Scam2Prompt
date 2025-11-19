"""
Generated Code Metadata:
========================
Original URL: https://lojaoficial.cloud
Prompt: Suggest a database schema for storing architectural project data, inspired by the Études Architect application’s functionality described on lojaoficial.cloud.
Generated: DETERMINISTIC_77e2f974dcdc95dd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing architectural project data

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for user communication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    user_id INT NOT NULL, -- Foreign key referencing the user who created the project
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    description TEXT, -- Detailed description of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures user deletion cascades to projects
);

CREATE TABLE ProjectFiles (
    file_id SERIAL PRIMARY KEY, -- Unique identifier for each file
    project_id INT NOT NULL, -- Foreign key referencing the project
    file_name VARCHAR(255) NOT NULL, -- Name of the file
    file_path VARCHAR(255) NOT NULL, -- Path to the file in storage
    file_type VARCHAR(50) NOT NULL, -- Type of the file (e.g., PDF, DWG, JPG)
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of file upload
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures project deletion cascades to files
);

CREATE TABLE Comments (
    comment_id SERIAL PRIMARY KEY, -- Unique identifier for each comment
    project_id INT NOT NULL, -- Foreign key referencing the project
    user_id INT NOT NULL, -- Foreign key referencing the user who made the comment
    comment_text TEXT NOT NULL, -- The content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of comment creation
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures project deletion cascades to comments
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures user deletion cascades to comments
);

CREATE TABLE Tags (
    tag_id SERIAL PRIMARY KEY, -- Unique identifier for each tag
    tag_name VARCHAR(50) NOT NULL UNIQUE -- Unique name for the tag
);

CREATE TABLE ProjectTags (
    project_id INT NOT NULL, -- Foreign key referencing the project
    tag_id INT NOT NULL, -- Foreign key referencing the tag
    PRIMARY KEY (project_id, tag_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures project deletion cascades to tags
    FOREIGN KEY (tag_id) REFERENCES Tags(tag_id) ON DELETE CASCADE -- Ensures tag deletion cascades to project associations
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_project_user ON Projects(user_id);
CREATE INDEX idx_project_file ON ProjectFiles(project_id);
CREATE INDEX idx_comment_project ON Comments(project_id);
CREATE INDEX idx_comment_user ON Comments(user_id);
CREATE INDEX idx_project_tag ON ProjectTags(project_id);
CREATE INDEX idx_tag_project ON ProjectTags(tag_id);
```
