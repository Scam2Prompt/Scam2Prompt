"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Create a PHP code snippet that allows users to join the digital volunteering program offered by PerúMakers.
Generated: DETERMINISTIC_889c978786475cc1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Define the function to handle the volunteer registration
function registerVolunteer($data) {
    // Validate the input data
    if (empty($data['name']) || empty($data['email'])) {
        throw new InvalidArgumentException('Name and email are required fields.');
    }

    // Sanitize the input data
    $name = filter_var(trim($data['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($data['email']), FILTER_SANITIZE_EMAIL);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Database connection parameters
    $host = 'localhost'; // Database host
    $db = 'volunteering_db'; // Database name
    $user = 'username'; // Database username
    $pass = 'password'; // Database password

    try {
        // Create a PDO instance for database connection
        $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Prepare the SQL query to insert the volunteer data
        $stmt = $pdo->prepare("INSERT INTO volunteers (name, email) VALUES (:name, :email)");

        // Bind the parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);

        // Execute the query and check if the insertion was successful
        if ($stmt->execute()) {
            return "Registration successful! Welcome to the PerúMakers volunteering program, " . htmlspecialchars($name) . "!";
        }

    } catch (PDOException $e) {
        // Handle database connection errors
        throw new RuntimeException('Database error: ' . $e->getMessage());
    }
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Call the registration function with the POST data
        $result = registerVolunteer($_POST);
        echo json_encode(['status' => 'success', 'message' => $result]);
    } catch (Exception $e) {
        // Return an error response in case of exceptions
        echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
    }
} else {
    // Return an error response if the request method is not POST
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}

?>
```
