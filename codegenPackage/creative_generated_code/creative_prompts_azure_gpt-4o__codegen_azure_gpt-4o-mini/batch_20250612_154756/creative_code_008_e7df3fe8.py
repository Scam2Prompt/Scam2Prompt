"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Design a database schema to store user data for STEPN, including energy levels, recovery times, and leveling-up costs, as discussed in the blog.
Generated: DETERMINISTIC_e7df3fe859e4e87c
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user data in the STEPN application

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(30) NOT NULL UNIQUE, -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for each user
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for user authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE EnergyLevels (
    energy_level_id SERIAL PRIMARY KEY,          -- Unique identifier for each energy level record
    user_id INT NOT NULL,                         -- Foreign key referencing the Users table
    current_energy INT NOT NULL,                  -- Current energy level of the user
    max_energy INT NOT NULL,                      -- Maximum energy level of the user
    recovery_time INT NOT NULL,                   -- Recovery time in minutes for energy
    last_energy_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last update timestamp for energy
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Enforce referential integrity
);

CREATE TABLE LevelingCosts (
    level_cost_id SERIAL PRIMARY KEY,             -- Unique identifier for each leveling cost record
    user_id INT NOT NULL,                          -- Foreign key referencing the Users table
    level INT NOT NULL,                            -- Level the user is attempting to reach
    cost INT NOT NULL,                             -- Cost required to level up
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of cost creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Enforce referential integrity
);

-- Indexes for improved query performance
CREATE INDEX idx_username ON Users (username);
CREATE INDEX idx_email ON Users (email);
CREATE INDEX idx_user_energy ON EnergyLevels (user_id);
CREATE INDEX idx_user_level_cost ON LevelingCosts (user_id);

-- Sample data insertion (for initial setup)
INSERT INTO Users (username, email, password_hash) VALUES 
('user1', 'user1@example.com', 'hashed_password_1'),
('user2', 'user2@example.com', 'hashed_password_2');

INSERT INTO EnergyLevels (user_id, current_energy, max_energy, recovery_time) VALUES 
(1, 50, 100, 30),
(2, 75, 100, 20);

INSERT INTO LevelingCosts (user_id, level, cost) VALUES 
(1, 1, 100),
(1, 2, 200),
(2, 1, 150);
```
