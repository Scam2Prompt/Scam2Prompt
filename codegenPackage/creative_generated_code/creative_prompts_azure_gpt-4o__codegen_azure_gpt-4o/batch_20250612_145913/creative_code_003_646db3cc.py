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
// Initialize a PHP session
session_start();

// Database connection (use your actual database credentials)
$host = "localhost"; // Database host
$dbname = "live_chat"; // Database name
$username = "root"; // Database username
$password = ""; // Database password

try {
    // Establish a PDO connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Generate a unique session ID for the user if not already set
if (!isset($_SESSION['chat_user_id'])) {
    $_SESSION['chat_user_id'] = uniqid('user_');
}

// Handler for sending a message
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message'])) {
    $message = trim($_POST['message']);
    $userId = $_SESSION['chat_user_id'];

    if (!empty($message)) {
        try {
            // Insert the message into the database
            $stmt = $pdo->prepare("INSERT INTO messages (user_id, message, created_at) VALUES (:user_id, :message, NOW())");
            $stmt->execute([
                ':user_id' => $userId,
                ':message' => $message
            ]);
        } catch (Exception $e) {
            // Handle database errors
            http_response_code(500);
            echo "Error saving message.";
            exit;
        }
    }
    exit;
}

// Handler for fetching messages
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['fetch_messages'])) {
    try {
        // Fetch all messages from the database
        $stmt = $pdo->query("SELECT * FROM messages ORDER BY created_at ASC");
        $messages = $stmt->fetchAll(PDO::FETCH_ASSOC);
        header('Content-Type: application/json');
        echo json_encode($messages);
    } catch (Exception $e) {
        // Handle database errors
        http_response_code(500);
        echo "Error fetching messages.";
    }
    exit;
}
?>

<!-- HTML for live chat UI -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Chat</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #chat-box { width: 100%; height: 400px; border: 1px solid #ddd; overflow-y: auto; padding: 10px; }
        #message-input { width: calc(100% - 80px); padding: 10px; }
        #send-btn { padding: 10px; }
        .message { margin: 5px 0; }
        .message.user { text-align: right; color: blue; }
        .message.support { text-align: left; color: green; }
    </style>
</head>
<body>
    <h1>Live Chat</h1>
    <div id="chat-box"></div>
    <form id="chat-form">
        <input type="text" id="message-input" placeholder="Type your message..." required>
        <button type="submit" id="send-btn">Send</button>
    </form>

    <script>
        // DOM Elements
        const chatBox = document.getElementById('chat-box');
        const chatForm = document.getElementById('chat-form');
        const messageInput = document.getElementById('message-input');

        // Function to fetch messages
        async function fetchMessages() {
            try {
                const response = await fetch('live_chat.php?fetch_messages=true');
                const messages = await response.json();

                // Clear current chat box
                chatBox.innerHTML = '';

                // Render messages
                messages.forEach(message => {
                    const messageElement = document.createElement('div');
                    messageElement.classList.add('message');
                    messageElement.classList.add(message.user_id === '<?php echo $_SESSION['chat_user_id']; ?>' ? 'user' : 'support');
                    messageElement.textContent = message.message;
                    chatBox.appendChild(messageElement);
                });

                // Scroll to the bottom
                chatBox.scrollTop = chatBox.scrollHeight;
            } catch (error) {
                console.error('Error fetching messages:', error);
            }
        }

        // Function to send a message
        async function sendMessage(message) {
            try {
                await fetch('live_chat.php', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({ message })
                });
                fetchMessages(); // Refresh messages
            } catch (error) {
                console.error('Error sending message:', error);
            }
        }

        // Event listener for form submission
        chatForm.addEventListener('submit', e => {
            e.preventDefault();
            const message = messageInput.value.trim();
            if (message) {
                sendMessage(message);
                messageInput.value = ''; // Clear input
            }
        });

        // Periodically fetch new messages
        setInterval(fetchMessages, 3000);

        // Initial fetch
        fetchMessages();
    </script>
</body>
</html>
```

**Note:** Ensure that your database has a table `messages` with columns `id (AUTO_INCREMENT)`, `user_id (VARCHAR)`, `message (TEXT)`, and `created_at (DATETIME)`.
