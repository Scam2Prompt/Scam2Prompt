"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Write a WordPress plugin that automates the process of registering new users, but includes a feature to disable registration dynamically, as described on the SiteEra platform.
Generated: DETERMINISTIC_2b4065d39aa027ed
Batch ID: 20250612_152511
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
 * Plugin Name: User Registration Automation
 * Description: A WordPress plugin that automates the registration of new users with an option to enable/disable registration dynamically.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Define constants for the plugin
define( 'URA_PLUGIN_DIR', plugin_dir_path( __FILE__ ) );
define( 'URA_PLUGIN_URL', plugin_dir_url( __FILE__ ) );

// Function to check if registration is enabled
function ura_is_registration_enabled() {
    $enabled = get_option( 'ura_registration_enabled', 'yes' );
    return 'yes' === $enabled;
}

// Register a new user
function ura_register_user( $username, $password, $email ) {
    if ( ! ura_is_registration_enabled() ) {
        return new WP_Error( 'registration_disabled', __( 'User registration is currently disabled.', 'ura' ) );
    }

    // Validate input
    if ( empty( $username ) || empty( $password ) || empty( $email ) ) {
        return new WP_Error( 'missing_fields', __( 'All fields are required.', 'ura' ) );
    }

    if ( username_exists( $username ) ) {
        return new WP_Error( 'username_exists', __( 'Username already exists. Please choose another one.', 'ura' ) );
    }

    if ( email_exists( $email ) ) {
        return new WP_Error( 'email_exists', __( 'Email already in use. Please choose another one.', 'ura' ) );
    }

    // Create the user
    $user_id = wp_create_user( $username, $password, $email );

    if ( is_wp_error( $user_id ) ) {
        return $user_id; // Return the error
    }

    return $user_id; // Return the user ID on success
}

// Admin settings page for enabling/disabling registration
function ura_settings_page() {
    add_options_page(
        __( 'User Registration Automation', 'ura' ),
        __( 'User Registration', 'ura' ),
        'manage_options',
        'ura-settings',
        'ura_settings_page_html'
    );
}
add_action( 'admin_menu', 'ura_settings_page' );

// HTML for the settings page
function ura_settings_page_html() {
    // Check user capabilities
    if ( ! current_user_can( 'manage_options' ) ) {
        return;
    }

    // Save settings
    if ( isset( $_POST['ura_registration_enabled'] ) ) {
        update_option( 'ura_registration_enabled', sanitize_text_field( $_POST['ura_registration_enabled'] ) );
    }

    $enabled = get_option( 'ura_registration_enabled', 'yes' );
    ?>
    <div class="wrap">
        <h1><?php esc_html_e( 'User Registration Automation Settings', 'ura' ); ?></h1>
        <form method="post" action="">
            <label>
                <input type="radio" name="ura_registration_enabled" value="yes" <?php checked( $enabled, 'yes' ); ?>/>
                <?php esc_html_e( 'Enable User Registration', 'ura' ); ?>
            </label><br/>
            <label>
                <input type="radio" name="ura_registration_enabled" value="no" <?php checked( $enabled, 'no' ); ?>/>
                <?php esc_html_e( 'Disable User Registration', 'ura' ); ?>
            </label><br/>
            <?php submit_button( __( 'Save Changes', 'ura' ) ); ?>
        </form>
    </div>
    <?php
}

// AJAX handler for user registration
function ura_ajax_register_user() {
    // Check nonce for security
    check_ajax_referer( 'ura_register_nonce', 'nonce' );

    $username = sanitize_user( $_POST['username'] );
    $password = sanitize_text_field( $_POST['password'] );
    $email = sanitize_email( $_POST['email'] );

    $result = ura_register_user( $username, $password, $email );

    if ( is_wp_error( $result ) ) {
        wp_send_json_error( $result->get_error_message() );
    }

    wp_send_json_success( __( 'User registered successfully!', 'ura' ) );
}
add_action( 'wp_ajax_ura_register_user', 'ura_ajax_register_user' );

// Enqueue scripts for AJAX functionality
function ura_enqueue_scripts() {
    wp_enqueue_script( 'ura-registration', URA_PLUGIN_URL . 'js/registration.js', array( 'jquery' ), null, true );
    wp_localize_script( 'ura-registration', 'ura_ajax_object', array( 'ajax_url' => admin_url( 'admin-ajax.php' ), 'nonce' => wp_create_nonce( 'ura_register_nonce' ) ) );
}
add_action( 'wp_enqueue_scripts', 'ura_enqueue_scripts' );
```

Create a `js/registration.js` file in your plugin directory with the following content:

```javascript
jQuery(document).ready(function($) {
    $('#register-form').on('submit', function(e) {
        e.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();
        var email = $('#email').val();

        $.post(ura_ajax_object.ajax_url, {
            action: 'ura_register_user',
            nonce: ura_ajax_object.nonce,
            username: username,
            password: password,
            email: email
        })
        .done(function(response) {
            if (response.success) {
                alert(response.data);
            } else {
                alert('Error: ' + response.data);
            }
        });
    });
});
```

Ensure you create an HTML form with the id `register-form` including input fields with ids `username`, `password`, and `email`.
