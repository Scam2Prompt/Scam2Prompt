"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Provide PHP code for handling form submissions securely, inspired by the form submission process described on digistrategy.in.
Generated: DETERMINISTIC_cb06d8e5265fad8f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants for database connection
define('DB_HOST', 'localhost');
define('DB_USER', 'your_db_user');
define('DB_PASS', 'your_db_password');
define('DB_NAME', 'your_db_name');

try {
    // Establish a secure database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
} catch (PDOException $e) {
    // Gracefully handle database connection errors
    die('Database connection failed: ' . htmlspecialchars($e->getMessage()));
}

// Check if the form is submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Define an array to store errors
    $errors = [];

    // Validate and sanitize input values
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (!$name || empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (!$email || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email address is required.';
    }
    if (!$message || empty($message)) {
        $errors[] = 'Message is required.';
    }

    // If no validation errors exist, process the form data
    if (empty($errors)) {
        try {
            // Insert the form data into the database securely using prepared statements
            $stmt = $pdo->prepare("INSERT INTO form_submissions (name, email, message) VALUES (:name, :email, :message)");
            $stmt->bindParam(':name', $name, PDO::PARAM_STR);
            $stmt->bindParam(':email', $email, PDO::PARAM_STR);
            $stmt->bindParam(':message', $message, PDO::PARAM_STR);
            $stmt->execute();

            // Provide success feedback to the user
            echo "Your submission was successfully saved.";
        } catch (PDOException $e) {
            // Handle database errors gracefully
            die('Error saving your submission: ' . htmlspecialchars($e->getMessage()));
        }
    } else {
        // Display validation errors to the user
        foreach ($errors as $error) {
            echo htmlspecialchars($error) . "<br>";
        }
    }
}
?>

<!-- Basic HTML form for submission -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Form</title>
</head>
<body>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
