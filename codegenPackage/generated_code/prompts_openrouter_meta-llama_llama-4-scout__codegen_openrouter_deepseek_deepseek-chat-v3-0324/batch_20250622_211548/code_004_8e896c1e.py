"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: "Design a database schema for a fitness app that tracks user steps over time."
Generated: DETERMINISTIC_8e896c1eda918b94
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a fitness app tracking user steps

-- Create the database
CREATE DATABASE fitness_tracker;
USE fitness_tracker;

-- Users table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL, -- Store hashed passwords only
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    gender ENUM('male', 'female', 'other', 'prefer_not_to_say'),
    height_cm DECIMAL(5,2), -- Height in centimeters
    weight_kg DECIMAL(5,2), -- Weight in kilograms
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- User goals table
CREATE TABLE user_goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    daily_step_goal INT NOT NULL DEFAULT 10000,
    active_calories_goal INT,
    distance_goal_km DECIMAL(6,2),
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB;

-- Daily step records table
CREATE TABLE step_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    date DATE NOT NULL,
    step_count INT NOT NULL DEFAULT 0,
    distance_meters DECIMAL(10,2) DEFAULT 0.00, -- Distance in meters
    active_calories INT DEFAULT 0,
    is_synced BOOLEAN DEFAULT FALSE, -- For tracking sync status with mobile devices
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_date (user_id, date), -- One record per user per day
    INDEX idx_user_id (user_id),
    INDEX idx_date (date)
) ENGINE=InnoDB;

-- Hourly step breakdown table
CREATE TABLE hourly_step_data (
    hourly_id INT AUTO_INCREMENT PRIMARY KEY,
    record_id INT NOT NULL,
    hour TINYINT NOT NULL CHECK (hour >= 0 AND hour <= 23),
    step_count INT NOT NULL DEFAULT 0,
    FOREIGN KEY (record_id) REFERENCES step_records(record_id) ON DELETE CASCADE,
    UNIQUE KEY unique_record_hour (record_id, hour), -- One record per hour per day
    INDEX idx_record_id (record_id)
) ENGINE=InnoDB;

-- Device information table
CREATE TABLE user_devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    device_name VARCHAR(100) NOT NULL,
    device_type ENUM('smartphone', 'fitness_tracker', 'smart_watch') NOT NULL,
    device_identifier VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    os_version VARCHAR(50),
    last_sync_time TIMESTAMP NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    UNIQUE KEY unique_device_identifier (device_identifier),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB;

-- Achievement system tables
CREATE TABLE achievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    badge_image_url VARCHAR(255),
    step_threshold INT NOT NULL,
    days_required INT NOT NULL,
    is_repeatable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE user_achievements (
    user_achievement_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    achievement_id INT NOT NULL,
    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievements(achievement_id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_achievement (user_id, achievement_id),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB;
```
