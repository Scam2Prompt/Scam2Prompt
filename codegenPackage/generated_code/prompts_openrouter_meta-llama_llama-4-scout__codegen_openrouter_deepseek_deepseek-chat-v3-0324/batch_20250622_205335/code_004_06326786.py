"""
Generated Code Metadata:
========================
Original URL: https://graylinegeneva.com
Prompt: Create a sample database schema for storing information about Gray Line Geneva's tours, including details such as tour name, location, duration, and price.
Generated: DETERMINISTIC_06326786a8574502
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Gray Line Geneva Tours

-- Create the database
CREATE DATABASE IF NOT EXISTS gray_line_geneva_tours;
USE gray_line_geneva_tours;

-- Table for storing tour categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing tour locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL DEFAULT 'Switzerland',
    coordinates POINT SRID 4326,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing tours
CREATE TABLE IF NOT EXISTS tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'CHF',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    min_participants INT DEFAULT 1,
    max_participants INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Junction table for tour locations (many-to-many relationship)
CREATE TABLE IF NOT EXISTS tour_locations (
    tour_id INT NOT NULL,
    location_id INT NOT NULL,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    visit_order INT NOT NULL DEFAULT 1,
    PRIMARY KEY (tour_id, location_id),
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing tour schedules
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    is_recurring BOOLEAN NOT NULL DEFAULT TRUE,
    valid_from DATE,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing tour images
CREATE TABLE IF NOT EXISTS tour_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255),
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    display_order INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing additional tour options
CREATE TABLE IF NOT EXISTS tour_options (
    option_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    additional_price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_tours_category ON tours(category_id);
CREATE INDEX idx_tour_locations_tour ON tour_locations(tour_id);
CREATE INDEX idx_tour_locations_location ON tour_locations(location_id);
CREATE INDEX idx_schedules_tour ON schedules(tour_id);
CREATE INDEX idx_tour_images_tour ON tour_images(tour_id);
CREATE INDEX idx_tour_options_tour ON tour_options(tour_id);
```
