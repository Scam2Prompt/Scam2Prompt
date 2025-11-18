"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Write PHP code for a contact form that stores submissions in a MySQL database, optimized for free hosting environments.
Generated: DETERMINISTIC_938573e98c89e0dd
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
// Configuration for database connection
define('DB_HOST', 'localhost'); // Change this to your database host
define('DB_USERNAME', 'root'); // Change this to your database username
define('DB_PASSWORD', ''); // Change this to your database password
define('DB_NAME', 'contact_form'); // Change this to your database name

// Connect to MySQL Database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
        PDO::ATTR_EMULATE_PREPARES => false,         // Disable emulated prepares for security
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Check if form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input fields
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = htmlspecialchars(trim($_POST['email'] ?? ''));
    $message = htmlspecialchars(trim($_POST['message'] ?? ''));

    // Validation checks
    $errors = [];
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }
    if (empty($message)) {
        $errors[] = "Message is required.";
    }

    // If there are no errors, process the form submission
    if (empty($errors)) {
        try {
            // Prepare and execute SQL statement to insert data
            $stmt = $pdo->prepare("INSERT INTO submissions (name, email, message, submitted_at) VALUES (?, ?, ?, ?)");
            $stmt->execute([$name, $email, $message, date('Y-m-d H:i:s')]);

            // Success message
            echo "Thank you for your submission!";
        } catch (PDOException $e) {
            // Handle database error
            echo "An error occurred while saving your submission: " . $e->getMessage();
        }
    } else {
        // Display validation errors
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    }
}
?>

<!-- HTML Contact Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <!-- Contact Form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>

<?php
// SQL for creating the database table (run this separately in your database management tool)
/*
CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at DATETIME NOT NULL
);
*/
?>
```
