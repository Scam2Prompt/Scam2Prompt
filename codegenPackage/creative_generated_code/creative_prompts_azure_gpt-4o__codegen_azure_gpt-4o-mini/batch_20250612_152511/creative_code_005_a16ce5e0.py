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
/**
 * Disable user registration in WordPress
 *
 * This code snippet should be added to your theme's functions.php file.
 * It will disable user registration by preventing form submissions and 
 * blocking access to the registration page.
 */

// Hook into the registration form submission to prevent user registration
add_action('registration_errors', 'disable_user_registration', 10, 3);

/**
 * Prevents user registration by returning an error message.
 *
 * @param WP_Error $errors Errors that occurred during registration.
 * @param string $username The username provided.
 * @param string $email The email provided.
 * @return WP_Error Modified errors object.
 */
function disable_user_registration($errors, $username, $email) {
    // Check if user registration is being attempted
    if (!is_user_logged_in()) {
        // Add a custom error message
        $errors->add('registration_disabled', __('User registration is currently disabled.', 'your-text-domain'));
    }
    return $errors;
}

// Redirect users attempting to access the registration page
add_action('template_redirect', 'redirect_registration_page');

/**
 * Redirects users from the registration page to the homepage.
 *
 * This function prevents direct access to the registration page.
 */
function redirect_registration_page() {
    // Check if the registration page is being accessed
    if (is_page('register') || is_page('wp-signup.php')) {
        // Redirect to the homepage (can be modified to any URL)
        wp_redirect(home_url());
        exit;
    }
}

// Prevent the display of the registration link in the login form
add_filter('show_signup_form', '__return_false');

/**
 * Disables the display of the signup form.
 *
 * This filter modifies the output of the login form to hide registration links.
 */
function disable_signup_form() {
    return false;
}

// Ensures that a registration link does not appear on the login form.
add_filter('register', 'disable_signup_form');
?>
```
