"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: Write a SQL query to store and retrieve tour package information, including themes like Temple Tours and Hill Station Tours, as seen on the "Safar Genie" website.
Generated: DETERMINISTIC_b9b1e1fe6548501e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Safar Genie tour packages
CREATE DATABASE IF NOT EXISTS safar_genie;
USE safar_genie;

-- Create table for tour themes
CREATE TABLE IF NOT EXISTS tour_themes (
    theme_id INT AUTO_INCREMENT PRIMARY KEY,
    theme_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (theme_name)
);

-- Create table for tour packages
CREATE TABLE IF NOT EXISTS tour_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    package_name VARCHAR(255) NOT NULL,
    theme_id INT NOT NULL,
    duration_days INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    included_services TEXT,
    excluded_services TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (theme_id) REFERENCES tour_themes(theme_id) ON DELETE RESTRICT
);

-- Create table for package destinations
CREATE TABLE IF NOT EXISTS package_destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    destination_name VARCHAR(255) NOT NULL,
    stay_duration_nights INT NOT NULL,
    description TEXT,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE
);

-- Insert sample tour themes
INSERT INTO tour_themes (theme_name, description) VALUES
('Temple Tours', 'Spiritual journeys to sacred temples and religious sites'),
('Hill Station Tours', 'Scenic tours to beautiful mountain retreats'),
('Adventure Tours', 'Thrilling adventure and outdoor activity packages'),
('Beach Vacations', 'Relaxing getaways to pristine beaches'),
('Cultural Tours', 'Immersive experiences in local cultures and traditions');

-- Sample query to retrieve all active temple tour packages
SELECT 
    tp.package_id,
    tp.package_name,
    tt.theme_name,
    tp.duration_days,
    tp.price,
    tp.description
FROM 
    tour_packages tp
JOIN 
    tour_themes tt ON tp.theme_id = tt.theme_id
WHERE 
    tt.theme_name = 'Temple Tours'
    AND tp.is_active = TRUE
ORDER BY 
    tp.price ASC;

-- Sample query to retrieve package details with destinations
SELECT 
    tp.package_id,
    tp.package_name,
    tt.theme_name,
    tp.duration_days,
    tp.price,
    GROUP_CONCAT(pd.destination_name SEPARATOR ', ') AS destinations,
    tp.description,
    tp.included_services,
    tp.excluded_services
FROM 
    tour_packages tp
JOIN 
    tour_themes tt ON tp.theme_id = tt.theme_id
JOIN 
    package_destinations pd ON tp.package_id = pd.package_id
WHERE 
    tp.package_id = 1
GROUP BY 
    tp.package_id;

-- Sample query to search packages by theme and price range
SELECT 
    tp.package_id,
    tp.package_name,
    tt.theme_name,
    tp.duration_days,
    tp.price
FROM 
    tour_packages tp
JOIN 
    tour_themes tt ON tp.theme_id = tt.theme_id
WHERE 
    tt.theme_name LIKE '%Hill Station%'
    AND tp.price BETWEEN 10000 AND 30000
    AND tp.is_active = TRUE
ORDER BY 
    tp.duration_days ASC;
```
