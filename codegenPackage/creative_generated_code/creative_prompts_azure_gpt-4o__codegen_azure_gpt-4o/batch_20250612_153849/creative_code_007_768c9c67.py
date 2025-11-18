"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Write code in PHP to create a self-destructing note system where users can set expiration times and passwords, similar to the features on privnote.co.
Generated: DETERMINISTIC_768c9c67c8033d1f
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration
$dbHost = 'localhost';
$dbUser = 'root';
$dbPass = '';
$dbName = 'self_destructing_notes';

// Establish a database connection
try {
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUser, $dbPass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Helper function to generate a random string for note ID
function generateNoteId($length = 10) {
    return bin2hex(random_bytes($length / 2));
}

// Handle note creation
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['content'], $_POST['expiration_time'], $_POST['password'])) {
    try {
        // Sanitize input
        $content = htmlspecialchars($_POST['content']);
        $expirationTime = htmlspecialchars($_POST['expiration_time']);
        $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
        $noteId = generateNoteId();

        // Calculate expiration datetime
        $expirationDatetime = date('Y-m-d H:i:s', strtotime("+$expirationTime minutes"));

        // Insert the note into the database
        $stmt = $pdo->prepare("INSERT INTO notes (note_id, content, password, expiration_datetime) VALUES (?, ?, ?, ?)");
        $stmt->execute([$noteId, $content, $password, $expirationDatetime]);

        // Return the note link
        echo json_encode(['status' => 'success', 'note_link' => "view_note.php?note_id=$noteId"]);
    } catch (Exception $e) {
        echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
    }
    exit;
}

// Handle note retrieval
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['note_id'], $_GET['password'])) {
    try {
        // Sanitize input
        $noteId = htmlspecialchars($_GET['note_id']);
        $passwordInput = $_GET['password'];

        // Fetch the note from the database
        $stmt = $pdo->prepare("SELECT content, password, expiration_datetime FROM notes WHERE note_id = ?");
        $stmt->execute([$noteId]);
        $note = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$note) {
            echo json_encode(['status' => 'error', 'message' => 'Note not found or already deleted.']);
            exit;
        }

        // Check expiration
        $currentDatetime = date('Y-m-d H:i:s');
        if ($currentDatetime > $note['expiration_datetime']) {
            echo json_encode(['status' => 'error', 'message' => 'Note has expired.']);
            exit;
        }

        // Verify password
        if (!password_verify($passwordInput, $note['password'])) {
            echo json_encode(['status' => 'error', 'message' => 'Incorrect password.']);
            exit;
        }

        // Delete the note after viewing
        $stmt = $pdo->prepare("DELETE FROM notes WHERE note_id = ?");
        $stmt->execute([$noteId]);

        // Return the note content
        echo json_encode(['status' => 'success', 'content' => $note['content']]);
    } catch (Exception $e) {
        echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
    }
    exit;
}
?>

<!-- HTML Form for note creation -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Self-Destructing Notes</title>
</head>
<body>
    <h1>Create a Self-Destructing Note</h1>
    <form method="POST" action="">
        <label for="content">Note Content:</label><br>
        <textarea id="content" name="content" required></textarea><br><br>
        
        <label for="expiration_time">Expiration Time (in minutes):</label><br>
        <input id="expiration_time" name="expiration_time" type="number" required><br><br>
        
        <label for="password">Password:</label><br>
        <input id="password" name="password" type="password" required><br><br>
        
        <button type="submit">Create Note</button>
    </form>
</body>
</html>
```

**SQL Schema for the Database (`self_destructing_notes`):**
```sql
CREATE TABLE `notes` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `note_id` VARCHAR(255) NOT NULL UNIQUE,
    `content` TEXT NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `expiration_datetime` DATETIME NOT NULL
);
```
