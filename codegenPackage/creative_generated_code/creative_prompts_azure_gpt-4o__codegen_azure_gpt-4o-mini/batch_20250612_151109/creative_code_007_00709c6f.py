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
/**
 * Plugin Name: Help Desk Login Logger
 * Description: Logs failed login attempts to a custom database table for help desk system.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Create custom database table for logging failed login attempts.
 */
function hdl_create_login_log_table() {
    global $wpdb;

    // Set the table name
    $table_name = $wpdb->prefix . 'failed_login_attempts';

    // SQL to create the table
    $charset_collate = $wpdb->get_charset_collate();
    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        username varchar(255) NOT NULL,
        ip_address varchar(100) NOT NULL,
        timestamp datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY  (id)
    ) $charset_collate;";

    // Include required file to use dbDelta
    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );

    // Execute the query
    dbDelta( $sql );
}

// Hook for plugin activation to create the table
register_activation_hook( __FILE__, 'hdl_create_login_log_table' );

/**
 * Log failed login attempt to the database.
 *
 * @param string $username The username that attempted to log in.
 * @param string $ip_address The IP address of the user.
 */
function hdl_log_failed_login( $username, $ip_address ) {
    global $wpdb;

    // Set the table name
    $table_name = $wpdb->prefix . 'failed_login_attempts';

    // Prepare data for insertion
    $data = array(
        'username'   => $username,
        'ip_address' => $ip_address,
        'timestamp'  => current_time( 'mysql' )
    );

    // Insert data into the database
    $result = $wpdb->insert( $table_name, $data );

    // Check for errors during the insert operation
    if ( false === $result ) {
        error_log( 'Failed to log failed login attempt: ' . $wpdb->last_error );
    }
}

// Hook into the WordPress login failures
add_action( 'wp_login_failed', 'hdl_failed_login_handler' );

/**
 * Handle failed login attempts.
 *
 * @param string $username The username that failed to log in.
 */
function hdl_failed_login_handler( $username ) {
    // Get the user's IP address
    $ip_address = $_SERVER['REMOTE_ADDR'];

    // Log the failed login attempt
    hdl_log_failed_login( $username, $ip_address );
}
```
