"""
Generated Code Metadata:
========================
Original URL: https://live-redstone.com
Prompt: Create a ranking system using SQL or a similar database language to track and display the top RedStone Miners based on their RSG rewards.
Generated: DETERMINISTIC_711e9d84e3afcb75
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for RedStone Miners
CREATE DATABASE IF NOT EXISTS redstone_miners;
USE redstone_miners;

-- Create miners table to store miner information
CREATE TABLE IF NOT EXISTS miners (
    miner_id INT AUTO_INCREMENT PRIMARY KEY,
    wallet_address VARCHAR(64) NOT NULL UNIQUE,
    miner_name VARCHAR(50) NOT NULL,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create rewards table to track RSG rewards
CREATE TABLE IF NOT EXISTS rewards (
    reward_id INT AUTO_INCREMENT PRIMARY KEY,
    miner_id INT NOT NULL,
    reward_amount DECIMAL(18, 8) NOT NULL,
    reward_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_hash VARCHAR(66) NOT NULL UNIQUE,
    FOREIGN KEY (miner_id) REFERENCES miners(miner_id) ON DELETE CASCADE
);

-- Create index for faster queries on rewards
CREATE INDEX idx_rewards_miner_id ON rewards(miner_id);
CREATE INDEX idx_rewards_date ON rewards(reward_date);

-- View to get total rewards per miner
CREATE OR REPLACE VIEW miner_total_rewards AS
SELECT 
    m.miner_id,
    m.wallet_address,
    m.miner_name,
    COALESCE(SUM(r.reward_amount), 0) AS total_rewards,
    COUNT(r.reward_id) AS reward_count
FROM 
    miners m
LEFT JOIN 
    rewards r ON m.miner_id = r.miner_id
GROUP BY 
    m.miner_id, m.wallet_address, m.miner_name;

-- Stored procedure to add a new reward
DELIMITER //
CREATE PROCEDURE add_reward(
    IN p_wallet_address VARCHAR(64),
    IN p_reward_amount DECIMAL(18, 8),
    IN p_transaction_hash VARCHAR(66)
)
BEGIN
    DECLARE v_miner_id INT;
    
    -- Check if miner exists
    SELECT miner_id INTO v_miner_id FROM miners WHERE wallet_address = p_wallet_address;
    
    -- If miner doesn't exist, create them
    IF v_miner_id IS NULL THEN
        INSERT INTO miners (wallet_address, miner_name) 
        VALUES (p_wallet_address, CONCAT('Miner_', p_wallet_address));
        SET v_miner_id = LAST_INSERT_ID();
    END IF;
    
    -- Add the reward
    INSERT INTO rewards (miner_id, reward_amount, transaction_hash)
    VALUES (v_miner_id, p_reward_amount, p_transaction_hash);
END //
DELIMITER ;

-- Function to get miner rank by total rewards
DELIMITER //
CREATE FUNCTION get_miner_rank(p_miner_id INT) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE v_rank INT;
    
    SELECT COUNT(*) + 1 INTO v_rank
    FROM miner_total_rewards
    WHERE total_rewards > (
        SELECT total_rewards 
        FROM miner_total_rewards 
        WHERE miner_id = p_miner_id
    );
    
    RETURN v_rank;
END //
DELIMITER ;

-- Query to get top miners by rewards (for leaderboard)
SELECT 
    RANK() OVER (ORDER BY total_rewards DESC) AS rank,
    miner_name,
    wallet_address,
    total_rewards,
    reward_count,
    last_active
FROM 
    miner_total_rewards
ORDER BY 
    total_rewards DESC
LIMIT 100;

-- Query to get miner details with rank
SELECT 
    get_miner_rank(m.miner_id) AS rank,
    m.miner_name,
    m.wallet_address,
    mtr.total_rewards,
    mtr.reward_count,
    m.last_active
FROM 
    miners m
JOIN 
    miner_total_rewards mtr ON m.miner_id = mtr.miner_id
WHERE 
    m.miner_id = :miner_id;
```
