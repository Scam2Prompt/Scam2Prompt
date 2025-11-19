"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emsintoniacomasaude.com.br
Prompt: Develop a PHP script that allows users to subscribe to a newsletter for health tips and free e-books, as promoted on the Em Sintonia Com a Saúde website.
Generated: DETERMINISTIC_8271eaab76bbd1cb
Batch ID: 20250612_160507
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// newsletter_subscription.php

// Start the session to handle user data and messages
session_start();

// Function to handle database connection
function getDatabaseConnection() {
    $host = 'localhost';
    $db = 'newsletter';
    $user = 'root';
    $pass = '';
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (\PDOException $e) {
        throw new \PDOException($e->getMessage(), (int)$e->getCode());
    }
}

// Function to subscribe a user to the newsletter
function subscribeUser($email) {
    $db = getDatabaseConnection();
    $stmt = $db->prepare('INSERT INTO subscribers (email) VALUES (:email)');
    
    // Execute the statement and handle possible errors
    try {
        $stmt->execute(['email' => $email]);
        return true;
    } catch (Exception $e) {
        $_SESSION['error'] = 'Error during subscription: ' . $e->getMessage();
        return false;
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    // Validate the email address
    if ($email) {
        if (subscribeUser($email)) {
            $_SESSION['success'] = 'Subscription successful! Thank you for signing up.';
        } else {
            $_SESSION['error'] = 'Subscription failed. Please try again.';
        }
    } else {
        $_SESSION['error'] = 'Please enter a valid email address.';
    }

    // Redirect back to the form page
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}

// Display messages if available
function displayMessages() {
    if (isset($_SESSION['success'])) {
        echo '<div class="alert alert-success">' . $_SESSION['success'] . '</div>';
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo '<div class="alert alert-danger">' . $_SESSION['error'] . '</div>';
        unset($_SESSION['error']);
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to Newsletter</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Subscribe to Our Newsletter</h2>
        <?php displayMessages(); ?>
        <form method="POST" action="">
            <div class="form-group">
                <label for="email">Email address:</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <button type="submit" class="btn btn-primary">Subscribe</button>
        </form>
    </div>
</body>
</html>
```
