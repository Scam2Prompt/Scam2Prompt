"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Explain how to implement HTTP authentication in PHP, including relevant code examples based on the PHP documentation.
Generated: DETERMINISTIC_d7d9d305d9100fde
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script demonstrates HTTP Basic Authentication in PHP.
// Use this code in secure environments, such as HTTPS, to prevent credentials from being transmitted in plain text.

// Function to handle HTTP Basic Authentication
function authenticateUser($validUsers) {
    // Check if the user has provided authentication credentials
    if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
        sendAuthenticationHeader();
        exitWithUnauthorizedMessage();
    }

    // Validate provided credentials against the valid users array
    $username = $_SERVER['PHP_AUTH_USER'];
    $password = $_SERVER['PHP_AUTH_PW'];

    if (isset($validUsers[$username]) && password_verify($password, $validUsers[$username])) {
        // Authentication successful, return the username
        return $username;
    } else {
        // Authentication failed, send header again
        sendAuthenticationHeader();
        exitWithUnauthorizedMessage();
    }
}

// Function to send the authentication header
function sendAuthenticationHeader() {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
}

// Function to display unauthorized message and exit
function exitWithUnauthorizedMessage() {
    echo 'Unauthorized access. Please provide valid credentials.';
    exit;
}

// Example usage of authenticateUser function

// Hard-coded valid users array with hashed passwords (use a proper database in production)
$validUsers = [
    'admin' => password_hash('adminPass123', PASSWORD_DEFAULT), // Example user
    'user1' => password_hash('user1Pass456', PASSWORD_DEFAULT), // Another example user
];

// Authenticate the user
$authenticatedUser = authenticateUser($validUsers);

// If authentication is successful, display a welcome message
echo "Welcome, $authenticatedUser!";
?>
```
