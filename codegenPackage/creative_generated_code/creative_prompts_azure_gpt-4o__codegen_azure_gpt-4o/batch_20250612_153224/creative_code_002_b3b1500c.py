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
<!-- consigna_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu inmueble</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Consigna tu inmueble</h1>
    <!-- Property Consignment Form -->
    <form action="process_form.php" method="POST">
        <!-- Name Field -->
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        
        <!-- Email Field -->
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- Message Field -->
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

```php
<?php
// process_form.php

// Enable error reporting (for debugging purposes during development)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the form was submitted using POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Handle cases where input validation fails
    if (!$name || !$email || !$message) {
        // Redirect back to the form with an error message (optional)
        echo "Error: Please ensure all fields are correctly filled out.";
        exit;
    }

    // Example: Save the data to a database or send an email (implementation depends on requirements)
    try {
        // Placeholder for data processing logic (e.g., saving to a database)
        // Here, we'll simply display the submitted information as confirmation.
        echo "<h1>Form Submission Received</h1>";
        echo "<p>Nombre: " . htmlspecialchars($name) . "</p>";
        echo "<p>Correo Electrónico: " . htmlspecialchars($email) . "</p>";
        echo "<p>Mensaje: " . nl2br(htmlspecialchars($message)) . "</p>";

    } catch (Exception $e) {
        // Handle unforeseen errors gracefully
        echo "An error occurred while processing your request. Please try again later.";
    }
} else {
    // Redirect users who access this PHP file directly without submitting the form
    header("Location: consigna_form.html");
    exit;
}
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    line-height: 1.6;
}

form {
    max-width: 400px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input, textarea, button {
    width: 100%;
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

### Included Features:
- HTML form with necessary input validation (`required` attribute).
- PHP backend with input sanitization and validation.
- Example error handling in the backend PHP script.
- Basic CSS for styling the form.
