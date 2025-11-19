"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hdadpanaderos.es
Prompt: How can I implement a form submission in PHP to contact the Hermandad de los Panaderos for inquiries?
Generated: DETERMINISTIC_e9ddd5c82b583f1d
Batch ID: 20250612_155936
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

// Start the session for error handling and message passing
session_start();

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize variables and set to empty values
    $name = $email = $message = "";
    $errors = [];

    // Validate and sanitize name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitize_input($_POST["name"]);
        if (!preg_match("/^[a-zA-Z ]*$/", $name)) {
            $errors['name'] = "Only letters and white space allowed.";
        }
    }

    // Validate and sanitize email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } else {
        $email = sanitize_input($_POST["email"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = "Invalid email format.";
        }
    }

    // Validate and sanitize message
    if (empty($_POST["message"])) {
        $errors['message'] = "Message is required.";
    } else {
        $message = sanitize_input($_POST["message"]);
    }

    // If there are no errors, proceed with sending the email
    if (count($errors) === 0) {
        $to = "contact@panaderos.org"; // Change to the actual contact email
        $subject = "Inquiry from: $name";
        $body = "You have received a new message from the contact form:\n\n" .
                "Name: $name\n" .
                "Email: $email\n" .
                "Message:\n$message";
        $headers = "From: $email\r\n" .
                   "Reply-To: $email\r\n";

        // Attempt to send the email and handle any errors
        if (mail($to, $subject, $body, $headers)) {
            $_SESSION['success'] = "Your message has been sent successfully!";
            header("Location: success.php"); // Redirect to a success page
            exit();
        } else {
            $errors['mail'] = "Message could not be sent. Please try again later.";
        }
    }
}

// Include the form HTML
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Hermandad de los Panaderos</title>
</head>
<body>
    <h2>Contact Us</h2>
    
    <?php
    // Display any errors if they exist
    if (!empty($errors)) {
        echo '<div class="error">';
        foreach ($errors as $error) {
            echo "<p>$error</p>";
        }
        echo '</div>';
    }
    ?>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>"><br>

        <label for="email">Email:</label>
        <input type="text" id="email" name="email" value="<?php echo $email; ?>"><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message"><?php echo $message; ?></textarea><br>

        <input type="submit" value="Send Message">
    </form>
</body>
</html>
```
