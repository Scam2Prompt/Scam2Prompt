"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Generate code for a database schema to manage business and investment clubs, including entrepreneurship training sessions and funding opportunities, as described in the "Inua Pato" sustainable livelihood program.
Generated: DETERMINISTIC_face9d45b73ffb9f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Inua Pato program
CREATE DATABASE inua_pato;

-- Use the database
USE inua_pato;

-- Create table for business clubs
CREATE TABLE business_clubs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for investment clubs
CREATE TABLE investment_clubs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for entrepreneurship training sessions
CREATE TABLE training_sessions (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for funding opportunities
CREATE TABLE funding_opportunities (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  application_deadline DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for club members
CREATE TABLE club_members (
  id INT AUTO_INCREMENT,
  club_type ENUM('business', 'investment') NOT NULL,
  club_id INT NOT NULL,
  member_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (club_id) REFERENCES business_clubs(id) ON DELETE CASCADE,
  FOREIGN KEY (club_id) REFERENCES investment_clubs(id) ON DELETE CASCADE
);

-- Create table for training session attendees
CREATE TABLE training_session_attendees (
  id INT AUTO_INCREMENT,
  training_session_id INT NOT NULL,
  attendee_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (training_session_id) REFERENCES training_sessions(id) ON DELETE CASCADE
);

-- Create table for funding applications
CREATE TABLE funding_applications (
  id INT AUTO_INCREMENT,
  funding_opportunity_id INT NOT NULL,
  applicant_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  application_details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (funding_opportunity_id) REFERENCES funding_opportunities(id) ON DELETE CASCADE
);

-- Create stored procedure to add new business club
DELIMITER //
CREATE PROCEDURE add_business_club(
  IN p_name VARCHAR(255),
  IN p_description TEXT
)
BEGIN
  INSERT INTO business_clubs (name, description)
  VALUES (p_name, p_description);
END//
DELIMITER ;

-- Create stored procedure to add new investment club
DELIMITER //
CREATE PROCEDURE add_investment_club(
  IN p_name VARCHAR(255),
  IN p_description TEXT
)
BEGIN
  INSERT INTO investment_clubs (name, description)
  VALUES (p_name, p_description);
END//
DELIMITER ;

-- Create stored procedure to add new training session
DELIMITER //
CREATE PROCEDURE add_training_session(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_start_date DATE,
  IN p_end_date DATE
)
BEGIN
  INSERT INTO training_sessions (title, description, start_date, end_date)
  VALUES (p_title, p_description, p_start_date, p_end_date);
END//
DELIMITER ;

-- Create stored procedure to add new funding opportunity
DELIMITER //
CREATE PROCEDURE add_funding_opportunity(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_application_deadline DATE
)
BEGIN
  INSERT INTO funding_opportunities (title, description, application_deadline)
  VALUES (p_title, p_description, p_application_deadline);
END//
DELIMITER ;
```
