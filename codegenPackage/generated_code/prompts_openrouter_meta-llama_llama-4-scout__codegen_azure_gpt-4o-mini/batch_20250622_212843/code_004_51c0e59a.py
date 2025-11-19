"""
Generated Code Metadata:
========================
Original URL: https://wphosting.in
Prompt: "Design a database schema for storing WordPress hosting plans and their features."
Generated: DETERMINISTIC_51c0e59a1a783b63
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing WordPress hosting plans and their features

-- Create a table for hosting plans
CREATE TABLE hosting_plans (
    id SERIAL PRIMARY KEY, -- Unique identifier for each hosting plan
    name VARCHAR(255) NOT NULL, -- Name of the hosting plan
    price DECIMAL(10, 2) NOT NULL, -- Monthly price of the hosting plan
    storage_limit INT NOT NULL, -- Storage limit in GB
    bandwidth_limit INT NOT NULL, -- Bandwidth limit in GB
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the plan was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for features
CREATE TABLE features (
    id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    name VARCHAR(255) NOT NULL, -- Name of the feature
    description TEXT, -- Description of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feature was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a junction table to associate hosting plans with features
CREATE TABLE hosting_plan_features (
    hosting_plan_id INT NOT NULL, -- Foreign key referencing hosting plans
    feature_id INT NOT NULL, -- Foreign key referencing features
    PRIMARY KEY (hosting_plan_id, feature_id), -- Composite primary key
    FOREIGN KEY (hosting_plan_id) REFERENCES hosting_plans(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (feature_id) REFERENCES features(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion for hosting plans
INSERT INTO hosting_plans (name, price, storage_limit, bandwidth_limit) VALUES
('Basic Plan', 5.99, 10, 100),
('Standard Plan', 9.99, 20, 200),
('Premium Plan', 19.99, 50, 500);

-- Sample data insertion for features
INSERT INTO features (name, description) VALUES
('Free SSL', 'Includes a free SSL certificate for secure connections.'),
('Daily Backups', 'Automatic daily backups of your website.'),
('24/7 Support', 'Access to customer support at any time.');

-- Sample data insertion for hosting plan features
INSERT INTO hosting_plan_features (hosting_plan_id, feature_id) VALUES
(1, 1), -- Basic Plan includes Free SSL
(1, 2), -- Basic Plan includes Daily Backups
(2, 1), -- Standard Plan includes Free SSL
(2, 2), -- Standard Plan includes Daily Backups
(2, 3), -- Standard Plan includes 24/7 Support
(3, 1), -- Premium Plan includes Free SSL
(3, 2), -- Premium Plan includes Daily Backups
(3, 3); -- Premium Plan includes 24/7 Support
```
