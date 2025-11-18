"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendaportal.webcindario.com
Prompt: Write PHP code for a contact form that stores submissions in a MySQL database, optimized for free hosting environments.
Generated: DETERMINISTIC_938573e98c89e0dd
Batch ID: 20250612_151459
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
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Error handling for empty fields
    if (empty($name) || empty($email) || empty($message)) {
        die("Please fill in all fields.");
    }

    // Error handling for invalid email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())");

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);

    // Execute the statement and handle potential errors
    try {
        $stmt->execute();
        echo "Thank you for your submission!";
    } catch (PDOException $e) {
        die("Failed to store your message: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

Make sure to replace `'your_database_name'`, `'your_username'`, and `'your_password'` with your actual database credentials. Also, ensure that the database table `contacts` exists with the necessary columns: `name`, `email`, `message`, and `submitted_at`.
