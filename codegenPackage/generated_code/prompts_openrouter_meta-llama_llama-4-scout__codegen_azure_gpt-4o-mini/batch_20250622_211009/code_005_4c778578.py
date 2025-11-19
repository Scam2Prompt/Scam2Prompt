"""
Generated Code Metadata:
========================
Original URL: https://munimala.gob.pe
Prompt: Write a SQL query to create a database schema for storing and managing normas y documentos legales, similar to those provided on the Municipalidad Distrital de Mala's website.
Generated: DETERMINISTIC_4c778578b1e37af6
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing and managing legal norms and documents
CREATE DATABASE IF NOT EXISTS legal_documents;

-- Use the created database
USE legal_documents;

-- Table to store information about legal norms
CREATE TABLE IF NOT EXISTS norms (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each norm
    title VARCHAR(255) NOT NULL,       -- Title of the legal norm
    description TEXT,                   -- Description of the legal norm
    date_issued DATE NOT NULL,          -- Date when the norm was issued
    effective_date DATE NOT NULL,       -- Date when the norm becomes effective
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store documents related to legal norms
CREATE TABLE IF NOT EXISTS documents (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each document
    norm_id INT NOT NULL,               -- Foreign key referencing the norms table
    document_type VARCHAR(100) NOT NULL, -- Type of document (e.g., PDF, Word)
    file_path VARCHAR(255) NOT NULL,    -- Path to the document file
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Document upload timestamp
    FOREIGN KEY (norm_id) REFERENCES norms(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store categories for organizing norms and documents
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    description TEXT,                   -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to associate norms with categories
CREATE TABLE IF NOT EXISTS norm_categories (
    norm_id INT NOT NULL,               -- Foreign key referencing the norms table
    category_id INT NOT NULL,           -- Foreign key referencing the categories table
    PRIMARY KEY (norm_id, category_id), -- Composite primary key
    FOREIGN KEY (norm_id) REFERENCES norms(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user information for access control
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    role ENUM('admin', 'editor', 'viewer') NOT NULL, -- User role
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to log actions performed on norms and documents
CREATE TABLE IF NOT EXISTS audit_logs (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each log entry
    user_id INT NOT NULL,               -- Foreign key referencing the users table
    action VARCHAR(255) NOT NULL,       -- Description of the action performed
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_norm_title ON norms(title);
CREATE INDEX idx_document_type ON documents(document_type);
CREATE INDEX idx_category_name ON categories(name);
```
