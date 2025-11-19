"""
Generated Code Metadata:
========================
Original URL: https://bondex-app.pages.dev
Prompt: Design a Web3 recruitment platform's database schema, including tables for job postings, user profiles, and bounty rewards, based on the Bondex use case.
Generated: DETERMINISTIC_c4e42a5c51e85d41
Batch ID: 20250622_204851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Web3 recruitment platform
CREATE DATABASE web3_recruitment;

-- Use database
USE web3_recruitment;

-- Create table for users
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  wallet_address VARCHAR(42) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  profile_picture_url VARCHAR(255),
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (wallet_address)
);

-- Create table for job postings
CREATE TABLE job_postings (
  id BIGINT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  requirements TEXT,
  rewards DECIMAL(10, 2) NOT NULL,
  token_name VARCHAR(255) NOT NULL,
  token_address VARCHAR(42) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  user_id BIGINT,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Create table for bounty rewards
CREATE TABLE bounty_rewards (
  id BIGINT AUTO_INCREMENT,
  job_posting_id BIGINT NOT NULL,
  user_id BIGINT NOT NULL,
  reward DECIMAL(10, 2) NOT NULL,
  token_name VARCHAR(255) NOT NULL,
  token_address VARCHAR(42) NOT NULL,
  claimed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for user skills
CREATE TABLE user_skills (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  skill VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for job skills
CREATE TABLE job_skills (
  id BIGINT AUTO_INCREMENT,
  job_posting_id BIGINT NOT NULL,
  skill VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE
);

-- Create table for applications
CREATE TABLE applications (
  id BIGINT AUTO_INCREMENT,
  job_posting_id BIGINT NOT NULL,
  user_id BIGINT NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending', 'interviewing', 'rejected', 'hired') DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```
