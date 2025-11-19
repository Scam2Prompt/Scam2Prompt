"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Design a database schema to store 1-minute dog training sessions, including information on training methods, duration, and effectiveness.
Generated: DETERMINISTIC_0017eae7e3a21e49
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for dog training sessions tracking

CREATE TABLE dogs (
    dog_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    breed VARCHAR(100),
    age INTEGER,
    weight DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE training_methods (
    method_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL CHECK (category IN ('positive_reinforcement', 'negative_reinforcement', 'punishment', 'other'))
);

CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    dog_id INTEGER NOT NULL REFERENCES dogs(dog_id) ON DELETE CASCADE,
    method_id INTEGER NOT NULL REFERENCES training_methods(method_id) ON DELETE RESTRICT,
    session_date DATE NOT NULL DEFAULT CURRENT_DATE,
    duration_seconds INTEGER NOT NULL CHECK (duration_seconds > 0 AND duration_seconds <= 60),
    notes TEXT,
    effectiveness_rating INTEGER CHECK (effectiveness_rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_session_per_day UNIQUE (dog_id, session_date)
);

CREATE TABLE session_behaviors (
    behavior_id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,
    behavior_name VARCHAR(100) NOT NULL,
    pre_session_rating INTEGER CHECK (pre_session_rating BETWEEN 1 AND 5),
    post_session_rating INTEGER CHECK (post_session_rating BETWEEN 1 AND 5)
);

CREATE INDEX idx_sessions_dog_id ON sessions(dog_id);
CREATE INDEX idx_sessions_method_id ON sessions(method_id);
CREATE INDEX idx_session_behaviors_session_id ON session_behaviors(session_id);

-- Trigger to update timestamp on dog record modification
CREATE OR REPLACE FUNCTION update_dog_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER dog_update_timestamp
BEFORE UPDATE ON dogs
FOR EACH ROW
EXECUTE FUNCTION update_dog_timestamp();
```
