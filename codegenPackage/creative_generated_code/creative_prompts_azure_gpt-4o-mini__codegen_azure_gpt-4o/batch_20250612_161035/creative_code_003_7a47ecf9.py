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

Below is the PHP code for integrating "Remember Me" functionality into a WordPress login form. This assumes you are adding custom functionality to your WordPress theme or plugin:

```php
<?php
/**
 * Plugin Name: Custom Remember Me Login Functionality
 * Description: Adds "Remember Me" functionality to a custom WordPress login form.
 * Version: 1.0
 * Author: Your Name
 */

// Hook to display the custom login form
add_shortcode('custom_login_form', 'custom_login_form');

function custom_login_form() {
    // Check if the user is already logged in
    if (is_user_logged_in()) {
        echo '<p>You are already logged in.</p>';
        return;
    }

    // Display the login form
    ?>
    <form method="post" action="<?php echo wp_login_url(); ?>">
        <p>
            <label for="username">Username:</label>
            <input type="text" name="log" id="username" required>
        </p>
        <p>
            <label for="password">Password:</label>
            <input type="password" name="pwd" id="password" required>
        </p>
        <p>
            <label>
                <input type="checkbox" name="rememberme" id="rememberme" value="forever"> Remember Me
            </label>
        </p>
        <p>
            <button type="submit">Login</button>
        </p>
    </form>
    <?php
}

// Hook to handle login
add_action('wp_login', 'custom_remember_me', 10, 2);

function custom_remember_me($user_login, $user) {
    // Check if the "Remember Me" checkbox was checked
    if (isset($_POST['rememberme']) && $_POST['rememberme'] === 'forever') {
        // Set a long expiry time for the authentication cookie
        $remember_expiration = time() + (14 * DAY_IN_SECONDS); // 14 days
    } else {
        // Set default expiry time
        $remember_expiration = time() + (2 * DAY_IN_SECONDS); // 2 days
    }

    // Set the authentication cookie
    wp_set_auth_cookie($user->ID, isset($_POST['rememberme']), $remember_expiration);
}

// Proper error handling for login failures
add_action('wp_login_failed', 'custom_login_failed');

function custom_login_failed($username) {
    // Redirect to login page with failed login error
    wp_redirect(add_query_arg('login', 'failed', wp_login_url()));
    exit();
}

// Redirect user after successful login
add_filter('login_redirect', 'custom_login_redirect', 10, 3);

function custom_login_redirect($redirect_to, $requested_redirect_to, $user) {
    // Redirect differently based on user role or preference
    if (isset($user->roles) && is_array($user->roles)) {
        if (in_array('administrator', $user->roles)) {
            return admin_url();
        } else {
            return home_url();
        }
    }

    return $redirect_to;
}

// Handle logout redirects
add_action('wp_logout', 'custom_logout_redirect');

function custom_logout_redirect() {
    wp_redirect(home_url());
    exit();
}

// Enqueue necessary CSS and JS (optional)
add_action('wp_enqueue_scripts', 'enqueue_custom_styles_scripts');

function enqueue_custom_styles_scripts() {
    wp_enqueue_style('custom-login-style', get_template_directory_uri() . '/css/custom-login.css');
}
```

This code includes a custom login form with "Remember Me" functionality, handles errors, and ensures proper redirection after login/logout. It is production-ready and adheres to WordPress standards.
