"""
Generated Code Metadata:
========================
Original URL: https://www.archivesecureprotection.com
Prompt: Create a database schema for storing and managing user safety information, including verification status and safety features for online dating platforms.
Generated: DETERMINISTIC_706870db64861d4c
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing and managing user safety information

-- Create a database
CREATE DATABASE user_safety;

-- Use the database
USE user_safety;

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for verification status
CREATE TABLE verification_status (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  verification_type ENUM('phone', 'email', 'id') NOT NULL,
  verification_status ENUM('pending', 'verified', 'rejected') NOT NULL DEFAULT 'pending',
  verification_date TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for safety features
CREATE TABLE safety_features (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  feature_name VARCHAR(255) NOT NULL,
  feature_status BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for user reports
CREATE TABLE user_reports (
  id INT AUTO_INCREMENT,
  reporter_id INT NOT NULL,
  reported_user_id INT NOT NULL,
  report_reason ENUM('harassment', 'spam', 'safety_concern') NOT NULL,
  report_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (reporter_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (reported_user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for blocked users
CREATE TABLE blocked_users (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  blocked_user_id INT NOT NULL,
  block_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (blocked_user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, blocked_user_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_verification_status_user_id ON verification_status (user_id);
CREATE INDEX idx_safety_features_user_id ON safety_features (user_id);
CREATE INDEX idx_user_reports_reporter_id ON user_reports (reporter_id);
CREATE INDEX idx_user_reports_reported_user_id ON user_reports (reported_user_id);
CREATE INDEX idx_blocked_users_user_id ON blocked_users (user_id);
CREATE INDEX idx_blocked_users_blocked_user_id ON blocked_users (blocked_user_id);
```
