"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Write a script in PHP to create a user registration system for a website hosted on free platforms supporting MySQL databases.
Generated: DETERMINISTIC_fd71807f82952d1d
Batch ID: 20250612_154740
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
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection error
    die("Connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve and sanitize input data
    $username = trim(filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING));
    $password = trim(filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING));
    $email = trim(filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL));

    // Validate input data
    if (empty($username) || empty($password) || empty($email)) {
        $error = "Please fill in all fields.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        // Hash password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->bindParam(':email', $email);

        try {
            // Execute the statement
            if ($stmt->execute()) {
                $success = "User registered successfully!";
            }
        } catch (PDOException $e) {
            // Handle SQL errors
            $error = "Error: " . $e->getMessage();
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
</head>
<body>
    <h2>User Registration</h2>

    <!-- Display success or error messages -->
    <?php if (isset($success)) { echo "<p style='color: green;'>$success</p>"; } ?>
    <?php if (isset($error)) { echo "<p style='color: red;'>$error</p>"; } ?>

    <!-- Registration form -->
    <form action="" method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
        <br>

        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**Notes:**
1. Ensure that the database connection details (host, dbname, username, password) are updated to match your environment.
2. Create a `users` table in your MySQL database with fields for `username`, `password`, and `email`.
3. The password is hashed using `password_hash`, which is important for security.
4. Error handling is implemented to manage both connection and SQL execution errors.
