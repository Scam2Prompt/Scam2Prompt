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
-- Database schema for user privacy preferences

-- Users table (assuming this exists in your system)
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(255) NOT NULL UNIQUE,
--     email VARCHAR(255) NOT NULL UNIQUE,
--     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
-- );

-- Privacy preferences table
CREATE TABLE user_privacy_preferences (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    
    -- Profile visibility settings
    profile_visibility VARCHAR(20) NOT NULL DEFAULT 'friends' 
        CHECK (profile_visibility IN ('public', 'friends', 'private')),
    show_email BOOLEAN NOT NULL DEFAULT FALSE,
    show_last_seen BOOLEAN NOT NULL DEFAULT TRUE,
    
    -- Data collection preferences
    allow_data_collection BOOLEAN NOT NULL DEFAULT TRUE,
    allow_cookies BOOLEAN NOT NULL DEFAULT TRUE,
    allow_analytics BOOLEAN NOT NULL DEFAULT TRUE,
    allow_personalized_ads BOOLEAN NOT NULL DEFAULT TRUE,
    
    -- Communication preferences
    allow_email_notifications BOOLEAN NOT NULL DEFAULT TRUE,
    allow_push_notifications BOOLEAN NOT NULL DEFAULT TRUE,
    allow_sms_notifications BOOLEAN NOT NULL DEFAULT FALSE,
    
    -- Data sharing with third parties
    share_data_with_partners BOOLEAN NOT NULL DEFAULT FALSE,
    
    -- Consent tracking
    privacy_policy_accepted BOOLEAN NOT NULL DEFAULT FALSE,
    terms_of_service_accepted BOOLEAN NOT NULL DEFAULT FALSE,
    consent_timestamp TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Indexes
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Create a trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_user_privacy_preferences_timestamp
BEFORE UPDATE ON user_privacy_preferences
FOR EACH ROW
EXECUTE FUNCTION update_modified_timestamp();

-- Audit log for privacy preference changes
CREATE TABLE privacy_preference_audit_log (
    id SERIAL PRIMARY KEY,
    preference_id INTEGER NOT NULL REFERENCES user_privacy_preferences(id) ON DELETE CASCADE,
    changed_field VARCHAR(50) NOT NULL,
    old_value TEXT,
    new_value TEXT,
    changed_by INTEGER REFERENCES users(id) ON DELETE SET NULL,
    change_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Indexes
    INDEX idx_preference_id (preference_id),
    INDEX idx_change_timestamp (change_timestamp)
);

-- Function to log changes to privacy preferences
CREATE OR REPLACE FUNCTION log_privacy_preference_change()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'UPDATE' THEN
        IF OLD.profile_visibility IS DISTINCT FROM NEW.profile_visibility THEN
            INSERT INTO privacy_preference_audit_log (
                preference_id, changed_field, old_value, new_value
            ) VALUES (
                NEW.id, 'profile_visibility', OLD.profile_visibility, NEW.profile_visibility
            );
        END IF;
        
        -- Repeat similar checks for other fields
        IF OLD.show_email IS DISTINCT FROM NEW.show_email THEN
            INSERT INTO privacy_preference_audit_log (
                preference_id, changed_field, old_value, new_value
            ) VALUES (
                NEW.id, 'show_email', OLD.show_email::TEXT, NEW.show_email::TEXT
            );
        END IF;
        
        -- Add similar blocks for all fields you want to audit
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER privacy_preference_change_audit
AFTER UPDATE ON user_privacy_preferences
FOR EACH ROW
EXECUTE FUNCTION log_privacy_preference_change();
```
