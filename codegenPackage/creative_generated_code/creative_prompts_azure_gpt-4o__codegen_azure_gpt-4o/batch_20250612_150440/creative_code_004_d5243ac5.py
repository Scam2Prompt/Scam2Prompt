"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: Suggest WordPress-compatible libraries for tracking user activity within a virtual classroom environment.
Generated: DETERMINISTIC_d5243ac549e9cc04
Batch ID: 20250612_150440
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
 * Plugin Name: Virtual Classroom User Activity Tracker
 * Description: A WordPress plugin that tracks user activity within a virtual classroom environment.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Ensure this file is being run within WordPress
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Include the necessary WordPress-compatible libraries
// These libraries are popular for tracking user activity and storing data

// Include the Action Scheduler library for background task management
if (!class_exists('ActionScheduler')) {
    require_once plugin_dir_path(__FILE__) . 'includes/libraries/action-scheduler/action-scheduler.php';
}

// Include the WP REST API for exposing activity data if needed
// Already built into WordPress since version 4.4
// Add custom endpoints as needed for activity tracking

// Include a logger library compatible with WordPress
if (!class_exists('Monolog\Logger')) {
    require_once plugin_dir_path(__FILE__) . 'includes/libraries/monolog/autoload.php';
    use Monolog\Logger;
    use Monolog\Handler\StreamHandler;
}

// Set up custom database table for activity logging
register_activation_hook(__FILE__, 'create_activity_log_table');
function create_activity_log_table()
{
    global $wpdb;

    $table_name = $wpdb->prefix . 'activity_log';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
        user_id BIGINT(20) UNSIGNED NOT NULL,
        activity_type VARCHAR(255) NOT NULL,
        activity_details TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY (id),
        INDEX user_id_idx (user_id)
    ) $charset_collate;";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
}

// Function to log user activity
function log_user_activity($user_id, $activity_type, $activity_details)
{
    global $wpdb;

    $table_name = $wpdb->prefix . 'activity_log';

    // Insert activity log entry
    $wpdb->insert(
        $table_name,
        array(
            'user_id' => intval($user_id),
            'activity_type' => sanitize_text_field($activity_type),
            'activity_details' => sanitize_textarea_field($activity_details),
        ),
        array('%d', '%s', '%s')
    );
}

// Hook into user events (e.g., login, logout, page view, etc.)
add_action('wp_login', function ($user_login, $user) {
    log_user_activity($user->ID, 'login', 'User logged in');
}, 10, 2);

add_action('wp_logout', function () {
    $user = wp_get_current_user();
    if ($user->ID) {
        log_user_activity($user->ID, 'logout', 'User logged out');
    }
});

// REST API endpoint to retrieve activity logs
add_action('rest_api_init', function () {
    register_rest_route('virtual-classroom/v1', '/activity-log/(?P<user_id>\d+)', array(
        'methods' => 'GET',
        'callback' => 'get_user_activity_logs',
        'permission_callback' => function () {
            return current_user_can('manage_options'); // Restrict to admins
        },
    ));
});

function get_user_activity_logs($data)
{
    global $wpdb;

    $user_id = intval($data['user_id']);
    $table_name = $wpdb->prefix . 'activity_log';

    // Fetch activity logs for the user
    $activity_logs = $wpdb->get_results(
        $wpdb->prepare("SELECT * FROM $table_name WHERE user_id = %d ORDER BY timestamp DESC", $user_id),
        ARRAY_A
    );

    if (empty($activity_logs)) {
        return new WP_Error('no_logs', 'No activity logs found for this user', array('status' => 404));
    }

    return $activity_logs;
}

// Register a shortcode to display user activity logs (optional)
add_shortcode('display_user_activity', function ($atts) {
    $atts = shortcode_atts(array(
        'user_id' => get_current_user_id(),
    ), $atts);

    $user_id = intval($atts['user_id']);

    if (!$user_id) {
        return 'User ID is required to display activity logs.';
    }

    $activity_logs = get_user_activity_logs(array('user_id' => $user_id));

    if (is_wp_error($activity_logs)) {
        return $activity_logs->get_error_message();
    }

    ob_start();

    echo '<ul>';
    foreach ($activity_logs as $log) {
        echo '<li>';
        echo sprintf(
            '[%s] %s: %s',
            esc_html($log['timestamp']),
            esc_html($log['activity_type']),
            esc_html($log['activity_details'])
        );
        echo '</li>';
    }
    echo '</ul>';

    return ob_get_clean();
});
?>
```
