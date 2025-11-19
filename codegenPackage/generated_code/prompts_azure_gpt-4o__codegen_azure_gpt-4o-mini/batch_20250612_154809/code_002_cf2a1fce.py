"""
Generated Code Metadata:
========================
Original URL: https://suiwebio.rf.gd
Prompt: Generate PHP code for a website that can be hosted on a service offering multiple PHP versions and unlimited bandwidth, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_cf2a1fce9c8188d5
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// index.php

// Start the session
session_start();

/**
 * Function to connect to the database
 * 
 * @return PDO
 * @throws Exception if the connection fails
 */
function connectDatabase() {
    $host = 'localhost'; // Database host
    $db = 'your_database'; // Database name
    $user = 'your_username'; // Database username
    $pass = 'your_password'; // Database password
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (\PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

/**
 * Function to fetch all users from the database
 * 
 * @param PDO $pdo
 * @return array
 */
function fetchUsers($pdo) {
    $stmt = $pdo->query("SELECT id, username, email FROM users");
    return $stmt->fetchAll();
}

// Check if the request method is POST for form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    if ($username && $email) {
        try {
            $pdo = connectDatabase();
            $stmt = $pdo->prepare("INSERT INTO users (username, email) VALUES (?, ?)");
            $stmt->execute([$username, $email]);
            $_SESSION['message'] = "User added successfully!";
        } catch (Exception $e) {
            $_SESSION['error'] = "Error: " . $e->getMessage();
        }
    } else {
        $_SESSION['error'] = "Invalid input. Please try again.";
    }
}

// Fetch users to display
try {
    $pdo = connectDatabase();
    $users = fetchUsers($pdo);
} catch (Exception $e) {
    $_SESSION['error'] = "Error fetching users: " . $e->getMessage();
}

// HTML Output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>User Management</h1>

    <?php if (isset($_SESSION['message'])): ?>
        <div class="success"><?php echo $_SESSION['message']; unset($_SESSION['message']); ?></div>
    <?php endif; ?>

    <?php if (isset($_SESSION['error'])): ?>
        <div class="error"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></div>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <button type="submit">Add User</button>
    </form>

    <h2>Users List</h2>
    <ul>
        <?php foreach ($users as $user): ?>
            <li><?php echo htmlspecialchars($user['username']) . ' (' . htmlspecialchars($user['email']) . ')'; ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the user management page */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1, h2 {
    color: #333;
}

form {
    margin-bottom: 20px;
}

label {
    display: block;
    margin: 5px 0;
}

input {
    padding: 8px;
    margin-bottom: 10px;
    width: 100%;
    max-width: 300px;
}

button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.success {
    color: green;
}

.error {
    color: red;
}
```

**Note:** Make sure to replace `your_database`, `your_username`, and `your_password` with actual database credentials. Also, ensure that the database and the `users` table exist with appropriate columns (`id`, `username`, `email`).
