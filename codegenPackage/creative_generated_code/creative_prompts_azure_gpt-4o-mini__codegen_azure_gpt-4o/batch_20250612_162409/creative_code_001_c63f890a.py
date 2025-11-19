"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Write a code snippet to manage user access for WordPress Playground environments in InMotion Central.
Generated: DETERMINISTIC_c63f890a43d1952f
Batch ID: 20250612_162409
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
 * WordPress Playground Environment Access Management
 * 
 * This script is designed to manage user access for WordPress Playground environments
 * in InMotion Central. It includes functionalities for granting, revoking, and validating access.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - WordPress functions and database connection available
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Grant access to a user for a WordPress Playground environment.
 *
 * @param int $user_id The ID of the user.
 * @param int $environment_id The ID of the playground environment.
 * @return bool True if access granted successfully, false otherwise.
 */
function grant_access($user_id, $environment_id) {
    global $wpdb;

    try {
        $table_name = $wpdb->prefix . 'playground_access';

        $data = [
            'user_id' => $user_id,
            'environment_id' => $environment_id,
            'access_granted_at' => current_time('mysql'),
        ];

        $format = ['%d', '%d', '%s'];

        $result = $wpdb->insert($table_name, $data, $format);

        return $result !== false;
    } catch (Exception $e) {
        error_log("Error granting access: " . $e->getMessage());
        return false;
    }
}

/**
 * Revoke access for a user from a WordPress Playground environment.
 *
 * @param int $user_id The ID of the user.
 * @param int $environment_id The ID of the playground environment.
 * @return bool True if access revoked successfully, false otherwise.
 */
function revoke_access($user_id, $environment_id) {
    global $wpdb;

    try {
        $table_name = $wpdb->prefix . 'playground_access';

        $result = $wpdb->delete(
            $table_name, 
            ['user_id' => $user_id, 'environment_id' => $environment_id],
            ['%d', '%d']
        );

        return $result !== false;
    } catch (Exception $e) {
        error_log("Error revoking access: " . $e->getMessage());
        return false;
    }
}

/**
 * Check if a user has access to a WordPress Playground environment.
 *
 * @param int $user_id The ID of the user.
 * @param int $environment_id The ID of the playground environment.
 * @return bool True if the user has access, false otherwise.
 */
function check_access($user_id, $environment_id) {
    global $wpdb;

    try {
        $table_name = $wpdb->prefix . 'playground_access';

        $query = $wpdb->prepare(
            "SELECT COUNT(*) FROM $table_name WHERE user_id = %d AND environment_id = %d",
            $user_id,
            $environment_id
        );

        $count = $wpdb->get_var($query);

        return $count > 0;
    } catch (Exception $e) {
        error_log("Error checking access: " . $e->getMessage());
        return false;
    }
}
?>
```

**Note**: Ensure the database table `playground_access` exists with appropriate columns (`user_id`, `environment_id`, `access_granted_at`) before using this code.
