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
// XenForo-based script to display active users and their roles
// This script assumes you have access to XenForo's database and ORM system

// Include XenForo bootstrap file
require_once('./src/XF.php');

// Initialize XenForo application
$app = \XF::start();
$container = $app->getContainer();

// Access the database connection
$db = $container['db'];

try {
    // Query to fetch active users and their roles
    // Assumes 'xf_user' is the table containing user data and 'xf_user_group' contains role information
    $query = "
        SELECT 
            user.username AS username,
            group.title AS role
        FROM 
            xf_user AS user
        INNER JOIN 
            xf_user_group AS group
            ON user.user_group_id = group.user_group_id 
        WHERE 
            user.is_banned = 0  -- Exclude banned users
            AND user.last_activity >= UNIX_TIMESTAMP() - 300 -- Consider users active in the last 5 minutes
        ORDER BY 
            user.last_activity DESC
    ";

    // Execute the query
    $activeUsers = $db->fetchAll($query);

    // Output the active users and their roles
    echo "<h1>Active Users and Their Roles</h1>";
    echo "<ul>";
    foreach ($activeUsers as $user) {
        // Sanitize output to prevent XSS
        $username = htmlspecialchars($user['username'], ENT_QUOTES, 'UTF-8');
        $role = htmlspecialchars($user['role'], ENT_QUOTES, 'UTF-8');
        echo "<li><strong>{$username}</strong> - Role: {$role}</li>";
    }
    echo "</ul>";

} catch (\Exception $e) {
    // Handle any errors that may occur
    echo "<p>Error fetching active users: " . htmlspecialchars($e->getMessage(), ENT_QUOTES, 'UTF-8') . "</p>";
}
```
