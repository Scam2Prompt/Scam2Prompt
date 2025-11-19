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
-- Database schema for storing and managing user safety information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE SafetyFeatures (
    feature_id SERIAL PRIMARY KEY, -- Unique identifier for each safety feature
    feature_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the safety feature
    description TEXT, -- Description of the safety feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of feature creation
);

CREATE TABLE UserSafetyInfo (
    safety_info_id SERIAL PRIMARY KEY, -- Unique identifier for each safety info record
    user_id INT NOT NULL, -- Foreign key referencing Users table
    verification_status VARCHAR(50) NOT NULL CHECK (verification_status IN ('Pending', 'Verified', 'Rejected')), -- Status of user verification
    safety_feature_id INT, -- Foreign key referencing SafetyFeatures table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of safety info record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (safety_feature_id) REFERENCES SafetyFeatures(feature_id) ON DELETE SET NULL -- Allows safety feature to be optional
);

-- Indexes for performance optimization
CREATE INDEX idx_user_verification_status ON UserSafetyInfo(verification_status);
CREATE INDEX idx_user_id ON UserSafetyInfo(user_id);
CREATE INDEX idx_feature_id ON UserSafetyInfo(safety_feature_id);
```
