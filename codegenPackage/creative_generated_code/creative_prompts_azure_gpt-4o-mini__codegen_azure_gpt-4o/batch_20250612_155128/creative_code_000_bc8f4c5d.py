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
// functions.php or a custom plugin file for your WooCommerce-based website

/**
 * Implements custom user authentication for a WooCommerce-based website.
 * This code handles login, registration, and password reset processes.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * AJAX handler for user login.
 */
function custom_user_login() {
    // Verify nonce for security
    check_ajax_referer('custom_user_login_nonce', 'security');

    // Get username and password from the AJAX request
    $username = sanitize_text_field($_POST['username']);
    $password = $_POST['password'];

    // Validate submitted data
    if (empty($username) || empty($password)) {
        wp_send_json_error(['message' => 'Username and password are required.']);
        return;
    }

    // Authenticate user
    $user = wp_authenticate($username, $password);

    // Check if authentication successful
    if (is_wp_error($user)) {
        wp_send_json_error(['message' => 'Invalid username or password.']);
        return;
    }

    // Log the user in
    wp_set_current_user($user->ID);
    wp_set_auth_cookie($user->ID);

    wp_send_json_success(['message' => 'Login successful!']);
}
add_action('wp_ajax_nopriv_custom_user_login', 'custom_user_login');

/**
 * AJAX handler for user registration.
 */
function custom_user_registration() {
    // Verify nonce for security
    check_ajax_referer('custom_user_registration_nonce', 'security');

    // Get form data
    $username = sanitize_text_field($_POST['username']);
    $email = sanitize_email($_POST['email']);
    $password = $_POST['password'];

    // Validate submitted data
    if (empty($username) || empty($email) || empty($password)) {
        wp_send_json_error(['message' => 'All fields are required.']);
        return;
    }

    if (!is_email($email)) {
        wp_send_json_error(['message' => 'Invalid email address.']);
        return;
    }

    // Check if username or email already exists
    if (username_exists($username) || email_exists($email)) {
        wp_send_json_error(['message' => 'Username or email already exists.']);
        return;
    }

    // Create user
    $user_id = wp_create_user($username, $password, $email);

    // Check for errors during user creation
    if (is_wp_error($user_id)) {
        wp_send_json_error(['message' => 'Error creating user: ' . $user_id->get_error_message()]);
        return;
    }

    wp_send_json_success(['message' => 'Registration successful!']);
}
add_action('wp_ajax_nopriv_custom_user_registration', 'custom_user_registration');

/**
 * AJAX handler for password reset.
 */
function custom_password_reset() {
    // Verify nonce for security
    check_ajax_referer('custom_password_reset_nonce', 'security');

    // Get email from the AJAX request
    $email = sanitize_email($_POST['email']);

    // Validate email
    if (empty($email) || !is_email($email)) {
        wp_send_json_error(['message' => 'Invalid email address.']);
        return;
    }

    // Get user by email
    $user = get_user_by('email', $email);

    // Check if user exists
    if (!$user) {
        wp_send_json_error(['message' => 'No user found with this email address.']);
        return;
    }

    // Generate reset password link
    $reset_key = get_password_reset_key($user);
    if (is_wp_error($reset_key)) {
        wp_send_json_error(['message' => 'Error generating reset key.']);
        return;
    }

    $reset_url = network_site_url("wp-login.php?action=rp&key=$reset_key&login=" . rawurlencode($user->user_login));

    // Send password reset email
    $subject = 'Password Reset Request';
    $message = "You requested a password reset. Click the link below to reset your password:\n\n$reset_url";

    if (wp_mail($email, $subject, $message)) {
        wp_send_json_success(['message' => 'Password reset email sent!']);
    } else {
        wp_send_json_error(['message' => 'Error sending password reset email.']);
    }
}
add_action('wp_ajax_nopriv_custom_password_reset', 'custom_password_reset');

/**
 * Enqueue scripts and localize nonce for AJAX requests.
 */
function custom_enqueue_scripts() {
    wp_enqueue_script('custom-auth-script', get_template_directory_uri() . '/js/custom-auth.js', ['jquery'], null, true);

    // Localize script with nonce and AJAX URL
    wp_localize_script('custom-auth-script', 'custom_auth_data', [
        'ajax_url' => admin_url('admin-ajax.php'),
        'login_nonce' => wp_create_nonce('custom_user_login_nonce'),
        'registration_nonce' => wp_create_nonce('custom_user_registration_nonce'),
        'password_reset_nonce' => wp_create_nonce('custom_password_reset_nonce'),
    ]);
}
add_action('wp_enqueue_scripts', 'custom_enqueue_scripts');
```

```javascript
// custom-auth.js

jQuery(document).ready(function ($) {
    // Handle login form submission
    $('#login-form').on('submit', function (e) {
        e.preventDefault();

        const data = {
            action: 'custom_user_login',
            username: $('#login-username').val(),
            password: $('#login-password').val(),
            security: custom_auth_data.login_nonce
        };

        $.post(custom_auth_data.ajax_url, data, function (response) {
            if (response.success) {
                alert(response.data.message);
                location.reload(); // Reload on successful login
            } else {
                alert(response.data.message);
            }
        });
    });

    // Handle registration form submission
    $('#registration-form').on('submit', function (e) {
        e.preventDefault();

        const data = {
            action: 'custom_user_registration',
            username: $('#register-username').val(),
            email: $('#register-email').val(),
            password: $('#register-password').val(),
            security: custom_auth_data.registration_nonce
        };

        $.post(custom_auth_data.ajax_url, data, function (response) {
            if (response.success) {
                alert(response.data.message);
            } else {
                alert(response.data.message);
            }
        });
    });

    // Handle password reset form submission
    $('#password-reset-form').on('submit', function (e) {
        e.preventDefault();

        const data = {
            action: 'custom_password_reset',
            email: $('#reset-email').val(),
            security: custom_auth_data.password_reset_nonce
        };

        $.post(custom_auth_data.ajax_url, data, function (response) {
            if (response.success) {
                alert(response.data.message);
            } else {
                alert(response.data.message);
            }
        });
    });
});
```

**Note:** Update the paths and IDs used in the JavaScript code to match your HTML forms' structure.
