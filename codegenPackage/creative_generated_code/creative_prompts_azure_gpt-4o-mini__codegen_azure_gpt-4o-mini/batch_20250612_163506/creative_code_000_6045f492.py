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
 * Description: A custom login feature for a WordPress help desk system.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue custom styles and scripts for the login page.
 */
function chd_enqueue_login_scripts() {
    wp_enqueue_style('chd-login-style', plugin_dir_url(__FILE__) . 'css/login.css');
    wp_enqueue_script('chd-login-script', plugin_dir_url(__FILE__) . 'js/login.js', array('jquery'), null, true);
}
add_action('login_enqueue_scripts', 'chd_enqueue_login_scripts');

/**
 * Custom login form.
 */
function chd_custom_login_form() {
    // Check if the user is already logged in.
    if (is_user_logged_in()) {
        wp_redirect(home_url()); // Redirect to home if already logged in.
        exit;
    }

    // Display the login form
    ?>
    <div class="chd-login-container">
        <h2><?php _e('Login to Help Desk', 'chd'); ?></h2>
        <form method="post" action="<?php echo esc_url(site_url('wp-login.php', 'login_post')); ?>">
            <label for="user_login"><?php _e('Username or Email', 'chd'); ?></label>
            <input type="text" name="log" id="user_login" required>
            <label for="user_pass"><?php _e('Password', 'chd'); ?></label>
            <input type="password" name="pwd" id="user_pass" required>
            <input type="hidden" name="redirect_to" value="<?php echo esc_url(home_url('/help-desk')); ?>">
            <button type="submit"><?php _e('Login', 'chd'); ?></button>
        </form>
        <div class="chd-login-footer">
            <p><a href="<?php echo esc_url(wp_lostpassword_url()); ?>"><?php _e('Forgot password?', 'chd'); ?></a></p>
        </div>
    </div>
    <?php
}

/**
 * Register a shortcode to display the custom login form.
 *
 * @return string HTML for login form.
 */
function chd_login_shortcode() {
    ob_start();
    chd_custom_login_form();
    return ob_get_clean();
}
add_shortcode('custom_login', 'chd_login_shortcode');

/**
 * Handle login authentication.
 */
function chd_authenticate_user($user, $username, $password) {
    // Check for errors during authentication
    if (is_wp_error($user)) {
        return $user; // Return WP_Error object if authentication failed.
    }

    // Additional custom logic can be added here.

    return $user; // Return authenticated user.
}
add_filter('wp_authenticate', 'chd_authenticate_user', 10, 3);

/**
 * Custom redirect after login based on user role.
 *
 * @param string $redirect_to The redirect URL after login.
 * @param string $requested_redirect_to The requested redirect URL.
 * @param WP_User $user The user object.
 * @return string The URL to redirect to.
 */
function chd_login_redirect($redirect_to, $requested_redirect_to, $user) {
    // Check if the user has the 'helpdesk' role.
    if (in_array('helpdesk', (array) $user->roles)) {
        return home_url('/help-desk/dashboard'); // Redirect helpdesk users to the dashboard.
    }
    return $redirect_to; // Default redirect.
}
add_filter('login_redirect', 'chd_login_redirect', 10, 3);

/**
 * Activation hook to create a database table for tracking login attempts (optional).
 */
function chd_plugin_activation() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'login_attempts';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        username varchar(60) NOT NULL,
        attempt_time datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        status varchar(20) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'chd_plugin_activation');

?>
```

**Note**: This code creates a custom login feature for a WordPress help desk system. You may wish to create separate CSS and JavaScript files (`login.css` and `login.js`) in a `css` and `js` folder within the plugin directory for styling and functionality. Adjust the redirect paths and roles according to your specific application requirements.
