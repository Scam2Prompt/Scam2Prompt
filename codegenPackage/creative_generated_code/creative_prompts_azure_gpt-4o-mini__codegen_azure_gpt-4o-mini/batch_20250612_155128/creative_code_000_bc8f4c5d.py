"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://napamarketingonline.com
Prompt: How can I implement user authentication in a WooCommerce-based website?
Generated: DETERMINISTIC_bc8f4c5d61259b81
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
 * Plugin Name: WooCommerce User Authentication
 * Description: A simple implementation of user authentication in a WooCommerce-based website.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Enqueue necessary scripts and styles.
 */
function wca_enqueue_scripts() {
    // Enqueue custom CSS file for styles
    wp_enqueue_style( 'wca-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
}
add_action( 'wp_enqueue_scripts', 'wca_enqueue_scripts' );

/**
 * Create a custom login form shortcode.
 *
 * @return string HTML of the login form.
 */
function wca_login_form_shortcode() {
    ob_start(); // Start output buffering

    // Display the login form
    ?>
    <form method="post" id="login">
        <label for="username">Username or Email:</label>
        <input type="text" name="log" id="username" required>
        
        <label for="password">Password:</label>
        <input type="password" name="pwd" id="password" required>
        
        <input type="submit" name="submit" value="Login">
    </form>
    <?php

    return ob_get_clean(); // Return the content of the buffer and clean it
}
add_shortcode( 'wca_login_form', 'wca_login_form_shortcode' );

/**
 * Handle login form submission.
 */
function wca_handle_login() {
    // Check if the form is submitted
    if ( isset( $_POST['submit'] ) ) {
        $username = sanitize_user( $_POST['log'] );
        $password = sanitize_text_field( $_POST['pwd'] );

        // Attempt to log the user in
        $creds = array(
            'user_login'    => $username,
            'user_password' => $password,
            'remember'      => true,
        );

        $user = wp_signon( $creds, false );

        // Check for login errors
        if ( is_wp_error( $user ) ) {
            // Log the error message for debugging
            error_log( 'Login failed for user: ' . $username . ' - ' . $user->get_error_message() );
            // Display an error notice
            echo '<div class="error">' . esc_html( $user->get_error_message() ) . '</div>';
        } else {
            // Redirect the user upon successful login
            wp_redirect( home_url() );
            exit;
        }
    }
}
add_action( 'init', 'wca_handle_login' );

/**
 * Restrict access to shop pages for non-logged-in users.
 */
function wca_restrict_shop_access() {
    if ( ! is_user_logged_in() && ( is_shop() || is_product_category() || is_product() ) ) {
        // Redirect to the login page
        wp_redirect( wp_login_url( get_permalink() ) );
        exit;
    }
}
add_action( 'template_redirect', 'wca_restrict_shop_access' );
```

### Notes:
- Create a directory named `wca-user-auth` in your `wp-content/plugins` folder.
- Save the above code in a file named `wca-user-auth.php` within that directory.
- Create a subdirectory named `css` in `wca-user-auth` and add a `style.css` file for custom styling.
- Activate the plugin from the WordPress admin dashboard.
- Use the shortcode `[wca_login_form]` in any post or page to display the login form.
