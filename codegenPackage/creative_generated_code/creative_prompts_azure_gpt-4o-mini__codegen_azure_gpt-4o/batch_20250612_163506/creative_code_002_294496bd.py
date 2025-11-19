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
 * Password Recovery Feature for a WordPress Help Desk Application
 * 
 * This script includes functionality to generate a password recovery link,
 * send it via email, and handle password reset requests securely.
 * 
 * Author: [Your Name]
 * Date: [Current Date]
 */

/** 
 * Hook to handle password recovery email request 
 */
add_action('init', 'handle_password_recovery_request');

/**
 * Process the password recovery request
 */
function handle_password_recovery_request() {
    if (isset($_POST['email']) && isset($_POST['action']) && $_POST['action'] === 'password_recovery') {
        $email = sanitize_email($_POST['email']);

        if (!is_email($email) || !email_exists($email)) {
            // Handle invalid or non-existent email
            wp_die('Invalid email address or user does not exist.');
        }

        $user = get_user_by('email', $email);

        // Generate secure token
        $token = wp_generate_password(24, false, false);
        update_user_meta($user->ID, 'password_reset_token', $token);

        // Create password reset link
        $reset_link = add_query_arg([
            'action' => 'password_reset',
            'token' => $token,
            'user_id' => $user->ID,
        ], site_url());

        // Send recovery email
        wp_mail(
            $email, 
            'Password Recovery Request', 
            "Click the following link to reset your password: $reset_link", 
            ['Content-Type: text/html; charset=UTF-8']
        );

        wp_die('Password recovery email sent successfully.');
    }
}

/**
 * Hook to handle password reset form submission
 */
add_action('init', 'handle_password_reset_request');

/**
 * Process the password reset request
 */
function handle_password_reset_request() {
    if (isset($_POST['action']) && $_POST['action'] === 'reset_password') {
        $user_id = intval($_POST['user_id']);
        $token = sanitize_text_field($_POST['token']);
        $new_password = sanitize_text_field($_POST['new_password']);

        // Validate inputs
        if (empty($user_id) || empty($token) || empty($new_password)) {
            wp_die('Missing required fields.');
        }

        $stored_token = get_user_meta($user_id, 'password_reset_token', true);

        if ($stored_token !== $token) {
            wp_die('Invalid or expired password reset token.');
        }

        // Update user password
        wp_set_password($new_password, $user_id);

        // Remove token after successful reset
        delete_user_meta($user_id, 'password_reset_token');

        wp_die('Your password has been reset successfully.');
    }
}

/**
 * Render password recovery form
 */
function render_password_recovery_form() {
    ?>
    <form method="POST" action="">
        <input type="hidden" name="action" value="password_recovery">
        <label for="email">Enter your email:</label>
        <input type="email" name="email" required>
        <button type="submit">Send Recovery Email</button>
    </form>
    <?php
}

/**
 * Render password reset form
 */
function render_password_reset_form() {
    if (isset($_GET['action'], $_GET['token'], $_GET['user_id']) && $_GET['action'] === 'password_reset') {
        ?>
        <form method="POST" action="">
            <input type="hidden" name="action" value="reset_password">
            <input type="hidden" name="user_id" value="<?php echo intval($_GET['user_id']); ?>">
            <input type="hidden" name="token" value="<?php echo sanitize_text_field($_GET['token']); ?>">
            <label for="new_password">Enter new password:</label>
            <input type="password" name="new_password" required>
            <button type="submit">Reset Password</button>
        </form>
        <?php
    } else {
        wp_die('Invalid password reset link.');
    }
}

/**
 * Shortcodes for rendering forms
 */
add_shortcode('password_recovery_form', 'render_password_recovery_form');
add_shortcode('password_reset_form', 'render_password_reset_form');
```

This code creates a password recovery feature for a WordPress help desk application. Use the `[password_recovery_form]` shortcode to display the email recovery form and `[password_reset_form]` to display the password reset form.
