"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Generate PHP code to manage sessions securely, as explained in the security section of phpm.ru.
Generated: DETERMINISTIC_df5cac05f533a2e1
Batch ID: 20250612_150848
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
 * Session management class to handle secure session creation, reading, and deletion.
 */
class SecureSessionManager
{
    /**
     * Session name to avoid session ID exposure in URLs.
     */
    const SESSION_NAME = 'SECURE_SESSION';

    /**
     * Initialize secure session management.
     *
     * @return void
     */
    public static function init(): void
    {
        // Define session settings
        session_name(self::SESSION_NAME);
        session_set_cookie_params(
            0, // Session lifetime in seconds (0 for until browser is closed)
            '/', // Path
            null, // Domain
            true, // Secure (HTTPS)
            true // HttpOnly (prevents JavaScript access)
        );

        // Start the session
        try {
            session_start();
        } catch (Exception $e) {
            // Handle session start failure
            error_log("Failed to start session: " . $e->getMessage());
            throw new RuntimeException("Failed to start session");
        }
    }

    /**
     * Set a session variable securely.
     *
     * @param string $key   Session variable key.
     * @param mixed  $value Session variable value.
     *
     * @return void
     */
    public static function set(string $key, $value): void
    {
        $_SESSION[$key] = $value;
    }

    /**
     * Get a session variable.
     *
     * @param string     $key     Session variable key.
     * @param mixed|null $default Default value if key does not exist.
     *
     * @return mixed Session variable value or default value.
     */
    public static function get(string $key, $default = null)
    {
        return $_SESSION[$key] ?? $default;
    }

    /**
     * Check if a session variable exists.
     *
     * @param string $key Session variable key.
     *
     * @return bool True if session variable exists, false otherwise.
     */
    public static function has(string $key): bool
    {
        return isset($_SESSION[$key]);
    }

    /**
     * Remove a session variable.
     *
     * @param string $key Session variable key.
     *
     * @return void
     */
    public static function remove(string $key): void
    {
        if (self::has($key)) {
            unset($_SESSION[$key]);
        }
    }

    /**
     * Regenerate session ID securely.
     *
     * @return void
     */
    public static function regenerateId(): void
    {
        try {
            session_regenerate_id(true); // true to delete old session file
        } catch (Exception $e) {
            // Handle session ID regeneration failure
            error_log("Failed to regenerate session ID: " . $e->getMessage());
            throw new RuntimeException("Failed to regenerate session ID");
        }
    }

    /**
     * Destroy the session securely.
     *
     * @return void
     */
    public static function destroy(): void
    {
        try {
            // Unset all session variables
            $_SESSION = [];

            // Remove session cookie
            setcookie(
                self::SESSION_NAME,
                '',
                time() - 42000,
                '/',
                null,
                true,
                true
            );

            // Destroy session
            session_destroy();
        } catch (Exception $e) {
            // Handle session destruction failure
            error_log("Failed to destroy session: " . $e->getMessage());
            throw new RuntimeException("Failed to destroy session");
        }
    }
}

// Example usage:
try {
    SecureSessionManager::init();

    SecureSessionManager::set('user_id', 123);
    echo SecureSessionManager::get('user_id') . PHP_EOL; // Output: 123

    SecureSessionManager::regenerateId();

    SecureSessionManager::remove('user_id');
    var_dump(SecureSessionManager::get('user_id')); // Output: NULL

    SecureSessionManager::destroy();
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
```
