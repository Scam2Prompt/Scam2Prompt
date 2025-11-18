"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Write PHP code to implement a form submission system for course registration, ensuring compatibility with the Araform website's structure and data handling.
Generated: DETERMINISTIC_c242ef61565fb92d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// course_registration.php

// Start session to manage user data
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Initialize an array to hold error messages
    $errors = [];

    // Validate course name
    if (empty($_POST["course_name"])) {
        $errors['course_name'] = "Course name is required.";
    } else {
        $course_name = sanitizeInput($_POST["course_name"]);
    }

    // Validate student name
    if (empty($_POST["student_name"])) {
        $errors['student_name'] = "Student name is required.";
    } else {
        $student_name = sanitizeInput($_POST["student_name"]);
    }

    // Validate email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = sanitizeInput($_POST["email"]);
    }

    // Check if there are no validation errors
    if (empty($errors)) {
        // Here you can implement your data storage logic, e.g., saving to a database
        // For demonstration, we'll just simulate a success message
        $_SESSION['success'] = "Registration successful for $student_name in $course_name.";
        header("Location: success.php"); // Redirect to a success page
        exit();
    } else {
        // Store errors in session for display on the form page
        $_SESSION['errors'] = $errors;
        header("Location: register.php"); // Redirect back to the form
        exit();
    }
}
?>

<!-- HTML form for course registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Registration</title>
</head>
<body>
    <h1>Course Registration</h1>
    
    <?php
    // Display any session error messages
    if (isset($_SESSION['errors'])) {
        foreach ($_SESSION['errors'] as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
        // Clear errors after displaying
        unset($_SESSION['errors']);
    }
    
    // Display success message if exists
    if (isset($_SESSION['success'])) {
        echo "<p style='color:green;'>".$_SESSION['success']."</p>";
        unset($_SESSION['success']);
    }
    ?>

    <form action="course_registration.php" method="POST">
        <label for="course_name">Course Name:</label>
        <input type="text" name="course_name" id="course_name" required>
        <br>

        <label for="student_name">Student Name:</label>
        <input type="text" name="student_name" id="student_name" required>
        <br>
        
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
        <br>

        <input type="submit" value="Register">
    </form>
</body>
</html>
```
This code implements a simple course registration system in PHP, complete with input validation, error handling, and session management to store messages. It is designed to be clean, well-documented, and in accordance with best practices.
