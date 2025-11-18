"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Provide a PHP code example that uses the "Session Extensions" to securely manage user sessions.
Generated: DETERMINISTIC_3cfb09e009c31821
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
// Start output buffering to prevent "headers already sent" errors
ob_start();

// Start the session and enable session extension
session_start([
    'cookie_lifetime' => 86400, // Session cookie lasts for one day
    'cookie_secure' => true, // Ensure cookie is sent over secure connections
    'cookie_httponly' => true, // Prevent JavaScript access to session cookie
    'use_strict_mode' => true, // Prevent uninitialized session IDs
]);

/**
 * Function to securely regenerate session ID to prevent session fixation
 */
function regenerateSession() {
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_regenerate_id(true); // Regenerate session ID and delete old session
    } else {
        throw new Exception("Session is not active.");
    }
}

/**
 * Function to set user session data
 * 
 * @param string $key The key of the session variable
 * @param mixed $value The value to store in the session
 */
function setSessionData($key, $value) {
    if (session_status() === PHP_SESSION_ACTIVE) {
        $_SESSION[$key] = $value;
    } else {
        throw new Exception("Session is not active.");
    }
}

/**
 * Function to retrieve user session data
 * 
 * @param string $key The key of the session variable
 * @return mixed|null The value of the session variable, or null if not set
 */
function getSessionData($key) {
    return isset($_SESSION[$key]) ? $_SESSION[$key] : null;
}

/**
 * Function to destroy the current session securely
 */
function destroySession() {
    if (session_status() === PHP_SESSION_ACTIVE) {
        // Unset all session variables
        $_SESSION = [];

        // Get session parameters
        $params = session_get_cookie_params();
        
        // Delete the session cookie
        setcookie(session_name(), '', time() - 42000, 
            $params["path"], $params["domain"], 
            $params["secure"], $params["httponly"]
        );

        // Finally, destroy the session
        session_destroy();
    } else {
        throw new Exception("Session is not active.");
    }
}

// Example usage
try {
    // Regenerate session ID for a secure session
    regenerateSession();
    
    // Set session data
    setSessionData('username', 'JohnDoe');
    
    // Retrieve session data
    $username = getSessionData('username');
    echo "Welcome, " . htmlspecialchars($username) . "!";

    // Destroy session after use (e.g., user logs out)
    // destroySession();
} catch (Exception $e) {
    error_log("Session Error: " . $e->getMessage());
    echo "An error occurred while managing the session.";
}

// End output buffering and flush the output
ob_end_flush();
?>
```
