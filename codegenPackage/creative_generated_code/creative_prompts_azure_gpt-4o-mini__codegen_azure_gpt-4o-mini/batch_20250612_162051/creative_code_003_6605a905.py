"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onedivepb.com
Prompt: Develop a PHP script that allows users to contact One Dive for more information about their diving certifications.
Generated: DETERMINISTIC_6605a905952b6ff0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact.php

// Start a session to manage form submissions
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Initialize variables to hold form data and error messages
$name = $email = $message = "";
$errors = [];

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate inputs
    if (empty($_POST['name'])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST['name']);
    }

    if (empty($_POST['email'])) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var(sanitizeInput($_POST['email']), FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = sanitizeInput($_POST['email']);
    }

    if (empty($_POST['message'])) {
        $errors['message'] = "Message is required.";
    } else {
        $message = sanitizeInput($_POST['message']);
    }

    // If there are no errors, attempt to send the email
    if (empty($errors)) {
        $to = "info@onedive.com"; // Change to the actual contact email
        $subject = "Contact Form Submission from " . $name;
        $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
        $headers = "From: $email\r\nReply-To: $email\r\n";

        // Attempt to send the email and handle errors
        if (mail($to, $subject, $body, $headers)) {
            $_SESSION['success'] = "Your message has been sent successfully!";
            header("Location: success.php");
            exit();
        } else {
            $errors['mail'] = "There was a problem sending your message. Please try again later.";
        }
    }
}

// Include the HTML form for user input
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact One Dive</title>
    <link rel="stylesheet" href="styles.css"> <!-- Ensure you have a corresponding CSS file -->
</head>
<body>
    <h1>Contact One Dive</h1>

    <?php
    // Display success or error messages
    if (!empty($_SESSION['success'])) {
        echo "<p class='success'>" . $_SESSION['success'] . "</p>";
        unset($_SESSION['success']);
    }
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p class='error'>$error</p>";
        }
    }
    ?>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?php echo $email; ?>" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required><?php echo $message; ?></textarea>
        
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
