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
// Start the session to manage form submission data
session_start();

// Include necessary libraries for validation (if any)
require 'vendor/autoload.php'; // Composer autoloader for validation libraries

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Function to validate email address
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// Function to handle form submission
function handleFormSubmission() {
    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Initialize an array to hold errors
        $errors = [];

        // Fetch and sanitize form data
        $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
        $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
        $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';

        // Validate the name
        if (empty($name)) {
            $errors[] = "Name is required.";
        }

        // Validate the email
        if (empty($email)) {
            $errors[] = "Email is required.";
        } elseif (!isValidEmail($email)) {
            $errors[] = "Invalid email format.";
        }

        // Validate the message
        if (empty($message)) {
            $errors[] = "Message is required.";
        }

        // Check for errors
        if (empty($errors)) {
            // Process the form (e.g., send email or save to database)
            // Example: Sending an email (update with your email configurations)
            $to = 'youremail@example.com'; // Change to your email
            $subject = 'New Form Submission';
            $body = "Name: $name\nEmail: $email\nMessage:\n$message";
            $headers = "From: $email";

            if (mail($to, $subject, $body, $headers)) {
                // Success response
                $_SESSION['success'] = "Your message has been sent successfully!";
            } else {
                // Failure response
                $_SESSION['error'] = "There was an error sending your message. Please try again later.";
            }
        } else {
            // Store errors in session for displaying to user
            $_SESSION['errors'] = $errors;
        }

        // Redirect to the previous page or a confirmation page
        header("Location: " . $_SERVER['HTTP_REFERER']);
        exit;
    }
}

// Call the form handling function
handleFormSubmission();
?>
```

### Form HTML Example
```html
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
        echo "<p style='color: green;'>".$_SESSION['success']."</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p style='color: red;'>".$_SESSION['error']."</p>";
        unset($_SESSION['error']);
    }
    if (isset($_SESSION['errors'])) {
        foreach ($_SESSION['errors'] as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
        unset($_SESSION['errors']);
    }
    ?>
    <form action="your_script.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
