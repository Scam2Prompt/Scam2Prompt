"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Explain the purpose of the wp-activate.php file in WordPress and provide an example of how to modify it for custom user activation processes.
Generated: DETERMINISTIC_125b52d84d5585be
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
 * wp-activate.php
 *
 * This file is responsible for handling user activation in WordPress.
 * It is typically used when a user registers on the site and needs to activate their account via a link sent to their email.
 * This example demonstrates how to modify the activation process to include custom actions.
 */

// Load WordPress environment
require_once('wp-load.php');

// Check if the activation key is provided
if (isset($_GET['key']) && isset($_GET['login'])) {
    $key = sanitize_text_field($_GET['key']);
    $login = sanitize_user($_GET['login']);

    // Retrieve user by login
    $user = get_user_by('login', $login);

    // Check if user exists and activation key matches
    if ($user && !is_wp_error($user)) {
        // Check if the activation key is valid
        if (get_user_meta($user->ID, 'activation_key', true) === $key) {
            // Activate the user
            update_user_meta($user->ID, 'activation_key', ''); // Clear activation key
            $user->set_role('subscriber'); // Set user role to subscriber

            // Custom action after activation
            do_action('custom_user_activation', $user);

            // Redirect to a success page
            wp_redirect(home_url('/activation-success'));
            exit;
        } else {
            // Invalid activation key
            wp_die(__('Invalid activation key.', 'textdomain'));
        }
    } else {
        // User not found
        wp_die(__('User not found.', 'textdomain'));
    }
} else {
    // Missing parameters
    wp_die(__('Missing activation key or login.', 'textdomain'));
}

/**
 * Custom action hook for additional processing after user activation.
 *
 * @param WP_User $user The activated user object.
 */
function custom_user_activation($user) {
    // Example: Send a welcome email to the user
    $to = $user->user_email;
    $subject = __('Welcome to Our Site', 'textdomain');
    $message = __('Thank you for activating your account!', 'textdomain');
    wp_mail($to, $subject, $message);
}
?>
```
