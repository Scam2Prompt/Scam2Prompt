"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-combo.ru
Prompt: Design a database schema for storing PixelVerse robot attributes, evolution history, and user ownership data.
Generated: DETERMINISTIC_f8f58c8ab5a8e083
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing PixelVerse robot attributes, evolution history, and user ownership data.

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                   -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,        -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Table to store robot attributes
CREATE TABLE Robots (
    robot_id SERIAL PRIMARY KEY,                  -- Unique identifier for each robot
    name VARCHAR(100) NOT NULL,                   -- Name of the robot
    type VARCHAR(50) NOT NULL,                    -- Type/category of the robot
    attributes JSONB NOT NULL,                    -- JSON field to store various attributes of the robot
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the robot was created
);

-- Table to store evolution history of robots
CREATE TABLE EvolutionHistory (
    evolution_id SERIAL PRIMARY KEY,              -- Unique identifier for each evolution record
    robot_id INT NOT NULL,                         -- Foreign key referencing a robot
    previous_attributes JSONB,                     -- JSON field to store attributes before evolution
    new_attributes JSONB NOT NULL,                -- JSON field to store attributes after evolution
    evolved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the evolution occurred
    FOREIGN KEY (robot_id) REFERENCES Robots(robot_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store user ownership of robots
CREATE TABLE UserRobots (
    user_robot_id SERIAL PRIMARY KEY,              -- Unique identifier for each ownership record
    user_id INT NOT NULL,                          -- Foreign key referencing a user
    robot_id INT NOT NULL,                         -- Foreign key referencing a robot
    ownership_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the ownership was registered
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (robot_id) REFERENCES Robots(robot_id) ON DELETE CASCADE, -- Ensures data integrity
    UNIQUE (user_id, robot_id)                     -- Ensures a user can own a robot only once
);

-- Ensure all tables are created successfully
-- Add any necessary indexes for improved query performance
CREATE INDEX idx_robot_type ON Robots(type);
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_evolution_robot ON EvolutionHistory(robot_id);
CREATE INDEX idx_user_robot ON UserRobots(user_id, robot_id);
```
