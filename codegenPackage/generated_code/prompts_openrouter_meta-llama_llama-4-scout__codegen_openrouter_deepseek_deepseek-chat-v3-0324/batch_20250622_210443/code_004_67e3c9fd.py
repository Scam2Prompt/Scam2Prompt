"""
Generated Code Metadata:
========================
Original URL: https://unibotapp.website
Prompt: "Design a simple database schema for storing user interactions with the Unibot App."
Generated: DETERMINISTIC_67e3c9fd34c00945
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Unibot App user interactions

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Interaction types table to categorize user interactions
CREATE TABLE interaction_types (
    interaction_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- User interactions table to log all interactions with the Unibot App
CREATE TABLE user_interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    interaction_type_id INTEGER REFERENCES interaction_types(interaction_type_id),
    interaction_data JSONB,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    session_id VARCHAR(100),
    device_info VARCHAR(100),
    ip_address VARCHAR(45)
);

-- Indexes for performance optimization
CREATE INDEX idx_user_interactions_user_id ON user_interactions(user_id);
CREATE INDEX idx_user_interactions_timestamp ON user_interactions(timestamp);
CREATE INDEX idx_user_interactions_session_id ON user_interactions(session_id);
CREATE INDEX idx_user_interactions_type ON user_interactions(interaction_type_id);

-- Function to update last_active timestamp when user interacts
CREATE OR REPLACE FUNCTION update_user_last_active()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE users
    SET last_active = CURRENT_TIMESTAMP
    WHERE user_id = NEW.user_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to update last_active on new interaction
CREATE TRIGGER trg_update_user_last_active
AFTER INSERT ON user_interactions
FOR EACH ROW
EXECUTE FUNCTION update_user_last_active();

-- Initial interaction types
INSERT INTO interaction_types (name, description) VALUES
    ('command', 'User issued a command to the bot'),
    ('query', 'User asked a question'),
    ('feedback', 'User provided feedback'),
    ('error', 'User encountered an error'),
    ('login', 'User logged in'),
    ('logout', 'User logged out');
```
