"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a PHP application that provides a community support system for users to share insights and celebrate wins, similar to the features of the Action Accelerator Academy.
Generated: DETERMINISTIC_ef269e6df1f05b08
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Community Support System Application
// Provides features for users to share insights and celebrate wins
// Author: [Your Name]
// Date: [Insert date]
// License: [Specify license]

// Enable error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration (replace with your credentials)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'community_support');

try {
    // Establish database connection
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Helper function to sanitize input
function sanitizeInput($input)
{
    return htmlspecialchars(strip_tags(trim($input)));
}

// POST request handler for creating a new post
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {
    switch ($_POST['action']) {
        case 'create_post':
            createPost($db);
            break;
        default:
            echo json_encode(['status' => 'error', 'message' => 'Invalid action']);
    }
}

// Create a new post (insight or celebration)
function createPost($db)
{
    $userName = sanitizeInput($_POST['user_name'] ?? '');
    $postType = sanitizeInput($_POST['post_type'] ?? '');
    $content = sanitizeInput($_POST['content'] ?? '');

    // Validate input
    if (empty($userName) || empty($postType) || empty($content)) {
        echo json_encode(['status' => 'error', 'message' => 'All fields are required']);
        return;
    }

    if (!in_array($postType, ['insight', 'celebration'])) {
        echo json_encode(['status' => 'error', 'message' => 'Invalid post type']);
        return;
    }

    try {
        // Insert post into the database
        $query = "INSERT INTO posts (user_name, post_type, content, created_at) VALUES (:user_name, :post_type, :content, NOW())";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':user_name', $userName);
        $stmt->bindParam(':post_type', $postType);
        $stmt->bindParam(':content', $content);
        $stmt->execute();

        echo json_encode(['status' => 'success', 'message' => 'Post created successfully']);
    } catch (PDOException $e) {
        echo json_encode(['status' => 'error', 'message' => 'Failed to create post: ' . $e->getMessage()]);
    }
}

// Fetch all posts from the database (GET request)
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    fetchPosts($db);
}

// Fetch posts
function fetchPosts($db)
{
    try {
        $query = "SELECT * FROM posts ORDER BY created_at DESC";
        $stmt = $db->query($query);
        $posts = $stmt->fetchAll(PDO::FETCH_ASSOC);

        echo json_encode(['status' => 'success', 'data' => $posts]);
    } catch (PDOException $e) {
        echo json_encode(['status' => 'error', 'message' => 'Failed to fetch posts: ' . $e->getMessage()]);
    }
}

?>
```

### SQL Setup Script
```sql
-- Create the database
CREATE DATABASE community_support;

-- Use the database
USE community_support;

-- Create the posts table
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    post_type ENUM('insight', 'celebration') NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL
);
```

### Notes:
- Replace the `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` constants with your actual database credentials.
- This application assumes the PHP server is configured and running. You can deploy this code within a PHP application and create the database using the provided SQL script.
- For production use, ensure proper security measures (e.g., prepared statements, HTTPS, authentication, etc.) are implemented.
