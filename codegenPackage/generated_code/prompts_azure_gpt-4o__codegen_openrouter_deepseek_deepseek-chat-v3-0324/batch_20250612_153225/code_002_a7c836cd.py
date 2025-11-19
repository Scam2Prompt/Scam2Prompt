"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a database schema in SQL for a personal training service that stores user information, training plans, physical evaluations, and communication logs via WhatsApp and an exclusive app.
Generated: DETERMINISTIC_a7c836cd0fc9fd19
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a personal training service

-- Create the database
CREATE DATABASE IF NOT EXISTS personal_training_service;
USE personal_training_service;

-- Users table to store client and trainer information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say'),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    user_type ENUM('Client', 'Trainer', 'Admin') NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    profile_picture_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Training plans table
CREATE TABLE IF NOT EXISTS training_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    trainer_id INT NOT NULL,
    client_id INT NOT NULL,
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (trainer_id) REFERENCES users(user_id),
    FOREIGN KEY (client_id) REFERENCES users(user_id),
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date >= start_date)
) ENGINE=InnoDB;

-- Workout sessions table
CREATE TABLE IF NOT EXISTS workout_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_id INT NOT NULL,
    session_name VARCHAR(100) NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME,
    end_time TIME,
    location VARCHAR(100),
    notes TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (plan_id) REFERENCES training_plans(plan_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Exercises table
CREATE TABLE IF NOT EXISTS exercises (
    exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    exercise_name VARCHAR(100) NOT NULL,
    description TEXT,
    muscle_group VARCHAR(50),
    equipment_needed VARCHAR(100),
    difficulty_level ENUM('Beginner', 'Intermediate', 'Advanced')
) ENGINE=InnoDB;

-- Session exercises (many-to-many relationship between sessions and exercises)
CREATE TABLE IF NOT EXISTS session_exercises (
    session_exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    exercise_id INT NOT NULL,
    sets INT,
    reps INT,
    weight DECIMAL(5,2),
    duration_minutes INT,
    rest_seconds INT,
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES workout_sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id),
    CONSTRAINT chk_positive_values CHECK (sets > 0 AND reps > 0 AND (weight IS NULL OR weight > 0) AND (duration_minutes IS NULL OR duration_minutes > 0) AND (rest_seconds IS NULL OR rest_seconds > 0))
) ENGINE=InnoDB;

-- Physical evaluations table
CREATE TABLE IF NOT EXISTS physical_evaluations (
    evaluation_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    trainer_id INT NOT NULL,
    evaluation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    weight_kg DECIMAL(5,2),
    height_cm DECIMAL(5,2),
    body_fat_percentage DECIMAL(5,2),
    muscle_mass_kg DECIMAL(5,2),
    chest_cm DECIMAL(5,2),
    waist_cm DECIMAL(5,2),
    hips_cm DECIMAL(5,2),
    resting_heart_rate INT,
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    flexibility_score INT,
    strength_score INT,
    endurance_score INT,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES users(user_id),
    FOREIGN KEY (trainer_id) REFERENCES users(user_id),
    CONSTRAINT chk_blood_pressure CHECK (blood_pressure_systolic > 0 AND blood_pressure_diastolic > 0 AND blood_pressure_systolic > blood_pressure_diastolic)
) ENGINE=InnoDB;

-- Progress photos table
CREATE TABLE IF NOT EXISTS progress_photos (
    photo_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    photo_url VARCHAR(255) NOT NULL,
    photo_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    angle ENUM('Front', 'Side', 'Back'),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Communication channels table
CREATE TABLE IF NOT EXISTS communication_channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(50) NOT NULL,
    description TEXT
) ENGINE=InnoDB;

-- Pre-populate communication channels
INSERT IGNORE INTO communication_channels (channel_id, channel_name, description) VALUES 
(1, 'WhatsApp', 'WhatsApp messaging'),
(2, 'In-App', 'Built-in app messaging system'),
(3, 'Email', 'Email communication'),
(4, 'Phone', 'Phone calls');

-- Communication logs table
CREATE TABLE IF NOT EXISTS communication_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    channel_id INT NOT NULL,
    message_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    message_content TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    read_date DATETIME,
    FOREIGN KEY (sender_id) REFERENCES users(user_id),
    FOREIGN KEY (receiver_id) REFERENCES users(user_id),
    FOREIGN KEY (channel_id) REFERENCES communication_channels(channel_id)
) ENGINE=InnoDB;

-- Goals table
CREATE TABLE IF NOT EXISTS goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    goal_description TEXT NOT NULL,
    target_date DATE,
    is_achieved BOOLEAN DEFAULT FALSE,
    achieved_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    trainer_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('Credit Card', 'Debit Card', 'Bank Transfer', 'Cash', 'Other'),
    payment_status ENUM('Pending', 'Completed', 'Failed', 'Refunded') DEFAULT 'Pending',
    invoice_number VARCHAR(50),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES users(user_id),
    FOREIGN KEY (trainer_id) REFERENCES users(user_id),
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_user_type ON users(user_type);
CREATE INDEX idx_training_plans_client ON training_plans(client_id);
CREATE INDEX idx_training_plans_trainer ON training_plans(trainer_id);
CREATE INDEX idx_workout_sessions_plan ON workout_sessions(plan_id);
CREATE INDEX idx_physical_evaluations_client ON physical_evaluations(client_id);
CREATE INDEX idx_communication_logs_sender ON communication_logs(sender_id);
CREATE INDEX idx_communication_logs_receiver ON communication_logs(receiver_id);
```
