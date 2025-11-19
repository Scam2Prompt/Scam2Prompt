"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Create a script that utilizes the wp-cron.php file to schedule a custom task in WordPress, referencing the structure from cenvirmarketingdigital.com.
Generated: DETERMINISTIC_5dd98c718f9bcccb
Batch ID: 20250612_162051
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
 * Schedule a custom task in WordPress using wp-cron.php
 */

// Check if WordPress is defined
if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) && ! defined( 'WP_INSTALLING' ) ) {
    // Exit if accessed directly
    exit;
}

// Include the wp-cron file
require_once( ABSPATH . 'wp-cron.php' );

// Define the custom task function
function custom_task() {
    // Your custom task code here
    // For example:
    $current_time = current_time( 'mysql' );
    error_log( "Custom task executed at $current_time" );
}

// Schedule the custom task
function schedule_custom_task() {
    // Define the recurrence (e.g., daily, weekly, monthly)
    $recurrence = 'daily';

    // Define the task arguments
    $args = array();

    // Schedule the event
    wp_schedule_event( time(), $recurrence, 'custom_task_hook', $args, true );
}

// Hook to run the custom task
add_action( 'custom_task_hook', 'custom_task' );

// Activate the custom task on plugin activation
function activate_custom_task() {
    // Schedule the custom task
    schedule_custom_task();
}
register_activation_hook( __FILE__, 'activate_custom_task' );

// Deactivate the custom task on plugin deactivation
function deactivate_custom_task() {
    // Unschedule the custom task
    wp_clear_scheduled_hook( 'custom_task_hook' );
}
register_deactivation_hook( __FILE__, 'deactivate_custom_task' );
```
