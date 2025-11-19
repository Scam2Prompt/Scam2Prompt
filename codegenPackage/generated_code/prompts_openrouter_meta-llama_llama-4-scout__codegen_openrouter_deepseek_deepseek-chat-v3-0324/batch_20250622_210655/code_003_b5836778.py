"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: "Create a SQL database schema to store information about hiking excursions, including columns for destination, date, and description."
Generated: DETERMINISTIC_b5836778b018b43f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a hiking excursions database schema
-- Table: excursions
-- Purpose: Stores information about hiking trips

CREATE TABLE excursions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    destination VARCHAR(100) NOT NULL,
    hike_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Ensure destination is not empty
    CONSTRAINT chk_destination CHECK (destination <> ''),
    
    -- Ensure date is not in the future
    CONSTRAINT chk_date CHECK (hike_date <= CURRENT_DATE)
);

-- Index for frequently queried columns
CREATE INDEX idx_excursion_destination ON excursions(destination);
CREATE INDEX idx_excursion_date ON excursions(hike_date);

-- Optional: Table for excursion participants if needed
CREATE TABLE participants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    excursion_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (excursion_id) REFERENCES excursions(id) ON DELETE CASCADE,
    
    CONSTRAINT chk_name CHECK (name <> ''),
    CONSTRAINT chk_email_format CHECK (email LIKE '%_@__%.__%')
);

-- Optional: Table for excursion photos if needed
CREATE TABLE photos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    excursion_id INT NOT NULL,
    photo_url VARCHAR(255) NOT NULL,
    caption VARCHAR(200),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (excursion_id) REFERENCES excursions(id) ON DELETE CASCADE,
    
    CONSTRAINT chk_photo_url CHECK (photo_url <> '')
);
```
