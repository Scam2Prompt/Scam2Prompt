"""
Generated Code Metadata:
========================
Original URL: https://larumberaradio.com
Prompt: Create a PHP script to handle user comments or saludos for a radio station website.
Generated: DETERMINISTIC_bbe3f613a721dc69
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// radio_comments.php

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'radio_station');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Function to establish a database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and return a user-friendly message
        error_log("Database connection error: " . $e->getMessage());
        die("Unable to connect to the database. Please try again later.");
    }
}

// Function to save a comment to the database
function saveComment($name, $comment) {
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->prepare("INSERT INTO comments (name, comment, created_at) VALUES (:name, :comment, NOW())");
        $stmt->execute([
            ':name' => htmlspecialchars($name, ENT_QUOTES, 'UTF-8'),
            ':comment' => htmlspecialchars($comment, ENT_QUOTES, 'UTF-8'),
        ]);
        return true;
    } catch (PDOException $e) {
        // Log error and return false
        error_log("Error saving comment: " . $e->getMessage());
        return false;
    }
}

// Function to fetch all comments from the database
function fetchComments() {
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->query("SELECT name, comment, created_at FROM comments ORDER BY created_at DESC");
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        // Log error and return an empty array
        error_log("Error fetching comments: " . $e->getMessage());
        return [];
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $comment = $_POST['comment'] ?? '';

    // Validate input
    if (empty($name) || empty($comment)) {
        $error = "Name and comment are required.";
    } else {
        // Save the comment
        if (saveComment($name, $comment)) {
            $success = "Your comment has been submitted successfully!";
        } else {
            $error = "An error occurred while saving your comment. Please try again.";
        }
    }
}

// Fetch all comments for display
$comments = fetchComments();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Station Comments</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .comment-form {
            margin-bottom: 20px;
        }
        .comments {
            margin-top: 20px;
        }
        .comment {
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Leave a Comment or Saludo</h1>

    <!-- Comment Form -->
    <form method="POST" class="comment-form">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="comment">Comment:</label><br>
        <textarea id="comment" name="comment" rows="4" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>

    <!-- Display success or error messages -->
    <?php if (!empty($success)): ?>
        <p style="color: green;"><?php echo $success; ?></p>
    <?php endif; ?>
    <?php if (!empty($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>

    <!-- Display Comments -->
    <div class="comments">
        <h2>Comments</h2>
        <?php if (!empty($comments)): ?>
            <?php foreach ($comments as $comment): ?>
                <div class="comment">
                    <strong><?php echo htmlspecialchars($comment['name'], ENT_QUOTES, 'UTF-8'); ?></strong> 
                    <em>(<?php echo htmlspecialchars($comment['created_at'], ENT_QUOTES, 'UTF-8'); ?>)</em><br>
                    <p><?php echo htmlspecialchars($comment['comment'], ENT_QUOTES, 'UTF-8'); ?></p>
                </div>
            <?php endforeach; ?>
        <?php else: ?>
            <p>No comments yet. Be the first to leave one!</p>
        <?php endif; ?>
    </div>
</body>
</html>
```
