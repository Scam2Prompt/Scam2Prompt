"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Write code in PHP to create a self-destructing note system where users can set expiration times and passwords, similar to the features on privnote.co.
Generated: DETERMINISTIC_768c9c67c8033d1f
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
    'note_expiration_time' => 604800, // 1 week in seconds
];

// Create a PDO instance
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Connection failed: ' . $e->getMessage());
}

// Create table if it doesn't exist
$pdo->exec('
    CREATE TABLE IF NOT EXISTS notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        note TEXT NOT NULL,
        password VARCHAR(255) NOT NULL,
        expires_at INT NOT NULL,
        created_at INT NOT NULL DEFAULT ' . time() . '
    );
');

// Function to create a new note
function createNote($note, $password, $expires_at) {
    global $pdo;
    $stmt = $pdo->prepare('INSERT INTO notes (note, password, expires_at) VALUES (:note, :password, :expires_at)');
    $stmt->bindParam(':note', $note);
    $stmt->bindParam(':password', $password);
    $stmt->bindParam(':expires_at', $expires_at);
    $stmt->execute();
    return $pdo->lastInsertId();
}

// Function to get a note
function getNote($id, $password) {
    global $pdo;
    $stmt = $pdo->prepare('SELECT * FROM notes WHERE id = :id AND password = :password');
    $stmt->bindParam(':id', $id);
    $stmt->bindParam(':password', $password);
    $stmt->execute();
    return $stmt->fetch();
}

// Function to check if a note has expired
function hasNoteExpired($note) {
    return $note['expires_at'] < time();
}

// Function to delete a note
function deleteNote($id) {
    global $pdo;
    $stmt = $pdo->prepare('DELETE FROM notes WHERE id = :id');
    $stmt->bindParam(':id', $id);
    $stmt->execute();
}

// API Endpoints

// Create a new note
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['note']) && isset($_POST['password']) && isset($_POST['expires_at'])) {
    $note = trim($_POST['note']);
    $password = trim($_POST['password']);
    $expires_at = (int) $_POST['expires_at'];

    if (empty($note) || empty($password) || empty($expires_at)) {
        http_response_code(400);
        echo json_encode(['error' => 'Please fill in all fields']);
        exit;
    }

    $id = createNote($note, password_hash($password, PASSWORD_BCRYPT), $expires_at);
    echo json_encode(['id' => $id]);
}

// Get a note
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['id']) && isset($_GET['password'])) {
    $id = (int) $_GET['id'];
    $password = trim($_GET['password']);

    if (empty($id) || empty($password)) {
        http_response_code(400);
        echo json_encode(['error' => 'Please fill in all fields']);
        exit;
    }

    $note = getNote($id, $password);

    if (!$note) {
        http_response_code(404);
        echo json_encode(['error' => 'Note not found']);
        exit;
    }

    if (hasNoteExpired($note)) {
        deleteNote($id);
        http_response_code(410);
        echo json_encode(['error' => 'Note has expired']);
        exit;
    }

    echo json_encode(['note' => $note['note']]);
}

// Delete a note
if ($_SERVER['REQUEST_METHOD'] === 'DELETE' && isset($_GET['id']) && isset($_GET['password'])) {
    $id = (int) $_GET['id'];
    $password = trim($_GET['password']);

    if (empty($id) || empty($password)) {
        http_response_code(400);
        echo json_encode(['error' => 'Please fill in all fields']);
        exit;
    }

    $note = getNote($id, $password);

    if (!$note) {
        http_response_code(404);
        echo json_encode(['error' => 'Note not found']);
        exit;
    }

    deleteNote($id);
    http_response_code(200);
    echo json_encode(['message' => 'Note deleted']);
}
```
