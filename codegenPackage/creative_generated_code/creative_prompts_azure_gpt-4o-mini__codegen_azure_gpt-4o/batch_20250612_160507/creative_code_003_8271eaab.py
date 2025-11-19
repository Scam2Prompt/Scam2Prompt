"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emsintoniacomasaude.com.br
Prompt: Develop a PHP script that allows users to subscribe to a newsletter for health tips and free e-books, as promoted on the Em Sintonia Com a Saúde website.
Generated: DETERMINISTIC_8271eaab76bbd1cb
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Ensure the script is run only from a web server
if (php_sapi_name() === 'cli') {
    exit("This script can only be run from a web server.\n");
}

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'newsletter_database');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Error handling for database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle POST request for subscription
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    if (!$name || !$email) {
        // If validation fails, return an error message
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Invalid name or email.']);
        exit;
    }

    try {
        // Check if the email is already subscribed
        $stmt = $pdo->prepare("SELECT id FROM subscriptions WHERE email = :email");
        $stmt->execute(['email' => $email]);

        if ($stmt->rowCount() > 0) {
            echo json_encode(['message' => 'You are already subscribed.']);
        } else {
            // Insert subscription record into the database
            $stmt = $pdo->prepare("INSERT INTO subscriptions (name, email) VALUES (:name, :email)");
            $stmt->execute(['name' => $name, 'email' => $email]);
            echo json_encode(['message' => 'Subscription successful!']);
        }
    } catch (PDOException $e) {
        // Handle database errors
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => 'An error occurred while processing your request.']);
    }
    exit;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to Health Tips</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        input[type="text"], input[type="email"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            display: inline-block;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .message {
            margin-top: 20px;
            text-align: center;
            font-weight: bold;
        }
    </style>
</head>
<body>

<h1>Subscribe to Health Tips and Free E-books</h1>
<p>Fill in your details below to receive weekly health tips and free e-books.</p>

<form id="subscriptionForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <button type="submit">Subscribe</button>
</form>

<div class="message" id="message"></div>

<script>
    const form = document.getElementById('subscriptionForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                messageDiv.textContent = data.message;
                messageDiv.style.color = 'green';
                form.reset();
            } else {
                messageDiv.textContent = data.error || 'An error occurred.';
                messageDiv.style.color = 'red';
            }
        } catch (error) {
            messageDiv.textContent = 'An error occurred while contacting the server.';
            messageDiv.style.color = 'red';
        }
    });
</script>

</body>
</html>
```
