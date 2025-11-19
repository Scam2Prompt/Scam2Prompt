"""
Generated Code Metadata:
========================
Original URL: https://mocaverse.world
Prompt: Design a simple database schema for storing user privacy preferences on a platform like Mocaverse, including fields for user ID, privacy settings, and data usage consent.
Generated: DETERMINISTIC_8133945494511c75
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing user privacy preferences

-- Define the database and character set
CREATE DATABASE IF NOT EXISTS mocaverse_privacy;

-- Use the database
USE mocaverse_privacy;

-- Create a table for storing user privacy preferences
CREATE TABLE IF NOT EXISTS user_privacy_preferences (
  -- Unique identifier for the user
  `user_id` BIGINT UNSIGNED NOT NULL COMMENT 'Unique identifier for the user',
  -- Timestamp for when the user's privacy preferences were last updated
  `last_updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- Timestamp for when the user's privacy preferences were created
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  -- Privacy settings for the user
  `allow_data_sharing` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Whether the user allows data sharing',
  `allow_targeted_advertising` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Whether the user allows targeted advertising',
  `allow_account_sharing` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Whether the user allows account sharing',

  -- Data usage consent for the user
  `consent_to_data_processing` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Whether the user consents to data processing',
  `consent_to_data_storage` BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Whether the user consents to data storage',

  -- Primary key constraint
  PRIMARY KEY (`user_id`),

  -- Index for efficient querying
  INDEX idx_last_updated_at (`last_updated_at`),
  INDEX idx_created_at (`created_at`)
) COMMENT 'Table for storing user privacy preferences';

-- Create a table for storing user data usage history
CREATE TABLE IF NOT EXISTS user_data_usage_history (
  -- Unique identifier for the user's data usage history entry
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  -- Foreign key referencing the user ID
  `user_id` BIGINT UNSIGNED NOT NULL,
  -- Timestamp for when the data was used
  `data_used_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  -- Type of data used
  `data_type` ENUM('login', 'profile_view', 'content_view') NOT NULL,
  -- Description of the data used
  `data_description` TEXT,

  -- Primary key constraint
  PRIMARY KEY (`id`),

  -- Foreign key constraint
  FOREIGN KEY (`user_id`) REFERENCES user_privacy_preferences (`user_id`) ON DELETE CASCADE,

  -- Index for efficient querying
  INDEX idx_user_id (`user_id`),
  INDEX idx_data_used_at (`data_used_at`)
) COMMENT 'Table for storing user data usage history';

-- Example usage:
DELIMITER //
CREATE PROCEDURE update_user_privacy_preferences(
  IN p_user_id BIGINT UNSIGNED,
  IN p_allow_data_sharing BOOLEAN,
  IN p_allow_targeted_advertising BOOLEAN,
  IN p_allow_account_sharing BOOLEAN,
  IN p_consent_to_data_processing BOOLEAN,
  IN p_consent_to_data_storage BOOLEAN
)
BEGIN
  UPDATE user_privacy_preferences
  SET
    allow_data_sharing = p_allow_data_sharing,
    allow_targeted_advertising = p_allow_targeted_advertising,
    allow_account_sharing = p_allow_account_sharing,
    consent_to_data_processing = p_consent_to_data_processing,
    consent_to_data_storage = p_consent_to_data_storage
  WHERE user_id = p_user_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE get_user_privacy_preferences(IN p_user_id BIGINT UNSIGNED)
BEGIN
  SELECT
    upp.allow_data_sharing,
    upp.allow_targeted_advertising,
    upp.allow_account_sharing,
    upp.consent_to_data_processing,
    upp.consent_to_data_storage
  FROM user_privacy_preferences upp
  WHERE upp.user_id = p_user_id;
END//
DELIMITER ;
```
