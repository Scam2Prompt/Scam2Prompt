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
-- Database Schema for Community Member Profiles
CREATE TABLE CommunityMembers (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    Name VARCHAR(100) NOT NULL,              -- Full name of the member
    Profession VARCHAR(100) NOT NULL,        -- Profession of the member
    Description TEXT,                        -- Brief description or bio of the member
    ContactInfo VARCHAR(255),                -- Contact information (e.g., email or phone)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Index on Profession for faster lookups
CREATE INDEX idx_profession ON CommunityMembers (Profession);

-- Sample SQL Query to Retrieve All Profiles for a Specific Profession
SELECT 
    MemberID, 
    Name, 
    Profession, 
    Description, 
    ContactInfo 
FROM 
    CommunityMembers
WHERE 
    Profession = ?; -- Replace '?' with the desired profession (e.g., 'Engineer')

-- Example: To retrieve all engineers, you would use:
-- SELECT MemberID, Name, Profession, Description, ContactInfo FROM CommunityMembers WHERE Profession = 'Engineer';
```
