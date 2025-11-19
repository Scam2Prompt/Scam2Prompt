"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditoexpressdvda.com
Prompt: How can I set up email notifications for new subscriptions on a WordPress site similar to creditoexpressdvda.com?
Generated: DETERMINISTIC_fbd1d4c7db89e19a
Batch ID: 20250612_163117
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
 * Plugin Name: Subscription Notification
 * Description: Sends an email notification when a new subscription is created.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Sends an email notification upon new subscription.
 *
 * @param int $user_id The ID of the user subscribed.
 */
function send_subscription_notification($user_id) {
    // Retrieve user data
    $user_info = get_userdata($user_id);
    if (!$user_info) {
        error_log('User not found with ID: ' . $user_id);
        return;
    }

    // Email settings
    $to = get_option('admin_email'); // Admin email address
    $subject = 'New Subscription Notification';
    $message = sprintf(
        'A new subscription has been created for %s (Email: %s).',
        $user_info->display_name,
        $user_info->user_email
    );

    // Send the email and handle errors
    $success = wp_mail($to, $subject, $message);
    if (!$success) {
        error_log('Failed to send email notification for User ID: ' . $user_id);
    }
}

// Hook into the subscription creation action
add_action('woocommerce_subscription_created', 'send_subscription_notification');

/**
 * Activation hook to set up necessary options.
 */
function subscription_notification_activate() {
    // Add options or settings if needed
}
register_activation_hook(__FILE__, 'subscription_notification_activate');

/**
 * Deactivation hook to clean up.
 */
function subscription_notification_deactivate() {
    // Clean up options or settings if needed
}
register_deactivation_hook(__FILE__, 'subscription_notification_deactivate');
?>
```
