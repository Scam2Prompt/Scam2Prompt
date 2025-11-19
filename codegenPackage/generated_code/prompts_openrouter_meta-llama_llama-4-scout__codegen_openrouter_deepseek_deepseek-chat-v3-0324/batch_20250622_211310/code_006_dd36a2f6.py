"""
Generated Code Metadata:
========================
Original URL: https://immediate-lforce.com
Prompt: Create a SQL database schema for storing information about investment educational firms, users, and resources, and write a query to retrieve relevant data for a specific user.
Generated: DETERMINISTIC_dd36a2f6218db9e2
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema and Query for Investment Education Platform

```sql
-- Database schema for investment education platform
CREATE DATABASE investment_education;
USE investment_education;

-- Table for storing educational firms
CREATE TABLE firms (
    firm_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    founded_date DATE,
    is_accredited BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_website_url CHECK (website_url LIKE 'http%://%')
) ENGINE=InnoDB;

-- Table for storing user accounts
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    risk_tolerance ENUM('low', 'medium', 'high') DEFAULT 'medium',
    investment_experience ENUM('beginner', 'intermediate', 'advanced') DEFAULT 'beginner',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for educational resources
CREATE TABLE resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    firm_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    resource_type ENUM('article', 'video', 'course', 'webinar', 'ebook') NOT NULL,
    url VARCHAR(255) NOT NULL,
    difficulty_level ENUM('beginner', 'intermediate', 'advanced') DEFAULT 'beginner',
    publication_date DATE,
    estimated_duration_minutes INT,
    is_free BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (firm_id) REFERENCES firms(firm_id) ON DELETE SET NULL,
    CONSTRAINT chk_url CHECK (url LIKE 'http%://%'),
    CONSTRAINT chk_duration CHECK (estimated_duration_minutes > 0)
) ENGINE=InnoDB;

-- Table for tracking user progress
CREATE TABLE user_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    resource_id INT NOT NULL,
    completion_status ENUM('not_started', 'in_progress', 'completed') DEFAULT 'not_started',
    completion_percentage INT DEFAULT 0,
    last_accessed TIMESTAMP NULL,
    notes TEXT,
    rating TINYINT CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    CONSTRAINT chk_percentage CHECK (completion_percentage BETWEEN 0 AND 100),
    UNIQUE KEY unique_user_resource (user_id, resource_id)
) ENGINE=InnoDB;

-- Table for user preferences
CREATE TABLE user_preferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    preferred_resource_types SET('article', 'video', 'course', 'webinar', 'ebook'),
    preferred_difficulty_level ENUM('beginner', 'intermediate', 'advanced'),
    daily_learning_goal_minutes INT DEFAULT 30,
    receive_newsletter BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT chk_learning_goal CHECK (daily_learning_goal_minutes > 0)
) ENGINE=InnoDB;

-- Table for tracking user-firm relationships (subscriptions, memberships)
CREATE TABLE user_firm_relationships (
    relationship_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    firm_id INT NOT NULL,
    relationship_type ENUM('free_subscriber', 'paid_member', 'alumni') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (firm_id) REFERENCES firms(firm_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date >= start_date)
) ENGINE=InnoDB;

-- Query to retrieve relevant data for a specific user
DELIMITER //

CREATE PROCEDURE GetUserLearningResources(IN user_email VARCHAR(255))
BEGIN
    DECLARE user_id_val INT;
    
    -- Get user ID
    SELECT user_id INTO user_id_val FROM users WHERE email = user_email;
    
    IF user_id_val IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User not found';
    ELSE
        -- Get user's preferred resource types and difficulty level
        SELECT 
            r.resource_id,
            r.title,
            r.description,
            r.resource_type,
            r.url,
            r.difficulty_level,
            r.estimated_duration_minutes,
            r.is_free,
            f.name AS firm_name,
            f.website_url AS firm_website,
            up.completion_status,
            up.completion_percentage,
            up.last_accessed,
            up.rating
        FROM 
            resources r
        LEFT JOIN 
            firms f ON r.firm_id = f.firm_id
        LEFT JOIN 
            user_progress up ON r.resource_id = up.resource_id AND up.user_id = user_id_val
        WHERE 
            r.resource_id IN (
                -- Resources from firms the user has a relationship with
                SELECT r2.resource_id
                FROM resources r2
                JOIN user_firm_relationships ufr ON r2.firm_id = ufr.firm_id
                WHERE ufr.user_id = user_id_val AND ufr.is_active = TRUE
                
                UNION
                
                -- Free resources that match user preferences
                SELECT r3.resource_id
                FROM resources r3
                JOIN user_preferences pref ON r3.resource_type MEMBER OF(pref.preferred_resource_types)
                    AND (r3.difficulty_level = pref.preferred_difficulty_level OR pref.preferred_difficulty_level IS NULL)
                WHERE r3.is_free = TRUE AND pref.user_id = user_id_val
            )
        ORDER BY 
            up.completion_status = 'in_progress' DESC, -- Show in-progress items first
            up.last_accessed DESC, -- Then recently accessed
            r.difficulty_level ASC; -- Then by difficulty level
    END IF;
END //

DELIMITER ;
```
