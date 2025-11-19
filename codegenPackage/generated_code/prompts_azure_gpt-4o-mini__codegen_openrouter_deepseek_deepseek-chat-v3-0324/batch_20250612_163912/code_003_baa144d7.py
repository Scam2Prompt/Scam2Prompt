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
-- Database schema for a dating platform with user profiles and compatibility scores

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store basic user information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20) NOT NULL,
    gender_preference VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    CONSTRAINT valid_age CHECK (date_of_birth <= CURRENT_DATE - INTERVAL '18 years')
);

-- User profiles table with detailed information
CREATE TABLE user_profiles (
    profile_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    bio TEXT,
    height_cm INTEGER,
    education_level VARCHAR(100),
    occupation VARCHAR(100),
    relationship_goal VARCHAR(100),
    religion VARCHAR(100),
    political_leaning VARCHAR(100),
    has_children BOOLEAN DEFAULT FALSE,
    wants_children BOOLEAN,
    smoking_habit VARCHAR(50),
    drinking_habit VARCHAR(50),
    exercise_habit VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_height CHECK (height_cm BETWEEN 100 AND 250)
);

-- User interests table (many-to-many with users)
CREATE TABLE interests (
    interest_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(100) NOT NULL
);

CREATE TABLE user_interests (
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    interest_id INTEGER NOT NULL REFERENCES interests(interest_id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, interest_id)
);

-- Compatibility questions
CREATE TABLE compatibility_questions (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    weight DECIMAL(3,2) NOT NULL DEFAULT 1.00,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_weight CHECK (weight BETWEEN 0.1 AND 2.0)
);

-- User answers to compatibility questions
CREATE TABLE user_answers (
    answer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    question_id INTEGER NOT NULL REFERENCES compatibility_questions(question_id) ON DELETE CASCADE,
    answer_value INTEGER NOT NULL,
    importance INTEGER NOT NULL DEFAULT 3,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_question UNIQUE (user_id, question_id),
    CONSTRAINT valid_answer_value CHECK (answer_value BETWEEN 1 AND 5),
    CONSTRAINT valid_importance CHECK (importance BETWEEN 1 AND 5)
);

-- Compatibility scores between users
CREATE TABLE compatibility_scores (
    user1_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    user2_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    overall_score DECIMAL(5,2) NOT NULL,
    values_score DECIMAL(5,2) NOT NULL,
    lifestyle_score DECIMAL(5,2) NOT NULL,
    personality_score DECIMAL(5,2) NOT NULL,
    last_calculated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user1_id, user2_id),
    CONSTRAINT valid_users_order CHECK (user1_id < user2_id),
    CONSTRAINT valid_score_range CHECK (
        overall_score BETWEEN 0 AND 100 AND
        values_score BETWEEN 0 AND 100 AND
        lifestyle_score BETWEEN 0 AND 100 AND
        personality_score BETWEEN 0 AND 100
    )
);

-- User photos table
CREATE TABLE user_photos (
    photo_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    photo_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    position INTEGER NOT NULL,
    CONSTRAINT single_primary_photo UNIQUE (user_id, is_primary) DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT valid_position CHECK (position >= 0)
);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_modtime
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_profiles_modtime
BEFORE UPDATE ON user_profiles
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_answers_modtime
BEFORE UPDATE ON user_answers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Indexes for performance optimization
CREATE INDEX idx_compatibility_scores_user1 ON compatibility_scores(user1_id);
CREATE INDEX idx_compatibility_scores_user2 ON compatibility_scores(user2_id);
CREATE INDEX idx_compatibility_scores_overall ON compatibility_scores(overall_score);
CREATE INDEX idx_user_answers_user ON user_answers(user_id);
CREATE INDEX idx_user_photos_user ON user_photos(user_id);
```
