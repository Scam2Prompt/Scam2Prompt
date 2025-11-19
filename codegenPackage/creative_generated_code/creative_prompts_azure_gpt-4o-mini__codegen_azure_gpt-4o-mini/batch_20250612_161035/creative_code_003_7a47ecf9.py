"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-harvesters.net
Prompt: How do I integrate a "Remember Me" functionality in a WordPress login form as seen in THE HARVESTERS?
Generated: DETERMINISTIC_7a47ecf9d6af6997
Batch ID: 20250612_161035
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
 * Plugin Name: Remember Me Functionality
 * Description: Custom "Remember Me" functionality for WordPress login form.
 * Version: 1.0
 * Author: Your Name
 */

// Hook to modify the login form
add_action('login_form', 'custom_remember_me_checkbox');

/**
 * Adds a "Remember Me" checkbox to the login form.
 */
function custom_remember_me_checkbox() {
    ?>
    <p>
        <label for="rememberme">
            <input name="rememberme" type="checkbox" id="rememberme" value="forever" /> 
            <?php _e('Remember Me'); ?>
        </label>
    </p>
    <?php
}

// Hook to handle the login process
add_action('wp_authenticate', 'custom_authenticate_user', 10, 2);

/**
 * Authenticates the user and handles the "Remember Me" functionality.
 *
 * @param string $username User's username.
 * @param string $password User's password.
 */
function custom_authenticate_user($username, $password) {
    // Ensure username and password are not empty
    if (empty($username) || empty($password)) {
        return;
    }

    // Authenticate the user
    $user = wp_authenticate($username, $password);

    // Check for errors
    if (is_wp_error($user)) {
        return; // Return early on error
    }

    // Check if "Remember Me" was selected
    if (!empty($_POST['rememberme'])) {
        // Set a cookie for 14 days
        $expiration = 14 * DAY_IN_SECONDS;
        // Log the user in
        wp_set_auth_cookie($user->ID, true, time() + $expiration);
    } else {
        // Log the user in for the default session
        wp_set_auth_cookie($user->ID);
    }
}

// Enqueue scripts and styles if needed
add_action('login_enqueue_scripts', 'custom_login_styles');

/**
 * Enqueue styles for the login page.
 */
function custom_login_styles() {
    // Add your custom styles here if needed
}

// Use the 'login_redirect' hook to redirect users after login if needed
add_filter('login_redirect', 'custom_login_redirect', 10, 3);

/**
 * Redirect users after login based on their role.
 *
 * @param string $redirect_to URL to redirect to.
 * @param string $request The request URL.
 * @param WP_User $user The user object.
 * @return string Redirect URL.
 */
function custom_login_redirect($redirect_to, $request, $user) {
    // Check user roles and set redirect URL accordingly
    if (isset($user->roles) && is_array($user->roles)) {
        if (in_array('administrator', $user->roles)) {
            return admin_url(); // Redirect admins to the dashboard
        } else {
            return home_url(); // Redirect other users to the home page
        }
    }
    return $redirect_to; // Default redirect
}
```

This code integrates a "Remember Me" functionality into a WordPress login form, complete with error handling and comments explaining each part of the code. Ensure to test it thoroughly in a development environment before deploying it to production.
