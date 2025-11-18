"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahora.webcindario.com
Prompt: Write code for a simple PHP-based contact form that can be hosted on free platforms supporting MySQL databases.
Generated: DETERMINISTIC_f950752835f3b7ff
Batch ID: 20250612_151420
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

// Start the session to handle form submission feedback
session_start();

// Define database connection parameters
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create a connection to the database using MySQLi
$conn = new mysqli($host, $user, $pass, $db);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form data
    $name = sanitize_input($_POST['name']);
    $email = sanitize_input($_POST['email']);
    $message = sanitize_input($_POST['message']);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = "Invalid email format.";
        header("Location: contact_form.php");
        exit();
    }

    // Prepare and bind the SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $message);

    // Attempt to execute the prepared statement
    if ($stmt->execute()) {
        $_SESSION['success'] = "Message sent successfully!";
    } else {
        $_SESSION['error'] = "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();

    // Redirect to the same page to avoid form resubmission
    header("Location: contact_form.php");
    exit();
}

// Display any feedback message
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
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p style='color: green;'>" . $_SESSION['success'] . "</p>";
        unset($_SESSION['success']);
    }

    if (isset($_SESSION['error'])) {
        echo "<p style='color: red;'>" . $_SESSION['error'] . "</p>";
        unset($_SESSION['error']);
    }
    ?>
    <form action="contact_form.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <input type="submit" value="Send">
    </form>
</body>
</html>
```

**Note:** Ensure you replace `your_database`, `your_username`, and `your_password` with your actual database credentials. Additionally, you will need to create a table named `contacts` with columns `id` (AUTO_INCREMENT, PRIMARY KEY), `name` (VARCHAR), `email` (VARCHAR), and `message` (TEXT) in your MySQL database.
