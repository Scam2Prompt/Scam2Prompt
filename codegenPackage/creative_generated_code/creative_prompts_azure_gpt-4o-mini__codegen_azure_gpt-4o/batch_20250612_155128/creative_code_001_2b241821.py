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
 *
 * Adds a custom login form to a WooCommerce site.
 * Place this snippet in the functions.php file of your active theme.
 */

// Shortcode to display the custom login form
function custom_woocommerce_login_form() {
    // Check if the user is already logged in
    if (is_user_logged_in()) {
        return '<p>You are already logged in.</p>';
    }

    ob_start();

    // Display error message if login failed
    if (isset($_GET['login']) && $_GET['login'] === 'failed') {
        echo '<div class="woocommerce-error">Invalid username or password.</div>';
    }

    // Display the login form
    ?>
    <form method="post" class="woocommerce-form woocommerce-form-login login" action="<?php echo esc_url(wp_login_url()); ?>">
        <p class="woocommerce-form-row woocommerce-form-row--wide form-row form-row-wide">
            <label for="username">Username or Email&nbsp;<span class="required">*</span></label>
            <input type="text" class="woocommerce-Input woocommerce-Input--text input-text" name="log" id="username" autocomplete="username" value="" required />
        </p>
        <p class="woocommerce-form-row woocommerce-form-row--wide form-row form-row-wide">
            <label for="password">Password&nbsp;<span class="required">*</span></label>
            <input type="password" class="woocommerce-Input woocommerce-Input--text input-text" name="pwd" id="password" autocomplete="current-password" required />
        </p>

        <p class="form-row">
            <input type="hidden" name="redirect_to" value="<?php echo esc_url(home_url('/my-account')); ?>" />
            <button type="submit" class="woocommerce-button button woocommerce-form-login__submit" name="login" value="<?php esc_attr_e('Log in', 'woocommerce'); ?>"><?php esc_html_e('Log in', 'woocommerce'); ?></button>
        </p>

        <p class="woocommerce-LostPassword lost_password">
            <a href="<?php echo esc_url(wp_lostpassword_url()); ?>"><?php esc_html_e('Lost your password?', 'woocommerce'); ?></a>
        </p>
    </form>
    <?php

    return ob_get_clean();
}

// Register the shortcode
add_shortcode('custom_login_form', 'custom_woocommerce_login_form');
```

This code can be used via the `[custom_login_form]` shortcode in WordPress to display a custom login form on a WooCommerce site.
