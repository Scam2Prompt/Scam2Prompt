"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Design a MySQL database schema to store information about ECBC Radio's programs, hosts, and playlists, and provide a sample query to retrieve the program schedule for a specific day of the week.
Generated: DETERMINISTIC_c3bf2a5330a77c5f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ECBC Radio's programs, hosts, and playlists
CREATE DATABASE IF NOT EXISTS ecbc_radio;
USE ecbc_radio;

-- Table to store information about hosts
CREATE TABLE IF NOT EXISTS hosts (
    host_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT,
    email VARCHAR(100) UNIQUE,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table to store program categories
CREATE TABLE IF NOT EXISTS program_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table to store programs
CREATE TABLE IF NOT EXISTS programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT,
    duration_minutes INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES program_categories(category_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Junction table for program-host many-to-many relationship
CREATE TABLE IF NOT EXISTS program_hosts (
    program_host_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    host_id INT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE CASCADE,
    UNIQUE KEY (program_id, host_id)
) ENGINE=InnoDB;

-- Table to store weekly schedule
CREATE TABLE IF NOT EXISTS program_schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    day_of_week TINYINT NOT NULL COMMENT '0=Sunday, 1=Monday, ..., 6=Saturday',
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    timezone VARCHAR(50) DEFAULT 'UTC',
    is_recurring BOOLEAN DEFAULT TRUE,
    valid_from DATE,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    CHECK (day_of_week BETWEEN 0 AND 6),
    CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Table to store playlists
CREATE TABLE IF NOT EXISTS playlists (
    playlist_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    air_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (program_id, air_date)
) ENGINE=InnoDB;

-- Table to store playlist tracks
CREATE TABLE IF NOT EXISTS playlist_tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    playlist_id INT NOT NULL,
    position INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    album VARCHAR(255),
    duration_seconds INT NOT NULL,
    isrc VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    UNIQUE KEY (playlist_id, position)
) ENGINE=InnoDB;

-- Sample query to retrieve program schedule for a specific day of the week
SELECT 
    p.title AS program_title,
    GROUP_CONCAT(h.name SEPARATOR ', ') AS hosts,
    ps.day_of_week,
    ps.start_time,
    ps.end_time,
    pc.name AS category
FROM 
    program_schedule ps
JOIN 
    programs p ON ps.program_id = p.program_id
LEFT JOIN 
    program_hosts ph ON p.program_id = ph.program_id
LEFT JOIN 
    hosts h ON ph.host_id = h.host_id
LEFT JOIN 
    program_categories pc ON p.category_id = pc.category_id
WHERE 
    ps.day_of_week = 2 -- Tuesday (0=Sunday, 1=Monday, etc.)
    AND (ps.valid_to IS NULL OR ps.valid_to >= CURDATE())
    AND (ps.valid_from IS NULL OR ps.valid_from <= CURDATE())
    AND p.is_active = TRUE
GROUP BY 
    p.program_id, ps.schedule_id
ORDER BY 
    ps.start_time;
```
