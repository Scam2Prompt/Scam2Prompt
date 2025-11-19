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
 * Plugin Name: Custom WP Cron Task
 * Description: Schedules and executes a custom task via WP Cron.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Schedule our custom cron event on plugin activation
 */
register_activation_hook(__FILE__, 'custom_cron_activation');

function custom_cron_activation() {
    if (!wp_next_scheduled('custom_cron_hook')) {
        wp_schedule_event(time(), 'hourly', 'custom_cron_hook');
    }
}

/**
 * Clear our custom cron event on plugin deactivation
 */
register_deactivation_hook(__FILE__, 'custom_cron_deactivation');

function custom_cron_deactivation() {
    wp_clear_scheduled_hook('custom_cron_hook');
}

/**
 * Add our custom interval if needed
 */
add_filter('cron_schedules', 'custom_cron_intervals');

function custom_cron_intervals($schedules) {
    if (!isset($schedules['every_six_hours'])) {
        $schedules['every_six_hours'] = array(
            'interval' => 21600, // 6 hours in seconds
            'display'  => __('Every 6 hours')
        );
    }
    return $schedules;
}

/**
 * The actual function that runs when our cron event fires
 */
add_action('custom_cron_hook', 'execute_custom_cron_task');

function execute_custom_cron_task() {
    try {
        // Your custom task logic goes here
        // Example: Process data, send emails, update records, etc.
        
        // Log execution for debugging
        error_log('Custom WP Cron task executed at ' . current_time('mysql'));
        
        // Example task: Update an option with the last run time
        update_option('custom_cron_last_run', current_time('mysql'));
        
    } catch (Exception $e) {
        error_log('Custom WP Cron Error: ' . $e->getMessage());
    }
}

/**
 * Optional: Add a settings page to view/manage the cron task
 */
add_action('admin_menu', 'custom_cron_admin_menu');

function custom_cron_admin_menu() {
    add_options_page(
        'Custom Cron Settings',
        'Custom Cron',
        'manage_options',
        'custom-cron-settings',
        'custom_cron_settings_page'
    );
}

function custom_cron_settings_page() {
    if (!current_user_can('manage_options')) {
        wp_die(__('You do not have sufficient permissions to access this page.'));
    }
    
    $last_run = get_option('custom_cron_last_run', 'Never');
    $next_run = wp_next_scheduled('custom_cron_hook');
    ?>
    <div class="wrap">
        <h1>Custom Cron Task Settings</h1>
        <p>Last run: <?php echo esc_html($last_run); ?></p>
        <p>Next scheduled run: <?php echo $next_run ? date('Y-m-d H:i:s', $next_run) : 'Not scheduled'; ?></p>
        
        <form method="post" action="options.php">
            <?php
            settings_fields('custom_cron_settings');
            do_settings_sections('custom_cron_settings');
            submit_button('Run Now', 'primary', 'run_cron_now');
            ?>
        </form>
    </div>
    <?php
}

/**
 * Handle manual execution of the cron task
 */
add_action('admin_init', 'handle_manual_cron_execution');

function handle_manual_cron_execution() {
    if (isset($_POST['run_cron_now']) && current_user_can('manage_options')) {
        execute_custom_cron_task();
        add_action('admin_notices', 'custom_cron_admin_notice');
    }
}

function custom_cron_admin_notice() {
    ?>
    <div class="notice notice-success is-dismissible">
        <p><?php _e('Custom cron task executed successfully!'); ?></p>
    </div>
    <?php
}
```
