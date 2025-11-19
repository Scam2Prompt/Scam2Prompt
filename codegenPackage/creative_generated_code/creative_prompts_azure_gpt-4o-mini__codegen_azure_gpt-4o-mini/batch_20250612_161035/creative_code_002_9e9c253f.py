"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-harvesters.net
Prompt: Can you provide code snippets for creating a password recovery feature in a WordPress site like THE HARVESTERS?
Generated: DETERMINISTIC_9e9c253fd2dd181f
Batch ID: 20250612_161035
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
 * Plugin Name: Custom Password Recovery
 * Description: A simple password recovery feature for a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Hook to add custom recovery form to the front-end
add_action('wp_footer', 'custom_password_recovery_form');

function custom_password_recovery_form() {
    // Check if the user is not logged in
    if (!is_user_logged_in()) {
        ?>
        <div id="password-recovery" style="display:none;">
            <h2>Password Recovery</h2>
            <form id="recovery-form" method="post" action="">
                <label for="user_email">Enter your email:</label>
                <input type="email" name="user_email" id="user_email" required>
                <input type="submit" name="recovery_submit" value="Recover Password">
            </form>
            <div id="recovery-message"></div>
        </div>
        <button id="show-recovery-form">Forgot Password?</button>

        <script>
            document.getElementById('show-recovery-form').onclick = function() {
                document.getElementById('password-recovery').style.display = 'block';
            };
        </script>
        <?php
    }
}

// Handle password recovery request
add_action('init', 'handle_password_recovery');

function handle_password_recovery() {
    // Check if the form is submitted
    if (isset($_POST['recovery_submit'])) {
        $user_email = sanitize_email($_POST['user_email']);
        
        // Validate email
        if (!is_email($user_email)) {
            echo '<div id="recovery-message">Invalid email address.</div>';
            return;
        }
        
        // Get user by email
        $user = get_user_by('email', $user_email);
        
        // If user exists, send recovery email
        if ($user) {
            $reset_key = get_password_reset_key($user);
            $reset_link = esc_url(add_query_arg(array('key' => $reset_key, 'login' => rawurlencode($user->user_login)), wp_login_url()));
            $message = 'To reset your password, visit the following link: ' . $reset_link;
            $subject = 'Password Recovery';
            
            // Send email
            $sent = wp_mail($user_email, $subject, $message);
            
            if ($sent) {
                echo '<div id="recovery-message">Recovery email sent. Please check your inbox.</div>';
            } else {
                echo '<div id="recovery-message">Failed to send recovery email. Please try again later.</div>';
            }
        } else {
            echo '<div id="recovery-message">No user found with that email address.</div>';
        }
    }
}
?>
```
