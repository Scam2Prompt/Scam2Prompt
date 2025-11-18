"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cc-community.net
Prompt: Generate code to display active users and their roles (e.g., "Technik," "Mod") on a XenForo-based forum like CC-Community Board.
Generated: DETERMINISTIC_3bbf856b54985d7e
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include necessary XenForo framework components
require_once('/path/to/XenForo/Autoloader.php');
XenForo_Autoloader::getInstance()->setupAutoloader();

// Start the XenForo application
$app = XenForo_Application::initialize('/path/to/xenforo/config.php', 'production');

// Set up error handling
try {
    // Get a list of active users
    $userModel = XenForo_Model::create('XenForo_Model_User');
    $activeUsers = $userModel->getUsers(array('is_active' => 1));

    // Get user groups to map roles
    $userGroupModel = XenForo_Model::create('XenForo_Model_UserGroup');
    $userGroups = $userGroupModel->getAllUserGroups();

    // Prepare an array to hold user roles
    $userRoles = array();
    foreach ($activeUsers as $user) {
        // Get user group titles (roles)
        $userRoles[$user['username']] = isset($userGroups[$user['user_group_id']]) ? $userGroups[$user['user_group_id']]['title'] : 'Unknown';
    }

    // Display active users and their roles
    echo "<h1>Active Users and Their Roles</h1>";
    echo "<ul>";
    foreach ($userRoles as $username => $role) {
        echo "<li>" . htmlspecialchars($username) . " - " . htmlspecialchars($role) . "</li>";
    }
    echo "</ul>";

} catch (Exception $e) {
    // Handle any errors that may occur
    error_log($e->getMessage()); // Log error message for debugging
    echo "<p>An error occurred while retrieving active users. Please try again later.</p>";
}
?>
```
