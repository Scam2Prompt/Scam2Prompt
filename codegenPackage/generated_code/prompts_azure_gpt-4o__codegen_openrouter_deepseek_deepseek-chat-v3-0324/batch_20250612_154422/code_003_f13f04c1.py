"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a database schema for managing IAS coaching resources, including categories like "Prelims Test Series," "Mains Test Series," "Optional Courses," and "Rapid Revision Books" as outlined by Shield IAS.
Generated: DETERMINISTIC_f13f04c17554320a
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Shield IAS coaching resources management

-- Create the database
CREATE DATABASE IF NOT EXISTS shield_ias;
USE shield_ias;

-- Table for resource categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_category_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for resources
CREATE TABLE IF NOT EXISTS resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration_weeks INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    INDEX idx_category (category_id),
    INDEX idx_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for resource materials (books, PDFs, videos, etc.)
CREATE TABLE IF NOT EXISTS resource_materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_id INT NOT NULL,
    material_type ENUM('book', 'pdf', 'video', 'test_paper', 'other') NOT NULL,
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(512),
    external_url VARCHAR(512),
    is_free BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    INDEX idx_resource (resource_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for batches/schedules
CREATE TABLE IF NOT EXISTS batches (
    batch_id INT AUTO_INCREMENT PRIMARY KEY,
    resource_id INT NOT NULL,
    batch_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_students INT,
    current_students INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    INDEX idx_resource (resource_id),
    INDEX idx_dates (start_date, end_date),
    CHECK (end_date > start_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert initial categories as specified
INSERT INTO categories (name, description) VALUES
('Prelims Test Series', 'Comprehensive test series for IAS Prelims examination'),
('Mains Test Series', 'Detailed test series for IAS Mains examination'),
('Optional Courses', 'Specialized courses for optional subjects'),
('Rapid Revision Books', 'Concise books for quick revision before exams')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```
