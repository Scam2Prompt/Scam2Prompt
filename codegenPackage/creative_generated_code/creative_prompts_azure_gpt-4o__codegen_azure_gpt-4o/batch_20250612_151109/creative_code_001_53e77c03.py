"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Generate PHP code to integrate a "Lost your password?" functionality into a WordPress-based help desk login page.
Generated: DETERMINISTIC_53e77c038405be82
Batch ID: 20250612_151109
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
 * Plugin Name: Custom Lost Password Integration for Help Desk
 * Description: Adds "Lost your password?" functionality to a custom help desk login page in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Ensure no direct script access for security
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Shortcode to display a custom "Lost Password" form.
 */
function custom_lost_password_form() {
    // Check if the user is already logged in
    if (is_user_logged_in()) {
        return '<p>You are already logged in.</p>';
    }

    // Handle form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['user_login'])) {
        $user_login = sanitize_text_field($_POST['user_login']);
        
        // Check if a username or email was provided
        if (empty($user_login)) {
            $error = 'Please enter your username or email address.';
        } else {
            $user = get_user_by('email', $user_login) ?: get_user_by('login', $user_login);

            if (!$user) {
                $error = 'No user found with that username or email address.';
            } else {
                // Generate password reset key
                $reset_key = get_password_reset_key($user);

                if (is_wp_error($reset_key)) {
                    $error = 'Failed to generate password reset request.';
                } else {
                    // Generate reset link
                    $reset_url = network_site_url("wp-login.php?action=rp&key=$reset_key&login=" . rawurlencode($user->user_login));

                    // Send the reset email
                    $email_sent = wp_mail(
                        $user->user_email,
                        'Password Reset Request',
                        "Click the following link to reset your password:\n\n" . $reset_url
                    );

                    if (!$email_sent) {
                        $error = 'Failed to send the password reset email.';
                    } else {
                        $success = 'A password reset link has been sent to your email address.';
                    }
                }
            }
        }
    }

    // Display the form with error/success messages
    ob_start();
    ?>
    <form method="post" action="">
        <p>Enter your username or email address, and we will send you a link to reset your password.</p>
        
        <?php if (!empty($error)): ?>
            <div style="color: red;"><?php echo esc_html($error); ?></div>
        <?php endif; ?>

        <?php if (!empty($success)): ?>
            <div style="color: green;"><?php echo esc_html($success); ?></div>
        <?php else: ?>
            <p>
                <label for="user_login">Username or Email Address:</label><br>
                <input type="text" name="user_login" id="user_login" required>
            </p>
            <p>
                <input type="submit" value="Reset Password">
            </p>
        <?php endif; ?>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('custom_lost_password', 'custom_lost_password_form');

/**
 * Redirect users to the custom "Lost Password" page instead of default WordPress page.
 */
function custom_lost_password_redirect() {
    if (isset($_GET['action']) && $_GET['action'] === 'lostpassword') {
        wp_redirect(home_url('/custom-lost-password/')); // Change this to the actual page URL
        exit;
    }
}
add_action('login_form_lostpassword', 'custom_lost_password_redirect');

/**
 * Disable the default password reset email sent by WordPress.
 */
function disable_default_password_reset_email($email, $user, $reset_key, $reset_url) {
    return false; // Prevent the default email from being sent
}
add_filter('retrieve_password_message', 'disable_default_password_reset_email', 10, 4);

/**
 * Create a custom page for the "Lost Password" functionality.
 */
function custom_lost_password_page() {
    $page_title = 'Lost Password';
    $page_slug = 'custom-lost-password';

    // Check if the page already exists
    $existing_page = get_page_by_path($page_slug);
    if (!$existing_page) {
        wp_insert_post(array(
            'post_title' => $page_title,
            'post_name' => $page_slug,
            'post_content' => '[custom_lost_password]', // Use the shortcode
            'post_status' => 'publish',
            'post_type' => 'page',
        ));
    }
}
register_activation_hook(__FILE__, 'custom_lost_password_page');
```
