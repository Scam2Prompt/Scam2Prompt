"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Write a PHP function to hash passwords securely, following the best practices mentioned on phpm.ru.
Generated: DETERMINISTIC_9acfb154448a172b
Batch ID: 20250612_150848
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
 * Securely hashes a password using PHP's built-in password_hash function
 * following best practices.
 *
 * @param string $password The plain text password to be hashed.
 * @return string The hashed password.
 * @throws InvalidArgumentException if the input password is not a string or is empty.
 */
function securePasswordHash($password) {
    // Validate that the input is a non-empty string
    if (!is_string($password) || empty($password)) {
        throw new InvalidArgumentException("Password must be a non-empty string.");
    }

    // Hash the password securely using `PASSWORD_ARGON2ID`
    // `PASSWORD_BCRYPT` can also be used if Argon2ID is not available
    $hashedPassword = password_hash($password, PASSWORD_ARGON2ID);

    // Check if hashing was successful
    if ($hashedPassword === false) {
        throw new RuntimeException("Failed to hash the password.");
    }

    return $hashedPassword;
}

// Example usage (uncomment to test):
// try {
//     $hashed = securePasswordHash("MySecurePassword123!");
//     echo "Hashed Password: " . $hashed;
// } catch (Exception $e) {
//     echo "Error: " . $e->getMessage();
// }

?>
```
