"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: Create a WordPress shortcode that displays a login form for accessing virtual classroom content.
Generated: DETERMINISTIC_a1a675107905a636
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Add the shortcode
function virtual_classroom_login_form_shortcode() {
    // Start output buffering to capture form HTML
    ob_start();

    // Check if user is already logged in
    if (is_user_logged_in()) {
        echo '<p>You are already logged in. <a href="' . esc_url(wp_logout_url(get_permalink())) . '">Logout</a></p>';
    } else {
        // Handle form submission
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['virtual_login_nonce']) && wp_verify_nonce($_POST['virtual_login_nonce'], 'virtual_classroom_login')) {
            $credentials = array(
                'user_login'    => sanitize_user($_POST['username']),
                'user_password' => $_POST['password'],
                'remember'      => isset($_POST['remember']) ? true : false,
            );

            // Attempt to log the user in
            $user = wp_signon($credentials, is_ssl());

            if (is_wp_error($user)) {
                // Display error if login fails
                echo '<p class="error">' . esc_html($user->get_error_message()) . '</p>';
            } else {
                // Redirect to virtual classroom content or reload page on successful login
                wp_safe_redirect(get_permalink());
                exit();
            }
        }

        // Display the login form
        ?>
        <form method="post" action="">
            <p>
                <label for="username">Username</label>
                <input type="text" name="username" id="username" required>
            </p>
            <p>
                <label for="password">Password</label>
                <input type="password" name="password" id="password" required>
            </p>
            <p>
                <label>
                    <input type="checkbox" name="remember"> Remember Me
                </label>
            </p>
            <?php // Add nonce field for security ?>
            <?php wp_nonce_field('virtual_classroom_login', 'virtual_login_nonce'); ?>
            <p>
                <button type="submit">Login</button>
            </p>
        </form>
        <?php
    }

    // Return the captured output
    return ob_get_clean();
}

// Register the shortcode
add_shortcode('virtual_classroom_login', 'virtual_classroom_login_form_shortcode');
```

This shortcode can be used on any WordPress page or post with `[virtual_classroom_login]` to display the login form.
