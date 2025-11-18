"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appvirtuals.webcindario.com
Prompt: Write PHP code for a basic contact form that stores submissions in a MySQL database, optimized for free hosting services.
Generated: DETERMINISTIC_9cefbe5c5f6f4a5e
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Start a session to store error messages
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance to connect to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input fields
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);
    
    $errors = [];

    // Basic validation
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "A valid email address is required.";
    }
    if (empty($message)) {
        $errors[] = "Message cannot be empty.";
    }

    // Check for errors
    if (empty($errors)) {
        // Prepare SQL query to insert the form data into the database
        $sql = "INSERT INTO contact_form (name, email, message) VALUES (:name, :email, :message)";
        
        try {
            $stmt = $pdo->prepare($sql);
            // Bind parameters to the SQL query
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':message', $message);
            
            // Execute the statement
            $stmt->execute();
            // Redirect or show success message
            $_SESSION['success'] = "Thank you for contacting us!";
            header("Location: thank_you.php");
            exit();
        } catch (PDOException $e) {
            // Handle SQL errors
            $errors[] = "Database error: " . $e->getMessage();
        }
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

    <?php
    // Display errors, if any
    if (!empty($errors)) {
        echo '<div style="color:red;">' . implode('<br>', $errors) . '</div>';
    }
    ?>

    <form action="contact_form.php" method="post">
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

### Note:
- Replace `'your_database'`, `'your_username'`, and `'your_password'` with your actual database credentials.
- Create a table `contact_form` in your MySQL database with columns: `id` (INT, AUTO_INCREMENT, PRIMARY KEY), `name` (VARCHAR), `email` (VARCHAR), `message` (TEXT).
- An additional `thank_you.php` page is recommended to display a success message after form submission.
