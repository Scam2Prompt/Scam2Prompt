"""
Generated Code Metadata:
========================
Original URL: https://k7play.top
Prompt: Design a database schema to store information about streaming services like K7 Play, including user data, content metadata, and subscription plans.
Generated: DETERMINISTIC_4f219e52e9e66d75
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a streaming service

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store content metadata
CREATE TABLE Content (
    content_id SERIAL PRIMARY KEY,        -- Unique identifier for each content item
    title VARCHAR(255) NOT NULL,          -- Title of the content
    description TEXT,                      -- Description of the content
    release_date DATE,                     -- Release date of the content
    genre VARCHAR(50),                     -- Genre of the content
    duration INT,                          -- Duration of the content in minutes
    rating DECIMAL(3, 2),                  -- Rating of the content (e.g., 4.5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Content creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store subscription plans
CREATE TABLE SubscriptionPlans (
    plan_id SERIAL PRIMARY KEY,            -- Unique identifier for each subscription plan
    plan_name VARCHAR(100) NOT NULL,      -- Name of the subscription plan
    price DECIMAL(10, 2) NOT NULL,        -- Price of the subscription plan
    duration_months INT NOT NULL,         -- Duration of the plan in months
    features TEXT,                        -- Features included in the subscription plan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Plan creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store user subscriptions
CREATE TABLE UserSubscriptions (
    subscription_id SERIAL PRIMARY KEY,    -- Unique identifier for each subscription record
    user_id INT NOT NULL,                  -- Foreign key referencing Users table
    plan_id INT NOT NULL,                  -- Foreign key referencing SubscriptionPlans table
    start_date DATE NOT NULL,              -- Start date of the subscription
    end_date DATE NOT NULL,                -- End date of the subscription
    status VARCHAR(20) NOT NULL DEFAULT 'active', -- Status of the subscription (active, cancelled, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Subscription record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Cascade delete on user removal
    FOREIGN KEY (plan_id) REFERENCES SubscriptionPlans(plan_id) ON DELETE CASCADE -- Cascade delete on plan removal
);

-- Create a table to store user content interactions (e.g., watch history, favorites)
CREATE TABLE UserContentInteractions (
    interaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each interaction record
    user_id INT NOT NULL,                  -- Foreign key referencing Users table
    content_id INT NOT NULL,               -- Foreign key referencing Content table
    interaction_type VARCHAR(20) NOT NULL, -- Type of interaction (e.g., 'watched', 'favorited')
    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the interaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Cascade delete on user removal
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE -- Cascade delete on content removal
);
```
