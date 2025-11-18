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
 * Hashes a password securely using the BCRYPT algorithm.
 *
 * This function takes a plain text password and returns a hashed version
 * of it. It uses the password_hash function which is considered the best 
 * practice for hashing passwords in PHP.
 *
 * @param string $password The plain text password to hash.
 * @param int $cost The cost parameter for the hashing algorithm (default is 10).
 * @return string|false Returns the hashed password on success, or false on failure.
 * @throws InvalidArgumentException if the provided password is empty.
 */
function hashPassword(string $password, int $cost = 10) {
    // Validate the password input
    if (empty($password)) {
        throw new InvalidArgumentException('Password cannot be empty.');
    }

    // Create options array for password_hash
    $options = [
        'cost' => $cost,
    ];

    // Hash the password with the specified cost
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT, $options);

    // Check if the hashing was successful
    if ($hashedPassword === false) {
        // Log the error or handle it as needed
        error_log('Password hashing failed.');
        return false; // or throw an exception
    }

    return $hashedPassword;
}

/**
 * Verifies a password against a hashed password.
 *
 * This function compares a plain text password with a hashed password
 * to check if they match.
 *
 * @param string $password The plain text password to verify.
 * @param string $hashedPassword The hashed password to check against.
 * @return bool Returns true if the password matches, false otherwise.
 */
function verifyPassword(string $password, string $hashedPassword): bool {
    // Validate the inputs
    if (empty($password) || empty($hashedPassword)) {
        throw new InvalidArgumentException('Password and hashed password cannot be empty.');
    }

    // Use password_verify to check if the password matches the hash
    return password_verify($password, $hashedPassword);
}
?>
```
