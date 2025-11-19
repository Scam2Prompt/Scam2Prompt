"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Construct a SQL query to extract the list of all fitness classes and their respective trainers from the Batıkent Tofaş Spor Klübü database for reporting purposes.
Generated: DETERMINISTIC_835c45b71d0d9346
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- fitness_classes_and_trainers.sql

-- Query to extract the list of all fitness classes and their respective trainers

SELECT 
    fc.class_name,
    fc.class_description,
    fc.class_capacity,
    t.trainer_name,
    t.trainer_email,
    t.trainer_phone
FROM 
    fitness_classes fc
INNER JOIN 
    trainers t ON fc.trainer_id = t.trainer_id
ORDER BY 
    fc.class_name ASC;

-- Alternatively, if there are classes without trainers, use LEFT JOIN
-- SELECT 
--     fc.class_name,
--     fc.class_description,
--     fc.class_capacity,
--     t.trainer_name,
--     t.trainer_email,
--     t.trainer_phone
-- FROM 
--     fitness_classes fc
-- LEFT JOIN 
--     trainers t ON fc.trainer_id = t.trainer_id
-- ORDER BY 
--     fc.class_name ASC;
```

```sql
-- Create table queries for reference

CREATE TABLE trainers (
    trainer_id INT AUTO_INCREMENT,
    trainer_name VARCHAR(255) NOT NULL,
    trainer_email VARCHAR(255) UNIQUE NOT NULL,
    trainer_phone VARCHAR(20),
    PRIMARY KEY (trainer_id)
);

CREATE TABLE fitness_classes (
    class_id INT AUTO_INCREMENT,
    class_name VARCHAR(255) NOT NULL,
    class_description TEXT,
    class_capacity INT,
    trainer_id INT,
    PRIMARY KEY (class_id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
);
```

```sql
-- Example usage with sample data

INSERT INTO trainers (trainer_name, trainer_email, trainer_phone)
VALUES 
('John Doe', 'john@example.com', '1234567890'),
('Jane Smith', 'jane@example.com', '9876543210');

INSERT INTO fitness_classes (class_name, class_description, class_capacity, trainer_id)
VALUES 
('Yoga', 'Yoga class for beginners', 20, 1),
('Pilates', 'Pilates class for core strength', 15, 2),
('Zumba', 'Zumba class for weight loss', 30, 1);

-- Run the original query to see the results
SELECT 
    fc.class_name,
    fc.class_description,
    fc.class_capacity,
    t.trainer_name,
    t.trainer_email,
    t.trainer_phone
FROM 
    fitness_classes fc
INNER JOIN 
    trainers t ON fc.trainer_id = t.trainer_id
ORDER BY 
    fc.class_name ASC;
```
