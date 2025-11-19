"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Design a database schema to store information about suspension training sessions, trainers, and clients for a studio like Breakthrough Studio, and provide a simple query example.
Generated: DETERMINISTIC_ebb6581c126ba545
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Breakthrough Studio suspension training system

-- Create database
CREATE DATABASE breakthrough_studio;
USE breakthrough_studio;

-- Users table (common fields for both trainers and clients)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Trainers table (extends users)
CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY,
    certification VARCHAR(100),
    specialization TEXT,
    hire_date DATE NOT NULL,
    hourly_rate DECIMAL(10, 2),
    FOREIGN KEY (trainer_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Clients table (extends users)
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    membership_start_date DATE NOT NULL,
    membership_type ENUM('basic', 'premium', 'vip') NOT NULL,
    health_notes TEXT,
    fitness_goals TEXT,
    FOREIGN KEY (client_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Equipment table
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    purchase_date DATE,
    last_maintenance_date DATE,
    status ENUM('active', 'maintenance', 'retired') DEFAULT 'active'
);

-- Training sessions table
CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    trainer_id INT NOT NULL,
    client_id INT NOT NULL,
    equipment_id INT,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    duration_minutes INT GENERATED ALWAYS AS (TIMESTAMPDIFF(MINUTE, start_time, end_time)) STORED,
    notes TEXT,
    status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    CHECK (start_time < end_time)
);

-- Session exercises table (many-to-many relationship between sessions and exercises)
CREATE TABLE session_exercises (
    session_exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    exercise_name VARCHAR(100) NOT NULL,
    sets INT,
    reps INT,
    difficulty_level ENUM('beginner', 'intermediate', 'advanced'),
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'debit_card', 'bank_transfer') NOT NULL,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Example query: Get all completed sessions for a specific client with trainer details
SELECT 
    s.session_id,
    s.session_date,
    s.start_time,
    s.end_time,
    CONCAT(u_trainer.first_name, ' ', u_trainer.last_name) AS trainer_name,
    e.name AS equipment_used,
    COUNT(se.exercise_name) AS exercises_completed
FROM 
    sessions s
JOIN 
    trainers t ON s.trainer_id = t.trainer_id
JOIN 
    users u_trainer ON t.trainer_id = u_trainer.user_id
LEFT JOIN 
    equipment e ON s.equipment_id = e.equipment_id
LEFT JOIN 
    session_exercises se ON s.session_id = se.session_id
WHERE 
    s.client_id = 123 
    AND s.status = 'completed'
GROUP BY 
    s.session_id, s.session_date, s.start_time, s.end_time, trainer_name, equipment_used
ORDER BY 
    s.session_date DESC, s.start_time DESC;
```
