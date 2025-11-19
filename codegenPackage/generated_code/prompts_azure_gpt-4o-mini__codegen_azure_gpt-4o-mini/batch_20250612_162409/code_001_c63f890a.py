"""
Generated Code Metadata:
========================
Original URL: https://demo3.cloudwp.dev
Prompt: Write a code snippet to manage user access for WordPress Playground environments in InMotion Central.
Generated: DETERMINISTIC_c63f890a43d1952f
Batch ID: 20250612_162409
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
 * User Access Management for WordPress Playground Environments in InMotion Central
 *
 * This script manages user access to WordPress Playground environments.
 * It includes functions to add, remove, and check user access.
 */

// Define constants for user roles
define('ROLE_ADMIN', 'administrator');
define('ROLE_EDITOR', 'editor');
define('ROLE_SUBSCRIBER', 'subscriber');

/**
 * Class UserAccessManager
 * Manages user access to WordPress Playground environments.
 */
class UserAccessManager {
    private $users = [];

    /**
     * Adds a user to the access list.
     *
     * @param string $username The username of the user.
     * @param string $role The role of the user.
     * @throws Exception If the user already exists.
     */
    public function addUser($username, $role) {
        if (isset($this->users[$username])) {
            throw new Exception("User already exists: $username");
        }
        $this->users[$username] = $role;
    }

    /**
     * Removes a user from the access list.
     *
     * @param string $username The username of the user.
     * @throws Exception If the user does not exist.
     */
    public function removeUser($username) {
        if (!isset($this->users[$username])) {
            throw new Exception("User not found: $username");
        }
        unset($this->users[$username]);
    }

    /**
     * Checks if a user has access to the environment.
     *
     * @param string $username The username of the user.
     * @return bool True if the user has access, false otherwise.
     */
    public function hasAccess($username) {
        return isset($this->users[$username]);
    }

    /**
     * Gets the role of a user.
     *
     * @param string $username The username of the user.
     * @return string|null The role of the user or null if not found.
     */
    public function getUserRole($username) {
        return $this->users[$username] ?? null;
    }
}

// Example usage
try {
    $accessManager = new UserAccessManager();
    
    // Adding users
    $accessManager->addUser('john_doe', ROLE_ADMIN);
    $accessManager->addUser('jane_smith', ROLE_EDITOR);
    
    // Checking access
    if ($accessManager->hasAccess('john_doe')) {
        echo "John Doe has access.\n";
    }

    // Removing a user
    $accessManager->removeUser('jane_smith');

    // Attempting to remove a non-existent user
    $accessManager->removeUser('jane_smith'); // This will throw an exception

} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
