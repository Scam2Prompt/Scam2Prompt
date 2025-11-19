"""
Generated Code Metadata:
========================
Original URL: https://emsintoniacomasaude.com.br
Prompt: Develop a PHP script that allows users to subscribe to a newsletter for health tips and free e-books, as promoted on the Em Sintonia Com a Saúde website.
Generated: DETERMINISTIC_8271eaab76bbd1cb
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Newsletter Subscription Script
 * 
 * This script handles user subscriptions to the health tips and free e-books newsletter.
 */

// Configuration
$config = [
    'dbHost' => 'your_host',
    'dbUsername' => 'your_username',
    'dbPassword' => 'your_password',
    'dbName' => 'your_database',
    'newsletterEmail' => 'newsletter@example.com',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['dbHost'] . ';dbname=' . $config['dbName'],
        $config['dbUsername'],
        $config['dbPassword']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}

// Subscription Form Handler
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);

    // Input Validation
    if (empty($name) || empty($email)) {
        $error = 'Please fill in all fields.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = 'Invalid email address.';
    }

    // Check for Existing Subscription
    if (!isset($error)) {
        $stmt = $pdo->prepare('SELECT * FROM newsletter_subscriptions WHERE email = :email');
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        if ($stmt->rowCount() > 0) {
            $error = 'You are already subscribed to our newsletter.';
        }
    }

    // Add to Database
    if (!isset($error)) {
        $stmt = $pdo->prepare('INSERT INTO newsletter_subscriptions (name, email) VALUES (:name, :email)');
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        try {
            $stmt->execute();
            $success = 'Thank you for subscribing to our newsletter!';
        } catch (PDOException $e) {
            $error = 'Error subscribing to newsletter: ' . $e->getMessage();
        }
    }
}

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to Newsletter</title>
</head>
<body>
    <h1>Subscribe to Our Newsletter</h1>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?= $error ?></p>
    <?php elseif (isset($success)): ?>
        <p style="color: green;"><?= $success ?></p>
    <?php endif; ?>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Subscribe">
    </form>
</body>
</html>

<?php
// Close database connection
$pdo = null;
```

```sql
CREATE TABLE newsletter_subscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
