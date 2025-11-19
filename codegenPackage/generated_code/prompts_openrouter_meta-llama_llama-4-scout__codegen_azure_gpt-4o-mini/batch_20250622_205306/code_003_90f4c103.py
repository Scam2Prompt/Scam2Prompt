"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: "Design a basic database schema for a neon animal collector app using MySQL."
Generated: DETERMINISTIC_90f4c103eb600ab6
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Neon Animal Collector App

-- Create a database for the app
CREATE DATABASE neon_animal_collector;

-- Use the created database
USE neon_animal_collector;

-- Table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for each user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store animal information
CREATE TABLE animals (
    animal_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each animal
    name VARCHAR(50) NOT NULL,                 -- Name of the animal
    species VARCHAR(50) NOT NULL,              -- Species of the animal
    rarity ENUM('Common', 'Uncommon', 'Rare', 'Legendary') NOT NULL,  -- Rarity level of the animal
    description TEXT,                          -- Description of the animal
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of animal entry
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store user collections
CREATE TABLE user_collections (
    collection_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each collection
    user_id INT NOT NULL,                           -- Foreign key referencing users
    animal_id INT NOT NULL,                         -- Foreign key referencing animals
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the animal was collected
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (animal_id) REFERENCES animals(animal_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store user achievements
CREATE TABLE achievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each achievement
    user_id INT NOT NULL,                            -- Foreign key referencing users
    title VARCHAR(100) NOT NULL,                     -- Title of the achievement
    description TEXT,                                -- Description of the achievement
    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the achievement was earned
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store user preferences/settings
CREATE TABLE user_settings (
    setting_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each setting
    user_id INT NOT NULL,                        -- Foreign key referencing users
    setting_key VARCHAR(100) NOT NULL,          -- Key for the setting
    setting_value VARCHAR(255) NOT NULL,        -- Value for the setting
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_animal_species ON animals(species);
CREATE INDEX idx_user_collection ON user_collections(user_id);
CREATE INDEX idx_user_achievement ON achievements(user_id);
CREATE INDEX idx_user_setting ON user_settings(user_id);
```
