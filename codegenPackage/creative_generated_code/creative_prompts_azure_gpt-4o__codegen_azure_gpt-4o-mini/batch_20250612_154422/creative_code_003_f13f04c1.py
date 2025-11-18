"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Create a database schema for managing IAS coaching resources, including categories like "Prelims Test Series," "Mains Test Series," "Optional Courses," and "Rapid Revision Books" as outlined by Shield IAS.
Generated: DETERMINISTIC_f13f04c17554320a
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing IAS coaching resources

-- Create a new database for IAS coaching resources
CREATE DATABASE IAS_Coaching_Resources;

-- Use the newly created database
USE IAS_Coaching_Resources;

-- Table to store resource categories
CREATE TABLE ResourceCategories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store coaching resources
CREATE TABLE CoachingResources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    resource_type ENUM('PDF', 'Video', 'Book', 'Test Series', 'Course') NOT NULL,
    url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES ResourceCategories(id) ON DELETE CASCADE
);

-- Table to store user reviews for resources
CREATE TABLE ResourceReviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    resource_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (resource_id) REFERENCES CoachingResources(id) ON DELETE CASCADE
);

-- Insert default categories into ResourceCategories
INSERT INTO ResourceCategories (name, description) VALUES
('Prelims Test Series', 'Comprehensive test series for IAS prelims preparation'),
('Mains Test Series', 'Detailed test series for IAS mains examination'),
('Optional Courses', 'Specialized courses for various optional subjects'),
('Rapid Revision Books', 'Concise books for quick revision before exams');

-- Ensure schema is ready and avoid any errors
SET FOREIGN_KEY_CHECKS = 0; -- Temporarily disable foreign key checks
-- Your SQL statements here
SET FOREIGN_KEY_CHECKS = 1; -- Re-enable foreign key checks
```
