"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar5-cambio.webcindario.com
Prompt: Write code to implement a contact form in PHP that stores submissions in a MySQL database for a free website project.
Generated: DETERMINISTIC_af648b54ff7cb2db
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include configuration file for database connection
require_once 'config.php'; // Ensure this file contains proper database credentials

// Function to sanitize input data to prevent XSS and SQL injection
function sanitize_input($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Initialize variables for error messages and input values
$name = $email = $message = "";
$errors = [];

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate name input
    if (empty($_POST['name'])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitize_input($_POST['name']);
        if (strlen($name) < 3) {
            $errors['name'] = "Name must be at least 3 characters.";
        }
    }

    // Sanitize and validate email input
    if (empty($_POST['email'])) {
        $errors['email'] = "Email is required.";
    } else {
        $email = sanitize_input($_POST['email']);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = "Invalid email format.";
        }
    }

    // Sanitize and validate message input
    if (empty($_POST['message'])) {
        $errors['message'] = "Message is required.";
    } else {
        $message = sanitize_input($_POST['message']);
        if (strlen($message) < 10) {
            $errors['message'] = "Message must be at least 10 characters.";
        }
    }

    // If there are no errors, proceed to insert the data into the database
    if (empty($errors)) {
        try {
            // Establish a connection with the database
            $pdo = new PDO("mysql:host=$db_host;dbname=$db_name", $db_user, $db_password);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Prepare the SQL statement
            $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)");

            // Bind values to the statement
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':message', $message);

            // Execute the statement
            $stmt->execute();

            // Display success message
            echo "<p>Thank you for your submission. We will get back to you soon!</p>";
        } catch (PDOException $e) {
            // Handle database connection errors
            echo "<p>Sorry, there was an error saving your submission. Please try again later.</p>";
            error_log("Database error: " . $e->getMessage()); // Log the error to a file for debugging
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
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?= htmlspecialchars($name) ?>">
        <span style="color: red;"><?= $errors['name'] ?? '' ?></span>
        <br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?= htmlspecialchars($email) ?>">
        <span style="color: red;"><?= $errors['email'] ?? '' ?></span>
        <br><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message"><?= htmlspecialchars($message) ?></textarea>
        <span style="color: red;"><?= $errors['message'] ?? '' ?></span>
        <br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
