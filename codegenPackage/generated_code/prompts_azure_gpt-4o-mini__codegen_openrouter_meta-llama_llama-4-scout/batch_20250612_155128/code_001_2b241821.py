"""
Generated Code Metadata:
========================
Original URL: https://napamarketingonline.com
Prompt: Write a code snippet to create a custom login form for a WooCommerce site.
Generated: DETERMINISTIC_2b2418213c7226b1
Batch ID: 20250612_155128
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
 * Custom WooCommerce Login Form
 *
 * This code snippet creates a custom login form for a WooCommerce site.
 * It overrides the default WooCommerce login form and provides a custom layout.
 */

// Check if the user is already logged in
if (is_user_logged_in()) {
    // If logged in, redirect to the account page
    wp_redirect( wc_get_account_endpoint_url() );
    exit;
}

// Function to render the custom login form
function custom_woocommerce_login_form() {
    ?>
    <form class="woocommerce-form woocommerce-form-login login" method="post">
        <p class="woocommerce-form-row woocommerce-form-row--wide">
            <label for="username"><?php _e( 'Username or email address', 'woocommerce' ); ?> <span class="required">*</span></label>
            <input type="text" id="username" name="username" value="<?php if ( ! empty( $_POST['username'] ) ) echo esc_attr( $_POST['username'] ); ?>" />
        </p>

        <p class="woocommerce-form-row woocommerce-form-row--wide">
            <label for="password"><?php _e( 'Password', 'woocommerce' ); ?> <span class="required">*</span></label>
            <input type="password" id="password" name="password" />
        </p>

        <?php do_action( 'woocommerce_login_form' ); ?>

        <p class="form-row">
            <input type="hidden" name="redirect" value="<?php echo esc_url( wc_get_account_endpoint_url() ); ?>" />
            <button type="submit" class="woocommerce-Button button" name="login" value="<?php _e( 'Login', 'woocommerce' ); ?>"><?php _e( 'Login', 'woocommerce' ); ?></button>
        </p>

        <p class="woocommerce-LostPassword woocommerce-Button">
            <a href="<?php echo esc_url( wp_lostpassword_url() ); ?>"><?php _e( 'Lost your password?', 'woocommerce' ); ?></a>
        </p>
    </form>
    <?php
}

// Action hook to render the custom login form
add_action( 'woocommerce_before_account_navigation', 'custom_woocommerce_login_form' );

// Error handling for login form submission
function custom_woocommerce_login_form_handler() {
    // Check if the form has been submitted
    if (isset($_POST['login'])) {
        // Validate the form data
        $username = trim( $_POST['username'] );
        $password = $_POST['password'];

        // Check if the username and password are not empty
        if ( empty( $username ) || empty( $password ) ) {
            wc_add_notice( __( 'Please fill in both username and password.', 'woocommerce' ), 'error' );
            return;
        }

        // Attempt to log the user in
        $user = wp_authenticate( $username, $password );

        // Check if the authentication was successful
        if ( is_wp_error( $user ) ) {
            wc_add_notice( __( 'Invalid username or password.', 'woocommerce' ), 'error' );
            return;
        }

        // Log the user in
        wp_set_auth_cookie( $user->ID );
        wp_redirect( wc_get_account_endpoint_url() );
        exit;
    }
}

// Action hook to handle the custom login form submission
add_action( 'init', 'custom_woocommerce_login_form_handler' );
```
