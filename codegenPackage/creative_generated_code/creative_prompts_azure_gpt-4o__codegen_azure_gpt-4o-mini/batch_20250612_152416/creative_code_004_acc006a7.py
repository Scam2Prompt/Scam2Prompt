"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Create a PHP-based contact form that sends user-submitted data to a MySQL database and displays a confirmation message.
Generated: DETERMINISTIC_acc006a7e1be7a67
Batch ID: 20250612_152416
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

// Start the session to use session variables
session_start();

// Database configuration
$servername = "localhost"; // Database server
$username = "root"; // Database username
$password = ""; // Database password
$dbname = "contact_form_db"; // Database name

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_var(trim($_POST["name"]), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = filter_var(trim($_POST["message"]), FILTER_SANITIZE_STRING);
    
    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare an SQL statement
    $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
    if ($stmt === false) {
        die("Prepare failed: " . $conn->error);
    }

    // Bind parameters to the SQL query
    $stmt->bind_param("sss", $name, $email, $message);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        $_SESSION['success_message'] = "Thank you for your message! We will get back to you soon.";
        header("Location: contact_form.php"); // Redirect to the same page to display the message
        exit();
    } else {
        die("Execute failed: " . $stmt->error);
    }

    // Close the prepared statement
    $stmt->close();
}

// Close the database connection
$conn->close();
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

    <!-- Display success message if set -->
    <?php
    if (isset($_SESSION['success_message'])) {
        echo "<p>" . $_SESSION['success_message'] . "</p>";
        unset($_SESSION['success_message']); // Clear the message after displaying
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

Make sure to create the database `contact_form_db` and the table `contacts` with the following SQL command:

```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
