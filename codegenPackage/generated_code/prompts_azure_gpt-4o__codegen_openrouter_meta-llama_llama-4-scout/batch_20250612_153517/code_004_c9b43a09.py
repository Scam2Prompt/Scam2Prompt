"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Create a database schema for an online slot platform that includes game providers such as Pragmatic Play, Habanero, Joker123, PGSoft, and Spadegaming, as listed on ANGKA805.
Generated: DETERMINISTIC_c9b43a0940a09e01
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for online slot platform
CREATE DATABASE online_slot_platform;

-- Use the database
USE online_slot_platform;

-- Create table for game providers
CREATE TABLE game_providers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_game_provider_name` (`name`)
);

-- Create table for games
CREATE TABLE games (
  `id` INT AUTO_INCREMENT,
  `game_provider_id` INT NOT NULL,
  `game_code` VARCHAR(255) NOT NULL,
  `game_name` VARCHAR(255) NOT NULL,
  `game_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_game_provider_id` (`game_provider_id`),
  CONSTRAINT `fk_game_provider_id` FOREIGN KEY (`game_provider_id`) REFERENCES `game_providers` (`id`)
);

-- Create table for game categories
CREATE TABLE game_categories (
  `id` INT AUTO_INCREMENT,
  `game_id` INT NOT NULL,
  `category_name` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_game_id` (`game_id`),
  CONSTRAINT `fk_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
);

-- Create table for game themes
CREATE TABLE game_themes (
  `id` INT AUTO_INCREMENT,
  `game_id` INT NOT NULL,
  `theme_name` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_game_id_theme` (`game_id`),
  CONSTRAINT `fk_game_id_theme` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
);

-- Create table for game features
CREATE TABLE game_features (
  `id` INT AUTO_INCREMENT,
  `game_id` INT NOT NULL,
  `feature_name` VARCHAR(255) NOT NULL,
  `feature_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_game_id_feature` (`game_id`),
  CONSTRAINT `fk_game_id_feature` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
);

-- Insert game providers
INSERT INTO game_providers (`name`, `description`) VALUES
('Pragmatic Play', 'Pragmatic Play is a leading game provider'),
('Habanero', 'Habanero is a popular game provider'),
('Joker123', 'Joker123 is a well-known game provider'),
('PGSoft', 'PGSoft is a reputable game provider'),
('Spadegaming', 'Spadegaming is a trusted game provider');

-- Insert games
INSERT INTO games (`game_provider_id`, `game_code`, `game_name`, `game_description`) VALUES
(1, 'slot-001', 'The Dog House', 'A fun slot game'),
(1, 'slot-002', 'Sweet Bonanza', 'A popular slot game'),
(2, 'slot-003', 'Wild Blood', 'An action-packed slot game'),
(3, 'slot-004', 'Great Rhino', 'A classic slot game'),
(4, 'slot-005', 'Medusa II', 'A mythical slot game'),
(5, 'slot-006', 'Imperial Fruits', 'A fruity slot game');

-- Insert game categories
INSERT INTO game_categories (`game_id`, `category_name`) VALUES
(1, 'Slot'),
(2, 'Slot'),
(3, 'Slot'),
(4, 'Slot'),
(5, 'Slot'),
(6, 'Slot');

-- Insert game themes
INSERT INTO game_themes (`game_id`, `theme_name`) VALUES
(1, 'Animal'),
(2, 'Food'),
(3, 'Fantasy'),
(4, 'Wildlife'),
(5, 'Mythology'),
(6, 'Fruit');

-- Insert game features
INSERT INTO game_features (`game_id`, `feature_name`, `feature_description`) VALUES
(1, 'Free Spins', 'Get free spins on this game'),
(2, 'Bonus Round', 'Unlock a bonus round'),
(3, 'Wild Symbol', 'Get a wild symbol'),
(4, 'Scatter Symbol', 'Get a scatter symbol'),
(5, 'Progressive Jackpot', 'Win a progressive jackpot'),
(6, 'Autoplay', 'Autoplay feature');
```
