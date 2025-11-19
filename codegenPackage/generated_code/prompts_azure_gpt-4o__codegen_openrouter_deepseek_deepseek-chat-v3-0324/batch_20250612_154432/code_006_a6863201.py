"""
Generated Code Metadata:
========================
Original URL: https://oeg-group.com
Prompt: Create a database schema to manage project details for residential and commercial outdoor environments, inspired by the project categories listed on the Outdoor Environments Group website.
Generated: DETERMINISTIC_a6863201e6f3b705
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing outdoor environment projects

-- Create the database
CREATE DATABASE outdoor_environments_db;
USE outdoor_environments_db;

-- Project types table
CREATE TABLE project_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Project categories table
CREATE TABLE project_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES project_types(id) ON DELETE CASCADE,
    UNIQUE KEY (type_id, name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Projects table
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    start_date DATE,
    end_date DATE,
    status ENUM('planning', 'in_progress', 'completed', 'on_hold') DEFAULT 'planning',
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES project_categories(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Project images table
CREATE TABLE project_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Project features table
CREATE TABLE project_features (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    feature VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert initial project types
INSERT INTO project_types (name, description) VALUES 
('Residential', 'Projects for private homes and residential properties'),
('Commercial', 'Projects for businesses and commercial properties');

-- Insert initial project categories (residential)
INSERT INTO project_categories (type_id, name, description) VALUES 
(1, 'Outdoor Living', 'Creating beautiful outdoor living spaces'),
(1, 'Pools & Water Features', 'Custom pools and water features design'),
(1, 'Landscape Design', 'Comprehensive landscape design services'),
(1, 'Outdoor Kitchens', 'Design and installation of outdoor kitchens'),
(1, 'Fire Features', 'Custom fire pits, fireplaces, and fire tables');

-- Insert initial project categories (commercial)
INSERT INTO project_categories (type_id, name, description) VALUES 
(2, 'Hospitality', 'Outdoor spaces for hotels and resorts'),
(2, 'Retail', 'Outdoor environments for retail spaces'),
(2, 'Corporate', 'Corporate campus outdoor spaces'),
(2, 'Public Spaces', 'Parks, plazas, and community areas'),
(2, 'Multi-Family', 'Outdoor spaces for apartment complexes');

-- Create indexes for better performance
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_images_project ON project_images(project_id);
CREATE INDEX idx_project_features_project ON project_features(project_id);
```
