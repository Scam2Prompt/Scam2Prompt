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
-- schema.sql

-- Create database for streaming service
CREATE DATABASE streaming_service;

-- Use the database
USE streaming_service;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for content metadata
CREATE TABLE content (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  genre VARCHAR(255),
  director VARCHAR(255),
  release_year INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for subscription plans
CREATE TABLE subscription_plans (
  id INT AUTO_INCREMENT,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user subscriptions
CREATE TABLE user_subscriptions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  subscription_plan_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (subscription_plan_id) REFERENCES subscription_plans(id) ON DELETE CASCADE
);

-- Create table for user content ratings
CREATE TABLE user_ratings (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  content_id INT NOT NULL,
  rating TINYINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE,
  CHECK (rating BETWEEN 1 AND 5)
);

-- Create table for user content watch history
CREATE TABLE user_watch_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  content_id INT NOT NULL,
  watch_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO users (email, password, name)
VALUES 
('john.doe@example.com', 'password123', 'John Doe'),
('jane.doe@example.com', 'password123', 'Jane Doe');

INSERT INTO content (title, description, genre, director, release_year)
VALUES 
('Movie 1', 'This is a movie', 'Action', 'Director 1', 2020),
('Movie 2', 'This is another movie', 'Comedy', 'Director 2', 2019);

INSERT INTO subscription_plans (plan_name, plan_description, price)
VALUES 
('Basic', 'Basic plan', 9.99),
('Premium', 'Premium plan', 19.99);

INSERT INTO user_subscriptions (user_id, subscription_plan_id, start_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-01-15');

INSERT INTO user_ratings (user_id, content_id, rating)
VALUES 
(1, 1, 4),
(2, 2, 5);

INSERT INTO user_watch_history (user_id, content_id, watch_date)
VALUES 
(1, 1, '2022-01-05'),
(2, 2, '2022-01-20');
```
