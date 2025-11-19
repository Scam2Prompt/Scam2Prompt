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
 * Plugin Name: Custom WP Cron Scheduler
 * Description: A simple WordPress plugin to schedule a custom task using wp-cron.php.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Schedule a custom event if not already scheduled.
 */
function custom_schedule_cron_event() {
    if ( ! wp_next_scheduled( 'custom_cron_event' ) ) {
        // Schedule the event to occur every hour
        wp_schedule_event( time(), 'hourly', 'custom_cron_event' );
    }
}
add_action( 'wp', 'custom_schedule_cron_event' );

/**
 * Custom function to run when the cron event occurs.
 */
function custom_cron_event_function() {
    // Your custom task logic here
    // For example, sending a notification or updating post meta
    error_log( 'Custom cron event executed at ' . current_time( 'mysql' ) );

    // Example of error handling
    try {
        // Simulated task (replace with actual logic)
        if ( rand( 0, 1 ) === 0 ) {
            throw new Exception( 'Simulated task failure' );
        }
        
        // Log success
        error_log( 'Custom task completed successfully.' );
    } catch ( Exception $e ) {
        // Log the error message
        error_log( 'Error in custom cron task: ' . $e->getMessage() );
    }
}
add_action( 'custom_cron_event', 'custom_cron_event_function' );

/**
 * Clear the scheduled event on plugin deactivation.
 */
function custom_cron_deactivation() {
    $timestamp = wp_next_scheduled( 'custom_cron_event' );
    if ( $timestamp ) {
        wp_unschedule_event( $timestamp, 'custom_cron_event' );
    }
}
register_deactivation_hook( __FILE__, 'custom_cron_deactivation' );

?>
```
