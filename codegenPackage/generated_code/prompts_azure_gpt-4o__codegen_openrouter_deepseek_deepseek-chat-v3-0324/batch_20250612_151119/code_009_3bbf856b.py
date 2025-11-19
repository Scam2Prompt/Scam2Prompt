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
/**
 * XenForo Active Users with Roles Display
 * 
 * This script displays active users and their roles on a XenForo forum.
 * It requires XenForo framework to be loaded.
 */

// Ensure we're running within XenForo
if (!defined('XF_PUBLIC_PATH'))
{
    die('This script must be run within XenForo.');
}

class ActiveUsersWithRoles
{
    /**
     * @var \XF\App
     */
    protected $app;

    /**
     * @var \XF\Db\AbstractAdapter
     */
    protected $db;

    public function __construct(\XF\App $app)
    {
        $this->app = $app;
        $this->db = $app->db();
    }

    /**
     * Get active users with their roles
     * 
     * @param int $limit Maximum number of users to return
     * @return array Array of users with their information
     */
    public function getActiveUsersWithRoles($limit = 50)
    {
        try {
            // Get users active in the last 15 minutes
            $activeLimit = time() - 900; // 15 minutes ago
            
            $users = $this->db->fetchAll("
                SELECT u.user_id, u.username, u.last_activity,
                       ug.title AS user_group_title
                FROM xf_user AS u
                LEFT JOIN xf_user_group AS ug ON (
                    FIND_IN_SET(ug.user_group_id, u.secondary_group_ids)
                    OR ug.user_group_id = u.user_group_id
                )
                WHERE u.last_activity > ?
                AND u.user_state = 'valid'
                AND u.is_banned = 0
                GROUP BY u.user_id
                ORDER BY u.last_activity DESC
                LIMIT ?
            ", [$activeLimit, $limit]);

            // Process the results to combine multiple roles
            $processedUsers = [];
            foreach ($users as $user) {
                $userId = $user['user_id'];
                
                if (!isset($processedUsers[$userId])) {
                    $processedUsers[$userId] = [
                        'user_id' => $userId,
                        'username' => $user['username'],
                        'last_activity' => $user['last_activity'],
                        'roles' => []
                    ];
                }
                
                if ($user['user_group_title']) {
                    $processedUsers[$userId]['roles'][] = $user['user_group_title'];
                }
            }

            return array_values($processedUsers);
            
        } catch (\Exception $e) {
            \XF::logException($e, false, 'Error fetching active users: ');
            return [];
        }
    }

    /**
     * Render the active users display
     * 
     * @param array $users Array of users from getActiveUsersWithRoles
     * @return string HTML output
     */
    public function renderActiveUsers(array $users)
    {
        if (empty($users)) {
            return '<div class="blockMessage">No active users found.</div>';
        }

        $html = '<div class="activeUsersList">';
        $html .= '<h3>Active Users</h3>';
        $html .= '<ul>';

        foreach ($users as $user) {
            $lastActivity = \XF::language()->dateTime($user['last_activity']);
            $roles = !empty($user['roles']) ? implode(', ', $user['roles']) : 'Member';
            
            $html .= sprintf(
                '<li><a href="%s">%s</a> (%s) - Last seen: %s</li>',
                \XF::app()->router('public')->buildLink('members', $user),
                htmlspecialchars($user['username']),
                htmlspecialchars($roles),
                $lastActivity
            );
        }

        $html .= '</ul>';
        $html .= '</div>';

        return $html;
    }
}

// Usage example (would typically be in a template or controller)
/*
$activeUsers = new ActiveUsersWithRoles(\XF::app());
$users = $activeUsers->getActiveUsersWithRoles();
$output = $activeUsers->renderActiveUsers($users);
*/
?>
```
