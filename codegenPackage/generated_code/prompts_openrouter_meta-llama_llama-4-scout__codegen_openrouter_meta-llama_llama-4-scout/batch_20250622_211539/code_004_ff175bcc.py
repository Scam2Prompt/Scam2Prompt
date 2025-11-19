"""
Generated Code Metadata:
========================
Original URL: https://odishaolympic.org
Prompt: Design a database schema to store information about athletes, awards, and achievements, inspired by the Odisha Olympic Association's data.
Generated: DETERMINISTIC_ff175bcc6ae3f8a3
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Odisha Olympic Association
CREATE DATABASE odisha_olympic_association;

-- Use the database
USE odisha_olympic_association;

-- Create a table to store athlete information
CREATE TABLE athletes (
    athlete_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    sport VARCHAR(100) NOT NULL,
    PRIMARY KEY (athlete_id)
);

-- Create a table to store award information
CREATE TABLE awards (
    award_id INT AUTO_INCREMENT,
    award_name VARCHAR(255) NOT NULL,
    award_description TEXT,
    PRIMARY KEY (award_id)
);

-- Create a table to store achievement information
CREATE TABLE achievements (
    achievement_id INT AUTO_INCREMENT,
    athlete_id INT NOT NULL,
    award_id INT,
    achievement_date DATE NOT NULL,
    achievement_description TEXT,
    PRIMARY KEY (achievement_id),
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (award_id) REFERENCES awards(award_id) ON DELETE SET NULL
);

-- Create a table to store Olympic games information
CREATE TABLE olympic_games (
    game_id INT AUTO_INCREMENT,
    game_name VARCHAR(255) NOT NULL,
    game_date DATE NOT NULL,
    location VARCHAR(255) NOT NULL,
    PRIMARY KEY (game_id)
);

-- Create a table to store athlete participation in Olympic games
CREATE TABLE athlete_participations (
    participation_id INT AUTO_INCREMENT,
    athlete_id INT NOT NULL,
    game_id INT NOT NULL,
    sport VARCHAR(100) NOT NULL,
    event VARCHAR(100) NOT NULL,
    PRIMARY KEY (participation_id),
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES olympic_games(game_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert athlete information
DELIMITER //
CREATE PROCEDURE insert_athlete(
    IN p_first_name VARCHAR(255),
    IN p_last_name VARCHAR(255),
    IN p_date_of_birth DATE,
    IN p_email VARCHAR(255),
    IN p_phone_number VARCHAR(20),
    IN p_address VARCHAR(255),
    IN p_sport VARCHAR(100)
)
BEGIN
    INSERT INTO athletes (first_name, last_name, date_of_birth, email, phone_number, address, sport)
    VALUES (p_first_name, p_last_name, p_date_of_birth, p_email, p_phone_number, p_address, p_sport);
END//
DELIMITER ;

-- Create a stored procedure to insert award information
DELIMITER //
CREATE PROCEDURE insert_award(
    IN p_award_name VARCHAR(255),
    IN p_award_description TEXT
)
BEGIN
    INSERT INTO awards (award_name, award_description)
    VALUES (p_award_name, p_award_description);
END//
DELIMITER ;

-- Create a stored procedure to insert achievement information
DELIMITER //
CREATE PROCEDURE insert_achievement(
    IN p_athlete_id INT,
    IN p_award_id INT,
    IN p_achievement_date DATE,
    IN p_achievement_description TEXT
)
BEGIN
    INSERT INTO achievements (athlete_id, award_id, achievement_date, achievement_description)
    VALUES (p_athlete_id, p_award_id, p_achievement_date, p_achievement_description);
END//
DELIMITER ;

-- Example usage:
CALL insert_athlete('John', 'Doe', '1990-01-01', 'john@example.com', '1234567890', 'New York', 'Swimming');
CALL insert_award('Gold Medal', 'First place in a competition');
CALL insert_achievement(1, 1, '2020-01-01', 'Won gold medal in swimming');

-- Select all athletes
SELECT * FROM athletes;

-- Select all awards
SELECT * FROM awards;

-- Select all achievements
SELECT * FROM achievements;
```
