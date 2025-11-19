"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Create a PHP script that processes job applications for the Philippine Coast Guard, capturing user inputs like name, age, and contact information.
Generated: DETERMINISTIC_90ab8665fbfda964
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// job_application.php

// Start session to track form submissions and errors
session_start();

/**
 * Function to sanitize user inputs
 * 
 * @param string $data User input data
 * @return string Sanitized data
 */
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize an array to hold error messages
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture and sanitize user inputs
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $age = isset($_POST['age']) ? sanitizeInput($_POST['age']) : '';
    $contact = isset($_POST['contact']) ? sanitizeInput($_POST['contact']) : '';

    // Validate name
    if (empty($name)) {
        $errors['name'] = "Name is required.";
    }

    // Validate age
    if (empty($age) || !is_numeric($age) || $age <= 0) {
        $errors['age'] = "Valid age is required.";
    }

    // Validate contact information
    if (empty($contact) || !preg_match('/^[0-9]{10}$/', $contact)) {
        $errors['contact'] = "Valid contact number is required (10 digits).";
    }

    // If there are no errors, process the application
    if (empty($errors)) {
        // Here, you can implement the code to save the application to a database or send an email
        // For demonstration, we'll just store the success message in a session variable
        $_SESSION['success'] = "Application submitted successfully!";
        header("Location: success.php");
        exit();
    } else {
        // Store errors in session for display on the form page
        $_SESSION['errors'] = $errors;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Application - Philippine Coast Guard</title>
</head>
<body>
    <h1>Job Application Form</h1>

    <?php
    // Display error messages if there are any
    if (!empty($_SESSION['errors'])) {
        echo '<div style="color: red;">';
        foreach ($_SESSION['errors'] as $error) {
            echo "<p>$error</p>";
        }
        echo '</div>';
        // Clear errors after displaying
        unset($_SESSION['errors']);
    }
    ?>

    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>
        <br>

        <label for="age">Age:</label>
        <input type="number" name="age" id="age" required>
        <br>

        <label for="contact">Contact Number:</label>
        <input type="text" name="contact" id="contact" required>
        <br>

        <button type="submit">Submit Application</button>
    </form>
</body>
</html>
```

```php
<?php
// success.php

// Start session to access success message
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Successful</title>
</head>
<body>
    <h1>Application Status</h1>
    <?php
    // Display success message if available
    if (isset($_SESSION['success'])) {
        echo "<p style='color: green;'>{$_SESSION['success']}</p>";
        // Clear success message after displaying
        unset($_SESSION['success']);
    } else {
        echo "<p>No application submitted.</p>";
    }
    ?>
    <a href="job_application.php">Back to Application Form</a>
</body>
</html>
```
