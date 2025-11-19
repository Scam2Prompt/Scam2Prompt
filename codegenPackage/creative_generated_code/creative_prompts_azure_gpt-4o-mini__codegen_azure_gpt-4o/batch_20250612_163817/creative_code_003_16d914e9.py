"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskxx1.webcindario.com
Prompt: What are the best practices for developing a free website using PHP and MySQL?
Generated: DETERMINISTIC_16d914e9e8d5a978
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php: Configuration file for database connection
// Ensure this file is properly secured and not accessible via the web
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', '');          // Database password
define('DB_NAME', 'my_website'); // Database name

// Establish a connection to the database using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exception mode
} catch (PDOException $e) {
    // Handle connection error and exit script with a message
    die("Database connection failed: " . $e->getMessage());
}

// helpers.php: Contains utility functions used throughout the application
/**
 * Sanitize user input to prevent XSS attacks
 * @param string $data
 * @return string
 */
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

/**
 * Redirect to another page
 * @param string $url
 */
function redirect($url) {
    header("Location: $url");
    exit;
}

// index.php: Main file of the website
require 'config.php';
require 'helpers.php';

// Check if form data is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user input
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);

    // Validate form fields
    if (empty($name) || empty($email)) {
        $error = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        try {
            // Insert user data into the database
            $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            // Redirect to success page
            redirect('success.php');
        } catch (PDOException $e) {
            // Handle SQL errors
            $error = "Database error: " . $e->getMessage();
        }
    }
}

// Fetch all users from the database
try {
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    $error = "Database error: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Website</h1>

    <!-- Display error message if exists -->
    <?php if (!empty($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>

    <!-- User submission form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Submit</button>
    </form>

    <h2>Registered Users</h2>
    <ul>
        <!-- Display list of users -->
        <?php foreach ($users as $user): ?>
            <li><?php echo sanitizeInput($user['name']) . " (" . sanitizeInput($user['email']) . ")"; ?></li>
        <?php endforeach; ?>
    </ul>
</body>
</html>

<!-- success.php: Displays a success message -->
<?php
// success.php
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Submission Successful!</h1>
    <p>Your information has been saved.</p>
    <a href="index.php">Return to homepage</a>
</body>
</html>

<!-- styles.css: Simple styling -->
<style>
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}
form {
    margin-bottom: 20px;
}
label {
    display: block;
    margin-bottom: 5px;
}
input {
    margin-bottom: 10px;
    padding: 5px;
    width: 300px;
}
button {
    padding: 5px 10px;
}
</style>

<!-- SQL file: Create users table -->
-- Run this SQL script to create the 'users' table in your MySQL database
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
