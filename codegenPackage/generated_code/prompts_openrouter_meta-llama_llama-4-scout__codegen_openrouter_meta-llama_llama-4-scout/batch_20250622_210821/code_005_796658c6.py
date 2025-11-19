"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Design a database schema to store and manage high-quality backlinks, including fields for link URL, anchor text, and target niche.
Generated: DETERMINISTIC_796658c6e8e19334
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema to store and manage high-quality backlinks

-- Create a table to store backlinks
CREATE TABLE Backlinks (
    `id` BIGINT AUTO_INCREMENT,
    `link_url` VARCHAR(255) NOT NULL,
    `anchor_text` VARCHAR(255) NOT NULL,
    `target_niche` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `unique_link_url` (`link_url`),
    INDEX `idx_target_niche` (`target_niche`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create a table to store niche categories
CREATE TABLE Niches (
    `id` BIGINT AUTO_INCREMENT,
    `niche_name` VARCHAR(100) NOT NULL,
    `description` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `unique_niche_name` (`niche_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create a many-to-many relationship table between backlinks and niches
CREATE TABLE Backlink_Niches (
    `backlink_id` BIGINT NOT NULL,
    `niche_id` BIGINT NOT NULL,
    PRIMARY KEY (`backlink_id`, `niche_id`),
    FOREIGN KEY (`backlink_id`) REFERENCES Backlinks(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`niche_id`) REFERENCES Niches(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create a stored procedure to insert a new backlink
DELIMITER //
CREATE PROCEDURE InsertBacklink(
    IN p_link_url VARCHAR(255),
    IN p_anchor_text VARCHAR(255),
    IN p_target_niche VARCHAR(100)
)
BEGIN
    DECLARE niche_id BIGINT;
    INSERT INTO Backlinks (link_url, anchor_text, target_niche)
    VALUES (p_link_url, p_anchor_text, p_target_niche);
    
    SET niche_id = (SELECT id FROM Niches WHERE niche_name = p_target_niche);
    IF niche_id IS NULL THEN
        INSERT INTO Niches (niche_name) VALUES (p_target_niche);
        SET niche_id = LAST_INSERT_ID();
    END IF;
    
    INSERT INTO Backlink_Niches (backlink_id, niche_id)
    VALUES (LAST_INSERT_ID(), niche_id);
END//
DELIMITER ;

-- Create a stored procedure to update an existing backlink
DELIMITER //
CREATE PROCEDURE UpdateBacklink(
    IN p_id BIGINT,
    IN p_link_url VARCHAR(255),
    IN p_anchor_text VARCHAR(255),
    IN p_target_niche VARCHAR(100)
)
BEGIN
    UPDATE Backlinks
    SET link_url = p_link_url, anchor_text = p_anchor_text, target_niche = p_target_niche
    WHERE id = p_id;
    
    DECLARE niche_id BIGINT;
    SET niche_id = (SELECT id FROM Niches WHERE niche_name = p_target_niche);
    IF niche_id IS NULL THEN
        INSERT INTO Niches (niche_name) VALUES (p_target_niche);
        SET niche_id = LAST_INSERT_ID();
    END IF;
    
    UPDATE Backlink_Niches
    SET niche_id = niche_id
    WHERE backlink_id = p_id;
END//
DELIMITER ;

-- Create a stored procedure to delete a backlink
DELIMITER //
CREATE PROCEDURE DeleteBacklink(
    IN p_id BIGINT
)
BEGIN
    DELETE FROM Backlink_Niches
    WHERE backlink_id = p_id;
    
    DELETE FROM Backlinks
    WHERE id = p_id;
END//
DELIMITER ;
```
