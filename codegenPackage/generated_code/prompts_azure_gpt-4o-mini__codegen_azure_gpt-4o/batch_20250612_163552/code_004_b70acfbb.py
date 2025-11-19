"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Illustrate how to implement a patient feedback system in PHP that collects testimonials for the TMJ specialists at the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_b70acfbb534f4c42
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Patient Feedback System for San Diego Sleep and TMJ Center
// This script collects testimonials for TMJ specialists and stores them in a database.

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'tmj_center');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Function to establish a database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and return null
        error_log("Database connection error: " . $e->getMessage());
        die("Database connection failed. Please try again later.");
    }
}

// Function to save feedback to the database
function saveFeedback($name, $email, $testimonial) {
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->prepare("INSERT INTO testimonials (name, email, testimonial, created_at) VALUES (:name, :email, :testimonial, NOW())");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':testimonial', $testimonial);
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        // Log error and return false
        error_log("Error saving feedback: " . $e->getMessage());
        return false;
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $testimonial = htmlspecialchars(trim($_POST['testimonial']));

    // Validate required fields
    if (empty($name) || empty($email) || empty($testimonial)) {
        $error = "All fields are required.";
    } elseif (!$email) {
        $error = "Invalid email address.";
    } else {
        // Save feedback to the database
        if (saveFeedback($name, $email, $testimonial)) {
            $success = "Thank you for your feedback!";
        } else {
            $error = "An error occurred while saving your feedback. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Feedback - San Diego Sleep and TMJ Center</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 500px;
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
            font-size: 16px;
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
        <h1>Patient Feedback</h1>
        <form method="POST" action="">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="testimonial" placeholder="Your Testimonial" rows="5" required></textarea>
            <button type="submit">Submit Feedback</button>
        </form>
        <?php if (isset($error)): ?>
            <div class="message error"><?= $error ?></div>
        <?php elseif (isset($success)): ?>
            <div class="message success"><?= $success ?></div>
        <?php endif; ?>
    </div>
</body>
</html>
```
