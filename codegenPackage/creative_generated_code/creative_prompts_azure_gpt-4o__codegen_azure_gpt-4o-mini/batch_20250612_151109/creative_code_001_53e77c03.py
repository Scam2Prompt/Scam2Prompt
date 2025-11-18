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
 * Custom Lost Password functionality for WordPress Help Desk Login Page
 *
 * This code integrates a "Lost your password?" feature into a WordPress
 * help desk login page. It handles user input, validates it, and sends
 * a password reset link to the user's email address if the email is
 * associated with an account.
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Function to display the lost password form
function display_lost_password_form() {
    ?>
    <div class="lost-password-form">
        <h2><?php esc_html_e( 'Lost Your Password?', 'text-domain' ); ?></h2>
        <form method="post" action="">
            <label for="user_login"><?php esc_html_e( 'Email Address', 'text-domain' ); ?></label>
            <input type="email" name="user_login" id="user_login" required>
            <button type="submit" name="submit_lost_password"><?php esc_html_e( 'Get New Password', 'text-domain' ); ?></button>
        </form>
    </div>
    <?php
}

// Function to handle password reset request
function handle_lost_password_request() {
    if ( isset( $_POST['submit_lost_password'] ) && ! empty( $_POST['user_login'] ) ) {
        $user_login = sanitize_email( $_POST['user_login'] );

        // Validate email format
        if ( ! is_email( $user_login ) ) {
            echo '<div class="error">' . esc_html__( 'Invalid email address.', 'text-domain' ) . '</div>';
            return;
        }

        // Retrieve user by email
        $user = get_user_by( 'email', $user_login );

        // Check if user exists
        if ( ! $user ) {
            echo '<div class="error">' . esc_html__( 'No user found with that email address.', 'text-domain' ) . '</div>';
            return;
        }

        // Generate password reset key
        $reset_key = get_password_reset_key( $user );

        // Set up the reset password link
        $reset_link = add_query_arg( [
            'key' => $reset_key,
            'login' => rawurlencode( $user->user_login ),
        ], wp_login_url( 'resetpass' ) );

        // Prepare email
        $subject = __( 'Password Reset Request', 'text-domain' );
        $message = sprintf( __( 'Hello, %s. To reset your password, click the link below:' ), $user->display_name ) . "\r\n\r\n";
        $message .= $reset_link;

        // Send password reset email
        if ( wp_mail( $user_login, $subject, $message ) ) {
            echo '<div class="success">' . esc_html__( 'Check your email for the password reset link.', 'text-domain' ) . '</div>';
        } else {
            echo '<div class="error">' . esc_html__( 'Failed to send password reset email. Please try again later.', 'text-domain' ) . '</div>';
        }
    }
}

// Hook to display the lost password form and handle the request
function lost_password_page() {
    handle_lost_password_request();
    display_lost_password_form();
}

// Shortcode to display the lost password functionality
add_shortcode( 'lost_password', 'lost_password_page' );

// Example usage: [lost_password]
?>
```
