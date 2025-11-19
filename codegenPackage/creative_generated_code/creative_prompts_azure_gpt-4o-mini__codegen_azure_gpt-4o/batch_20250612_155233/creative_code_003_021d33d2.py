"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: What libraries or tools are recommended for developing a free website with PHP and MySQL?
Generated: DETERMINISTIC_021d33d27a677e7e
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// ---------------------------------------------
// Simple PHP script to set up a basic website
// with MySQL integration
// ---------------------------------------------

// Configuration for database connection
define('DB_HOST', 'localhost');    // Database host
define('DB_USER', 'root');         // Database user
define('DB_PASS', '');             // Database password
define('DB_NAME', 'example_db');   // Database name

// Utility: Connect to the MySQL database
function connectDatabase() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die("Database connection failed: " . $mysqli->connect_error);
    }

    return $mysqli;
}

// Utility: Create a table if it doesn't exist
function createTable($mysqli) {
    $createTableSQL = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    if ($mysqli->query($createTableSQL) === FALSE) {
        die("Error creating table: " . $mysqli->error);
    }
}

// Utility: Insert a user into the database
function addUser($mysqli, $name, $email) {
    $stmt = $mysqli->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    if (!$stmt) {
        die("Prepare failed: " . $mysqli->error);
    }

    $stmt->bind_param("ss", $name, $email);
    if (!$stmt->execute()) {
        die("Execution failed: " . $stmt->error);
    }

    $stmt->close();
}

// Main: Handle incoming requests
// ---------------------------------------------
// For demonstration purposes, we'll simulate
// adding a user via a simple form submission.
// ---------------------------------------------

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Connect to the database
    $mysqli = connectDatabase();

    // Create the table if it doesn't exist
    createTable($mysqli);

    // Retrieve and sanitize user input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));

    // Validate user input
    if (empty($name) || empty($email)) {
        echo "<p>Error: Name and email are required.</p>";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<p>Error: Invalid email format.</p>";
    } else {
        // Add user to the database
        addUser($mysqli, $name, $email);
        echo "<p>User successfully added!</p>";
    }

    // Close the database connection
    $mysqli->close();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP Website</title>
</head>
<body>
    <!-- Simple form to add a user -->
    <h1>Add a User</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
