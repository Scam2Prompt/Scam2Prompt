"""
Generated Code Metadata:
========================
Original URL: https://cjcamfu72.ukit.me
Prompt: "Design a database schema for a uKit-like website builder using MySQL."
Generated: DETERMINISTIC_03145e2605c65543
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a uKit-like website builder

-- Table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username for login
    email VARCHAR(100) NOT NULL UNIQUE,     -- Email address
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store websites created by users
CREATE TABLE websites (
    website_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each website
    user_id INT NOT NULL,                      -- Foreign key linking to the user who owns the website
    name VARCHAR(100) NOT NULL,                -- Name of the website
    domain VARCHAR(255) UNIQUE,                -- Custom domain for the website
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of website creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store pages within a website
CREATE TABLE pages (
    page_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each page
    website_id INT NOT NULL,                -- Foreign key linking to the website
    title VARCHAR(100) NOT NULL,            -- Title of the page
    slug VARCHAR(255) NOT NULL,             -- URL-friendly identifier for the page
    content TEXT,                           -- HTML content of the page
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of page creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (website_id) REFERENCES websites(website_id) ON DELETE CASCADE -- Cascade delete if website is deleted
);

-- Table to store templates for websites/pages
CREATE TABLE templates (
    template_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each template
    name VARCHAR(100) NOT NULL UNIQUE,          -- Name of the template
    description TEXT,                           -- Description of the template
    html_content TEXT NOT NULL,                 -- HTML structure of the template
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of template creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store website settings
CREATE TABLE website_settings (
    setting_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each setting
    website_id INT NOT NULL,                   -- Foreign key linking to the website
    key VARCHAR(100) NOT NULL,                 -- Setting key (e.g., "theme", "analytics_id")
    value TEXT NOT NULL,                       -- Setting value
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of setting creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (website_id) REFERENCES websites(website_id) ON DELETE CASCADE -- Cascade delete if website is deleted
);

-- Table to store media files uploaded by users
CREATE TABLE media (
    media_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media file
    user_id INT NOT NULL,                    -- Foreign key linking to the user who uploaded the file
    website_id INT,                          -- Optional foreign key linking to the website (if media is website-specific)
    file_name VARCHAR(255) NOT NULL,         -- Name of the file
    file_path VARCHAR(255) NOT NULL,         -- Path to the file on the server
    file_type VARCHAR(50) NOT NULL,          -- Type of the file (e.g., "image/png", "video/mp4")
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of file upload
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (website_id) REFERENCES websites(website_id) ON DELETE SET NULL -- Set to NULL if website is deleted
);

-- Table to store user roles and permissions
CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each role
    name VARCHAR(50) NOT NULL UNIQUE,       -- Name of the role (e.g., "admin", "editor")
    description TEXT                        -- Description of the role
);

-- Table to assign roles to users
CREATE TABLE user_roles (
    user_id INT NOT NULL,                   -- Foreign key linking to the user
    role_id INT NOT NULL,                   -- Foreign key linking to the role
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of role assignment
    PRIMARY KEY (user_id, role_id),         -- Composite primary key to prevent duplicate assignments
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE -- Cascade delete if role is deleted
);

-- Table to store analytics data for websites
CREATE TABLE analytics (
    analytics_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each analytics record
    website_id INT NOT NULL,                     -- Foreign key linking to the website
    page_id INT,                                 -- Optional foreign key linking to the page (if page-specific analytics)
    visit_count INT DEFAULT 0,                   -- Number of visits
    last_visited TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the last visit
    FOREIGN KEY (website_id) REFERENCES websites(website_id) ON DELETE CASCADE, -- Cascade delete if website is deleted
    FOREIGN KEY (page_id) REFERENCES pages(page_id) ON DELETE SET NULL -- Set to NULL if page is deleted
);
```
