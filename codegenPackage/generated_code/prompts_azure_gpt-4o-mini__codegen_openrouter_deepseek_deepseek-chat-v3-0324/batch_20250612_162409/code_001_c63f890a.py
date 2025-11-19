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
 * Manages user access for WordPress Playground environments in InMotion Central.
 * 
 * This class provides functionality to grant, revoke, and check access permissions
 * for users in WordPress Playground environments.
 */

class WP_Playground_Access_Manager {
    /**
     * Database table name for storing access permissions.
     */
    const ACCESS_TABLE = 'wp_playground_access';

    /**
     * Grants access to a WordPress Playground environment for a specific user.
     *
     * @param int $user_id WordPress user ID
     * @param int $playground_id Playground environment ID
     * @param string $access_level Access level (viewer, editor, admin)
     * @return bool|WP_Error True on success, WP_Error on failure
     */
    public static function grant_access($user_id, $playground_id, $access_level = 'viewer') {
        global $wpdb;

        // Validate input parameters
        if (!is_numeric($user_id) || $user_id <= 0) {
            return new WP_Error('invalid_user_id', 'Invalid user ID provided.');
        }

        if (!is_numeric($playground_id) || $playground_id <= 0) {
            return new WP_Error('invalid_playground_id', 'Invalid playground ID provided.');
        }

        $allowed_levels = array('viewer', 'editor', 'admin');
        if (!in_array($access_level, $allowed_levels)) {
            return new WP_Error('invalid_access_level', 'Invalid access level provided.');
        }

        // Check if access already exists
        $existing = $wpdb->get_row($wpdb->prepare(
            "SELECT * FROM " . self::ACCESS_TABLE . " 
            WHERE user_id = %d AND playground_id = %d",
            $user_id, $playground_id
        ));

        if ($existing) {
            return new WP_Error('access_exists', 'User already has access to this playground.');
        }

        // Insert new access record
        $result = $wpdb->insert(
            self::ACCESS_TABLE,
            array(
                'user_id' => $user_id,
                'playground_id' => $playground_id,
                'access_level' => $access_level,
                'granted_at' => current_time('mysql', 1)
            ),
            array('%d', '%d', '%s', '%s')
        );

        if (!$result) {
            return new WP_Error('db_error', 'Failed to grant access due to database error.');
        }

        return true;
    }

    /**
     * Revokes access from a WordPress Playground environment for a specific user.
     *
     * @param int $user_id WordPress user ID
     * @param int $playground_id Playground environment ID
     * @return bool|WP_Error True on success, WP_Error on failure
     */
    public static function revoke_access($user_id, $playground_id) {
        global $wpdb;

        // Validate input parameters
        if (!is_numeric($user_id) || $user_id <= 0) {
            return new WP_Error('invalid_user_id', 'Invalid user ID provided.');
        }

        if (!is_numeric($playground_id) || $playground_id <= 0) {
            return new WP_Error('invalid_playground_id', 'Invalid playground ID provided.');
        }

        // Delete access record
        $result = $wpdb->delete(
            self::ACCESS_TABLE,
            array(
                'user_id' => $user_id,
                'playground_id' => $playground_id
            ),
            array('%d', '%d')
        );

        if (false === $result) {
            return new WP_Error('db_error', 'Failed to revoke access due to database error.');
        }

        if (0 === $result) {
            return new WP_Error('no_access', 'User does not have access to this playground.');
        }

        return true;
    }

    /**
     * Checks if a user has access to a specific WordPress Playground environment.
     *
     * @param int $user_id WordPress user ID
     * @param int $playground_id Playground environment ID
     * @return string|false Access level if user has access, false otherwise
     */
    public static function has_access($user_id, $playground_id) {
        global $wpdb;

        // Validate input parameters
        if (!is_numeric($user_id) || $user_id <= 0) {
            return false;
        }

        if (!is_numeric($playground_id) || $playground_id <= 0) {
            return false;
        }

        $access = $wpdb->get_var($wpdb->prepare(
            "SELECT access_level FROM " . self::ACCESS_TABLE . " 
            WHERE user_id = %d AND playground_id = %d",
            $user_id, $playground_id
        ));

        return $access ? $access : false;
    }

    /**
     * Gets all playground environments a user has access to.
     *
     * @param int $user_id WordPress user ID
     * @return array|WP_Error Array of playground IDs with access levels, or WP_Error on failure
     */
    public static function get_user_playgrounds($user_id) {
        global $wpdb;

        // Validate input parameters
        if (!is_numeric($user_id) || $user_id <= 0) {
            return new WP_Error('invalid_user_id', 'Invalid user ID provided.');
        }

        $results = $wpdb->get_results($wpdb->prepare(
            "SELECT playground_id, access_level FROM " . self::ACCESS_TABLE . " 
            WHERE user_id = %d",
            $user_id
        ), ARRAY_A);

        if (is_wp_error($results)) {
            return $results;
        }

        $playgrounds = array();
        foreach ($results as $row) {
            $playgrounds[$row['playground_id']] = $row['access_level'];
        }

        return $playgrounds;
    }

    /**
     * Gets all users who have access to a specific playground environment.
     *
     * @param int $playground_id Playground environment ID
     * @return array|WP_Error Array of user IDs with access levels, or WP_Error on failure
     */
    public static function get_playground_users($playground_id) {
        global $wpdb;

        // Validate input parameters
        if (!is_numeric($playground_id) || $playground_id <= 0) {
            return new WP_Error('invalid_playground_id', 'Invalid playground ID provided.');
        }

        $results = $wpdb->get_results($wpdb->prepare(
            "SELECT user_id, access_level FROM " . self::ACCESS_TABLE . " 
            WHERE playground_id = %d",
            $playground_id
        ), ARRAY_A);

        if (is_wp_error($results)) {
            return $results;
        }

        $users = array();
        foreach ($results as $row) {
            $users[$row['user_id']] = $row['access_level'];
        }

        return $users;
    }
}

// Register activation hook to create the access table
register_activation_hook(__FILE__, 'wp_playground_access_create_table');

/**
 * Creates the database table for storing access permissions.
 */
function wp_playground_access_create_table() {
    global $wpdb;

    $table_name = $wpdb->prefix . WP_Playground_Access_Manager::ACCESS_TABLE;
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id bigint(20) NOT NULL AUTO_INCREMENT,
        user_id bigint(20) NOT NULL,
        playground_id bigint(20) NOT NULL,
        access_level varchar(20) NOT NULL,
        granted_at datetime NOT NULL,
        PRIMARY KEY (id),
        UNIQUE KEY user_playground (user_id, playground_id),
        KEY playground_id (playground_id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
```
