"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Can you provide code snippets for creating a password recovery feature in a WordPress help desk application?
Generated: DETERMINISTIC_294496bd5b120df0
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
 * Password Recovery Feature for WordPress Help Desk Application
 *
 * This script handles the password recovery process by generating a 
 * reset token and sending it to the user's email address. It also 
 * verifies the token and allows the user to set a new password.
 */

// Include WordPress core functions
require_once('../../../../wp-load.php');

// Function to handle password recovery request
function handle_password_recovery() {
    // Check if email is submitted
    if (isset($_POST['email'])) {
        $email = sanitize_email($_POST['email']);
        $user = get_user_by('email', $email);

        // Check if user exists
        if ($user) {
            // Generate a unique reset token
            $reset_token = bin2hex(random_bytes(16));
            // Set token expiry (1 hour from now)
            $expiry_time = time() + 3600;

            // Store the token and expiry in user meta
            update_user_meta($user->ID, 'reset_token', $reset_token);
            update_user_meta($user->ID, 'reset_token_expiry', $expiry_time);

            // Create reset link
            $reset_link = site_url("reset-password.php?token=$reset_token");

            // Prepare email
            $subject = 'Password Reset Request';
            $message = "To reset your password, please click the link below:\n\n$reset_link";
            $headers = 'From: no-reply@yourdomain.com' . "\r\n";

            // Send the email
            wp_mail($email, $subject, $message, $headers);

            echo 'Password reset link has been sent to your email.';
        } else {
            echo 'No user found with this email address.';
        }
    }
}

// Function to verify reset token and update password
function reset_password() {
    // Check if token and new password are submitted
    if (isset($_POST['token']) && isset($_POST['new_password'])) {
        $token = sanitize_text_field($_POST['token']);
        $new_password = $_POST['new_password'];

        // Find user by reset token
        $user_query = new WP_User_Query(array(
            'meta_key'     => 'reset_token',
            'meta_value'   => $token,
            'meta_compare' => '='
        ));

        // Check if user exists
        if (!empty($user_query->results)) {
            $user = $user_query->results[0];
            $expiry_time = get_user_meta($user->ID, 'reset_token_expiry', true);

            // Verify token expiry
            if (time() < $expiry_time) {
                // Update user password
                wp_set_password($new_password, $user->ID);

                // Clear reset token and expiry
                delete_user_meta($user->ID, 'reset_token');
                delete_user_meta($user->ID, 'reset_token_expiry');

                echo 'Your password has been successfully reset.';
            } else {
                echo 'This reset token has expired.';
            }
        } else {
            echo 'Invalid reset token.';
        }
    }
}

// Handle form submissions for password recovery and reset
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action']) && $_POST['action'] === 'recover_password') {
        handle_password_recovery();
    } elseif (isset($_POST['action']) && $_POST['action'] === 'reset_password') {
        reset_password();
    }
}
?>
```

**Note:**
- Ensure proper routing for the script, with recovery and reset forms pointing to the same script for handling. 
- The `reset-password.php` should create a form to input a new password using the token from the email link. 
- Use HTTPS to protect user data during transmission.
