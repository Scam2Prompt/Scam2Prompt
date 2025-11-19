"""
Generated Code Metadata:
========================
Original URL: https://the-cryptosoft-pro.com
Prompt: Develop a PHP application that allows users to report fraudulent investment schemes, similar to the actions taken against the platform discussed on thecryptosoft-pro.com.
Generated: DETERMINISTIC_519450bc0c62ee0e
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// fraud_report.php

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'fraud_reports');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish database connection
function connectDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $schemeName = htmlspecialchars(trim($_POST['scheme_name']));
    $description = htmlspecialchars(trim($_POST['description']));

    // Check for required fields
    if (empty($name) || empty($email) || empty($schemeName) || empty($description)) {
        $error = "All fields are required.";
    } elseif (!$email) {
        $error = "Invalid email address.";
    } else {
        try {
            // Insert report into the database
            $pdo = connectDatabase();
            $stmt = $pdo->prepare("INSERT INTO reports (name, email, scheme_name, description, created_at) VALUES (:name, :email, :scheme_name, :description, NOW())");
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':scheme_name', $schemeName);
            $stmt->bindParam(':description', $description);
            $stmt->execute();
            $success = "Fraud report submitted successfully.";
        } catch (PDOException $e) {
            $error = "Failed to submit report: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Fraudulent Investment Scheme</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
        }
        .form-container h1 {
            text-align: center;
        }
        .form-container form {
            display: flex;
            flex-direction: column;
        }
        .form-container form input, .form-container form textarea {
            margin-bottom: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .form-container form button {
            padding: 10px;
            font-size: 16px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        .form-container form button:hover {
            background-color: #0056b3;
        }
        .message {
            text-align: center;
            margin-top: 20px;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Report Fraudulent Investment Scheme</h1>
        <?php if (isset($error)): ?>
            <div class="message error"><?= $error ?></div>
        <?php elseif (isset($success)): ?>
            <div class="message success"><?= $success ?></div>
        <?php endif; ?>
        <form method="POST" action="">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <input type="text" name="scheme_name" placeholder="Scheme Name" required>
            <textarea name="description" placeholder="Description of Fraudulent Activity" rows="5" required></textarea>
            <button type="submit">Submit Report</button>
        </form>
    </div>
</body>
</html>

<?php
// Database schema (for reference):
// CREATE TABLE reports (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     name VARCHAR(255) NOT NULL,
//     email VARCHAR(255) NOT NULL,
//     scheme_name VARCHAR(255) NOT NULL,
//     description TEXT NOT NULL,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
