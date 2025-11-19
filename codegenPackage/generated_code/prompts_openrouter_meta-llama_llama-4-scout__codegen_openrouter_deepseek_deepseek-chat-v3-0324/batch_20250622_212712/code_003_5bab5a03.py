"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Design a database schema to store user information, fitness goals, and personalized coaching plans for a nutrition and training coaching platform like Legacy Training & Nutrition.
Generated: DETERMINISTIC_5bab5a0332f7d866
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Legacy Training & Nutrition platform

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(20),
    phone_number VARCHAR(20),
    profile_image_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_coach BOOLEAN DEFAULT FALSE,
    CHECK (gender IN ('Male', 'Female', 'Other', 'Prefer not to say'))
);

-- User biometrics table
CREATE TABLE user_biometrics (
    biometric_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    height_cm DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    body_fat_percentage DECIMAL(5,2),
    measurement_date DATE NOT NULL DEFAULT CURRENT_DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Fitness goals table
CREATE TABLE fitness_goals (
    goal_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    goal_type VARCHAR(50) NOT NULL,
    target_value DECIMAL(10,2),
    current_value DECIMAL(10,2),
    start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    target_date DATE,
    is_achieved BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (goal_type IN ('Weight Loss', 'Muscle Gain', 'Endurance', 'Strength', 'Flexibility', 'Other'))
);

-- Nutrition plans table
CREATE TABLE nutrition_plans (
    plan_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    coach_id INTEGER REFERENCES users(user_id),
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    daily_calories INTEGER,
    protein_grams INTEGER,
    carb_grams INTEGER,
    fat_grams INTEGER,
    is_active BOOLEAN DEFAULT FALSE,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Meal table
CREATE TABLE meals (
    meal_id SERIAL PRIMARY KEY,
    plan_id INTEGER REFERENCES nutrition_plans(plan_id) ON DELETE CASCADE,
    meal_name VARCHAR(100) NOT NULL,
    meal_time VARCHAR(50) NOT NULL,
    calories INTEGER,
    protein_grams INTEGER,
    carb_grams INTEGER,
    fat_grams INTEGER,
    instructions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (meal_time IN ('Breakfast', 'Lunch', 'Dinner', 'Snack', 'Pre-workout', 'Post-workout'))
);

-- Training plans table
CREATE TABLE training_plans (
    plan_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    coach_id INTEGER REFERENCES users(user_id),
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty_level VARCHAR(50),
    is_active BOOLEAN DEFAULT FALSE,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (difficulty_level IN ('Beginner', 'Intermediate', 'Advanced', 'Elite'))
);

-- Workouts table
CREATE TABLE workouts (
    workout_id SERIAL PRIMARY KEY,
    plan_id INTEGER REFERENCES training_plans(plan_id) ON DELETE CASCADE,
    day_of_week VARCHAR(20) NOT NULL,
    workout_name VARCHAR(100) NOT NULL,
    duration_minutes INTEGER,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
);

-- Exercises table
CREATE TABLE exercises (
    exercise_id SERIAL PRIMARY KEY,
    workout_id INTEGER REFERENCES workouts(workout_id) ON DELETE CASCADE,
    exercise_name VARCHAR(100) NOT NULL,
    sets INTEGER,
    reps INTEGER,
    weight_kg DECIMAL(5,2),
    rest_seconds INTEGER,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Progress tracking table
CREATE TABLE progress_tracking (
    tracking_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    entry_date DATE NOT NULL DEFAULT CURRENT_DATE,
    weight_kg DECIMAL(5,2),
    body_fat_percentage DECIMAL(5,2),
    waist_circumference_cm DECIMAL(5,2),
    mood VARCHAR(50),
    energy_level VARCHAR(50),
    sleep_hours DECIMAL(3,1),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Coach-client relationship table
CREATE TABLE coach_client_relationships (
    relationship_id SERIAL PRIMARY KEY,
    coach_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    client_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (coach_id, client_id),
    CHECK (coach_id != client_id)
);

-- Messages table for coach-client communication
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    receiver_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    message_text TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_user_biometrics_user_id ON user_biometrics(user_id);
CREATE INDEX idx_fitness_goals_user_id ON fitness_goals(user_id);
CREATE INDEX idx_nutrition_plans_user_id ON nutrition_plans(user_id);
CREATE INDEX idx_training_plans_user_id ON training_plans(user_id);
CREATE INDEX idx_progress_tracking_user_id ON progress_tracking(user_id);
CREATE INDEX idx_coach_client_coach_id ON coach_client_relationships(coach_id);
CREATE INDEX idx_coach_client_client_id ON coach_client_relationships(client_id);
CREATE INDEX idx_messages_sender_receiver ON messages(sender_id, receiver_id);
```
