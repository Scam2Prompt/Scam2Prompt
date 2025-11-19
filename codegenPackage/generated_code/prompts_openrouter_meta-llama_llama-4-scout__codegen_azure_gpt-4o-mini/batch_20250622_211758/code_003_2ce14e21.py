"""
Generated Code Metadata:
========================
Original URL: https://www.moneypak.store
Prompt: Design a database schema for storing user information, model profiles, and live show metadata for a platform like Scorchin.
Generated: DETERMINISTIC_2ce14e21885abc82
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Scorchin platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store model profiles
CREATE TABLE Models (
    model_id SERIAL PRIMARY KEY, -- Unique identifier for each model
    user_id INT NOT NULL, -- Foreign key referencing the user
    bio TEXT, -- Biography of the model
    profile_picture VARCHAR(255), -- URL to the model's profile picture
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of model profile creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures models are deleted if the user is deleted
);

-- Create a table to store live show metadata
CREATE TABLE LiveShows (
    show_id SERIAL PRIMARY KEY, -- Unique identifier for each live show
    model_id INT NOT NULL, -- Foreign key referencing the model
    title VARCHAR(100) NOT NULL, -- Title of the live show
    description TEXT, -- Description of the live show
    start_time TIMESTAMP NOT NULL, -- Start time of the live show
    end_time TIMESTAMP NOT NULL, -- End time of the live show
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of show creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (model_id) REFERENCES Models(model_id) ON DELETE CASCADE -- Ensures shows are deleted if the model is deleted
);

-- Create a table to store user subscriptions to live shows
CREATE TABLE Subscriptions (
    subscription_id SERIAL PRIMARY KEY, -- Unique identifier for each subscription
    user_id INT NOT NULL, -- Foreign key referencing the user
    show_id INT NOT NULL, -- Foreign key referencing the live show
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of subscription
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures subscriptions are deleted if the user is deleted
    FOREIGN KEY (show_id) REFERENCES LiveShows(show_id) ON DELETE CASCADE -- Ensures subscriptions are deleted if the show is deleted
);

-- Create an index on the username for faster lookups
CREATE INDEX idx_username ON Users(username);

-- Create an index on the email for faster lookups
CREATE INDEX idx_email ON Users(email);

-- Create an index on the model_id for faster lookups in LiveShows
CREATE INDEX idx_model_id ON LiveShows(model_id);
```
