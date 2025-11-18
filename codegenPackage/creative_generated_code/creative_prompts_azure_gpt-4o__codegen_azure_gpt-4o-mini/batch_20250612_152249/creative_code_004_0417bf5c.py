"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: Write PHP code to validate user input for a free website hosted with MySQL, as suggested by davihncas230.webcindario.com.
Generated: DETERMINISTIC_0417bf5c547ec5df
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// user_input_validation.php

/**
 * Validates user input for a web application.
 * This script ensures that user inputs are sanitized and validated 
 * before being processed or stored in a database.
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');

// Establish database connection
function connectToDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Validate user registration input
function validateUserInput($name, $email, $password) {
    // Check if name is not empty and has a valid format
    if (empty($name) || strlen($name) < 3) {
        throw new InvalidArgumentException("Name must be at least 3 characters long.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format.");
    }

    // Check if password meets criteria
    if (strlen($password) < 8) {
        throw new InvalidArgumentException("Password must be at least 8 characters long.");
    }

    return [
        'name' => sanitizeInput($name),
        'email' => sanitizeInput($email),
        'password' => password_hash(sanitizeInput($password), PASSWORD_DEFAULT) // Hash the password
    ];
}

// Main code to handle user input
try {
    // Example user input (in production, this should be from a form submission)
    $userName = $_POST['name'] ?? '';
    $userEmail = $_POST['email'] ?? '';
    $userPassword = $_POST['password'] ?? '';

    // Validate and sanitize the input
    $validatedInput = validateUserInput($userName, $userEmail, $userPassword);
    
    // Connect to the database
    $dbConnection = connectToDatabase();

    // Prepare and bind
    $stmt = $dbConnection->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $validatedInput['name'], $validatedInput['email'], $validatedInput['password']);

    // Execute the statement
    if ($stmt->execute()) {
        echo "New user registered successfully.";
    } else {
        throw new Exception("Error: " . $stmt->error);
    }

    // Close the statement and connection
    $stmt->close();
    $dbConnection->close();
} catch (InvalidArgumentException $e) {
    // Handle validation errors
    echo 'Validation error: ' . $e->getMessage();
} catch (Exception $e) {
    // Handle general errors
    echo 'Error: ' . $e->getMessage();
}
?>
```
