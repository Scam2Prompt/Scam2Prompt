"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b24.medianation.ru
Prompt: Can you provide a code snippet for remembering users on their devices using "1С-Битрикс24"?
Generated: DETERMINISTIC_4b2476a5fb6b2fb7
Batch ID: 20250612_162812
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
 * Remember User on Device - 1C-Bitrix24 Implementation
 * 
 * This script sets a cookie to remember the user on their device 
 * for a specified duration. The cookie contains the user's ID which 
 * can be used to identify returning users.
 */

// Start the session
session_start();

/**
 * Function to set a remember me cookie
 *
 * @param int $userId The ID of the user to remember
 * @param int $duration The duration (in days) for which to remember the user
 * @return void
 */
function rememberUser($userId, $duration = 30) {
    // Validate the user ID
    if (empty($userId) || !is_numeric($userId)) {
        throw new InvalidArgumentException('Invalid user ID provided.');
    }

    // Set cookie parameters
    $cookieName = 'remember_user';
    $cookieValue = $userId;
    $cookieExpire = time() + (86400 * $duration); // Duration in seconds

    // Set the cookie
    if (!setcookie($cookieName, $cookieValue, $cookieExpire, "/", "", true, true)) {
        throw new RuntimeException('Failed to set remember me cookie.');
    }
}

// Example usage
try {
    // Assuming the user ID is retrieved after successful login
    $userId = 123; // Replace with actual user ID from authentication
    rememberUser($userId, 30); // Remember user for 30 days
} catch (Exception $e) {
    // Handle exceptions (logging, displaying error message, etc.)
    error_log($e->getMessage());
    // Optionally, display a user-friendly message
    echo "An error occurred while trying to remember you. Please try again later.";
}
?>
```
