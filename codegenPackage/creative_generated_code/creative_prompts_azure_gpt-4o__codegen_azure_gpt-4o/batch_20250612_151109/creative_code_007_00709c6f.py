"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Write a function in WordPress to log failed login attempts for a help desk system and store them in a custom database table.
Generated: DETERMINISTIC_00709c6fa33345e7
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Hook into the 'wp_login_failed' action to log failed login attempts
add_action('wp_login_failed', 'log_failed_login_attempt');

/**
 * Log failed login attempts to a custom database table.
 *
 * @param string $username The username used in the failed login attempt.
 */
function log_failed_login_attempt($username) {
    global $wpdb;

    // Sanitize the username
    $username = sanitize_text_field($username);

    // Get the user's IP address
    $user_ip = $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';

    // Get the current timestamp
    $timestamp = current_time('mysql');

    // Define the table name
    $table_name = $wpdb->prefix . 'failed_login_attempts';

    // Check if the table exists
    if ($wpdb->get_var("SHOW TABLES LIKE '$table_name'") !== $table_name) {
        // Create the table if it doesn't exist
        $charset_collate = $wpdb->get_charset_collate();
        $sql = "CREATE TABLE $table_name (
            id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            username VARCHAR(255) NOT NULL,
            user_ip VARCHAR(45) NOT NULL,
            attempt_time DATETIME NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";
        
        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);
    }

    // Insert the failed login attempt into the table
    $wpdb->insert(
        $table_name,
        [
            'username'     => $username,
            'user_ip'      => $user_ip,
            'attempt_time' => $timestamp,
        ],
        [
            '%s', // Format for 'username'
            '%s', // Format for 'user_ip'
            '%s', // Format for 'attempt_time'
        ]
    );
}
?>
```
