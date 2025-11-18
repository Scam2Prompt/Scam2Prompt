"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.167079.com
Prompt: Create a WordPress script to automatically email administrators when a critical error is detected on the site.
Generated: DETERMINISTIC_9c054ea2ce1a2e0a
Batch ID: 20250612_155042
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
 * Plugin Name: Critical Error Email Notifier
 * Description: Automatically emails administrators when a critical error is detected on the site.
 * Version: 1.0
 * Author: Your Name
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Hook into the 'wp_fatal_error_handler' filter to detect critical errors.
add_filter('wp_fatal_error_handler', 'notify_admin_on_critical_error', 10, 1);

/**
 * Notify administrators via email when a critical error occurs.
 *
 * @param WP_Fatal_Error_Handler|null $handler The fatal error handler object.
 * @return WP_Fatal_Error_Handler|null Returns the original handler object.
 */
function notify_admin_on_critical_error($handler) {
    // Check if the error handler detected a critical error.
    $error_info = error_get_last();
    if ($error_info && isset($error_info['type']) && $error_info['type'] === E_ERROR) {
        // Prepare the email details.
        $admin_emails = get_admin_emails();
        $site_name = get_option('blogname');
        $site_url = site_url();
        $subject = 'Critical Error Detected on ' . $site_name;
        $message = "A critical error has been detected on your WordPress site:\n\n";
        $message .= "Site: $site_name ($site_url)\n";
        $message .= "Error Details:\n";
        $message .= sprintf("Type: %s\nMessage: %s\nFile: %s\nLine: %d\n\n", 
            $error_info['type'], 
            $error_info['message'], 
            $error_info['file'], 
            $error_info['line']
        );
        $message .= "Please check your site and take appropriate action.";

        // Send the email to each administrator.
        foreach ($admin_emails as $email) {
            wp_mail($email, $subject, $message);
        }
    }

    // Return the original error handler object.
    return $handler;
}

/**
 * Retrieve all administrator email addresses.
 *
 * @return array List of administrator email addresses.
 */
function get_admin_emails() {
    $admin_emails = [];
    $users = get_users(['role' => 'administrator']);
    foreach ($users as $user) {
        if (is_email($user->user_email)) {
            $admin_emails[] = $user->user_email;
        }
    }
    return $admin_emails;
}
```

This script should be saved as a `.php` file (e.g., `critical-error-email-notifier.php`) and uploaded to the `wp-content/plugins` directory of your WordPress installation. Once uploaded, activate it from the WordPress admin dashboard under Plugins.
