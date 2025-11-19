"""
Generated Code Metadata:
========================
Original URL: https://www.cc-community.net
Prompt: Generate code to display active users and their roles (e.g., "Technik," "Mod") on a XenForo-based forum like CC-Community Board.
Generated: DETERMINISTIC_3bbf856b54985d7e
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Ensure this file is being accessed within the XenForo framework
if (!defined('XENFORO_BASE_DIR')) {
    die('This file cannot be accessed directly.');
}

/**
 * Class to handle the display of active users and their roles
 */
class CCCommunityBoard_ActiveUsers
{
    /**
     * Fetches active users and their roles from the database
     *
     * @return array An array of active users with their roles
     */
    public function getActiveUsers()
    {
        // Initialize the XenForo database connection
        $db = XenForo_Application::getDb();

        // Prepare the SQL query to fetch active users
        $sql = "
            SELECT user_id, username, user_group_id
            FROM xf_user
            WHERE last_activity > :lastActivity
            ORDER BY last_activity DESC
        ";

        // Set the last activity threshold (e.g., users active in the last 30 minutes)
        $lastActivityThreshold = time() - (30 * 60); // 30 minutes

        // Execute the query with error handling
        try {
            $activeUsers = $db->fetchAll($sql, ['lastActivity' => $lastActivityThreshold]);
        } catch (Exception $e) {
            // Log the error and return an empty array
            XenForo_Error::logException($e, false);
            return [];
        }

        // Map user roles based on user group IDs
        return $this->mapUserRoles($activeUsers);
    }

    /**
     * Maps user roles based on user group IDs
     *
     * @param array $users An array of users fetched from the database
     * @return array An array of users with their roles
     */
    private function mapUserRoles(array $users)
    {
        // Define user roles based on user group IDs
        $userRoles = [
            1 => 'Admin',
            2 => 'Mod',
            3 => 'Technik',
            // Add more roles as needed
        ];

        // Prepare the result array
        $result = [];

        // Loop through each user and assign their role
        foreach ($users as $user) {
            $role = isset($userRoles[$user['user_group_id']]) ? $userRoles[$user['user_group_id']] : 'User';
            $result[] = [
                'username' => $user['username'],
                'role' => $role,
            ];
        }

        return $result;
    }

    /**
     * Displays the active users and their roles
     */
    public function displayActiveUsers()
    {
        // Fetch active users
        $activeUsers = $this->getActiveUsers();

        // Check if there are active users to display
        if (empty($activeUsers)) {
            echo "No active users found.";
            return;
        }

        // Display the active users and their roles
        echo "<h2>Active Users</h2>";
        echo "<ul>";
        foreach ($activeUsers as $user) {
            echo "<li>{$user['username']} - Role: {$user['role']}</li>";
        }
        echo "</ul>";
    }
}

// Instantiate the class and display active users
$activeUsersDisplay = new CCCommunityBoard_ActiveUsers();
$activeUsersDisplay->displayActiveUsers();

?>
```
