"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseaquii.webcindario.com
Prompt: Generate a PHP script for creating a user registration form with MySQL integration, optimized for deployment on free hosting services.
Generated: DETERMINISTIC_78c72afaa33b5260
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

// Database configuration
$dbHost = 'localhost'; // Database host
$dbUsername = 'username'; // Database username
$dbPassword = 'password'; // Database password
$dbName = 'database'; // Database name

// Create connection
$conn = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags($data));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize an array to hold errors
    $errors = [];

    // Validate and sanitize input fields
    $username = isset($_POST['username']) ? sanitizeInput($_POST['username']) : '';
    $password = isset($_POST['password']) ? sanitizeInput($_POST['password']) : '';

    // Simple validation
    if (empty($username)) {
        $errors[] = "Username is required.";
    }
    if (empty($password)) {
        $errors[] = "Password is required.";
    }

    // If no errors, proceed to register the user
    if (empty($errors)) {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare a SQL statement to insert the user into the database
        $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        $stmt->bind_param("ss", $username, $hashedPassword);

        // Execute the statement and check for errors
        if ($stmt->execute()) {
            $_SESSION['success'] = "Registration successful. You can now log in.";
            header("Location: login.php"); // Redirect to login page
            exit();
        } else {
            $errors[] = "Error: " . $stmt->error;
        }
        $stmt->close();
    }

    // Store errors in session for display
    if (!empty($errors)) {
        $_SESSION['errors'] = $errors;
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link rel="stylesheet" href="style.css"> <!-- Include your stylesheet -->
</head>
<body>
    <h2>User Registration</h2>
    <?php
    // Display errors if any
    if (isset($_SESSION['errors'])) {
        foreach ($_SESSION['errors'] as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
        unset($_SESSION['errors']); // Clear errors after displaying
    }
    ?>
    <form action="" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```
