"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Design a database schema for storing community member profiles, including fields for name, profession, description, and contact information, and write a simple SQL query to retrieve all profiles for a specific profession."
Generated: DETERMINISTIC_fb6284ba05a09564
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for community member profiles
CREATE TABLE member_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    profession VARCHAR(100) NOT NULL,
    description TEXT,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_profession (profession)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- SQL query to retrieve all profiles for a specific profession
SELECT 
    id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    profession,
    description,
    email,
    phone
FROM 
    member_profiles
WHERE 
    profession = :profession
ORDER BY 
    last_name, first_name;
```
