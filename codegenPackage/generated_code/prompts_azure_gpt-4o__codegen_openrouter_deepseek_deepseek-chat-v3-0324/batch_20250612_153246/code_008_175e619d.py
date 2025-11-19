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
// Define variables and initialize with empty values
$name = $contact = $message = "";
$name_err = $contact_err = $message_err = "";
$success_message = "";

// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $name_err = "Vă rugăm să introduceți numele.";
    } else {
        $name = sanitize_input($_POST["name"]);
        // Check if name contains only letters and whitespace
        if (!preg_match("/^[a-zA-ZăâîșțĂÂÎȘȚ ]*$/", $name)) {
            $name_err = "Numele poate conține doar litere și spații.";
        }
    }

    // Validate contact (email or phone)
    if (empty(trim($_POST["contact"]))) {
        $contact_err = "Vă rugăm să introduceți un email sau un număr de telefon.";
    } else {
        $contact = sanitize_input($_POST["contact"]);
        // Check if it's an email or phone number
        if (!filter_var($contact, FILTER_VALIDATE_EMAIL) && !preg_match("/^[0-9]{10}$/", $contact)) {
            $contact_err = "Vă rugăm să introduceți un email valid sau un număr de telefon (10 cifre).";
        }
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Vă rugăm să introduceți un mesaj.";
    } else {
        $message = sanitize_input($_POST["message"]);
    }

    // Check input errors before sending email
    if (empty($name_err) && empty($contact_err) && empty($message_err)) {
        // Recipient email (replace with your email)
        $to = "contact@yourwebdesignagency.com";
        $subject = "New Contact Form Submission";
        $email_body = "Name: $name\n";
        $email_body .= "Contact: $contact\n";
        $email_body .= "Message:\n$message\n";

        // Email headers
        $headers = "From: webform@yourwebdesignagency.com\r\n";
        $headers .= "Reply-To: $contact\r\n";

        // Send email
        if (mail($to, $subject, $email_body, $headers)) {
            $success_message = "Mesajul dumneavoastră a fost trimis cu succes! Vă vom contacta în curând.";
            // Clear form fields
            $name = $contact = $message = "";
        } else {
            $message_err = "A apărut o eroare la trimiterea mesajului. Vă rugăm să încercați din nou.";
        }
    }
}

// Function to sanitize form inputs
function sanitize_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>

<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        .error { color: red; }
        .success { color: green; }
        form {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 5px 0 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <h2>Contactați-ne</h2>
        
        <?php if (!empty($success_message)): ?>
            <p class="success"><?php echo $success_message; ?></p>
        <?php endif; ?>
        
        <label for="name">Nume:</label>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>">
        <span class="error"><?php echo $name_err; ?></span>
        
        <label for="contact">Email sau telefon:</label>
        <input type="text" id="contact" name="contact" value="<?php echo $contact; ?>">
        <span class="error"><?php echo $contact_err; ?></span>
        
        <label for="message">Mesaj:</label>
        <textarea id="message" name="message" rows="5"><?php echo $message; ?></textarea>
        <span class="error"><?php echo $message_err; ?></span>
        
        <button type="submit" name="submit">Trimite</button>
    </form>
</body>
</html>
```
