"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Develop a PHP contact form with validation for a photography website, including fields for name, email, and message, similar to the one on Perth Real Estate Photography's contact page.
Generated: DETERMINISTIC_a751a896d05fce1b
Batch ID: 20250612_152620
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

// Start the session to manage form submission feedback
session_start();

// Define variables and initialize with empty values
$name = $email = $message = "";
$name_err = $email_err = $message_err = "";

// Process the form when it is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $name_err = "Please enter your name.";
    } else {
        $name = trim($_POST["name"]);
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $email_err = "Please enter your email address.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $email_err = "Invalid email format.";
    } else {
        $email = trim($_POST["email"]);
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Please enter a message.";
    } else {
        $message = trim($_POST["message"]);
    }

    // Check for errors before sending the email
    if (empty($name_err) && empty($email_err) && empty($message_err)) {
        // Prepare the email
        $to = "your-email@example.com"; // Replace with your email address
        $subject = "New Contact Form Submission";
        $body = "Name: $name\nEmail: $email\nMessage:\n$message";
        $headers = "From: $email";

        // Attempt to send the email
        if (mail($to, $subject, $body, $headers)) {
            // Redirect to success page or show a success message
            $_SESSION['success'] = "Message sent successfully!";
            header("location: success.php");
            exit;
        } else {
            // Handle error in sending email
            $_SESSION['error'] = "Oops! Something went wrong. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include your stylesheet -->
</head>
<body>
    <h1>Contact Us</h1>
    
    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p class='success'>{$_SESSION['success']}</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p class='error'>{$_SESSION['error']}</p>";
        unset($_SESSION['error']);
    }
    ?>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
            <label for="name">Name:</label>
            <input type="text" name="name" value="<?php echo htmlspecialchars($name); ?>">
            <span class="error"><?php echo $name_err; ?></span>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="text" name="email" value="<?php echo htmlspecialchars($email); ?>">
            <span class="error"><?php echo $email_err; ?></span>
        </div>
        <div>
            <label for="message">Message:</label>
            <textarea name="message"><?php echo htmlspecialchars($message); ?></textarea>
            <span class="error"><?php echo $message_err; ?></span>
        </div>
        <div>
            <button type="submit">Send Message</button>
        </div>
    </form>
</body>
</html>
```

```php
<?php
// success.php

// Start session to display success message
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include your stylesheet -->
</head>
<body>
    <h1>Thank You!</h1>
    <p>Your message has been sent successfully.</p>
    <a href="contact.php">Return to Contact Form</a>
</body>
</html>
```

### Notes:
- Ensure you replace `your-email@example.com` with your actual email address.
- Include error handling and feedback mechanisms to inform users of success or failure.
- This code uses HTML escaping to prevent XSS attacks and validate inputs before processing.
- Make sure to style the form and messages for better user experience in your `styles.css` file.
