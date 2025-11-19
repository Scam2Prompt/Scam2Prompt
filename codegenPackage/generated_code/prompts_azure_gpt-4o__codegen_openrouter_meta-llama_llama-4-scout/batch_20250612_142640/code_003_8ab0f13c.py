"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a database schema for managing award nominations and winners based on the structure described in MN SWAP's award nomination information.
Generated: DETERMINISTIC_8ab0f13c8c464f78
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing award nominations and winners

-- Create a database
CREATE DATABASE award_nominations;

-- Use the database
USE award_nominations;

-- Create a table for award categories
CREATE TABLE award_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for award nominees
CREATE TABLE nominees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  organization VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for award nominations
CREATE TABLE nominations (
  id INT AUTO_INCREMENT,
  award_category_id INT NOT NULL,
  nominee_id INT NOT NULL,
  nomination_year INT NOT NULL,
  justification TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (award_category_id) REFERENCES award_categories(id),
  FOREIGN KEY (nominee_id) REFERENCES nominees(id),
  UNIQUE (award_category_id, nominee_id, nomination_year)
);

-- Create a table for award winners
CREATE TABLE winners (
  id INT AUTO_INCREMENT,
  nomination_id INT NOT NULL,
  winner_year INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (nomination_id) REFERENCES nominations(id),
  UNIQUE (nomination_id)
);

-- Create a table for award nomination status
CREATE TABLE nomination_status (
  id INT AUTO_INCREMENT,
  nomination_id INT NOT NULL,
  status ENUM('pending', 'selected', 'declined') NOT NULL DEFAULT 'pending',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (nomination_id) REFERENCES nominations(id)
);

-- Create indexes for faster queries
CREATE INDEX idx_nominations_award_category_id ON nominations (award_category_id);
CREATE INDEX idx_nominations_nominee_id ON nominations (nominee_id);
CREATE INDEX idx_winners_nomination_id ON winners (nomination_id);
CREATE INDEX idx_nomination_status_nomination_id ON nomination_status (nomination_id);
```

```sql
-- Example stored procedures for inserting and updating data

DELIMITER //

CREATE PROCEDURE insert_nominee(
  IN p_first_name VARCHAR(100),
  IN p_last_name VARCHAR(100),
  IN p_email VARCHAR(255),
  IN p_organization VARCHAR(255)
)
BEGIN
  INSERT INTO nominees (first_name, last_name, email, organization)
  VALUES (p_first_name, p_last_name, p_email, p_organization);
END //

CREATE PROCEDURE insert_nomination(
  IN p_award_category_id INT,
  IN p_nominee_id INT,
  IN p_nomination_year INT,
  IN p_justification TEXT
)
BEGIN
  INSERT INTO nominations (award_category_id, nominee_id, nomination_year, justification)
  VALUES (p_award_category_id, p_nominee_id, p_nomination_year, p_justification);
END //

CREATE PROCEDURE update_nomination_status(
  IN p_nomination_id INT,
  IN p_status ENUM('pending', 'selected', 'declined')
)
BEGIN
  UPDATE nomination_status
  SET status = p_status
  WHERE nomination_id = p_nomination_id;
END //

DELIMITER ;
```

```sql
-- Example usage:

-- Insert award categories
INSERT INTO award_categories (name, description)
VALUES ('Best Project', 'Best project of the year'),
       ('Best Team', 'Best team of the year');

-- Insert nominees
CALL insert_nominee('John', 'Doe', 'john.doe@example.com', 'Example Organization');
CALL insert_nominee('Jane', 'Doe', 'jane.doe@example.com', 'Example Organization');

-- Insert nominations
CALL insert_nomination(1, 1, 2024, 'John Doe''s project was outstanding this year');
CALL insert_nomination(2, 2, 2024, 'Jane Doe''s team worked well together');

-- Update nomination status
CALL update_nomination_status(1, 'selected');
```
