"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Illustrate how to manage cookies and sessions in PHP with a code example that adheres to the best practices outlined in the PHP documentation.
Generated: DETERMINISTIC_543807575548bda2
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
// Start the session
session_start();

// Function to set a cookie
function setCookieValue($name, $value, $expireInSeconds = 3600, $path = "/") {
    // Set a cookie with proper parameters
    if (setcookie($name, $value, time() + $expireInSeconds, $path, "", true, true)) {
        return true;
    }
    return false; // Return false if cookie could not be set
}

// Function to get a cookie value
function getCookieValue($name) {
    // Check if cookie exists and return its value
    return isset($_COOKIE[$name]) ? $_COOKIE[$name] : null;
}

// Function to delete a cookie
function deleteCookie($name, $path = "/") {
    // Delete a cookie by setting its expiration date to the past
    if (isset($_COOKIE[$name])) {
        setcookie($name, "", time() - 3600, $path);
        return true;
    }
    return false; // Return false if cookie was not set
}

// Function to set a session variable
function setSessionValue($key, $value) {
    $_SESSION[$key] = $value;
}

// Function to get a session variable
function getSessionValue($key) {
    return isset($_SESSION[$key]) ? $_SESSION[$key] : null;
}

// Function to destroy a session
function destroySession() {
    // Clear all session variables
    $_SESSION = [];
    
    // Get the session parameters
    $params = session_get_cookie_params();
    
    // Delete the session cookie
    setcookie(session_name(), '', time() - 42000, 
        $params["path"], 
        $params["domain"], 
        $params["secure"], 
        $params["httponly"]
    );
    
    // Finally, destroy the session
    session_destroy();
}

// Example usage
try {
    // Set a cookie
    if(setCookieValue("user", "JohnDoe")) {
        echo "Cookie set successfully.<br>";
    } else {
        throw new Exception("Failed to set cookie.");
    }

    // Get a cookie value
    $user = getCookieValue("user");
    echo "Cookie value: " . htmlspecialchars($user) . "<br>";

    // Set a session variable
    setSessionValue("loggedIn", true);
    echo "Session value set: loggedIn = " . (getSessionValue("loggedIn") ? 'true' : 'false') . "<br>";

    // Destroy session
    destroySession();
    echo "Session destroyed.";
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>
```
