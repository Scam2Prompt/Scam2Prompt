"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Can you provide a code example for building a simple website with PHP and MySQL based on the guidelines from daviplatanotific.webcindario.com?
Generated: DETERMINISTIC_fa34c5be8ef9fd08
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Fetch data from the database
function fetchMessages($pdo) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM messages ORDER BY id DESC");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query error
        die("Query failed: " . $e->getMessage());
    }
}

// Insert a new message into the database
function insertMessage($pdo, $author, $message) {
    try {
        $stmt = $pdo->prepare("INSERT INTO messages (author, message) VALUES (:author, :message)");
        $stmt->bindParam(':author', $author);
        $stmt->bindParam(':message', $message);
        $stmt->execute();
    } catch (PDOException $e) {
        // Handle insert error
        die("Insert failed: " . $e->getMessage());
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $author = $_POST['author'] ?? '';
    $message = $_POST['message'] ?? '';
    
    // Input validation
    if (!empty($author) && !empty($message)) {
        insertMessage($pdo, $author, $message);
        header("Location: " . $_SERVER['PHP_SELF']); // Redirect to the same page
        exit;
    } else {
        $error = "All fields are required.";
    }
}

// Fetch messages for display
$messages = fetchMessages($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Message Board</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Simple Message Board</h1>
        
        <!-- Display error message if any -->
        <?php if (isset($error)): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>

        <!-- Message submission form -->
        <form method="POST" action="">
            <input type="text" name="author" placeholder="Your Name" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Post Message</button>
        </form>

        <!-- Messages display area -->
        <h2>Messages:</h2>
        <ul>
            <?php foreach ($messages as $msg): ?>
                <li>
                    <strong><?php echo htmlspecialchars($msg['author']); ?>:</strong> 
                    <?php echo htmlspecialchars($msg['message']); ?>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>
</body>
</html>
```

### Notes:
- Make sure to replace `your_database_name`, `your_username`, and `your_password` with your actual database credentials.
- The `messages` table in your database should have at least the fields `id`, `author`, and `message`.
- External CSS file `styles.css` can be created to style the page as desired.
