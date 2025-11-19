"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://napamarketingonline.com
Prompt: Write a code snippet to create a custom login form for a WooCommerce site.
Generated: DETERMINISTIC_2b2418213c7226b1
Batch ID: 20250612_155128
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
 * Custom Login Form for WooCommerce
 * This code snippet creates a custom login form that can be placed in a WooCommerce site.
 */

// Add shortcode to display login form
add_shortcode('custom_login_form', 'render_custom_login_form');

function render_custom_login_form() {
    // Check if user is already logged in
    if (is_user_logged_in()) {
        return '<p>You are already logged in.</p>';
    }

    // Start output buffering
    ob_start();
    ?>

    <div class="custom-login-form">
        <h2><?php esc_html_e('Login', 'woocommerce'); ?></h2>
        <form method="post" class="woocommerce-form woocommerce-form-login login">
            <p class="form-row form-row-wide">
                <label for="username"><?php esc_html_e('Username or email address', 'woocommerce'); ?> <span class="required">*</span></label>
                <input type="text" class="input-text" name="username" id="username" required />
            </p>
            <p class="form-row form-row-wide">
                <label for="password"><?php esc_html_e('Password', 'woocommerce'); ?> <span class="required">*</span></label>
                <input class="input-text" type="password" name="password" id="password" required />
            </p>
            <p class="form-row">
                <input type="hidden" name="login_nonce" value="<?php echo wp_create_nonce('custom_login_nonce'); ?>" />
                <button type="submit" class="button woocommerce-button woocommerce-form-login__submit" name="login"><?php esc_html_e('Login', 'woocommerce'); ?></button>
            </p>
        </form>
        
        <?php
        // Handle form submission
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
            // Validate nonce
            if (!isset($_POST['login_nonce']) || !wp_verify_nonce($_POST['login_nonce'], 'custom_login_nonce')) {
                echo '<p class="error">' . esc_html__('Nonce verification failed. Please retry.', 'woocommerce') . '</p>';
            } else {
                $creds = array();
                $creds['user_login'] = sanitize_text_field($_POST['username']);
                $creds['user_password'] = sanitize_text_field($_POST['password']);
                $creds['remember'] = true;

                // Attempt to login
                $user = wp_signon($creds, false);

                // Check for errors
                if (is_wp_error($user)) {
                    echo '<p class="error">' . esc_html($user->get_error_message()) . '</p>';
                } else {
                    // Redirect to the previous page or to a specific page
                    wp_redirect(home_url());
                    exit;
                }
            }
        }
        ?>
    </div>

    <?php
    // Return the buffered output
    return ob_get_clean();
}
?>

```
