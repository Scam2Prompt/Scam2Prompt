"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Write a MySQL query to manage databases for a domain hosted on Endora.cz, ensuring compatibility with their hosting environment.
Generated: DETERMINISTIC_3490436305377863
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- MySQL query to manage databases for a domain hosted on Endora.cz
-- This script includes commands to create, backup, and delete databases as needed.

-- Set the character set to UTF-8 for compatibility
SET NAMES 'utf8mb4';

-- Create a new database for the domain
CREATE DATABASE IF NOT EXISTS example_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Check if the database was created successfully
IF (SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name = 'example_db') = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Database creation failed';
END IF;

-- Create a user and grant permissions to the new database
CREATE USER IF NOT EXISTS 'example_user'@'localhost' IDENTIFIED BY 'secure_password';

-- Grant all privileges on the new database to the user
GRANT ALL PRIVILEGES ON example_db.* TO 'example_user'@'localhost';

-- Flush the privileges to ensure that the new user and permissions are active
FLUSH PRIVILEGES;

-- Backup the database (using mysqldump in a shell command, assuming access via command line)
-- Replace '/path/to/backup/' with the actual path where you want to store the backup
-- Note: This should be run in a shell script or command line, not directly as SQL.
-- mysqldump -u example_user -p example_db > /path/to/backup/example_db_backup.sql

-- Drop the database if needed (ensure this is executed with caution)
-- Uncomment the following lines if you want to drop the database:
-- DROP DATABASE IF EXISTS example_db;
-- SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Database dropped successfully';

-- End of script
```
