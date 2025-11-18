"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iniciosecurity1.webcindario.com
Prompt: Provide code examples for setting up a MySQL database schema for a free website created with PHP, as mentioned on miarroba.com.
Generated: DETERMINISTIC_532961f3b245d91f
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- MySQL Database Schema for a Free Website

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

-- Create a table to store user information
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username, must be unique
    password VARCHAR(255) NOT NULL,          -- Password, stored as a hashed value
    email VARCHAR(100) NOT NULL UNIQUE,      -- User's email address, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Account creation timestamp
) ENGINE=InnoDB;

-- Create a table for storing website posts
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each post
    user_id INT NOT NULL,                    -- ID of the user who created the post
    title VARCHAR(255) NOT NULL,             -- Title of the post
    content TEXT NOT NULL,                    -- Content of the post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Post creation timestamp
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE  -- Relationship to users
) ENGINE=InnoDB;

-- Create a table for storing comments on posts
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each comment
    post_id INT NOT NULL,                    -- ID of the post being commented on
    user_id INT NOT NULL,                    -- ID of the user who made the comment
    content TEXT NOT NULL,                   -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Comment creation timestamp
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,  -- Relationship to posts
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE   -- Relationship to users
) ENGINE=InnoDB;

-- Optional: Create an index on username for faster lookup
CREATE INDEX idx_username ON users(username);

-- Optional: Create an index on post creation date for faster retrieval of recent posts
CREATE INDEX idx_created_at ON posts(created_at);
```

```php
<?php
// Database connection settings
$host = 'localhost'; // Database host
$db = 'your_database_name'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

try {
    // Establish a connection to the MySQL database using PDO
    $dsn = "mysql:host=$host;dbname=$db;charset=utf8mb4";
    $pdo = new PDO($dsn, $user, $pass);
    
    // Set the PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create tables if they do not exist
    $createTablesSQL = "
        -- MySQL Database Schema for a Free Website
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;

        CREATE TABLE IF NOT EXISTS posts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        ) ENGINE=InnoDB;

        CREATE TABLE IF NOT EXISTS comments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        ) ENGINE=InnoDB;
    ";

    // Execute the table creation SQL
    $pdo->exec($createTablesSQL);
    echo "Database schema created successfully.";

} catch (PDOException $e) {
    // Handle connection errors and execution errors
    echo "Database error: " . $e->getMessage();
}
?>
```
