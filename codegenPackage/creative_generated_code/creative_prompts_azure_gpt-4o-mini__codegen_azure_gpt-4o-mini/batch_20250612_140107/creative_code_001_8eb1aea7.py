"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interline-asia.com
Prompt: Write a PHP code snippet to customize the welcome message on a WordPress blog.
Generated: DETERMINISTIC_8eb1aea7d2016c97
Batch ID: 20250612_140107
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
 * Custom Welcome Message for WordPress
 *
 * This code snippet allows you to customize the welcome message 
 * displayed on your WordPress blog based on the user's role.
 *
 * Place this code in your theme's functions.php file or in a custom plugin.
 */

// Hook into the 'wp_head' action to add a custom welcome message
add_action('wp_head', 'custom_welcome_message');

function custom_welcome_message() {
    // Check if the user is logged in
    if (is_user_logged_in()) {
        // Get the current user's data
        $current_user = wp_get_current_user();
        
        // Check if user has a valid role
        if (isset($current_user->roles) && !empty($current_user->roles)) {
            // Get the first role of the user
            $user_role = $current_user->roles[0];

            // Define a custom welcome message based on user role
            switch ($user_role) {
                case 'administrator':
                    $message = 'Welcome back, Admin ' . esc_html($current_user->display_name) . '!';
                    break;
                case 'editor':
                    $message = 'Welcome back, Editor ' . esc_html($current_user->display_name) . '!';
                    break;
                case 'author':
                    $message = 'Welcome back, Author ' . esc_html($current_user->display_name) . '!';
                    break;
                case 'contributor':
                    $message = 'Welcome back, Contributor ' . esc_html($current_user->display_name) . '!';
                    break;
                case 'subscriber':
                    $message = 'Welcome back, valued Subscriber ' . esc_html($current_user->display_name) . '!';
                    break;
                default:
                    $message = 'Welcome back, ' . esc_html($current_user->display_name) . '!';
            }
        } else {
            // Fallback message if user roles are not set
            $message = 'Welcome back, ' . esc_html($current_user->display_name) . '!';
        }

        // Output the welcome message
        echo '<div class="welcome-message">' . $message . '</div>';
    } else {
        // Message for non-logged in users
        echo '<div class="welcome-message">Welcome to our blog! Please log in to access your account.</div>';
    }
}
?>
```
