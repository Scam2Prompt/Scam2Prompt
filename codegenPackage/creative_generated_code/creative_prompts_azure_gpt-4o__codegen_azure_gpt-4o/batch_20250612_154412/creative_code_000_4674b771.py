"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviseguridadon.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, using free hosting services similar to those mentioned on daviseguridadon.webcindario.com.
Generated: DETERMINISTIC_4674b77189ac7c11
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Initialize the session and error reporting
session_start();
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'localhost'); // Replace with your free hosting DB host
define('DB_USER', 'root');      // Replace with your free hosting DB user
define('DB_PASS', '');          // Replace with your free hosting DB password
define('DB_NAME', 'my_database'); // Replace with your free hosting DB name

// Establish a connection to MySQL database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for error handling
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Create a table if it doesn't exist
$tableQuery = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
try {
    $pdo->exec($tableQuery);
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Handle form submission for new user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['name'], $_POST['email'])) {
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);

    // Insert user into the database
    try {
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->execute(['name' => $name, 'email' => $email]);
        $successMessage = "User registered successfully!";
    } catch (PDOException $e) {
        $errorMessage = "Registration failed: " . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 400px;
            margin: auto;
        }
        .form-container form {
            display: flex;
            flex-direction: column;
        }
        .form-container form input {
            margin-bottom: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .form-container form button {
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .message {
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Register User</h1>
        <form method="POST" action="">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <button type="submit">Register</button>
        </form>

        <!-- Display messages -->
        <?php if (!empty($successMessage)): ?>
            <div class="message" style="color: green;"><?php echo $successMessage; ?></div>
        <?php elseif (!empty($errorMessage)): ?>
            <div class="message" style="color: red;"><?php echo $errorMessage; ?></div>
        <?php endif; ?>
    </div>

    <h2>Registered Users</h2>
    <ul>
        <?php
        // Fetch and display users from the database
        try {
            $stmt = $pdo->query("SELECT name, email FROM users ORDER BY created_at DESC");
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo "<li>{$row['name']} ({$row['email']})</li>";
            }
        } catch (PDOException $e) {
            echo "Error fetching users: " . $e->getMessage();
        }
        ?>
    </ul>
</body>
</html>
```
