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
// self_destructing_note.php

// Database configuration (adjust to your settings)
$host = 'localhost';
$db = 'self_destruct_notes';
$user = 'your_username';
$pass = 'your_password';

try {
    // Create a new PDO connection
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to create a self-destructing note
function createNote($content, $expiration, $password) {
    global $pdo;

    // Validate inputs
    if (empty($content) || empty($expiration) || empty($password)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    // Prepare SQL to insert note
    $stmt = $pdo->prepare("INSERT INTO notes (content, expiration, password, created_at) VALUES (?, ?, ?, NOW())");
    
    // Execute the statement with provided data
    $stmt->execute([$content, $expiration, password_hash($password, PASSWORD_DEFAULT)]);

    return $pdo->lastInsertId();
}

// Function to retrieve a note (and check if it is expired)
function getNote($id, $password) {
    global $pdo;

    // Prepare SQL to retrieve the note
    $stmt = $pdo->prepare("SELECT content, expiration, created_at, password FROM notes WHERE id = ?");
    $stmt->execute([$id]);
    $note = $stmt->fetch(PDO::FETCH_ASSOC);

    // Check if note exists
    if (!$note) {
        throw new Exception("Note not found.");
    }

    // Check if the note is expired
    $createdAt = new DateTime($note['created_at']);
    $expiration = new DateTime($note['expiration']);
    if (new DateTime() > $expiration) {
        // Delete the note as it is expired
        deleteNote($id);
        throw new Exception("This note has expired.");
    }

    // Check password
    if (!password_verify($password, $note['password'])) {
        throw new Exception("Invalid password.");
    }

    return $note['content'];
}

// Function to delete a note
function deleteNote($id) {
    global $pdo;

    // Prepare SQL to delete the note
    $stmt = $pdo->prepare("DELETE FROM notes WHERE id = ?");
    $stmt->execute([$id]);
}

// Example usage
try {
    // Create a self-destructing note
    $noteId = createNote("This is a confidential message.", "2023-12-31 23:59:59", "securepassword");
    echo "Note created with ID: $noteId\n";

    // Retrieve the note (for demonstration purposes, assume ID and password are known)
    $content = getNote($noteId, "securepassword");
    echo "Retrieved Note Content: $content\n";

    // Clean up (delete the note)
    deleteNote($noteId);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (InvalidArgumentException $e) {
    echo "Input Error: " . $e->getMessage() . "\n";
}

?>
```
**Note:** The above code assumes you have a MySQL database set up with the necessary table structure. Ensure you create a table called `notes` with at least the following columns: `id` (AUTO_INCREMENT, PRIMARY KEY), `content` (TEXT), `expiration` (DATETIME), `password` (VARCHAR), and `created_at` (DATETIME). Make sure to handle database credentials securely and never expose them in your code.
