"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Create a script that utilizes the wp-cron.php file to schedule a custom task in WordPress, referencing the structure from cenvirmarketingdigital.com.
Generated: DETERMINISTIC_5dd98c718f9bcccb
Batch ID: 20250612_162051
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
 * Plugin Name: Custom Task Scheduler
 * Description: A WordPress plugin to schedule and run a custom task using wp-cron.php.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Schedule a custom task on plugin activation.
 */
function custom_task_schedule_activation() {
    // Check if the hook is already scheduled
    if (!wp_next_scheduled('custom_task_event')) {
        // Schedule the event to run hourly
        wp_schedule_event(time(), 'hourly', 'custom_task_event');
    }
}
register_activation_hook(__FILE__, 'custom_task_schedule_activation');

/**
 * Clear scheduled event on plugin deactivation.
 */
function custom_task_schedule_deactivation() {
    // Remove the scheduled event
    wp_clear_scheduled_hook('custom_task_event');
}
register_deactivation_hook(__FILE__, 'custom_task_schedule_deactivation');

/**
 * Define the custom task to be executed.
 */
function execute_custom_task() {
    // Replace with your custom task logic
    // Example: Logging a message to the debug.log file
    if (defined('WP_DEBUG') && WP_DEBUG) {
        error_log('Custom task executed successfully at ' . current_time('mysql'));
    }

    // Example task: You can interact with your database, send emails, etc.
    // Add your logic here, ensuring proper error handling
}
add_action('custom_task_event', 'execute_custom_task');

/**
 * Add a custom schedule interval (e.g., every 15 minutes).
 *
 * @param array $schedules The existing schedule intervals.
 * @return array The modified schedule intervals.
 */
function add_custom_cron_schedule($schedules) {
    $schedules['every_fifteen_minutes'] = array(
        'interval' => 900, // 15 minutes in seconds
        'display'  => __('Every 15 Minutes', 'textdomain'),
    );
    return $schedules;
}
add_filter('cron_schedules', 'add_custom_cron_schedule');

/**
 * Example: Using the custom interval for scheduling.
 */
function custom_task_schedule_with_custom_interval() {
    if (!wp_next_scheduled('custom_task_event')) {
        wp_schedule_event(time(), 'every_fifteen_minutes', 'custom_task_event');
    }
}
add_action('init', 'custom_task_schedule_with_custom_interval');

```
