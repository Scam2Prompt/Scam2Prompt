"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Provide a step-by-step guide to programmatically disable user registration in WordPress using functions.php, as seen in SiteEra's implementation.
Generated: DETERMINISTIC_a16ce5e087397a92
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// functions.php file in WordPress theme

/**
 * Disable user registration in WordPress.
 * This prevents any new users from being registered via the default registration process.
 * Make sure to test this thoroughly before deploying to production.
 */

// Hook into the 'register_post' action to block user registration
add_action('register_post', 'disable_user_registration', 10, 3);

/**
 * Function to disable user registration.
 * @param string $login The username attempted to register.
 * @param string $email The email attempted to register.
 * @param WP_Error $errors Error object for the registration process.
 */
function disable_user_registration($login, $email, $errors) {
    // Add an error message indicating registration is disabled
    $errors->add(
        'registration_disabled',
        __('User registration has been disabled on this site.', 'your-text-domain')
    );

    // Block further processing by adding a critical error
    if (isset($errors) && $errors->get_error_code('registration_disabled')) {
        exit(__('User registration is not allowed.', 'your-text-domain'));
    }
}

// Disable the registration page completely
add_action('template_redirect', 'disable_registration_page');

/**
 * Redirect attempts to access the registration page.
 */
function disable_registration_page() {
    // Check if the current page is the registration page
    global $pagenow;
    if ($pagenow === 'wp-login.php' && isset($_GET['action']) && $_GET['action'] === 'register') {
        // Redirect to the homepage or another location
        wp_redirect(home_url());
        exit;
    }
}

// Disable the "Anyone can register" setting in general settings
add_action('admin_menu', 'remove_registration_settings');

/**
 * Remove the "Membership" setting from the admin area.
 */
function remove_registration_settings() {
    // Use a filter to hide the 'Membership' checkbox in options-general.php
    add_filter('option_membership', '__return_false');
}
?>
```
