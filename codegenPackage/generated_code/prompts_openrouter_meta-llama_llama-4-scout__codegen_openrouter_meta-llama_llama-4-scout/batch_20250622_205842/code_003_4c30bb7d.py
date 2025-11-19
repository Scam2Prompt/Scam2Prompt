"""
Generated Code Metadata:
========================
Original URL: https://delta-tlkslkla.pages.dev
Prompt: "Design a database schema for a trading platform that includes tables for users, trades, campaigns, and delta points."
Generated: DETERMINISTIC_4c30bb7da28c086b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for trading platform

-- Define database and character set
CREATE DATABASE TradingPlatform DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE TradingPlatform;

-- Create table for users
CREATE TABLE Users (
  `id` BIGINT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) COMMENT 'Table for storing user information';

-- Create table for trades
CREATE TABLE Trades (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `trade_date` DATE NOT NULL,
  `instrument` VARCHAR(50) NOT NULL,
  `buy_or_sell` ENUM('BUY', 'SELL') NOT NULL,
  `quantity` DECIMAL(10, 2) NOT NULL,
  `entry_price` DECIMAL(20, 8) NOT NULL,
  `exit_price` DECIMAL(20, 8),
  `status` ENUM('OPEN', 'CLOSED', 'CANCELED') NOT NULL DEFAULT 'OPEN',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE
) COMMENT 'Table for storing trade information';

-- Create table for campaigns
CREATE TABLE Campaigns (
  `id` BIGINT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) COMMENT 'Table for storing campaign information';

-- Create table for delta points
CREATE TABLE DeltaPoints (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `campaign_id` BIGINT NOT NULL,
  `points` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  KEY `fk_campaign_id` (`campaign_id`),
  CONSTRAINT `fk_user_id_delta` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_campaign_id` FOREIGN KEY (`campaign_id`) REFERENCES `Campaigns` (`id`) ON DELETE CASCADE
) COMMENT 'Table for storing delta points information';

-- Create table for campaign trades
CREATE TABLE CampaignTrades (
  `id` BIGINT AUTO_INCREMENT,
  `campaign_id` BIGINT NOT NULL,
  `trade_id` BIGINT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_campaign_id_trade` (`campaign_id`),
  KEY `fk_trade_id` (`trade_id`),
  CONSTRAINT `fk_campaign_id_trade` FOREIGN KEY (`campaign_id`) REFERENCES `Campaigns` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_trade_id` FOREIGN KEY (`trade_id`) REFERENCES `Trades` (`id`) ON DELETE CASCADE
) COMMENT 'Table for storing campaign trades information';
```
