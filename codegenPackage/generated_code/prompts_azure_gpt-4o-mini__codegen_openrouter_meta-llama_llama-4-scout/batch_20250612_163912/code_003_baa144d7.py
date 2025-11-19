"""
Generated Code Metadata:
========================
Original URL: https://www.eharmony.co.uk
Prompt: Create a sample SQL database schema for storing user profiles and compatibility scores for a dating platform inspired by eharmony.
Generated: DETERMINISTIC_baa144d7b5886548
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for dating platform
CREATE DATABASE dating_platform;

-- Use the database
USE dating_platform;

-- Create table for user profiles
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  birth_date DATE NOT NULL,
  location VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user profile details
CREATE TABLE user_profiles (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  gender ENUM('male', 'female', 'other') NOT NULL,
  orientation ENUM('heterosexual', 'homosexual', 'bisexual', 'other') NOT NULL,
  height INT,
  body_type ENUM('slim', 'average', 'athletic', 'curvy', 'other'),
  ethnicity ENUM('asian', 'black', 'caucasian', 'hispanic', 'indian', 'middle eastern', 'other'),
  education_level ENUM('high school', 'some college', 'bachelors', 'masters', 'phd', 'other'),
  interests TEXT,
  about_me TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for compatibility scores
CREATE TABLE compatibility_scores (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  matched_user_id INT NOT NULL,
  score DECIMAL(3, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (matched_user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, matched_user_id)
);

-- Create table for user preferences
CREATE TABLE user_preferences (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  min_age INT,
  max_age INT,
  min_height INT,
  max_height INT,
  preferred_gender ENUM('male', 'female', 'other'),
  preferred_orientation ENUM('heterosexual', 'homosexual', 'bisexual', 'other'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX idx_compatibility_scores_user_id ON compatibility_scores(user_id);
CREATE INDEX idx_compatibility_scores_matched_user_id ON compatibility_scores(matched_user_id);
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id);
```
