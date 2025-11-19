"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Write a code snippet in PHP to create a simple form for submitting consultas (inquiries) similar to the one found on the Hermandad de los Panaderos website.
Generated: DETERMINISTIC_d0ac11858feed1c2
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$config = [
    'db_host' => 'your_host',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Connection failed: ' . $e->getMessage());
}

// Form handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $phone = trim($_POST['phone']);
    $message = trim($_POST['message']);

    // Validation
    $errors = [];
    if (empty($name)) {
        $errors[] = 'Please enter your name.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Please enter a valid email address.';
    }
    if (empty($phone)) {
        $errors[] = 'Please enter your phone number.';
    }
    if (empty($message)) {
        $errors[] = 'Please enter your message.';
    }

    // Save to database
    if (empty($errors)) {
        $stmt = $pdo->prepare('
            INSERT INTO consultas (name, email, phone, message, created_at)
            VALUES (:name, :email, :phone, :message, NOW())
        ');
        $stmt->execute([
            'name' => $name,
            'email' => $email,
            'phone' => $phone,
            'message' => $message,
        ]);

        // Send confirmation email
        $to = 'your_email@example.com';
        $subject = 'New Inquiry Submitted';
        $body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage: $message";
        $headers = 'From: ' . $email . "\r\n";
        mail($to, $subject, $body, $headers);

        $success = 'Consulta enviada con éxito. Gracias por contactarnos.';
    }
}

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta</title>
    <style>
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
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
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
        .error {
            color: #f44336;
            font-size: 12px;
            margin-bottom: 10px;
        }
        .success {
            color: #4CAF50;
            font-size: 14px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Correo electrónico:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Teléfono:</label>
        <input type="text" id="phone" name="phone" required>

        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>

        <?php if (!empty($errors)) : ?>
            <?php foreach ($errors as $error) : ?>
                <div class="error"><?= $error ?></div>
            <?php endforeach ?>
        <?php endif ?>

        <?php if (isset($success)) : ?>
            <div class="success"><?= $success ?></div>
        <?php endif ?>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```
