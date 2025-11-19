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

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Websites;
DROP TABLE IF EXISTS Pages;
DROP TABLE IF EXISTS Elements;
DROP TABLE IF EXISTS Templates;
DROP TABLE IF EXISTS Styles;

-- Table to store user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for user communication
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store website information
CREATE TABLE Websites (
    website_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each website
    user_id INT NOT NULL,                        -- Foreign key referencing Users
    title VARCHAR(100) NOT NULL,                 -- Title of the website
    domain VARCHAR(100) NOT NULL UNIQUE,         -- Unique domain for the website
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of website creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE  -- Cascade delete on user removal
);

-- Table to store pages within each website
CREATE TABLE Pages (
    page_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each page
    website_id INT NOT NULL,                     -- Foreign key referencing Websites
    title VARCHAR(100) NOT NULL,                 -- Title of the page
    slug VARCHAR(100) NOT NULL UNIQUE,           -- URL-friendly identifier for the page
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of page creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (website_id) REFERENCES Websites(website_id) ON DELETE CASCADE  -- Cascade delete on website removal
);

-- Table to store elements on each page (e.g., text, images, buttons)
CREATE TABLE Elements (
    element_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each element
    page_id INT NOT NULL,                        -- Foreign key referencing Pages
    type ENUM('text', 'image', 'button', 'video') NOT NULL,  -- Type of the element
    content TEXT NOT NULL,                       -- Content of the element
    position INT NOT NULL,                       -- Position of the element on the page
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of element creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (page_id) REFERENCES Pages(page_id) ON DELETE CASCADE  -- Cascade delete on page removal
);

-- Table to store templates for websites
CREATE TABLE Templates (
    template_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each template
    name VARCHAR(100) NOT NULL UNIQUE,           -- Name of the template
    description TEXT,                             -- Description of the template
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of template creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store styles associated with elements
CREATE TABLE Styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each style
    element_id INT NOT NULL,                      -- Foreign key referencing Elements
    property VARCHAR(50) NOT NULL,                -- CSS property (e.g., 'color', 'font-size')
    value VARCHAR(255) NOT NULL,                  -- Value for the CSS property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of style creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (element_id) REFERENCES Elements(element_id) ON DELETE CASCADE  -- Cascade delete on element removal
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_website_user ON Websites(user_id);
CREATE INDEX idx_page_website ON Pages(website_id);
CREATE INDEX idx_element_page ON Elements(page_id);
CREATE INDEX idx_style_element ON Styles(element_id);
```
