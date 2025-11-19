"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Develop a PHP contact form with validation for a photography website, including fields for name, email, and message, similar to the one on Perth Real Estate Photography's contact page.
Generated: DETERMINISTIC_a751a896d05fce1b
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// contact.php

// Start the session to store error messages
session_start();

// Initialize variables to hold form data and error messages
$name = $email = $message = "";
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $errors['name'] = "Name is required.";
    } else {
        $name = htmlspecialchars(trim($_POST["name"]));
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = htmlspecialchars(trim($_POST["email"]));
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $errors['message'] = "Message is required.";
    } else {
        $message = htmlspecialchars(trim($_POST["message"]));
    }

    // If there are no errors, process the form
    if (empty($errors)) {
        // Here you would typically send the email or save to a database
        // For demonstration, we'll just simulate a successful submission
        $_SESSION['success'] = "Your message has been sent successfully!";
        header("Location: thank_you.php");
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Contact Us</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="<?php echo $name; ?>">
            <span class="error"><?php echo isset($errors['name']) ? $errors['name'] : ''; ?></span>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="<?php echo $email; ?>">
            <span class="error"><?php echo isset($errors['email']) ? $errors['email'] : ''; ?></span>
        </div>
        <div>
            <label for="message">Message:</label>
            <textarea id="message" name="message"><?php echo $message; ?></textarea>
            <span class="error"><?php echo isset($errors['message']) ? $errors['message'] : ''; ?></span>
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
// thank_you.php

// Start the session
session_start();

// Check if the success message is set
if (!isset($_SESSION['success'])) {
    header("Location: contact.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
</head>
<body>
    <h1>Thank You!</h1>
    <p><?php echo $_SESSION['success']; ?></p>
    <a href="contact.php">Go back to contact form</a>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

form {
    max-width: 400px;
    margin: auto;
}

div {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.error {
    color: red;
    font-size: 0.9em;
}
```
