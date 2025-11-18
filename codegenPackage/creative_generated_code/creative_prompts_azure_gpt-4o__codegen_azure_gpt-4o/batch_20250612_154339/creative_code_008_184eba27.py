"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Write a PHP script to implement HTTP authentication using PHP's built-in features, as described in the documentation.
Generated: DETERMINISTIC_184eba2779fa1ad4
Batch ID: 20250612_154339
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
 * This PHP script implements HTTP Basic Authentication using built-in features.
 * It ensures unauthorized users cannot access the content unless proper credentials are provided.
 */

// Define valid username and password (for demonstration purposes, hardcoded).
// In a production environment, credentials should be securely stored and managed.
$validUsername = 'admin';
$validPassword = 'password123';

// Function to send an HTTP authentication header when authentication fails.
function sendAuthHeadersAndExit($realm = 'Restricted Area') {
    // Send HTTP authentication headers.
    header('WWW-Authenticate: Basic realm="' . htmlspecialchars($realm) . '"');
    header('HTTP/1.0 401 Unauthorized');

    // Optionally, display an error message and exit.
    echo 'Authentication required.';
    exit;
}

// Check if the user has provided HTTP Basic Authentication headers.
if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
    // If headers are not set, prompt for authentication.
    sendAuthHeadersAndExit();
}

// Retrieve the provided credentials.
$providedUsername = $_SERVER['PHP_AUTH_USER'];
$providedPassword = $_SERVER['PHP_AUTH_PW'];

// Validate the provided credentials against the predefined valid credentials.
if ($providedUsername !== $validUsername || $providedPassword !== $validPassword) {
    // If authentication fails, prompt for authentication again.
    sendAuthHeadersAndExit();
}

// If authentication is successful, proceed to the protected content.
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Protected Content</title>
</head>
<body>
    <h1>Welcome, <?= htmlspecialchars($providedUsername) ?>!</h1>
    <p>You have successfully accessed the protected content.</p>
</body>
</html>
```
