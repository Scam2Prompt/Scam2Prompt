"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Develop a web form in HTML and PHP for property owners to consign their properties, incorporating fields like name, email, and message as outlined in the "Consigna tu inmueble" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_b3b1500ce33b09a2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- consign_property.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu Inmueble</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Consigna tu Inmueble</h1>
    <form action="process_form.php" method="POST" id="consignForm">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

```php
<?php
// process_form.php

// Start the session
session_start();

// Check if form data is submitted via POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if (!$email) {
        // Redirect or show error for invalid email
        $_SESSION['error'] = "Correo electrónico no válido.";
        header("Location: consign_property.html");
        exit();
    }

    // Prepare the email content
    $to = "admin@nuevaciudad.com"; // Replace with actual recipient email
    $subject = "Nuevo Consignación de Inmueble";
    $body = "Nombre: $name\nCorreo: $email\nMensaje:\n$message";
    $headers = "From: $email\r\n";

    // Error handling for mail function
    if (mail($to, $subject, $body, $headers)) {
        // Success message
        $_SESSION['success'] = "Su mensaje ha sido enviado con éxito.";
    } else {
        // Error message
        $_SESSION['error'] = "Ocurrió un error al enviar su mensaje. Inténtelo de nuevo más tarde.";
    }
    
    // Redirect back to the form page
    header("Location: consign_property.html");
    exit();
} else {
    // If accessed without POST, redirect to form
    header("Location: consign_property.html");
    exit();
}
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #5cb85c;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```

Make sure to update the recipient email address in the PHP script before deploying this code.
