"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aquatic-green.ir
Prompt: Create a PHP code snippet to handle user registration for purchasing TRUST products, including form validation and error handling.
Generated: DETERMINISTIC_e3585d79338bf104
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// User Registration Script for TRUST Products Purchase

// Enable Error Reporting (Remove or adjust in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database Connection Configuration (Replace with actual values)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'trust_products');

// Connect to the database
function connectToDatabase()
{
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    if ($mysqli->connect_error) {
        die("Database connection failed: " . $mysqli->connect_error);
    }
    return $mysqli;
}

// Validate Input Data
function validateFormData($data)
{
    $errors = [];
    $cleanData = [];

    // Validate name (Required, max length 100 characters)
    if (empty($data['name'])) {
        $errors['name'] = 'Name is required.';
    } elseif (strlen($data['name']) > 100) {
        $errors['name'] = 'Name cannot exceed 100 characters.';
    } else {
        $cleanData['name'] = htmlspecialchars(trim($data['name']));
    }

    // Validate email (Required, valid format)
    if (empty($data['email'])) {
        $errors['email'] = 'Email is required.';
    } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Invalid email format.';
    } else {
        $cleanData['email'] = htmlspecialchars(trim($data['email']));
    }

    // Validate password (Required, min length 8 characters)
    if (empty($data['password'])) {
        $errors['password'] = 'Password is required.';
    } elseif (strlen($data['password']) < 8) {
        $errors['password'] = 'Password must be at least 8 characters.';
    } else {
        $cleanData['password'] = password_hash(trim($data['password']), PASSWORD_BCRYPT);
    }

    return [$cleanData, $errors];
}

// Handle Form Submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Connect to the database
    $db = connectToDatabase();

    // Validate form data
    list($formData, $formErrors) = validateFormData($_POST);

    if (empty($formErrors)) {
        // Prepare and execute the SQL query
        $stmt = $db->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
        if ($stmt) {
            $stmt->bind_param("sss", $formData['name'], $formData['email'], $formData['password']);
            if ($stmt->execute()) {
                echo 'Registration successful!';
            } else {
                echo 'Error: ' . $stmt->error;
            }
            $stmt->close();
        } else {
            echo 'Error preparing query: ' . $db->error;
        }
    } else {
        // Display validation errors
        foreach ($formErrors as $field => $error) {
            echo "<p>$field: $error</p>";
        }
    }

    // Close the database connection
    $db->close();
}
?>

<!-- User Registration Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>Register to Purchase TRUST Products</h2>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
