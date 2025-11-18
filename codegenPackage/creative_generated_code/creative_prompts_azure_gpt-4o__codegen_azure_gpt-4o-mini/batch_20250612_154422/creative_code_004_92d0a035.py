"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Develop a database schema for a "五级三阶制直销软件" (five-level, three-stage direct selling system) that supports membership levels like E, D, C, B, and A, as detailed on JieyaSoft.
Generated: DETERMINISTIC_92d0a0355c0c3e4b
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for 五级三阶制直销软件 (Five-level, Three-stage Direct Selling System)

-- Drop existing tables if they exist (for re-creation purpose)
DROP TABLE IF EXISTS MembershipLevel;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Commission;
DROP TABLE IF EXISTS Sales;

-- Table to store membership levels
CREATE TABLE MembershipLevel (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for membership level
    level_name VARCHAR(10) NOT NULL,    -- Name of the membership level (E, D, C, B, A)
    commission_rate DECIMAL(5, 2) NOT NULL, -- Commission rate associated with the level
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store members in the system
CREATE TABLE Member (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the member
    username VARCHAR(50) NOT NULL UNIQUE, -- Member's username
    password VARCHAR(255) NOT NULL, -- Hashed password for security
    membership_level_id INT NOT NULL, -- Foreign key referencing MembershipLevel
    referral_id INT, -- Referral member's ID
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (membership_level_id) REFERENCES MembershipLevel(id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (referral_id) REFERENCES Member(id) ON DELETE SET NULL -- Optional referral relationship
);

-- Table to track sales made by members
CREATE TABLE Sales (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the sale
    member_id INT NOT NULL, -- Foreign key referencing the member making the sale
    sale_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the sale
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the sale
    FOREIGN KEY (member_id) REFERENCES Member(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to record commissions earned by members
CREATE TABLE Commission (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the commission record
    member_id INT NOT NULL, -- Foreign key referencing the member earning the commission
    amount DECIMAL(10, 2) NOT NULL, -- Amount of commission earned
    commission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of commission earned
    FOREIGN KEY (member_id) REFERENCES Member(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert initial membership levels
INSERT INTO MembershipLevel (level_name, commission_rate) VALUES 
('E', 5.00),
('D', 7.00),
('C', 10.00),
('B', 15.00),
('A', 20.00);

-- Query to fetch all members with their membership levels
SELECT 
    m.id AS member_id,
    m.username,
    ml.level_name,
    ml.commission_rate
FROM 
    Member m
JOIN 
    MembershipLevel ml ON m.membership_level_id = ml.id;
```
