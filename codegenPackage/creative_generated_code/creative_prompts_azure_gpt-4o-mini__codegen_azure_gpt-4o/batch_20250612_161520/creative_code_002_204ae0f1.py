"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Create a PHP code snippet that handles user registration for new members of the Grad košarke association, ensuring it captures essential details like name, email, and membership type.
Generated: DETERMINISTIC_204ae0f108de7856
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Grad košarke association - User Registration Script

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'grad_kosarke');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize input values
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize user input
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $membershipType = sanitizeInput($_POST['membershipType'] ?? '');

    // Basic validation
    $errors = [];
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }
    if (empty($membershipType)) {
        $errors[] = "Membership type is required.";
    }

    // If validation passes, proceed with registration
    if (empty($errors)) {
        try {
            // Prepare SQL statement to insert user data
            $stmt = $pdo->prepare("INSERT INTO members (name, email, membership_type) VALUES (:name, :email, :membershipType)");
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':membershipType', $membershipType);

            // Execute the query
            $stmt->execute();
            echo "Registration successful!";
        } catch (PDOException $e) {
            echo "Error: Could not complete the registration. " . $e->getMessage();
        }
    } else {
        // Display validation errors
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grad košarke Association - Registration</title>
</head>
<body>
    <h1>Register as a Member</h1>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="membershipType">Membership Type:</label><br>
        <select id="membershipType" name="membershipType" required>
            <option value="">Select</option>
            <option value="regular">Regular</option>
            <option value="premium">Premium</option>
            <option value="student">Student</option>
        </select><br><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```
