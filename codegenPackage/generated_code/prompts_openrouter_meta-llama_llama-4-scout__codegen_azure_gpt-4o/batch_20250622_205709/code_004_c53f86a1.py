"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Design a database schema for storing information about cofradías (brotherhoods) including details like sede (headquarters), patrimonio (heritage), and insignias (insignia).
Generated: DETERMINISTIC_c53f86a147d7bc66
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cofradías (brotherhoods)

-- Table: Cofradias
-- This table stores the main information about each cofradía.
CREATE TABLE Cofradias (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cofradía
    nombre VARCHAR(255) NOT NULL,      -- Name of the cofradía
    sede VARCHAR(255) NOT NULL,        -- Headquarters of the cofradía
    patrimonio TEXT,                   -- Description of the heritage of the cofradía
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Insignias
-- This table stores information about the insignias associated with each cofradía.
CREATE TABLE Insignias (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each insignia
    cofradia_id INT NOT NULL,          -- Foreign key referencing the Cofradias table
    nombre VARCHAR(255) NOT NULL,      -- Name of the insignia
    descripcion TEXT,                  -- Description of the insignia
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (cofradia_id) REFERENCES Cofradias(id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_cofradia_nombre ON Cofradias(nombre); -- Index for searching cofradías by name
CREATE INDEX idx_insignia_nombre ON Insignias(nombre); -- Index for searching insignias by name

-- Example error handling: Ensure the database engine supports foreign keys
-- This schema assumes the use of InnoDB as the storage engine for MySQL/MariaDB.
```
