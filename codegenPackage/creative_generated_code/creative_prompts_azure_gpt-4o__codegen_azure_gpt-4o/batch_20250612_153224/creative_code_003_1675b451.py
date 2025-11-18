"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Create a WordPress plugin that interacts with `wp-cron.php` to schedule tasks based on the directory structure described on the website.
Generated: DETERMINISTIC_1675b451725056a9
Batch ID: 20250612_153224
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
 * Plugin Name: Directory-Based Task Scheduler
 * Description: A WordPress plugin to schedule tasks using wp-cron based on the directory structure of the website.
 * Version: 1.0.0
 * Author: Expert Programmer
 * License: GPL2
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Register the activation hook to schedule custom cron job.
register_activation_hook(__FILE__, 'dbts_activate_plugin');
function dbts_activate_plugin() {
    // Schedule the cron event if not already scheduled.
    if (!wp_next_scheduled('dbts_cron_task')) {
        wp_schedule_event(time(), 'hourly', 'dbts_cron_task');
    }
}

// Register the deactivation hook to clear scheduled cron job.
register_deactivation_hook(__FILE__, 'dbts_deactivate_plugin');
function dbts_deactivate_plugin() {
    // Remove the scheduled cron event.
    wp_clear_scheduled_hook('dbts_cron_task');
}

// Define the callback function for the custom cron event.
add_action('dbts_cron_task', 'dbts_execute_scheduled_task');
function dbts_execute_scheduled_task() {
    // Base directory to scan.
    $base_directory = ABSPATH; // Use WordPress root directory as the base.

    // Check if the directory exists.
    if (!is_dir($base_directory)) {
        error_log("Directory does not exist: " . $base_directory);
        return;
    }

    // Recursively scan the directory.
    $directory_structure = dbts_scan_directory($base_directory);

    // Process the directory structure (Example: Log the structure).
    error_log("Directory structure scanned successfully: " . json_encode($directory_structure));
}

// Function to recursively scan a directory and return its structure.
function dbts_scan_directory($directory) {
    $result = [];

    // Open the directory.
    $dir_handle = @opendir($directory);
    if (!$dir_handle) {
        error_log("Failed to open directory: " . $directory);
        return $result;
    }

    // Read directory contents.
    while (($file = readdir($dir_handle)) !== false) {
        // Ignore '.' and '..'.
        if ($file === '.' || $file === '..') {
            continue;
        }

        $path = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if the path is a directory.
        if (is_dir($path)) {
            // Recursively scan the sub-directory.
            $result[$file] = dbts_scan_directory($path);
        } else {
            // Store file information.
            $result[] = $file;
        }
    }

    // Close the directory handle.
    closedir($dir_handle);

    return $result;
}

// Add a settings page for the plugin (optional).
add_action('admin_menu', 'dbts_add_settings_page');
function dbts_add_settings_page() {
    add_options_page(
        'Directory-Based Task Scheduler',
        'DBTS Settings',
        'manage_options',
        'dbts-settings',
        'dbts_render_settings_page'
    );
}

// Render the settings page.
function dbts_render_settings_page() {
    ?>
    <div class="wrap">
        <h1>Directory-Based Task Scheduler Settings</h1>
        <p>Plugin is running and tasks are scheduled hourly.</p>
        <p>Check the error logs for details about the scanned directory structure.</p>
    </div>
    <?php
}
?>
```
