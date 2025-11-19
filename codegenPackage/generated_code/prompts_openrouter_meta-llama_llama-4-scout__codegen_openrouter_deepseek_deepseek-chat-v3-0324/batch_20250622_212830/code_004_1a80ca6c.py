"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Write a SQL query to store and retrieve information about different types of stones and pebbles, including their certification and quality.
Generated: DETERMINISTIC_1a80ca6c22ff88e3
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for stone and pebble information
CREATE DATABASE IF NOT EXISTS stone_inventory;
USE stone_inventory;

-- Create table for stone types
CREATE TABLE IF NOT EXISTS stone_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (type_name)
) ENGINE=InnoDB;

-- Create table for certification standards
CREATE TABLE IF NOT EXISTS certifications (
    cert_id INT AUTO_INCREMENT PRIMARY KEY,
    cert_name VARCHAR(100) NOT NULL,
    issuing_authority VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (cert_name, issuing_authority)
) ENGINE=InnoDB;

-- Create table for quality grades
CREATE TABLE IF NOT EXISTS quality_grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    grade_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (grade_name)
) ENGINE=InnoDB;

-- Create main inventory table
CREATE TABLE IF NOT EXISTS stones (
    stone_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT NOT NULL,
    weight DECIMAL(10,2) NOT NULL,
    dimensions VARCHAR(50),
    color VARCHAR(50),
    origin VARCHAR(100),
    cert_id INT,
    grade_id INT,
    price DECIMAL(12,2),
    quantity INT DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES stone_types(type_id),
    FOREIGN KEY (cert_id) REFERENCES certifications(cert_id),
    FOREIGN KEY (grade_id) REFERENCES quality_grades(grade_id),
    CHECK (weight > 0),
    CHECK (quantity >= 0)
) ENGINE=InnoDB;

-- Insert sample stone types
INSERT INTO stone_types (type_name, description) VALUES
('Granite', 'A coarse-grained igneous rock composed mostly of quartz and feldspar'),
('Marble', 'A metamorphic rock composed of recrystallized carbonate minerals'),
('Quartz', 'A hard, crystalline mineral composed of silicon and oxygen atoms');

-- Insert sample certifications
INSERT INTO certifications (cert_name, issuing_authority, description) VALUES
('Gemological Institute', 'GIA', 'Standard certification for gemstones'),
('Natural Stone Council', 'NSC 373', 'Sustainability standard for natural stone'),
('ISO 9001', 'International Standards Organization', 'Quality management certification');

-- Insert sample quality grades
INSERT INTO quality_grades (grade_name, description) VALUES
('AAA', 'Highest quality with excellent characteristics'),
('AA', 'High quality with minor imperfections'),
('A', 'Good quality with noticeable imperfections');

-- Query to retrieve stone information with certification and quality details
SELECT 
    s.stone_id,
    st.type_name,
    s.weight,
    s.dimensions,
    s.color,
    s.origin,
    c.cert_name,
    c.issuing_authority,
    qg.grade_name,
    s.price,
    s.quantity,
    s.notes
FROM 
    stones s
JOIN 
    stone_types st ON s.type_id = st.type_id
LEFT JOIN 
    certifications c ON s.cert_id = c.cert_id
LEFT JOIN 
    quality_grades qg ON s.grade_id = qg.grade_id
ORDER BY 
    s.stone_id;
```
