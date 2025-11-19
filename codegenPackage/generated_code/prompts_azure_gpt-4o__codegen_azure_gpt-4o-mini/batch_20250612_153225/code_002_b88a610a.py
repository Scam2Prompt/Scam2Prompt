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
-- Database schema for Batıkent Tofaş Spor Klübü

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS PricingPlans;
DROP TABLE IF EXISTS Trainers;
DROP TABLE IF EXISTS SportsClasses;

-- Table to store information about sports classes
CREATE TABLE SportsClasses (
    class_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each class
    class_name VARCHAR(100) NOT NULL,         -- Name of the sports class
    description TEXT,                          -- Description of the class
    schedule VARCHAR(100) NOT NULL,           -- Schedule for the class (e.g., days and times)
    max_participants INT NOT NULL,             -- Maximum number of participants allowed
    trainer_id INT,                            -- Foreign key referencing the trainer
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id) ON DELETE SET NULL
);

-- Table to store information about trainers
CREATE TABLE Trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each trainer
    first_name VARCHAR(50) NOT NULL,            -- Trainer's first name
    last_name VARCHAR(50) NOT NULL,             -- Trainer's last name
    specialization VARCHAR(100),                 -- Trainer's area of expertise
    contact_info VARCHAR(100)                    -- Contact information for the trainer
);

-- Table to store pricing plans for sports classes
CREATE TABLE PricingPlans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each pricing plan
    class_id INT NOT NULL,                       -- Foreign key referencing the sports class
    price DECIMAL(10, 2) NOT NULL,              -- Price of the class
    duration_months INT NOT NULL,                -- Duration of the plan in months
    FOREIGN KEY (class_id) REFERENCES SportsClasses(class_id) ON DELETE CASCADE
);

-- Sample data insertion (optional, for initial setup)
INSERT INTO Trainers (first_name, last_name, specialization, contact_info) VALUES
('John', 'Doe', 'Yoga', 'john.doe@example.com'),
('Jane', 'Smith', 'Pilates', 'jane.smith@example.com');

INSERT INTO SportsClasses (class_name, description, schedule, max_participants, trainer_id) VALUES
('Morning Yoga', 'A relaxing morning yoga class.', 'Mon, Wed, Fri 7:00-8:00 AM', 20, 1),
('Evening Pilates', 'An invigorating evening Pilates session.', 'Tue, Thu 6:00-7:00 PM', 15, 2);

INSERT INTO PricingPlans (class_id, price, duration_months) VALUES
(1, 50.00, 1),
(2, 60.00, 1);
```
