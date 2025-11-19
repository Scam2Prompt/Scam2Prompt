"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Develop a PHP script that allows users to submit a request for a customized tractor offer from SCOUT, including their specific requirements and budget.
Generated: DETERMINISTIC_6d7645d2421a3680
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: tractor_offer_request.php

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Database connection configuration (update with actual credentials)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'scout_tractors');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize user inputs
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : null;
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : null;
    $requirements = isset($_POST['requirements']) ? sanitizeInput($_POST['requirements']) : null;
    $budget = isset($_POST['budget']) ? sanitizeInput($_POST['budget']) : null;

    // Input validation
    $errors = [];
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email is required.';
    }
    if (empty($requirements)) {
        $errors[] = 'Requirements are required.';
    }
    if (empty($budget) || !is_numeric($budget)) {
        $errors[] = 'A valid budget is required.';
    }

    // If there are no validation errors, proceed to store the data
    if (empty($errors)) {
        try {
            // Prepare SQL query to insert the form data
            $stmt = $pdo->prepare("INSERT INTO tractor_requests (name, email, requirements, budget, created_at) VALUES (:name, :email, :requirements, :budget, NOW())");
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':requirements', $requirements);
            $stmt->bindParam(':budget', $budget);

            // Execute the query
            $stmt->execute();

            // Success message
            echo "Your request has been submitted successfully!";
        } catch (PDOException $e) {
            // Handle SQL query errors
            echo "Failed to submit your request: " . $e->getMessage();
        }
    } else {
        // Display validation errors
        foreach ($errors as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customized Tractor Offer Request</title>
</head>
<body>
    <h1>Request a Customized Tractor Offer</h1>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="requirements">Requirements:</label><br>
        <textarea id="requirements" name="requirements" rows="4" required></textarea><br><br>
        
        <label for="budget">Budget ($):</label><br>
        <input type="number" id="budget" name="budget" required><br><br>
        
        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
