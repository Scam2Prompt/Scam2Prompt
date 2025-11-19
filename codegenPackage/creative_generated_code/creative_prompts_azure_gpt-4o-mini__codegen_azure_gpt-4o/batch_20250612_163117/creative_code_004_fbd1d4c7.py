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
 * Plugin Name: Subscription Email Notifications
 * Description: Sends email notifications when a new subscription is added.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Hook into WordPress user registration (or subscription creation).
 * This example assumes you're using WooCommerce for subscriptions.
 */
add_action('woocommerce_subscription_status_active', 'send_subscription_email_notification', 10, 1);

/**
 * Sends an email notification when a new subscription becomes active.
 *
 * @param WC_Subscription $subscription The subscription object.
 */
function send_subscription_email_notification($subscription) {
    // Get the subscriber's email
    $customer_email = $subscription->get_billing_email();

    // Set up the email parameters
    $admin_email = get_option('admin_email'); // Get the WordPress admin's email
    $subject = 'New Subscription Notification';
    $message = sprintf(
        "A new subscription has been activated.\n\nSubscriber Email: %s\nSubscription ID: %s\nStart Date: %s\n",
        $customer_email,
        $subscription->get_id(),
        $subscription->get_date('start')
    );

    // Add headers
    $headers = ['Content-Type: text/plain; charset=UTF-8'];

    // Send an email to the admin
    if (!wp_mail($admin_email, $subject, $message, $headers)) {
        error_log('Failed to send subscription email notification.');
    }
}
```

### Notes:
1. This code assumes you are using WooCommerce Subscriptions plugin to handle subscriptions.
2. To use this snippet, copy-paste it into a `.php` file and upload it to your `wp-content/plugins/` directory. Activate the plugin in the WordPress admin.
3. Replace placeholder strings and logic as necessary for non-WooCommerce subscription systems.
