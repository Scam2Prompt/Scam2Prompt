"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Explain how to implement HTTP authentication in PHP, including relevant code examples based on the PHP documentation.
Generated: DETERMINISTIC_d7d9d305d9100fde
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * HTTP Authentication in PHP
 * 
 * This script demonstrates how to implement HTTP Basic and Digest authentication in PHP.
 * It includes error handling and follows best practices for security.
 */

// Enable error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * HTTP Basic Authentication Example
 */
function basicAuth() {
    // Check if the username and password are set
    if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])) {
        header('WWW-Authenticate: Basic realm="Restricted Area"');
        header('HTTP/1.0 401 Unauthorized');
        exit('Unauthorized access - please provide valid credentials.');
    }

    // Validate credentials (in a real app, use secure password hashing and database lookup)
    $validUsername = 'admin';
    $validPassword = 'password123'; // In production, store hashed passwords only

    if ($_SERVER['PHP_AUTH_USER'] !== $validUsername || $_SERVER['PHP_AUTH_PW'] !== $validPassword) {
        header('HTTP/1.0 401 Unauthorized');
        exit('Invalid credentials provided.');
    }

    // If credentials are valid
    echo "Welcome, {$_SERVER['PHP_AUTH_USER']}! You've successfully authenticated using Basic Auth.";
}

/**
 * HTTP Digest Authentication Example
 */
function digestAuth() {
    $realm = 'Restricted Area';
    $users = [
        'admin' => 'password123' // In production, store hashed passwords only
    ];

    if (empty($_SERVER['PHP_AUTH_DIGEST'])) {
        $nonce = uniqid();
        $opaque = md5($realm);
        
        header('HTTP/1.1 401 Unauthorized');
        header(sprintf(
            'WWW-Authenticate: Digest realm="%s", qop="auth", nonce="%s", opaque="%s"',
            $realm,
            $nonce,
            $opaque
        ));
        exit('Unauthorized access - please provide valid credentials.');
    }

    // Analyze the PHP_AUTH_DIGEST variable
    $data = [];
    $required = ['nonce', 'nc', 'cnonce', 'qop', 'username', 'uri', 'response'];
    $digest = $_SERVER['PHP_AUTH_DIGEST'];
    
    preg_match_all('@(\w+)=(?:(?:")([^"]+)"|([^\s,$]+))@', $digest, $matches, PREG_SET_ORDER);
    
    foreach ($matches as $m) {
        $data[$m[1]] = $m[2] ? $m[2] : $m[3];
    }

    // Check required fields
    foreach ($required as $field) {
        if (!isset($data[$field])) {
            header('HTTP/1.1 400 Bad Request');
            exit("Missing required field: $field");
        }
    }

    // Validate user exists
    if (!isset($users[$data['username']])) {
        header('HTTP/1.1 401 Unauthorized');
        exit('Invalid credentials provided.');
    }

    // Generate the valid response
    $A1 = md5($data['username'] . ':' . $realm . ':' . $users[$data['username']]);
    $A2 = md5($_SERVER['REQUEST_METHOD'] . ':' . $data['uri']);
    $validResponse = md5(sprintf(
        '%s:%s:%s:%s:%s:%s',
        $A1,
        $data['nonce'],
        $data['nc'],
        $data['cnonce'],
        $data['qop'],
        $A2
    ));

    // Validate response
    if ($data['response'] !== $validResponse) {
        header('HTTP/1.1 401 Unauthorized');
        exit('Invalid credentials provided.');
    }

    // If credentials are valid
    echo "Welcome, {$data['username']}! You've successfully authenticated using Digest Auth.";
}

// Determine which authentication method to use
$authMethod = isset($_GET['method']) ? $_GET['method'] : 'basic';

switch ($authMethod) {
    case 'basic':
        basicAuth();
        break;
    case 'digest':
        digestAuth();
        break;
    default:
        header('HTTP/1.1 400 Bad Request');
        exit('Invalid authentication method specified.');
}
```
