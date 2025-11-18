"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Write a PHP script to authenticate users logging into a satisfaction survey portal for an edible printing service.
Generated: DETERMINISTIC_fb0e81b4877363af
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Satisfaction Survey Portal Authentication Script for Edible Printing Service
// Author: [Your Name]
// Description: This script handles user authentication for logging into the satisfaction survey portal.
// Last Updated: [Date]

// Start the session to track user login state
session_start();

// Database connection settings
define('DB_HOST', 'localhost'); // Change to your DB host
define('DB_USER', 'root');      // Change to your DB username
define('DB_PASS', 'password');  // Change to your DB password
define('DB_NAME', 'survey_db'); // Change to your DB name

try {
    // Establish a connection with the database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Set PDO error mode
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Check if the login form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $username = isset($_POST['username']) ? sanitizeInput($_POST['username']) : '';
    $password = isset($_POST['password']) ? sanitizeInput($_POST['password']) : '';

    // Ensure fields are not empty
    if (empty($username) || empty($password)) {
        echo "Please enter both username and password.";
        exit;
    }

    // Prepare SQL query to fetch user details
    $sql = "SELECT id, username, password FROM users WHERE username = :username LIMIT 1";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':username', $username, PDO::PARAM_STR);

    try {
        // Execute the query
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user) {
            // Verify the password
            if (password_verify($password, $user['password'])) {
                // Set session variables for the logged-in user
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $user['username'];

                // Redirect to the satisfaction survey page
                header("Location: survey.php");
                exit;
            } else {
                echo "Invalid credentials. Please try again.";
            }
        } else {
            echo "User not found. Please try again.";
        }
    } catch (PDOException $e) {
        // Handle query execution errors
        echo "An error occurred: " . $e->getMessage();
    }
} else {
    // Display the login form
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Satisfaction Survey Login</title>
    </head>
    <body>
        <h1>Login to Satisfaction Survey Portal</h1>
        <form method="POST" action="">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
