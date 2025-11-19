"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Design a database schema for an esports management firm like Ace Pro Sports Technologies, including tables for teams, players, tournaments, and apparel orders.
Generated: DETERMINISTIC_ad36e2caa453dcca
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for esports management
CREATE DATABASE IF NOT EXISTS esports_management;

-- Use the database
USE esports_management;

-- Create table for teams
CREATE TABLE IF NOT EXISTS teams (
  team_id INT AUTO_INCREMENT,
  team_name VARCHAR(255) NOT NULL,
  team_abbreviation VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id),
  UNIQUE (team_name),
  UNIQUE (team_abbreviation)
);

-- Create table for players
CREATE TABLE IF NOT EXISTS players (
  player_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  team_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (player_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE SET NULL
);

-- Create table for tournaments
CREATE TABLE IF NOT EXISTS tournaments (
  tournament_id INT AUTO_INCREMENT,
  tournament_name VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  tournament_type VARCHAR(50) NOT NULL,
  prize_pool DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (tournament_id)
);

-- Create table for team tournament participation
CREATE TABLE IF NOT EXISTS team_tournament_participation (
  team_id INT NOT NULL,
  tournament_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id, tournament_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
  FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id) ON DELETE CASCADE
);

-- Create table for apparel orders
CREATE TABLE IF NOT EXISTS apparel_orders (
  order_id INT AUTO_INCREMENT,
  team_id INT,
  player_id INT,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE SET NULL,
  FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE SET NULL
);

-- Create table for apparel items
CREATE TABLE IF NOT EXISTS apparel_items (
  item_id INT AUTO_INCREMENT,
  item_name VARCHAR(100) NOT NULL,
  item_description TEXT,
  item_price DECIMAL(10, 2) NOT NULL,
  item_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (item_id)
);

-- Create table for order items
CREATE TABLE IF NOT EXISTS order_items (
  order_id INT NOT NULL,
  item_id INT NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id, item_id),
  FOREIGN KEY (order_id) REFERENCES apparel_orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (item_id) REFERENCES apparel_items(item_id) ON DELETE CASCADE
);
```
