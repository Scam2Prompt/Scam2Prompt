"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Write a WordPress plugin to create a custom login page for a help desk system, including fields for username, email address, password, and a "Remember Me" checkbox.
Generated: DETERMINISTIC_d6f5a21d5aac1a5e
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
/*
Plugin Name: Custom Help Desk Login
Description: A custom login page for a help desk system with fields for username, email, password, and a "Remember Me" checkbox.
Version: 1.0
Author: Your Name
*/

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Enqueue styles and scripts for the custom login page
function chdl_enqueue_styles() {
    if ( is_page( 'custom-login' ) ) {
        wp_enqueue_style( 'chdl-styles', plugin_dir_url( __FILE__ ) . 'css/custom-login.css' );
    }
}
add_action( 'wp_enqueue_scripts', 'chdl_enqueue_styles' );

// Create the custom login page shortcode
function chdl_custom_login_page() {
    ob_start(); ?>

    <div class="chdl-login-form">
        <h2><?php _e( 'Help Desk Login', 'chdl-text-domain' ); ?></h2>
        <form method="post" action="<?php echo esc_url( site_url( 'wp-login.php', 'login_post' ) ); ?>">
            <p>
                <label for="username"><?php _e( 'Username', 'chdl-text-domain' ); ?></label>
                <input type="text" name="log" id="username" required>
            </p>
            <p>
                <label for="email"><?php _e( 'Email', 'chdl-text-domain' ); ?></label>
                <input type="email" name="email" id="email" required>
            </p>
            <p>
                <label for="password"><?php _e( 'Password', 'chdl-text-domain' ); ?></label>
                <input type="password" name="pwd" id="password" required>
            </p>
            <p>
                <input type="checkbox" name="rememberme" id="rememberme" value="forever">
                <label for="rememberme"><?php _e( 'Remember Me', 'chdl-text-domain' ); ?></label>
            </p>
            <p>
                <input type="submit" value="<?php _e( 'Login', 'chdl-text-domain' ); ?>">
            </p>
        </form>
    </div>

    <?php
    return ob_get_clean();
}
add_shortcode( 'custom_login', 'chdl_custom_login_page' );

// Handle the login process
function chdl_login_user() {
    if ( isset( $_POST['log'] ) && isset( $_POST['pwd'] ) ) {
        $username = sanitize_user( $_POST['log'] );
        $password = sanitize_text_field( $_POST['pwd'] );
        $email = sanitize_email( $_POST['email'] );

        // Attempt to log the user in
        $creds = array(
            'user_login'    => $username,
            'user_password' => $password,
            'remember'      => isset( $_POST['rememberme'] )
        );

        $user = wp_signon( $creds, false );

        // Check for errors
        if ( is_wp_error( $user ) ) {
            echo '<div class="chdl-error">' . $user->get_error_message() . '</div>';
        } else {
            // Redirect to the dashboard (or any desired location)
            wp_redirect( admin_url() );
            exit;
        }
    }
}
add_action( 'init', 'chdl_login_user' );

// Create the custom login page
function chdl_create_login_page() {
    $new_page_title = 'Custom Login';
    $new_page_content = '[custom_login]';
    $new_page_template = ''; // Use default template

    // Check if page already exists
    $page_check = get_page_by_path( 'custom-login' );
    if ( ! isset( $page_check->ID ) ) {
        // Create the page
        $new_page_id = wp_insert_post( array(
            'post_title'   => $new_page_title,
            'post_content' => $new_page_content,
            'post_status'  => 'publish',
            'post_type'    => 'page',
            'post_author'  => 1,
            'post_slug'    => sanitize_title( $new_page_title )
        ) );
    }
}
register_activation_hook( __FILE__, 'chdl_create_login_page' );
```
