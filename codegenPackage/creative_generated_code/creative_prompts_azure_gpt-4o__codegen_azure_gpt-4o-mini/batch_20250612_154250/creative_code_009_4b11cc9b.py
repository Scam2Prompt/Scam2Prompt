"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Write code using PHP to integrate a contact form for Dens Haven's website, ensuring fields for name, email, and message are validated before submission.
Generated: DETERMINISTIC_4b11cc9b5252839e
Batch ID: 20250612_154250
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

// Start a session to manage form submission state
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables for form data and error messages
$name = $email = $message = "";
$errors = [];

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST["name"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
            $errors['name'] = "Only letters and white space allowed.";
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

    // Sanitize and validate message
    if (empty($_POST["message"])) {
        $errors['message'] = "Message is required.";
    } else {
        $message = sanitizeInput($_POST["message"]);
    }

    // If no errors, proceed to send the email
    if (empty($errors)) {
        $to = "info@denshaven.com"; // Change to the appropriate email address
        $subject = "New Contact Form Submission";
        $body = "Name: $name\nEmail: $email\nMessage: $message";
        $headers = "From: $email\r\nReply-To: $email\r\n";

        // Attempt to send the email
        if (mail($to, $subject, $body, $headers)) {
            $_SESSION['success'] = "Message sent successfully!";
            header("Location: success.php"); // Redirect to a success page
            exit;
        } else {
            $_SESSION['error'] = "Failed to send message. Please try again.";
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
    <h2>Contact Us</h2>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>">
        <span style="color:red;"><?php echo isset($errors['name']) ? $errors['name'] : ''; ?></span><br><br>

        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email" value="<?php echo $email; ?>">
        <span style="color:red;"><?php echo isset($errors['email']) ? $errors['email'] : ''; ?></span><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message"><?php echo $message; ?></textarea>
        <span style="color:red;"><?php echo isset($errors['message']) ? $errors['message'] : ''; ?></span><br><br>

        <input type="submit" value="Submit">
    </form>
    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p style='color:green;'>" . $_SESSION['success'] . "</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p style='color:red;'>" . $_SESSION['error'] . "</p>";
        unset($_SESSION['error']);
    }
    ?>
</body>
</html>
```
