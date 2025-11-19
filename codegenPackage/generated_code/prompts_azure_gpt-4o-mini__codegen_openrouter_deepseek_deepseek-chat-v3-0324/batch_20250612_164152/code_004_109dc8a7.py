"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Construct a database schema for storing information about comic books, focusing on the "Top G" series and its unique features like collectible editions.
Generated: DETERMINISTIC_109dc8a78bf3d965
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Comic Book Store (Top G Series Focus)

```sql
-- Database schema for storing information about comic books, with focus on Top G series
-- Includes support for collectible editions and related features

CREATE TABLE publishers (
    publisher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    founded_year INT,
    headquarters VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE series (
    series_id INT PRIMARY KEY AUTO_INCREMENT,
    publisher_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    start_year INT NOT NULL,
    end_year INT,
    ongoing BOOLEAN DEFAULT TRUE,
    description TEXT,
    is_top_g_series BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id),
    INDEX (title),
    INDEX (is_top_g_series)
);

CREATE TABLE issues (
    issue_id INT PRIMARY KEY AUTO_INCREMENT,
    series_id INT NOT NULL,
    issue_number VARCHAR(20) NOT NULL,
    title VARCHAR(255),
    release_date DATE NOT NULL,
    cover_price DECIMAL(10,2),
    page_count INT,
    isbn VARCHAR(20),
    description TEXT,
    is_special_edition BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (series_id) REFERENCES series(series_id),
    UNIQUE KEY (series_id, issue_number),
    INDEX (release_date)
);

CREATE TABLE collectible_editions (
    edition_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT NOT NULL,
    edition_type ENUM('Variant Cover', 'Signed', 'Graded', 'Limited Run', 'Special Foil') NOT NULL,
    limited_run_count INT,
    grade DECIMAL(3,1),
    grader VARCHAR(50),
    certification_number VARCHAR(50),
    additional_features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
    INDEX (edition_type),
    INDEX (grade)
);

CREATE TABLE creators (
    creator_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    country VARCHAR(50),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (full_name)
);

CREATE TABLE creator_roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE issue_creators (
    issue_creator_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT NOT NULL,
    creator_id INT NOT NULL,
    role_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
    FOREIGN KEY (creator_id) REFERENCES creators(creator_id),
    FOREIGN KEY (role_id) REFERENCES creator_roles(role_id),
    UNIQUE KEY (issue_id, creator_id, role_id)
);

CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT,
    edition_id INT,
    condition ENUM('Mint', 'Near Mint', 'Very Fine', 'Fine', 'Good', 'Fair', 'Poor') NOT NULL,
    quantity_in_stock INT DEFAULT 0,
    price DECIMAL(10,2),
    last_restocked DATE,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
    FOREIGN KEY (edition_id) REFERENCES collectible_editions(edition_id),
    CHECK (issue_id IS NOT NULL OR edition_id IS NOT NULL),
    INDEX (condition),
    INDEX (is_available)
);

CREATE TABLE top_g_special_features (
    feature_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT NOT NULL,
    feature_type ENUM('Holographic Cover', 'Embedded Token', 'Augmented Reality', 'Special Insert', 'Collector Card') NOT NULL,
    description TEXT,
    rarity ENUM('Common', 'Uncommon', 'Rare', 'Ultra Rare', 'One of a Kind') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
    INDEX (feature_type),
    INDEX (rarity)
);

-- Stored procedure for adding new Top G series issues with validation
DELIMITER //
CREATE PROCEDURE add_top_g_issue(
    IN p_series_id INT,
    IN p_issue_number VARCHAR(20),
    IN p_title VARCHAR(255),
    IN p_release_date DATE,
    IN p_cover_price DECIMAL(10,2),
    IN p_page_count INT,
    IN p_description TEXT,
    IN p_is_special_edition BOOLEAN,
    OUT p_issue_id INT
)
BEGIN
    DECLARE is_top_g BOOLEAN;
    
    -- Check if series is a Top G series
    SELECT is_top_g_series INTO is_top_g FROM series WHERE series_id = p_series_id;
    
    IF is_top_g THEN
        INSERT INTO issues (
            series_id, 
            issue_number, 
            title, 
            release_date, 
            cover_price, 
            page_count, 
            description, 
            is_special_edition
        ) VALUES (
            p_series_id, 
            p_issue_number, 
            p_title, 
            p_release_date, 
            p_cover_price, 
            p_page_count, 
            p_description, 
            p_is_special_edition
        );
        
        SET p_issue_id = LAST_INSERT_ID();
    ELSE
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Cannot add issue: Specified series is not a Top G series';
    END IF;
END //
DELIMITER ;

-- View for Top G series collectible editions
CREATE VIEW top_g_collectibles AS
SELECT 
    s.title AS series_title,
    i.issue_number,
    i.title AS issue_title,
    ce.edition_type,
    ce.grade,
    ce.limited_run_count,
    inv.price,
    inv.condition
FROM 
    collectible_editions ce
JOIN 
    issues i ON ce.issue_id = i.issue_id
JOIN 
    series s ON i.series_id = s.series_id
JOIN 
    inventory inv ON (inv.edition_id = ce.edition_id OR inv.issue_id = i.issue_id)
WHERE 
    s.is_top_g_series = TRUE
ORDER BY 
    s.title, i.issue_number, ce.edition_type;
```
