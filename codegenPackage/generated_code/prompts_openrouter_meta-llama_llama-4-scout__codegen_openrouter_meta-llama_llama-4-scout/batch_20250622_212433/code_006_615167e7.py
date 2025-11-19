"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a SQL query to manage and track player resources, such as poop, chests, and vouchers, within the SIMemes game database.
Generated: DETERMINISTIC_615167e74056de2c
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create table for players
CREATE TABLE IF NOT EXISTS players (
    player_id INT AUTO_INCREMENT,
    player_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (player_id)
);

-- Create table for resources
CREATE TABLE IF NOT EXISTS resources (
    resource_id INT AUTO_INCREMENT,
    resource_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (resource_id)
);

-- Create table for player resources
CREATE TABLE IF NOT EXISTS player_resources (
    player_id INT NOT NULL,
    resource_id INT NOT NULL,
    quantity INT DEFAULT 0,
    PRIMARY KEY (player_id, resource_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id)
);

-- Insert initial resources
INSERT INTO resources (resource_name) 
VALUES 
('poop'),
('chests'),
('vouchers')
ON DUPLICATE KEY UPDATE resource_name = resource_name;

-- Procedure to add player resource
DELIMITER //
CREATE PROCEDURE add_player_resource(
    IN p_player_id INT,
    IN p_resource_name VARCHAR(255),
    IN p_quantity INT
)
BEGIN
    DECLARE resource_id INT;
    SET resource_id = (SELECT resource_id FROM resources WHERE resource_name = p_resource_name);
    
    IF resource_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Resource does not exist';
    END IF;
    
    INSERT INTO player_resources (player_id, resource_id, quantity) 
    VALUES (p_player_id, resource_id, p_quantity)
    ON DUPLICATE KEY UPDATE quantity = quantity + p_quantity;
END//
DELIMITER ;

-- Procedure to remove player resource
DELIMITER //
CREATE PROCEDURE remove_player_resource(
    IN p_player_id INT,
    IN p_resource_name VARCHAR(255),
    IN p_quantity INT
)
BEGIN
    DECLARE resource_id INT;
    SET resource_id = (SELECT resource_id FROM resources WHERE resource_name = p_resource_name);
    
    IF resource_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Resource does not exist';
    END IF;
    
    UPDATE player_resources 
    SET quantity = quantity - p_quantity 
    WHERE player_id = p_player_id AND resource_id = resource_id;
    
    IF ROW_COUNT() = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough resources';
    END IF;
END//
DELIMITER ;

-- Procedure to get player resource
DELIMITER //
CREATE PROCEDURE get_player_resource(
    IN p_player_id INT,
    IN p_resource_name VARCHAR(255)
)
BEGIN
    DECLARE resource_id INT;
    SET resource_id = (SELECT resource_id FROM resources WHERE resource_name = p_resource_name);
    
    IF resource_id IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Resource does not exist';
    END IF;
    
    SELECT pr.quantity 
    FROM player_resources pr 
    WHERE pr.player_id = p_player_id AND pr.resource_id = resource_id;
END//
DELIMITER ;

-- Example usage
CALL add_player_resource(1, 'poop', 100);
CALL add_player_resource(1, 'chests', 5);
CALL add_player_resource(1, 'vouchers', 10);

CALL get_player_resource(1, 'poop');

CALL remove_player_resource(1, 'poop', 50);

CALL get_player_resource(1, 'poop');
```
