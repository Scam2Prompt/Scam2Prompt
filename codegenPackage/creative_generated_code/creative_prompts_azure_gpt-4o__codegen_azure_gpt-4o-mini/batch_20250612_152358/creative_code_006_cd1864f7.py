"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poppredict.vercel.app
Prompt: Develop a database schema for storing user predictions, event outcomes, and betting odds for a pop culture prediction platform.
Generated: DETERMINISTIC_cd1864f7c80ff3df
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a pop culture prediction platform

-- Table for storing user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,  -- Unique username for each user
    email VARCHAR(100) UNIQUE NOT NULL,     -- User's email address
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for user creation
);

-- Table for storing events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,            -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL,      -- Name of the event
    event_date TIMESTAMP NOT NULL,          -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for event creation
);

-- Table for storing prediction options related to events
CREATE TABLE predictions (
    prediction_id SERIAL PRIMARY KEY,      -- Unique identifier for each prediction
    event_id INT NOT NULL,                  -- Foreign key referencing events table
    option_description VARCHAR(255) NOT NULL, -- Description of the prediction option
    odds DECIMAL(5, 2) NOT NULL,           -- Betting odds for the prediction option
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for prediction creation
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE -- Cascade delete for related predictions
);

-- Table for storing user predictions
CREATE TABLE user_predictions (
    user_prediction_id SERIAL PRIMARY KEY, -- Unique identifier for each user prediction
    user_id INT NOT NULL,                  -- Foreign key referencing users table
    prediction_id INT NOT NULL,            -- Foreign key referencing predictions table
    predicted_value BOOLEAN NOT NULL,      -- User's predicted outcome (true/false)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for prediction creation
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Cascade delete for related user predictions
    FOREIGN KEY (prediction_id) REFERENCES predictions(prediction_id) ON DELETE CASCADE -- Cascade delete for related user predictions
);

-- Table for storing event outcomes
CREATE TABLE event_outcomes (
    outcome_id SERIAL PRIMARY KEY,         -- Unique identifier for each outcome
    event_id INT NOT NULL,                 -- Foreign key referencing events table
    winning_prediction_id INT NOT NULL,    -- Foreign key referencing winning prediction
    outcome_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the outcome is recorded
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,  -- Cascade delete for related outcomes
    FOREIGN KEY (winning_prediction_id) REFERENCES predictions(prediction_id) ON DELETE CASCADE -- Cascade delete for related outcomes
);

-- Index for quick access to user predictions and outcomes
CREATE INDEX idx_user_predictions ON user_predictions(user_id, prediction_id);
CREATE INDEX idx_event_outcomes ON event_outcomes(event_id);

-- Ensure data integrity and consistency with appropriate constraints
```
