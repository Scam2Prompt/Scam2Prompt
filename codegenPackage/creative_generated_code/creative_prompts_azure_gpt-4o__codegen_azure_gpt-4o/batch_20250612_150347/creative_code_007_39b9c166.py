"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Create a step-by-step guide to connect MapOS with an external authentication system and handle incorrect login attempts gracefully.
Generated: DETERMINISTIC_39b9c166e4dd65cd
Batch ID: 20250612_150347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://auth.example.com/api/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * External Authentication Integration for MapOS
 * 
 * This script demonstrates how to integrate an external authentication
 * system with MapOS. It includes handling incorrect login attempts
 * gracefully. Ensure you have the necessary permissions and access
 * to the external authentication API/system before implementing.
 */

// Example configuration for external authentication system
define('EXTERNAL_AUTH_API_URL', 'https://auth.example.com/api/login');
define('MAX_FAILED_ATTEMPTS', 5); // Maximum allowed failed login attempts
define('LOCKOUT_TIME', 900); // Lockout time in seconds (15 minutes)

// Database connection (Update with your credentials)
$pdo = new PDO('mysql:host=localhost;dbname=mapos', 'db_user', 'db_password', [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);

/**
 * Authenticate user with external system
 * 
 * @param string $username
 * @param string $password
 * @return bool True if authentication is successful, false otherwise.
 */
function authenticateWithExternalSystem($username, $password)
{
    $ch = curl_init();

    // Set up the cURL request to the external API
    curl_setopt($ch, CURLOPT_URL, EXTERNAL_AUTH_API_URL);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(['username' => $username, 'password' => $password]));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode === 200) {
        $responseData = json_decode($response, true);

        // Assume the API responds with {"success": true/false}
        return isset($responseData['success']) && $responseData['success'] === true;
    }

    return false;
}

/**
 * Handle user login
 * 
 * @param string $username
 * @param string $password
 * @return void
 */
function handleLogin($username, $password)
{
    global $pdo;

    try {
        // Check if the user exists in the database
        $stmt = $pdo->prepare('SELECT id, failed_attempts, last_failed_attempt FROM users WHERE username = :username');
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$user) {
            echo 'Invalid username or password.';
            return;
        }

        $currentTime = time();

        // Check if the user is locked out
        if ($user['failed_attempts'] >= MAX_FAILED_ATTEMPTS && 
            ($currentTime - strtotime($user['last_failed_attempt'])) < LOCKOUT_TIME) {
            echo 'Too many failed login attempts. Please try again later.';
            return;
        }

        // Authenticate with the external system
        $isAuthenticated = authenticateWithExternalSystem($username, $password);

        if ($isAuthenticated) {
            echo 'Login successful!';

            // Reset failed attempts on successful login
            $stmt = $pdo->prepare('UPDATE users SET failed_attempts = 0, last_failed_attempt = NULL WHERE id = :id');
            $stmt->execute(['id' => $user['id']]);
        } else {
            echo 'Invalid username or password.';
            
            // Increment failed attempts
            $stmt = $pdo->prepare(
                'UPDATE users SET failed_attempts = failed_attempts + 1, last_failed_attempt = NOW() WHERE id = :id'
            );
            $stmt->execute(['id' => $user['id']]);
        }
    } catch (Exception $e) {
        // Log the error and display a generic message
        error_log($e->getMessage());
        echo 'An error occurred during login. Please try again later.';
    }
}

/**
 * Example usage
 */

// Input from a login form (Sanitize inputs in real-world use cases)
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

if (!empty($username) && !empty($password)) {
    handleLogin($username, $password);
} else {
    echo 'Username and password are required.';
}
```
