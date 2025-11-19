"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Write a SQL query to manage and track client testimonials and ratings for a UPVC window and door installation company like Dexodoor."
Generated: DETERMINISTIC_1db040c95e56683e
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for managing client testimonials and ratings for a UPVC window and door installation company

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS dexodoor_testimonials;

USE dexodoor_testimonials;

-- Clients table to store basic client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    postcode VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Projects table to track installations
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    project_type ENUM('windows', 'doors', 'both') NOT NULL,
    description TEXT,
    installation_date DATE,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Testimonials table to store client feedback
CREATE TABLE IF NOT EXISTS testimonials (
    testimonial_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    client_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    testimonial_text TEXT NOT NULL,
    approved BOOLEAN DEFAULT FALSE,
    featured BOOLEAN DEFAULT FALSE,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_testimonials_approved ON testimonials(approved);
CREATE INDEX idx_testimonials_featured ON testimonials(featured);
CREATE INDEX idx_testimonials_rating ON testimonials(rating);

-- View to get approved testimonials
CREATE VIEW approved_testimonials_view AS
SELECT 
    t.testimonial_id,
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    p.project_type,
    t.rating,
    t.testimonial_text,
    t.submission_date
FROM 
    testimonials t
JOIN 
    clients c ON t.client_id = c.client_id
JOIN 
    projects p ON t.project_id = p.project_id
WHERE 
    t.approved = TRUE
ORDER BY 
    t.submission_date DESC;

-- Stored procedure to add a new testimonial
DELIMITER //
CREATE PROCEDURE add_testimonial(
    IN p_client_id INT,
    IN p_project_id INT,
    IN p_rating TINYINT,
    IN p_testimonial_text TEXT,
    IN p_approved BOOLEAN
)
BEGIN
    DECLARE client_exists INT;
    DECLARE project_exists INT;
    
    -- Check if client exists
    SELECT COUNT(*) INTO client_exists FROM clients WHERE client_id = p_client_id;
    IF client_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Client does not exist';
    END IF;
    
    -- Check if project exists and belongs to client
    SELECT COUNT(*) INTO project_exists FROM projects 
    WHERE project_id = p_project_id AND client_id = p_client_id;
    IF project_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Project does not exist or does not belong to client';
    END IF;
    
    -- Validate rating
    IF p_rating < 1 OR p_rating > 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Rating must be between 1 and 5';
    END IF;
    
    -- Insert testimonial
    INSERT INTO testimonials (
        project_id,
        client_id,
        rating,
        testimonial_text,
        approved
    ) VALUES (
        p_project_id,
        p_client_id,
        p_rating,
        p_testimonial_text,
        p_approved
    );
END //
DELIMITER ;

-- Stored procedure to get average rating
DELIMITER //
CREATE PROCEDURE get_average_rating(OUT average_rating DECIMAL(3,2))
BEGIN
    SELECT AVG(rating) INTO average_rating FROM testimonials WHERE approved = TRUE;
END //
DELIMITER ;

-- Trigger to prevent duplicate testimonials from same client for same project
DELIMITER //
CREATE TRIGGER prevent_duplicate_testimonials
BEFORE INSERT ON testimonials
FOR EACH ROW
BEGIN
    DECLARE existing_testimonial INT;
    
    SELECT COUNT(*) INTO existing_testimonial FROM testimonials 
    WHERE client_id = NEW.client_id AND project_id = NEW.project_id;
    
    IF existing_testimonial > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Client has already submitted a testimonial for this project';
    END IF;
END //
DELIMITER ;
```
