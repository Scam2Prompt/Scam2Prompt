"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://henfruit.ro
Prompt: Develop a PHP-based contact form for a web design agency, including fields for "Nume," "Email sau telefon," and a "Trimite" button, as seen on Henfruit's webpage.
Generated: DETERMINISTIC_175e619dfb5be81c
Batch ID: 20250612_153246
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

// Start the session for error reporting
session_start();

// Initialize an empty error message variable
$errorMessage = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input fields
    $name = trim($_POST['name']);
    $contactInfo = trim($_POST['contact_info']);

    if (empty($name) || empty($contactInfo)) {
        $errorMessage = "Toate câmpurile sunt obligatorii.";
    } elseif (!filter_var($contactInfo, FILTER_VALIDATE_EMAIL) && !preg_match('/^\+?[0-9]{10,15}$/', $contactInfo)) {
        $errorMessage = "Introduceți un email valid sau un număr de telefon.";
    } else {
        // Prepare email
        $to = 'contact@henfruit.com'; // Replace with your agency email
        $subject = 'New Contact Form Submission';
        $message = "Nume: $name\nContact: $contactInfo";
        $headers = "From: noreply@henfruit.com"; // Replace with a valid sender email

        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = "Mesajul a fost trimis cu succes!";
            header("Location: thank_you.php"); // Redirect to a thank you page
            exit();
        } else {
            $errorMessage = "A apărut o eroare la trimiterea mesajului. Vă rugăm să încercați din nou.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contactare Henfruit</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS styles -->
</head>
<body>
    <div class="contact-form-container">
        <h1>Contactați-ne</h1>
        <?php if ($errorMessage): ?>
            <div class="error-message"><?php echo $errorMessage; ?></div>
        <?php endif; ?>
        <form action="contact_form.php" method="POST">
            <label for="name">Nume:</label>
            <input type="text" id="name" name="name" required>

            <label for="contact_info">Email sau telefon:</label>
            <input type="text" id="contact_info" name="contact_info" required>

            <button type="submit">Trimite</button>
        </form>
    </div>
</body>
</html>
```

Make sure to create a separate `thank_you.php` file to handle the success response, and adjust the email addresses as necessary. Additionally, ensure to set up the necessary CSS in `styles.css` to style the contact form. This code assumes that the mail function is correctly configured on your server.
