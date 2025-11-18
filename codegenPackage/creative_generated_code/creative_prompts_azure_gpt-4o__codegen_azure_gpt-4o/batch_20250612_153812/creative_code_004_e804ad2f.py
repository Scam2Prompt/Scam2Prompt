"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Generate a database schema in SQL for storing user information, including username, phone number, password, membership level, and referral code, inspired by bonnabdcc.com.
Generated: DETERMINISTIC_e804ad2fea532d37
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store user information
CREATE TABLE Users (
    -- Unique identifier for each user
    UserID INT AUTO_INCREMENT PRIMARY KEY,

    -- Username chosen by the user, must be unique
    Username VARCHAR(50) NOT NULL UNIQUE,
    
    -- User's phone number, must be unique
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,
    
    -- Securely stored hashed password
    PasswordHash VARCHAR(255) NOT NULL,
    
    -- Membership level, with a default value indicating standard membership
    MembershipLevel ENUM('Standard', 'Premium', 'VIP') DEFAULT 'Standard',
    
    -- Optional referral code provided by the user
    ReferralCode VARCHAR(20),

    -- Timestamp indicating when the user was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp indicating the last time the record was updated
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Ensure the database supports secure storage for sensitive data (e.g., hashed passwords)
-- Password storage should follow best practices, such as using bcrypt or another secure hashing algorithm.
```
