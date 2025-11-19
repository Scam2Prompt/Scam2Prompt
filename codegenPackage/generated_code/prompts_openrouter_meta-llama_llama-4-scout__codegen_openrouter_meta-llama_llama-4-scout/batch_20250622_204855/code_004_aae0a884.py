"""
Generated Code Metadata:
========================
Original URL: https://annonceintimex.com
Prompt: "Design a database schema for storing user profiles, preferences, and matches on an erotic dating site, focusing on scalability and data protection."
Generated: DETERMINISTIC_aae0a8845e88f9b0
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema: Erotic Dating Site**
=====================================

```sql
-- Create a database for the erotic dating site
CREATE DATABASE erotic_dating_site;

-- Use the database
USE erotic_dating_site;

-- Create a table for user profiles
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  salt VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for user profile information
CREATE TABLE user_profiles (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  username VARCHAR(255) NOT NULL,
  age TINYINT NOT NULL,
  location VARCHAR(255) NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for user preferences
CREATE TABLE user_preferences (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  orientation ENUM('heterosexual', 'homosexual', 'bisexual', 'unspecified') NOT NULL,
  interested_in ENUM('male', 'female', 'both') NOT NULL,
  min_age TINYINT NOT NULL,
  max_age TINYINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for matches
CREATE TABLE matches (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  matched_user_id BIGINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (matched_user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, matched_user_id)
);

-- Create a table for user profile images
CREATE TABLE user_profile_images (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for user verification
CREATE TABLE user_verification (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  verification_status ENUM('pending', 'verified', 'rejected') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id);
CREATE INDEX idx_matches_user_id ON matches(user_id);
CREATE INDEX idx_matches_matched_user_id ON matches(matched_user_id);
CREATE INDEX idx_user_profile_images_user_id ON user_profile_images(user_id);
```

**Stored Procedures**
--------------------

```sql
-- Create a stored procedure for creating a new user
DELIMITER //
CREATE PROCEDURE create_user(
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255),
  IN p_salt VARCHAR(255)
)
BEGIN
  INSERT INTO users (email, password_hash, salt)
  VALUES (p_email, p_password_hash, p_salt);
END//
DELIMITER ;

-- Create a stored procedure for updating a user's profile
DELIMITER //
CREATE PROCEDURE update_user_profile(
  IN p_user_id BIGINT,
  IN p_username VARCHAR(255),
  IN p_age TINYINT,
  IN p_location VARCHAR(255),
  IN p_bio TEXT
)
BEGIN
  UPDATE user_profiles
  SET username = p_username,
      age = p_age,
      location = p_location,
      bio = p_bio
  WHERE user_id = p_user_id;
END//
DELIMITER ;

-- Create a stored procedure for creating a new match
DELIMITER //
CREATE PROCEDURE create_match(
  IN p_user_id BIGINT,
  IN p_matched_user_id BIGINT
)
BEGIN
  INSERT INTO matches (user_id, matched_user_id)
  VALUES (p_user_id, p_matched_user_id);
END//
DELIMITER ;
```

**Triggers**
------------

```sql
-- Create a trigger for updating the updated_at timestamp
DELIMITER //
CREATE TRIGGER update_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Create a trigger for updating the updated_at timestamp
DELIMITER //
CREATE TRIGGER update_user_profile_updated_at
BEFORE UPDATE ON user_profiles
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;
```
