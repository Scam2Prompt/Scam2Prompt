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
// comment_handler.php

// Start the session to manage user data
session_start();

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'radio_station'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to handle user comments
function handleComment($comment) {
    global $pdo;

    // Validate the comment input
    if (empty($comment)) {
        return "Comment cannot be empty.";
    }

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO comments (comment, created_at) VALUES (:comment, NOW())");

    // Bind parameters and execute the statement
    try {
        $stmt->bindParam(':comment', $comment);
        $stmt->execute();
        return "Comment submitted successfully!";
    } catch (PDOException $e) {
        // Handle SQL execution error
        return "Error submitting comment: " . $e->getMessage();
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user input
    $userComment = filter_input(INPUT_POST, 'comment', FILTER_SANITIZE_STRING);
    
    // Handle the comment submission
    $response = handleComment($userComment);
    
    // Store response in session to display to the user
    $_SESSION['response'] = $response;
    
    // Redirect to the same page to avoid resubmission
    header("Location: " . $_SERVER['PHP_SELF']);
    exit();
}

// Fetch all comments for display
function fetchComments() {
    global $pdo;
    $stmt = $pdo->query("SELECT * FROM comments ORDER BY created_at DESC");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Fetch comments to display on the page
$comments = fetchComments();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Station Comments</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>User Comments</h1>

    <!-- Display response message if available -->
    <?php if (isset($_SESSION['response'])): ?>
        <p><?php echo $_SESSION['response']; ?></p>
        <?php unset($_SESSION['response']); // Clear the message after displaying ?>
    <?php endif; ?>

    <!-- Comment submission form -->
    <form action="" method="POST">
        <textarea name="comment" rows="4" cols="50" placeholder="Leave your comment here..." required></textarea>
        <br>
        <button type="submit">Submit Comment</button>
    </form>

    <h2>All Comments:</h2>
    <ul>
        <?php foreach ($comments as $comment): ?>
            <li><?php echo htmlspecialchars($comment['comment']); ?> <em>(<?php echo $comment['created_at']; ?>)</em></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
