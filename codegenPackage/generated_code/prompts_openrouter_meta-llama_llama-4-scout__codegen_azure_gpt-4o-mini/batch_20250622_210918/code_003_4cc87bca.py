"""
Generated Code Metadata:
========================
Original URL: https://renzostudio.com
Prompt: "Design a database schema for storing information about architectural projects, including images, descriptions, and client details."
Generated: DETERMINISTIC_4cc87bca938da7ec
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about architectural projects

CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL, -- Client's name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email, must be unique
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    title VARCHAR(255) NOT NULL, -- Title of the project
    description TEXT NOT NULL, -- Detailed description of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')), -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ProjectImages (
    image_id SERIAL PRIMARY KEY, -- Unique identifier for each image
    project_id INT NOT NULL, -- Foreign key referencing Projects table
    image_url VARCHAR(255) NOT NULL, -- URL of the image
    description VARCHAR(255), -- Optional description of the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_project_client ON Projects(client_id);
CREATE INDEX idx_project_status ON Projects(status);
CREATE INDEX idx_project_images ON ProjectImages(project_id);
```
