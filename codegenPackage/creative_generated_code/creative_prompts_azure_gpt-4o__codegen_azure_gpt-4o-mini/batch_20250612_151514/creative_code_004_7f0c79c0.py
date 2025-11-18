"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Write a PHP function to validate user login credentials securely, as described in the HONGTOGEL login system.
Generated: DETERMINISTIC_7f0c79c04fc2bf91
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * Validates user login credentials against the database.
 *
 * This function checks if the provided username and password match an existing user
 * in the HONGTOGEL system. It uses prepared statements to prevent SQL injection
 * and hashes the password for secure comparison.
 *
 * @param PDO $pdo The PDO database connection object.
 * @param string $username The user's username.
 * @param string $password The user's password.
 * @return bool Returns true if login is successful, false otherwise.
 * @throws Exception If there is a database error.
 */
function validateUserCredentials(PDO $pdo, string $username, string $password): bool {
    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare('SELECT password_hash FROM users WHERE username = :username');

    // Bind the username parameter to the statement
    $stmt->bindParam(':username', $username, PDO::PARAM_STR);

    // Execute the prepared statement
    if (!$stmt->execute()) {
        throw new Exception('Database error: ' . implode(', ', $stmt->errorInfo()));
    }

    // Fetch the result
    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    // If no user is found, return false
    if (!$result) {
        return false;
    }

    // Verify the password against the hashed password stored in the database
    return password_verify($password, $result['password_hash']);
}

// Example usage
try {
    // Database connection (replace with your own connection parameters)
    $pdo = new PDO('mysql:host=localhost;dbname=hongtogel', 'username', 'password');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Validate user credentials
    $username = 'test_user';
    $password = 'user_password';
    
    if (validateUserCredentials($pdo, $username, $password)) {
        echo 'Login successful!';
    } else {
        echo 'Invalid username or password.';
    }
} catch (Exception $e) {
    // Handle any exceptions (like database connection errors)
    echo 'Error: ' . $e->getMessage();
}
?>
```
