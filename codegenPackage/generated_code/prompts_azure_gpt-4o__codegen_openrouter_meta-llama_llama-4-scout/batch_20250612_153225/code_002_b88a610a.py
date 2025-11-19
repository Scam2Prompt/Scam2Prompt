"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Create a database schema in SQL to store information about sports classes, trainers, and pricing plans as described on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_b88a610abd340b58
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Batıkent Tofaş Spor Klübü
CREATE DATABASE batikent_tofas_spor_klubu;

-- Use the created database
USE batikent_tofas_spor_klubu;

-- Create table for sports classes
CREATE TABLE sports_classes (
    class_id INT AUTO_INCREMENT,
    class_name VARCHAR(255) NOT NULL,
    class_description TEXT,
    class_duration INT,  -- in minutes
    class_capacity INT,
    PRIMARY KEY (class_id)
);

-- Create table for trainers
CREATE TABLE trainers (
    trainer_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    experience_years INT,
    PRIMARY KEY (trainer_id)
);

-- Create table for pricing plans
CREATE TABLE pricing_plans (
    plan_id INT AUTO_INCREMENT,
    plan_name VARCHAR(255) NOT NULL,
    plan_description TEXT,
    plan_price DECIMAL(10, 2) NOT NULL,
    plan_duration INT,  -- in months
    PRIMARY KEY (plan_id)
);

-- Create many-to-many relationship table for classes and trainers
CREATE TABLE class_trainers (
    class_id INT NOT NULL,
    trainer_id INT NOT NULL,
    PRIMARY KEY (class_id, trainer_id),
    FOREIGN KEY (class_id) REFERENCES sports_classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id) ON DELETE CASCADE
);

-- Create many-to-many relationship table for classes and pricing plans
CREATE TABLE class_pricing_plans (
    class_id INT NOT NULL,
    plan_id INT NOT NULL,
    PRIMARY KEY (class_id, plan_id),
    FOREIGN KEY (class_id) REFERENCES sports_classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES pricing_plans(plan_id) ON DELETE CASCADE
);

-- Create table for class schedules
CREATE TABLE class_schedules (
    schedule_id INT AUTO_INCREMENT,
    class_id INT NOT NULL,
    schedule_date DATE NOT NULL,
    schedule_time TIME NOT NULL,
    PRIMARY KEY (schedule_id),
    FOREIGN KEY (class_id) REFERENCES sports_classes(class_id) ON DELETE CASCADE
);

-- Create table for member registrations
CREATE TABLE member_registrations (
    registration_id INT AUTO_INCREMENT,
    class_id INT NOT NULL,
    member_name VARCHAR(255) NOT NULL,
    member_email VARCHAR(255) NOT NULL,
    registration_date DATE NOT NULL,
    PRIMARY KEY (registration_id),
    FOREIGN KEY (class_id) REFERENCES sports_classes(class_id) ON DELETE CASCADE
);

-- Insert sample data into tables
INSERT INTO sports_classes (class_name, class_description, class_duration, class_capacity)
VALUES 
('Basketball', 'Basketball training for adults', 60, 20),
('Football', 'Football training for kids', 90, 30),
('Tennis', 'Tennis lessons for beginners', 45, 10);

INSERT INTO trainers (first_name, last_name, email, phone_number, experience_years)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 5),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 3);

INSERT INTO pricing_plans (plan_name, plan_description, plan_price, plan_duration)
VALUES 
('Monthly', 'Monthly subscription plan', 50.00, 1),
('Quarterly', 'Quarterly subscription plan', 150.00, 3),
('Yearly', 'Yearly subscription plan', 500.00, 12);

INSERT INTO class_trainers (class_id, trainer_id)
VALUES 
(1, 1),
(2, 2),
(3, 1);

INSERT INTO class_pricing_plans (class_id, plan_id)
VALUES 
(1, 1),
(1, 3),
(2, 2),
(3, 1);

INSERT INTO class_schedules (class_id, schedule_date, schedule_time)
VALUES 
(1, '2024-09-16', '10:00:00'),
(2, '2024-09-17', '14:00:00'),
(3, '2024-09-18', '18:00:00');

INSERT INTO member_registrations (class_id, member_name, member_email, registration_date)
VALUES 
(1, 'Bob Johnson', 'bob.johnson@example.com', '2024-09-10'),
(2, 'Alice Brown', 'alice.brown@example.com', '2024-09-12'),
(3, 'Mike Davis', 'mike.davis@example.com', '2024-09-15');
```
