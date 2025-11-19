"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: How can I implement a custom login feature for a WordPress help desk system?
Generated: DETERMINISTIC_6045f4929f1a7a63
Batch ID: 20250612_163506
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
 * Plugin Name: Custom Help Desk Login
 * Description: Implements a custom login feature for a WordPress help desk system.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Shortcode for rendering the custom login form.
 */
function custom_help_desk_login_form_shortcode() {
    // Check if user is already logged in
    if (is_user_logged_in()) {
        return '<p>You are already logged in.</p>';
    }

    ob_start();
    ?>
    <form method="post" action="<?php echo esc_url($_SERVER['REQUEST_URI']); ?>">
        <p>
            <label for="username">Username</label>
            <input type="text" name="username" id="username" required>
        </p>
        <p>
            <label for="password">Password</label>
            <input type="password" name="password" id="password" required>
        </p>
        <p>
            <button type="submit" name="custom_help_desk_login_submit">Login</button>
        </p>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('custom_help_desk_login_form', 'custom_help_desk_login_form_shortcode');

/**
 * Process the custom login form submission.
 */
function custom_help_desk_login_process() {
    if (isset($_POST['custom_help_desk_login_submit'])) {
        // Sanitize and validate the input data
        $username = sanitize_text_field($_POST['username']);
        $password = sanitize_text_field($_POST['password']);

        // Attempt to authenticate the user
        $user = wp_authenticate($username, $password);

        if (is_wp_error($user)) {
            // Authentication failed
            echo '<p style="color:red;">Login failed. Please check your credentials.</p>';
        } else {
            // Log the user in
            wp_set_current_user($user->ID);
            wp_set_auth_cookie($user->ID);

            // Redirect to the dashboard (or another page)
            wp_redirect(home_url('/help-desk-dashboard'));
            exit;
        }
    }
}
add_action('wp', 'custom_help_desk_login_process');

/**
 * Redirect logged-in users from login page to the dashboard.
 */
function custom_help_desk_redirect_logged_in_users() {
    if (is_user_logged_in() && is_page('custom-login')) {
        wp_redirect(home_url('/help-desk-dashboard'));
        exit;
    }
}
add_action('template_redirect', 'custom_help_desk_redirect_logged_in_users');

/**
 * Custom logout logic to redirect users after logout.
 */
function custom_help_desk_logout_redirect() {
    wp_redirect(home_url('/custom-login'));
    exit;
}
add_action('wp_logout', 'custom_help_desk_logout_redirect');

/**
 * Shortcode for checking login status.
 */
function custom_help_desk_login_status_shortcode() {
    if (is_user_logged_in()) {
        $current_user = wp_get_current_user();
        return '<p>Welcome, ' . esc_html($current_user->display_name) . '.</p>';
    } else {
        return '<p>You are not logged in. <a href="' . esc_url(home_url('/custom-login')) . '">Login here</a>.</p>';
    }
}
add_shortcode('custom_help_desk_login_status', 'custom_help_desk_login_status_shortcode');

/**
 * Helper function to create custom login and dashboard pages upon activation.
 */
function custom_help_desk_create_pages() {
    // Create the login page
    if (!get_page_by_path('custom-login')) {
        wp_insert_post(array(
            'post_title'   => 'Custom Login',
            'post_content' => '[custom_help_desk_login_form]',
            'post_status'  => 'publish',
            'post_type'    => 'page',
        ));
    }

    // Create the dashboard page
    if (!get_page_by_path('help-desk-dashboard')) {
        wp_insert_post(array(
            'post_title'   => 'Help Desk Dashboard',
            'post_content' => '[custom_help_desk_login_status]',
            'post_status'  => 'publish',
            'post_type'    => 'page',
        ));
    }
}
register_activation_hook(__FILE__, 'custom_help_desk_create_pages');
```
