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

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate user inputs
    $name = htmlspecialchars(trim($_POST['name']));
    $contact = htmlspecialchars(trim($_POST['contact']));

    // Error handling
    $errors = [];
    if (empty($name)) {
        $errors[] = "Nume este obligatoriu.";
    }
    if (empty($contact)) {
        $errors[] = "Email sau telefon este obligatoriu.";
    }

    // Validate contact (basic validation for email or phone)
    if (!filter_var($contact, FILTER_VALIDATE_EMAIL) && !preg_match('/^[0-9\-\+\(\) ]+$/', $contact)) {
        $errors[] = "Email sau telefon invalid.";
    }

    // If there are no errors, proceed with form submission
    if (empty($errors)) {
        // (Optional) You can save the data to a database or send it via email
        // Example: sending email
        $to = "info@webdesignagency.com"; // Replace with your agency's email
        $subject = "New Contact Form Submission";
        $message = "Nume: $name\nContact: $contact";
        $headers = "From: no-reply@webdesignagency.com"; // Replace with your sender email

        if (mail($to, $subject, $message, $headers)) {
            $successMessage = "Formularul a fost trimis cu succes.";
        } else {
            $errors[] = "A apărut o eroare la trimiterea formularului.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        /* Simple styling */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .form-container {
            max-width: 400px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background: #f9f9f9;
        }
        .form-container input[type="text"],
        .form-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container input[type="submit"] {
            background: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .form-container input[type="submit"]:hover {
            background: #45a049;
        }
        .errors {
            color: red;
            margin-bottom: 10px;
        }
        .success {
            color: green;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
<div class="form-container">
    <h1>Contactează-ne</h1>
    <!-- Display errors, if any -->
    <?php if (!empty($errors)): ?>
        <div class="errors">
            <?php foreach ($errors as $error): ?>
                <p><?php echo $error; ?></p>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>

    <!-- Display success message -->
    <?php if (!empty($successMessage)): ?>
        <div class="success">
            <p><?php echo $successMessage; ?></p>
        </div>
    <?php endif; ?>

    <!-- Contact form -->
    <form method="POST" action="contact_form.php">
        <label for="name">Nume:</label>
        <input type="text" id="name" name="name" required>

        <label for="contact">Email sau telefon:</label>
        <input type="text" id="contact" name="contact" required>

        <input type="submit" value="Trimite">
    </form>
</div>
</body>
</html>
```
