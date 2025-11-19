"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Design a database schema to store information about Playland Kenya’s activities, pricing, and operating hours, ensuring it includes fields for activity names, costs, and time slots.
Generated: DETERMINISTIC_2a4638ea75565392
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Playland Kenya's activities, pricing, and operating hours

-- Create the database
CREATE DATABASE IF NOT EXISTS playland_kenya;
USE playland_kenya;

-- Activities table to store information about different activities
CREATE TABLE IF NOT EXISTS activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    minimum_age INT,
    maximum_participants INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_min_age CHECK (minimum_age >= 0),
    CONSTRAINT chk_max_participants CHECK (maximum_participants > 0)
) ENGINE=InnoDB;

-- Pricing table to store different pricing options for activities
CREATE TABLE IF NOT EXISTS pricing (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_id INT NOT NULL,
    price_type ENUM('child', 'adult', 'senior', 'group', 'special') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'KES',
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount CHECK (amount > 0),
    CONSTRAINT chk_dates CHECK (valid_to IS NULL OR valid_to >= valid_from)
) ENGINE=InnoDB;

-- Operating hours table for the entire facility
CREATE TABLE IF NOT EXISTS operating_hours (
    day_id INT AUTO_INCREMENT PRIMARY KEY,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    opening_time TIME NOT NULL,
    closing_time TIME NOT NULL,
    is_holiday_schedule BOOLEAN DEFAULT FALSE,
    special_notes VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_times CHECK (closing_time > opening_time),
    UNIQUE KEY unique_weekday (day_of_week, is_holiday_schedule)
) ENGINE=InnoDB;

-- Activity time slots table for specific activity scheduling
CREATE TABLE IF NOT EXISTS activity_time_slots (
    slot_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_id INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_capacity INT NOT NULL,
    is_recurring BOOLEAN DEFAULT FALSE,
    recurrence_pattern VARCHAR(50),
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Any'),
    valid_from DATE NOT NULL,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    CONSTRAINT chk_slot_times CHECK (end_time > start_time),
    CONSTRAINT chk_capacity CHECK (max_capacity > 0),
    CONSTRAINT chk_slot_dates CHECK (valid_to IS NULL OR valid_to >= valid_from)
) ENGINE=InnoDB;

-- Holidays and special closures table
CREATE TABLE IF NOT EXISTS special_closures (
    closure_id INT AUTO_INCREMENT PRIMARY KEY,
    closure_date DATE NOT NULL,
    closure_reason VARCHAR(255) NOT NULL,
    is_full_day BOOLEAN DEFAULT TRUE,
    partial_opening_time TIME,
    partial_closing_time TIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_partial_times CHECK (
        (is_full_day = TRUE AND partial_opening_time IS NULL AND partial_closing_time IS NULL) OR
        (is_full_day = FALSE AND partial_opening_time IS NOT NULL AND partial_closing_time IS NOT NULL AND partial_closing_time > partial_opening_time)
    ),
    UNIQUE KEY unique_closure_date (closure_date)
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_activity_name ON activities(name);
CREATE INDEX idx_price_activity ON pricing(activity_id);
CREATE INDEX idx_price_current ON pricing(is_current);
CREATE INDEX idx_slot_activity ON activity_time_slots(activity_id);
CREATE INDEX idx_slot_times ON activity_time_slots(start_time, end_time);
```
