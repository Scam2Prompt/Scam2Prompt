"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx40.com
Prompt: Write PHP code to implement a live chat feature for customer support, similar to the 24/7 live chat functionality on TANTE4D.
Generated: DETERMINISTIC_646db3cc381478a9
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Live Chat Feature for Customer Support

// Start the session to manage user state
session_start();

/**
 * Establish a database connection.
 * 
 * @return PDO $pdo The PDO instance for database interaction.
 * @throws Exception If unable to connect to the database.
 */
function getDatabaseConnection() {
    $host = 'localhost';
    $db = 'live_chat_support';
    $user = 'root';
    $pass = '';
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (Exception $e) {
        // Log the error and display a user-friendly message
        error_log('Database Connection Error: ' . $e->getMessage());
        die('Could not connect to the database. Please try again later.');
    }
}

/**
 * Send a chat message to the database.
 * 
 * @param string $userId The ID of the user sending the message.
 * @param string $message The chat message to send.
 * @return bool True on success, false on failure.
 */
function sendMessage($userId, $message) {
    $pdo = getDatabaseConnection();

    $sql = 'INSERT INTO messages (user_id, message, created_at) VALUES (:user_id, :message, NOW())';
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters to prevent SQL injection
    $stmt->bindParam(':user_id', $userId);
    $stmt->bindParam(':message', $message);

    return $stmt->execute();
}

/**
 * Fetch chat messages from the database.
 * 
 * @return array An array of messages.
 */
function fetchMessages() {
    $pdo = getDatabaseConnection();

    $sql = 'SELECT user_id, message, created_at FROM messages ORDER BY created_at ASC';
    $stmt = $pdo->query($sql);

    return $stmt->fetchAll();
}

// Check if the user is sending a message
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message'])) {
    $userId = isset($_SESSION['user_id']) ? $_SESSION['user_id'] : 'guest';
    $message = trim($_POST['message']);

    if (!empty($message)) {
        if (!sendMessage($userId, $message)) {
            // Handle error in message sending
            echo json_encode(['status' => 'error', 'message' => 'Message could not be sent.']);
            exit;
        }
    }
}

// Fetch messages for display
$messages = fetchMessages();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Chat Support</title>
    <style>
        /* Basic styles for chat interface */
        #chat-window {
            width: 300px;
            height: 400px;
            border: 1px solid #ccc;
            overflow-y: scroll;
            padding: 10px;
            position: relative;
        }
        #message-form {
            display: flex;
            margin-top: 10px;
        }
        #message-input {
            flex: 1;
            padding: 5px;
        }
        #send-button {
            padding: 5px 10px;
        }
    </style>
</head>
<body>
    <h1>Live Chat Support</h1>
    <div id="chat-window">
        <?php foreach ($messages as $message): ?>
            <div><strong><?= htmlspecialchars($message['user_id']) ?>:</strong> <?= htmlspecialchars($message['message']) ?> <em>(<?= $message['created_at'] ?>)</em></div>
        <?php endforeach; ?>
    </div>

    <form id="message-form" method="post">
        <input type="text" id="message-input" name="message" placeholder="Type your message..." required>
        <button type="submit" id="send-button">Send</button>
    </form>

    <script>
        // Optional: Add JavaScript to refresh chat window dynamically (using AJAX)
    </script>
</body>
</html>
```

**Database Schema** (for reference)
```sql
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
