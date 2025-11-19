"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Generate a database schema to store information about esports tournaments, participants, sponsors, and apparel designs, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_efa66cc7498ce3bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for esports tournament information
CREATE DATABASE ace_pro_sports;

-- Use the created database
USE ace_pro_sports;

-- Create table for tournaments
CREATE TABLE tournaments (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `prize_pool` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for participants
CREATE TABLE participants (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `team_name` VARCHAR(255),
  `player_tag` VARCHAR(255) NOT NULL,
  `game_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for sponsors
CREATE TABLE sponsors (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `logo_url` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for apparel designs
CREATE TABLE apparel_designs (
  `id` INT AUTO_INCREMENT,
  `design_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `image_url` VARCHAR(255) NOT NULL,
  `sponsor_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sponsor_id`) REFERENCES sponsors(`id`)
);

-- Create table for tournament participants
CREATE TABLE tournament_participants (
  `id` INT AUTO_INCREMENT,
  `tournament_id` INT NOT NULL,
  `participant_id` INT NOT NULL,
  `seed` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`tournament_id`) REFERENCES tournaments(`id`),
  FOREIGN KEY (`participant_id`) REFERENCES participants(`id`)
);

-- Create table for tournament sponsors
CREATE TABLE tournament_sponsors (
  `id` INT AUTO_INCREMENT,
  `tournament_id` INT NOT NULL,
  `sponsor_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`tournament_id`) REFERENCES tournaments(`id`),
  FOREIGN KEY (`sponsor_id`) REFERENCES sponsors(`id`)
);

-- Create table for participant apparel
CREATE TABLE participant_apparel (
  `id` INT AUTO_INCREMENT,
  `participant_id` INT NOT NULL,
  `apparel_design_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`participant_id`) REFERENCES participants(`id`),
  FOREIGN KEY (`apparel_design_id`) REFERENCES apparel_designs(`id`)
);
```
