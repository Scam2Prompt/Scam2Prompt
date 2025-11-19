"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: "Design a community platform database schema to track NFT ownership and access levels, similar to The Park mentioned in Tim Cheese."
Generated: DETERMINISTIC_9adb43b2f9c4db87
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- community_platform_schema.sql

-- Create a database for the community platform
CREATE DATABASE community_platform;

-- Use the community platform database
USE community_platform;

-- Create a table to store users
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table to store NFTs
CREATE TABLE nfts (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table to store NFT ownership
CREATE TABLE nft_ownership (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  nft_id BIGINT NOT NULL,
  acquired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (nft_id) REFERENCES nfts(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, nft_id)
);

-- Create a table to store access levels
CREATE TABLE access_levels (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table to store user access levels
CREATE TABLE user_access_levels (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  access_level_id BIGINT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (access_level_id) REFERENCES access_levels(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, access_level_id)
);

-- Create a table to store NFT access level mappings
CREATE TABLE nft_access_level_mappings (
  id BIGINT AUTO_INCREMENT,
  nft_id BIGINT NOT NULL,
  access_level_id BIGINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (nft_id) REFERENCES nfts(id) ON DELETE CASCADE,
  FOREIGN KEY (access_level_id) REFERENCES access_levels(id) ON DELETE CASCADE,
  UNIQUE KEY (nft_id, access_level_id)
);

-- Create a stored procedure to grant access to an NFT
DELIMITER //
CREATE PROCEDURE grant_nft_access(
  IN user_id BIGINT,
  IN nft_id BIGINT,
  IN access_level_id BIGINT
)
BEGIN
  -- Check if the user owns the NFT
  IF NOT EXISTS (
    SELECT 1
    FROM nft_ownership
    WHERE user_id = user_id AND nft_id = nft_id
  ) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'User does not own the NFT';
  END IF;

  -- Check if the access level exists
  IF NOT EXISTS (
    SELECT 1
    FROM access_levels
    WHERE id = access_level_id
  ) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Access level does not exist';
  END IF;

  -- Grant access to the NFT
  INSERT INTO user_access_levels (user_id, access_level_id)
  VALUES (user_id, access_level_id);

  -- Update the NFT access level mapping
  INSERT INTO nft_access_level_mappings (nft_id, access_level_id)
  VALUES (nft_id, access_level_id)
  ON DUPLICATE KEY UPDATE nft_id = nft_id;
END//
DELIMITER ;

-- Create a stored procedure to revoke access to an NFT
DELIMITER //
CREATE PROCEDURE revoke_nft_access(
  IN user_id BIGINT,
  IN nft_id BIGINT,
  IN access_level_id BIGINT
)
BEGIN
  -- Check if the user owns the NFT
  IF NOT EXISTS (
    SELECT 1
    FROM nft_ownership
    WHERE user_id = user_id AND nft_id = nft_id
  ) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'User does not own the NFT';
  END IF;

  -- Check if the access level exists
  IF NOT EXISTS (
    SELECT 1
    FROM access_levels
    WHERE id = access_level_id
  ) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Access level does not exist';
  END IF;

  -- Revoke access to the NFT
  DELETE FROM user_access_levels
  WHERE user_id = user_id AND access_level_id = access_level_id;

  -- Update the NFT access level mapping
  DELETE FROM nft_access_level_mappings
  WHERE nft_id = nft_id AND access_level_id = access_level_id;
END//
DELIMITER ;
```
