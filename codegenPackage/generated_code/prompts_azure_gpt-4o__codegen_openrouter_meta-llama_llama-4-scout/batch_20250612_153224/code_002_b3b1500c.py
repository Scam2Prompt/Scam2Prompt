"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a web form in HTML and PHP for property owners to consign their properties, incorporating fields like name, email, and message as outlined in the "Consigna tu inmueble" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_b3b1500ce33b09a2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu inmueble</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Consigna tu inmueble</h1>
    <form action="process_form.php" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

**process_form.php**
```php
<?php
/**
 * Process the property consignment form data.
 */

// Configuration
$config = [
    'admin_email' => 'admin@example.com',
];

// Check if form data is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate form data
        $name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
        $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
        $message = filter_var($_POST['message'], FILTER_SANITIZE_STRING);

        // Check for empty fields
        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception('Todos los campos son obligatorios.');
        }

        // Send email to admin
        $subject = 'Nueva consignación de inmueble';
        $body = "
            Nombre: $name
            Correo electrónico: $email
            Mensaje: $message
        ";

        $headers = [
            'From' => $email,
            'Reply-To' => $email,
            'Content-Type' => 'text/plain; charset=UTF-8',
        ];

        if (!mail($config['admin_email'], $subject, $body, implode("\r\n", $headers))) {
            throw new Exception('Error al enviar el correo electrónico.');
        }

        // Display success message
        $success_message = 'La consignación ha sido enviada correctamente.';
    } catch (Exception $e) {
        $error_message = $e->getMessage();
    }
} else {
    http_response_code(405);
    echo 'Método no permitido.';
    exit;
}

// Display form with messages
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu inmueble</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Consigna tu inmueble</h1>
    <form action="process_form.php" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required value="<?php echo $name ?? ''; ?>">

        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" name="email" required value="<?php echo $email ?? ''; ?>">

        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required><?php echo $message ?? ''; ?></textarea>

        <button type="submit">Enviar</button>
    </form>

    <?php if (isset($success_message)) : ?>
        <p style="color: green;"><?php echo $success_message; ?></p>
    <?php elseif (isset($error_message)) : ?>
        <p style="color: red;"><?php echo $error_message; ?></p>
    <?php endif; ?>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    height: 100px;
    resize: vertical;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```
