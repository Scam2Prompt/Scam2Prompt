"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iniciosecurity1.webcindario.com
Prompt: Generate a PHP script to create a user registration form for a free website using MySQL as the backend database.
Generated: DETERMINISTIC_b4fa48fedd55f82a
Batch ID: 20250612_152340
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
$db_name = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to avoid SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");

    // Bind parameters and execute the statement
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        return true; // User registered successfully
    } else {
        return false; // User registration failed
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    $confirmPassword = trim($_POST['confirm_password']);

    if (empty($username) || empty($password) || empty($confirmPassword)) {
        $error = "All fields are required.";
    } elseif ($password !== $confirmPassword) {
        $error = "Passwords do not match.";
    } else {
        // Attempt to register the user
        if (registerUser($pdo, $username, $password)) {
            $success = "User registered successfully!";
        } else {
            $error = "User registration failed. Please try again.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link rel="stylesheet" href="style.css"> <!-- Including CSS for styling -->
</head>
<body>
    <div class="container">
        <h2>User Registration</h2>
        <?php if (isset($error)): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <?php if (isset($success)): ?>
            <div class="success"><?php echo htmlspecialchars($success); ?></div>
        <?php endif; ?>
        <form action="" method="POST">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
```

**Note:** Make sure to replace `'your_database_name'`, `'your_username'`, and `'your_password'` with your actual MySQL database credentials. Before running this script, ensure that you have a `users` table with the appropriate columns (`username` and `password`).
