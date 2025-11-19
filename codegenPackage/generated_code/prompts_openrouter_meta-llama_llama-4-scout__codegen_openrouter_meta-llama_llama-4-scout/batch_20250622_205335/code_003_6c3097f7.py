"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: Design a database schema for storing information about NFTs, user votes, and claims on a platform similar to Shibuya, ensuring efficient lookup and retrieval of user data.
Generated: DETERMINISTIC_6c3097f7f8bcd63f
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- nft_platform_schema.sql

-- Create a database schema for storing NFT platform data

CREATE TABLE Users (
  `id` BIGINT AUTO_INCREMENT,
  `address` VARCHAR(42) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_address` (`address`)
);

CREATE TABLE NFTs (
  `id` BIGINT AUTO_INCREMENT,
  `contract_address` VARCHAR(42) NOT NULL,
  `token_id` BIGINT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `image_url` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_contract_token_id` (`contract_address`, `token_id`)
);

CREATE TABLE User_Votes (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `nft_id` BIGINT NOT NULL,
  `vote` ENUM('up', 'down') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  KEY `fk_nft_id` (`nft_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_nft_id` FOREIGN KEY (`nft_id`) REFERENCES `NFTs` (`id`) ON DELETE CASCADE
);

CREATE TABLE Claims (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `nft_id` BIGINT NOT NULL,
  `claim_type` ENUM('claim', 'reject') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  KEY `fk_nft_id` (`nft_id`),
  CONSTRAINT `fk_user_id_claims` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_nft_id_claims` FOREIGN KEY (`nft_id`) REFERENCES `NFTs` (`id`) ON DELETE CASCADE
);

CREATE TABLE User_Claim_History (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `nft_id` BIGINT NOT NULL,
  `claim_type` ENUM('claim', 'reject') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id_history` (`user_id`),
  KEY `fk_nft_id_history` (`nft_id`),
  CONSTRAINT `fk_user_id_history` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_nft_id_history` FOREIGN KEY (`nft_id`) REFERENCES `NFTs` (`id`) ON DELETE CASCADE
);

DELIMITER //
CREATE PROCEDURE UpdateUserVote(
  IN _user_id BIGINT,
  IN _nft_id BIGINT,
  IN _vote ENUM('up', 'down')
)
BEGIN
  IF EXISTS (SELECT 1 FROM User_Votes WHERE user_id = _user_id AND nft_id = _nft_id) THEN
    UPDATE User_Votes SET vote = _vote WHERE user_id = _user_id AND nft_id = _nft_id;
  ELSE
    INSERT INTO User_Votes (user_id, nft_id, vote) VALUES (_user_id, _nft_id, _vote);
  END IF;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetUserNFTVotes(
  IN _user_id BIGINT
)
BEGIN
  SELECT 
    n.id,
    n.contract_address,
    n.token_id,
    n.name,
    uv.vote
  FROM 
    User_Votes uv
  INNER JOIN 
    NFTs n ON uv.nft_id = n.id
  WHERE 
    uv.user_id = _user_id;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetNFTClaimStatus(
  IN _nft_id BIGINT
)
BEGIN
  SELECT 
    c.claim_type,
    u.address AS user_address
  FROM 
    Claims c
  INNER JOIN 
    Users u ON c.user_id = u.id
  WHERE 
    c.nft_id = _nft_id;
END//
DELIMITER ;
```
