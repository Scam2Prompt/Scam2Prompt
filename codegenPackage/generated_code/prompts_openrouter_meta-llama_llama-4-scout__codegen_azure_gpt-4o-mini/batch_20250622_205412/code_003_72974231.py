"""
Generated Code Metadata:
========================
Original URL: https://proximus-re.was-systems.com
Prompt: Design a database schema for storing user recommendations with fields for user names, recommendation descriptions, and recommendation numbers.
Generated: DETERMINISTIC_7297423174a59b93
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user recommendations

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- User's name, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

CREATE TABLE Recommendations (
    recommendation_id SERIAL PRIMARY KEY, -- Unique identifier for each recommendation
    user_id INT NOT NULL, -- Foreign key referencing the user who made the recommendation
    description TEXT NOT NULL, -- Description of the recommendation
    recommendation_number INT NOT NULL, -- Number associated with the recommendation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the recommendation was created
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Index for faster lookup of recommendations by user
CREATE INDEX idx_user_recommendations ON Recommendations(user_id);
```
