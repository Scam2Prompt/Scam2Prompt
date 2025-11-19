"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Develop a PHP-based contact form for a web design agency, including fields for "Nume," "Email sau telefon," and a "Trimite" button, as seen on Henfruit's webpage.
Generated: DETERMINISTIC_175e619dfb5be81c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// contact_form.php

// Start the session to handle form submissions
session_start();

// Initialize variables for form data and error messages
$name = '';
$contact = '';
$error_message = '';

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate the input data
    $name = trim($_POST['name']);
    $contact = trim($_POST['contact']);

    // Validate name
    if (empty($name)) {
        $error_message .= "Numele este obligatoriu.<br>";
    }

    // Validate contact (email or phone)
    if (empty($contact)) {
        $error_message .= "Email sau telefonul este obligatoriu.<br>";
    } elseif (!filter_var($contact, FILTER_VALIDATE_EMAIL) && !preg_match('/^\+?[0-9]{7,15}$/', $contact)) {
        $error_message .= "Introduceți un email valid sau un număr de telefon valid.<br>";
    }

    // If there are no errors, process the form
    if (empty($error_message)) {
        // Here you would typically send the email or save the data to a database
        // For demonstration, we'll just set a success message
        $_SESSION['success_message'] = "Mesajul a fost trimis cu succes!";
        header("Location: thank_you.php"); // Redirect to a thank you page
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <div class="contact-form">
        <h2>Contactați-ne</h2>
        <?php
        // Display error messages if any
        if (!empty($error_message)) {
            echo "<div class='error-message'>$error_message</div>";
        }
        ?>
        <form action="contact_form.php" method="POST">
            <label for="name">Nume:</label>
            <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>" required>

            <label for="contact">Email sau telefon:</label>
            <input type="text" id="contact" name="contact" value="<?php echo htmlspecialchars($contact); ?>" required>

            <button type="submit">Trimite</button>
        </form>
    </div>
</body>
</html>
```

```php
<?php
// thank_you.php

// Start the session to access session variables
session_start();
?>

<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mulțumim!</title>
</head>
<body>
    <div class="thank-you">
        <h2>Mulțumim pentru mesajul dumneavoastră!</h2>
        <?php
        // Display success message if it exists
        if (isset($_SESSION['success_message'])) {
            echo "<p>" . $_SESSION['success_message'] . "</p>";
            // Unset the success message after displaying it
            unset($_SESSION['success_message']);
        }
        ?>
        <a href="contact_form.php">Înapoi la formular</a>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.contact-form, .thank-you {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    margin: auto;
}

h2 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.error-message {
    color: red;
    margin-bottom: 10px;
}
```
