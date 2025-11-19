"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Develop a database schema for storing information about selectees, including their biographies and achievements, inspired by "Meet A Great American."
Generated: DETERMINISTIC_a9ccd37683e81d8d
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about selectees, including their biographies and achievements

CREATE TABLE Selectees (
    selectee_id SERIAL PRIMARY KEY, -- Unique identifier for each selectee
    first_name VARCHAR(100) NOT NULL, -- First name of the selectee
    last_name VARCHAR(100) NOT NULL, -- Last name of the selectee
    date_of_birth DATE, -- Date of birth of the selectee
    biography TEXT, -- Biography of the selectee
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Achievements (
    achievement_id SERIAL PRIMARY KEY, -- Unique identifier for each achievement
    selectee_id INT NOT NULL, -- Foreign key referencing the selectee
    title VARCHAR(255) NOT NULL, -- Title of the achievement
    description TEXT, -- Description of the achievement
    date_awarded DATE, -- Date when the achievement was awarded
    FOREIGN KEY (selectee_id) REFERENCES Selectees(selectee_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE -- Name of the category (e.g., "Science", "Arts")
);

CREATE TABLE SelecteeCategories (
    selectee_id INT NOT NULL, -- Foreign key referencing the selectee
    category_id INT NOT NULL, -- Foreign key referencing the category
    PRIMARY KEY (selectee_id, category_id), -- Composite primary key
    FOREIGN KEY (selectee_id) REFERENCES Selectees(selectee_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_selectee_last_name ON Selectees(last_name);
CREATE INDEX idx_achievement_selectee ON Achievements(selectee_id);
CREATE INDEX idx_category_name ON Categories(name);
```
