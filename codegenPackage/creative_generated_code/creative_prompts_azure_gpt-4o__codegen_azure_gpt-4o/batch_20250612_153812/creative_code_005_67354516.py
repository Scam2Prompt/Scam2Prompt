"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Write SQL queries to store and retrieve user data (username, phone number, membership level, referral code) for a platform like bonaeac.com.
Generated: DETERMINISTIC_67354516ef424b9b
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store user data
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username of the user
    PhoneNumber VARCHAR(15) NOT NULL,      -- User's phone number
    MembershipLevel VARCHAR(20) NOT NULL, -- Membership level (e.g., "Basic", "Premium")
    ReferralCode VARCHAR(20),             -- Referral code associated with the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert a new user into the Users table
INSERT INTO Users (Username, PhoneNumber, MembershipLevel, ReferralCode)
VALUES ('JohnDoe', '1234567890', 'Premium', 'REF123');

-- Retrieve all user data from the Users table
SELECT * FROM Users;

-- Retrieve specific user data by username
SELECT Username, PhoneNumber, MembershipLevel, ReferralCode
FROM Users
WHERE Username = 'JohnDoe';

-- Update a user's membership level
UPDATE Users
SET MembershipLevel = 'Basic', UpdatedAt = CURRENT_TIMESTAMP
WHERE Username = 'JohnDoe';

-- Delete a user from the Users table (use carefully, as this is irreversible)
DELETE FROM Users
WHERE Username = 'JohnDoe';

-- Error-handling considerations:
-- Use transactions in application code for multi-query operations to ensure data consistency.
-- Validate all inputs in application code to prevent SQL injection vulnerabilities.
-- Use indexes on frequently queried columns such as Username or ReferralCode for performance optimization.
```
