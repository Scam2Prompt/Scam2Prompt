"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Design a database schema for storing user information and relationships on a discreet dating platform, prioritizing data security and anonymity.
Generated: DETERMINISTIC_67d80a8b751e6839
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the discreet dating platform
CREATE DATABASE discreet_dating;

-- Use the discreet_dating database
USE discreet_dating;

-- Create a table for users
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `salt` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);

-- Create a table for user profiles
CREATE TABLE user_profiles (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `age` TINYINT,
  `gender` ENUM('male', 'female', 'non-binary', 'prefer not to say'),
  `interested_in` ENUM('male', 'female', 'non-binary', 'all'),
  `bio` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create a table for user relationships
CREATE TABLE user_relationships (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `matched_user_id` INT NOT NULL,
  `status` ENUM('pending', 'accepted', 'declined', 'blocked'),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`matched_user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  UNIQUE KEY `user_matched_user` (`user_id`, `matched_user_id`)
);

-- Create a table for user preferences
CREATE TABLE user_preferences (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `distance_max` INT,
  `age_min` TINYINT,
  `age_max` TINYINT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create a table for user blocks
CREATE TABLE user_blocks (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blocked_user_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`blocked_user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  UNIQUE KEY `user_blocked_user` (`user_id`, `blocked_user_id`)
);

-- Create a table for user reporting
CREATE TABLE user_reports (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `reported_user_id` INT NOT NULL,
  `reason` ENUM('inappropriate_content', 'harassment', 'spam'),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`reported_user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create indexes on frequently queried columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX idx_user_relationships_user_id ON user_relationships(user_id);
CREATE INDEX idx_user_preferences_user_id ON user_preferences(user_id);
CREATE INDEX idx_user_blocks_user_id ON user_blocks(user_id);
CREATE INDEX idx_user_reports_user_id ON user_reports(user_id);
```

```sql
-- Example stored procedure to create a new user
DELIMITER //
CREATE PROCEDURE create_user(
  IN p_email VARCHAR(255),
  IN p_password VARCHAR(255)
)
BEGIN
  DECLARE salt VARCHAR(255);
  SET salt = UNHEX(REPLACE(UUID(), '-', ''));
  INSERT INTO users (email, password_hash, salt)
  VALUES (p_email, UNHEX(SHA2(CONCAT(p_password, salt), 256)), salt);
END//
DELIMITER ;

-- Example stored procedure to create a new user profile
DELIMITER //
CREATE PROCEDURE create_user_profile(
  IN p_user_id INT,
  IN p_age TINYINT,
  IN p_gender ENUM('male', 'female', 'non-binary', 'prefer not to say'),
  IN p_interested_in ENUM('male', 'female', 'non-binary', 'all'),
  IN p_bio TEXT
)
BEGIN
  INSERT INTO user_profiles (user_id, age, gender, interested_in, bio)
  VALUES (p_user_id, p_age, p_gender, p_interested_in, p_bio);
END//
DELIMITER ;
```
