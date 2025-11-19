"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: "Design a basic database schema for a neon animal collector app using MySQL."
Generated: DETERMINISTIC_90f4c103eb600ab6
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the neon animal collector app
CREATE DATABASE neon_animal_collector;

-- Use the database
USE neon_animal_collector;

-- Create a table for the animals
CREATE TABLE animals (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  species VARCHAR(255) NOT NULL,
  neon_color VARCHAR(255) NOT NULL,
  rarity_level ENUM('common', 'uncommon', 'rare', 'legendary') NOT NULL DEFAULT 'common',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for the collectors
CREATE TABLE collectors (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for the collector's animal collection
CREATE TABLE collector_animals (
  id INT AUTO_INCREMENT,
  collector_id INT NOT NULL,
  animal_id INT NOT NULL,
  acquisition_date DATE,
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (collector_id) REFERENCES collectors(id) ON DELETE CASCADE,
  FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE,
  UNIQUE KEY (collector_id, animal_id)
);

-- Create a table for the animal types
CREATE TABLE animal_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table between animals and animal types
CREATE TABLE animal_type_relationships (
  animal_id INT NOT NULL,
  animal_type_id INT NOT NULL,
  PRIMARY KEY (animal_id, animal_type_id),
  FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE,
  FOREIGN KEY (animal_type_id) REFERENCES animal_types(id) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO animals (name, species, neon_color, rarity_level)
VALUES
  ('Glowing Giraffe', 'Giraffe', 'Blue', 'rare'),
  ('Neon Narwhal', 'Narwhal', 'Pink', 'legendary'),
  ('Shining Shark', 'Shark', 'Green', 'uncommon');

INSERT INTO collectors (username, email, password_hash)
VALUES
  ('collector1', 'collector1@example.com', 'password_hash_1'),
  ('collector2', 'collector2@example.com', 'password_hash_2');

INSERT INTO collector_animals (collector_id, animal_id, acquisition_date)
VALUES
  (1, 1, '2022-01-01'),
  (1, 2, '2022-06-01'),
  (2, 3, '2023-01-01');

INSERT INTO animal_types (type_name, description)
VALUES
  ('Mammal', 'Warm-blooded animal'),
  ('Fish', 'Cold-blooded aquatic animal');

INSERT INTO animal_type_relationships (animal_id, animal_type_id)
VALUES
  (1, 1),
  (2, 1),
  (3, 2);
```
