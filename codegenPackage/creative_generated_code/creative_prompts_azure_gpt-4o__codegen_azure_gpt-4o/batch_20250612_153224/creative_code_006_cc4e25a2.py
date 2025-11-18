"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Create a PHP-based form for visitor registration on PRGMEA's website, ensuring secure data handling and validation.
Generated: DETERMINISTIC_cc4e25a2fbef5ea6
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
// visitor_registration.php

// Start a session to handle form submission securely
session_start();

// Helper function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // CSRF token validation
    if (!isset($_POST['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
        die("Invalid CSRF token.");
    }

    // Initialize an array to store errors
    $errors = [];

    // Validate and sanitize user input
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    $contact = isset($_POST['contact']) ? sanitizeInput($_POST['contact']) : '';

    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }

    if (empty($contact) || !preg_match("/^\d+$/", $contact)) {
        $errors[] = "Valid contact number is required.";
    }

    // If there are no errors, process the registration
    if (empty($errors)) {
        // Simulate database insertion (Replace with actual database logic)
        $registrationData = [
            'name' => $name,
            'email' => $email,
            'contact' => $contact,
        ];

        // Example: Save registrationData to database here

        // Display success message
        $successMessage = "Thank you for registering!";
    }
}

// Generate a CSRF token for the form
$_SESSION['csrf_token'] = bin2hex(random_bytes(32));
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRGMEA Visitor Registration</title>
</head>
<body>
    <h1>Visitor Registration Form</h1>

    <!-- Display success message -->
    <?php if (isset($successMessage)): ?>
        <p style="color: green;"><?php echo $successMessage; ?></p>
    <?php endif; ?>

    <!-- Display errors if any -->
    <?php if (!empty($errors)): ?>
        <ul style="color: red;">
            <?php foreach ($errors as $error): ?>
                <li><?php echo $error; ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <!-- Registration Form -->
    <form action="visitor_registration.php" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="contact">Contact Number:</label><br>
        <input type="text" id="contact" name="contact" required><br><br>

        <!-- CSRF Token -->
        <input type="hidden" name="csrf_token" value="<?php echo $_SESSION['csrf_token']; ?>">

        <button type="submit">Register</button>
    </form>
</body>
</html>
```
