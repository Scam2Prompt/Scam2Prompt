"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-harvesters.net
Prompt: How can I implement a custom login form for a WordPress site similar to THE HARVESTERS?
Generated: DETERMINISTIC_efe257e5551d3ac0
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
 * Custom Login Form for WordPress
 *
 * This code creates a custom login form that can be embedded in a WordPress page.
 * It also handles user authentication and redirects upon successful login.
 */

// Shortcode to display the custom login form
function custom_login_form_shortcode() {
    // Check if the user is already logged in
    if (is_user_logged_in()) {
        return '<p>You are already logged in. <a href="' . wp_logout_url() . '">Log out</a></p>';
    }

    // Start output buffering
    ob_start();
    ?>
    <form action="<?php echo esc_url($_SERVER['REQUEST_URI']); ?>" method="post">
        <p>
            <label for="username">Username or Email Address<br />
            <input type="text" name="username" required /></label>
        </p>
        <p>
            <label for="password">Password<br />
            <input type="password" name="password" required /></label>
        </p>
        <p>
            <input type="submit" name="submit" value="Login" />
        </p>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('custom_login_form', 'custom_login_form_shortcode');

// Handle the form submission
function handle_login_form_submission() {
    if (isset($_POST['submit'])) {
        // Sanitize and validate input
        $username = sanitize_text_field($_POST['username']);
        $password = $_POST['password']; // Password does not need sanitization

        // Authenticate the user
        $user = wp_authenticate($username, $password);

        // Check for authentication errors
        if (is_wp_error($user)) {
            // Display error message if authentication fails
            echo '<p class="error">Invalid username or password.</p>';
        } else {
            // Clear any previous authentication cookies
            wp_clear_auth_cookie();
            // Log the user in
            wp_set_current_user($user->ID);
            wp_set_auth_cookie($user->ID);

            // Redirect to the home page or desired location after successful login
            wp_redirect(home_url());
            exit;
        }
    }
}
add_action('init', 'handle_login_form_submission');

// Enqueue custom styles for the login form (optional)
function custom_login_form_styles() {
    echo '<style>
        .error {
            color: red;
        }
        form {
            width: 300px;
            margin: 0 auto;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
        }
        input[type="submit"] {
            background-color: #0073aa;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #005177;
        }
    </style>';
}
add_action('wp_head', 'custom_login_form_styles');
?>
```

### Notes:
- To use this code, place it in your theme's `functions.php` file or in a custom plugin.
- Use the shortcode `[custom_login_form]` to display the login form on any page or post.
- Adjust the redirect URL in `wp_redirect(home_url());` if you want to redirect to a different page after login.
