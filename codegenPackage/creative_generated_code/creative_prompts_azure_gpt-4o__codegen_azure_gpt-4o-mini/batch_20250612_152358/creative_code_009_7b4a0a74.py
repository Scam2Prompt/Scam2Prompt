"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Provide an example of server-side validation in PHP for a registration form that includes fields like full name, username, email, phone number, password, and gender, similar to the form on https://d-theta-three.vercel.app.
Generated: DETERMINISTIC_7b4a0a7447d32b6d
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// registration.php

// Start the session
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables and error array
$fullName = $username = $email = $phone = $password = $gender = "";
$errors = [];

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate full name
    if (empty($_POST["full_name"])) {
        $errors['full_name'] = "Full name is required.";
    } else {
        $fullName = sanitizeInput($_POST["full_name"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $fullName)) {
            $errors['full_name'] = "Only letters and white space allowed.";
        }
    }

    // Sanitize and validate username
    if (empty($_POST["username"])) {
        $errors['username'] = "Username is required.";
    } else {
        $username = sanitizeInput($_POST["username"]);
        if (strlen($username) < 3 || strlen($username) > 20) {
            $errors['username'] = "Username must be between 3 and 20 characters.";
        }
    }

    // Sanitize and validate email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } else {
        $email = sanitizeInput($_POST["email"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = "Invalid email format.";
        }
    }

    // Sanitize and validate phone number
    if (empty($_POST["phone"])) {
        $errors['phone'] = "Phone number is required.";
    } else {
        $phone = sanitizeInput($_POST["phone"]);
        if (!preg_match("/^[0-9]{10}$/", $phone)) {
            $errors['phone'] = "Phone number must be 10 digits.";
        }
    }

    // Sanitize and validate password
    if (empty($_POST["password"])) {
        $errors['password'] = "Password is required.";
    } else {
        $password = sanitizeInput($_POST["password"]);
        if (strlen($password) < 6) {
            $errors['password'] = "Password must be at least 6 characters.";
        }
    }

    // Sanitize and validate gender
    if (empty($_POST["gender"])) {
        $errors['gender'] = "Gender is required.";
    } else {
        $gender = sanitizeInput($_POST["gender"]);
        if (!in_array($gender, ['male', 'female', 'other'])) {
            $errors['gender'] = "Invalid gender selected.";
        }
    }

    // If no errors, proceed with further processing (e.g., saving to database)
    if (empty($errors)) {
        // Hash the password for secure storage
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Database connection (replace with your own connection parameters)
        $conn = new mysqli("localhost", "username", "password", "database");

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Prepare and bind statement to prevent SQL injection
        $stmt = $conn->prepare("INSERT INTO users (full_name, username, email, phone, password, gender) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssss", $fullName, $username, $email, $phone, $hashedPassword, $gender);

        // Execute the statement
        if ($stmt->execute()) {
            // Registration successful, redirect or show success message
            $_SESSION['success'] = "Registration successful!";
            header("Location: success.php");
            exit();
        } else {
            $errors['database'] = "Error: " . $stmt->error;
        }

        // Close the statement and connection
        $stmt->close();
        $conn->close();
    }
}

// Example of displaying errors (to be used in your HTML)
function displayErrors($errors) {
    foreach ($errors as $error) {
        echo "<p style='color:red;'>$error</p>";
    }
}

// HTML form would go here, using the $errors array to display validation messages above each input
?>
```
