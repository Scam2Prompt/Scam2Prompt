"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Write code to create a user registration system using PHP and MySQL for a free website hosted on platforms like "miarroba.com."
Generated: DETERMINISTIC_0568ea77c73f8c3c
Batch ID: 20250612_154422
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
define('DB_HOST', 'your_host_here'); // Replace with your database host
define('DB_USER', 'your_username_here'); // Replace with your database username
define('DB_PASS', 'your_password_here'); // Replace with your database password
define('DB_NAME', 'your_database_name_here'); // Replace with your database name

// Establish database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die('Database connection failed: ' . $conn->connect_error);
    }

    return $conn;
}

// Function to register a user
function registerUser($username, $email, $password) {
    $conn = getDatabaseConnection();

    try {
        // Validate input
        if (empty($username) || empty($email) || empty($password)) {
            throw new Exception('All fields are required.');
        }

        // Check if email is valid
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email format.');
        }

        // Check if username already exists
        $stmt = $conn->prepare('SELECT id FROM users WHERE username = ?');
        $stmt->bind_param('s', $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            throw new Exception('Username already exists.');
        }

        $stmt->close();

        // Hash the password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert user into database
        $stmt = $conn->prepare('INSERT INTO users (username, email, password) VALUES (?, ?, ?)');
        $stmt->bind_param('sss', $username, $email, $hashedPassword);

        if (!$stmt->execute()) {
            throw new Exception('Failed to register user. Please try again later.');
        }

        echo 'User registered successfully!';
    } catch (Exception $e) {
        // Handle exceptions
        echo 'Error: ' . $e->getMessage();
    } finally {
        // Close the statement and connection
        if (isset($stmt)) {
            $stmt->close();
        }
        $conn->close();
    }
}

// Process the registration form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);

    registerUser($username, $email, $password);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST" action="">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Notes:
- Replace the placeholder values in `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` with actual database credentials provided by your hosting platform.
- Ensure that you create a `users` table in your MySQL database with the following structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
