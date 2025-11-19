"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Create a database schema for managing sports streaming subscriptions, giveaways, and user preferences, including features like extra channels and live game updates, as highlighted on Sportify.Club.
Generated: DETERMINISTIC_be59ef2df1474168
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- sportify_club_schema.sql

-- Create database
CREATE DATABASE sportify_club;

-- Use database
USE sportify_club;

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

-- Create table for subscriptions
CREATE TABLE subscriptions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  subscription_plan VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for extra channels
CREATE TABLE extra_channels (
  id INT AUTO_INCREMENT,
  channel_name VARCHAR(255) NOT NULL,
  channel_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user extra channel subscriptions
CREATE TABLE user_extra_channels (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  extra_channel_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (extra_channel_id) REFERENCES extra_channels(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, extra_channel_id)
);

-- Create table for giveaways
CREATE TABLE giveaways (
  id INT AUTO_INCREMENT,
  prize VARCHAR(255) NOT NULL,
  description TEXT,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user giveaway participations
CREATE TABLE user_giveaways (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  giveaway_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (giveaway_id) REFERENCES giveaways(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, giveaway_id)
);

-- Create table for live game updates
CREATE TABLE live_game_updates (
  id INT AUTO_INCREMENT,
  game_id INT NOT NULL,
  team1_score INT,
  team2_score INT,
  game_status VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user preferences
CREATE TABLE user_preferences (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  preferred_sports VARCHAR(255),
  preferred_teams VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id)
);

-- Create table for notifications
CREATE TABLE notifications (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  notification_message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```
