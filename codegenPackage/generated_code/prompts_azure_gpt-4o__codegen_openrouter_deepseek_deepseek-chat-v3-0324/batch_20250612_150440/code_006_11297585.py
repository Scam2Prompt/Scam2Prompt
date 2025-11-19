"""
Generated Code Metadata:
========================
Original URL: https://sajumavi.edu.pe
Prompt: Provide code to customize the WordPress login page for a virtual classroom, including branding and additional fields.
Generated: DETERMINISTIC_11297585222ef58b
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Virtual Classroom Login Customization
 * 
 * This code customizes the WordPress login page for a virtual classroom,
 * including branding and additional fields.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Enqueue custom styles for the login page
 */
function vc_custom_login_styles() {
    wp_enqueue_style(
        'vc-custom-login', 
        get_stylesheet_directory_uri() . '/css/vc-login.css', 
        array(), 
        '1.0'
    );
}
add_action('login_enqueue_scripts', 'vc_custom_login_styles');

/**
 * Change login logo URL to site homepage
 */
function vc_login_logo_url() {
    return home_url();
}
add_filter('login_headerurl', 'vc_login_logo_url');

/**
 * Change login logo title to site name
 */
function vc_login_logo_url_title() {
    return get_bloginfo('name');
}
add_filter('login_headertext', 'vc_login_logo_url_title');

/**
 * Add custom fields to login form
 */
function vc_add_login_fields() {
    ?>
    <p class="vc-custom-field">
        <label for="vc_class_code">Class Code<br>
        <input type="text" name="vc_class_code" id="vc_class_code" class="input" value="" size="20" required></label>
    </p>
    <?php
}
add_action('login_form', 'vc_add_login_fields');

/**
 * Validate custom login fields
 */
function vc_validate_login_fields($user, $password) {
    if (empty($_POST['vc_class_code'])) {
        $user = new WP_Error(
            'empty_class_code', 
            __('<strong>ERROR</strong>: Class code is required.', 'virtual-classroom')
        );
    } elseif ($_POST['vc_class_code'] !== 'VC2023') { // Example validation
        $user = new WP_Error(
            'invalid_class_code', 
            __('<strong>ERROR</strong>: Invalid class code.', 'virtual-classroom')
        );
    }
    return $user;
}
add_filter('authenticate', 'vc_validate_login_fields', 30, 2);

/**
 * Add custom message above login form
 */
function vc_login_message($message) {
    if (empty($message)) {
        return '<div class="vc-login-message">Welcome to Virtual Classroom! Please log in with your credentials.</div>';
    } else {
        return $message;
    }
}
add_filter('login_message', 'vc_login_message');

/**
 * Redirect users after successful login
 */
function vc_login_redirect($redirect_to, $request, $user) {
    if (isset($user->roles) && is_array($user->roles)) {
        if (in_array('administrator', $user->roles)) {
            return admin_url();
        } else {
            return home_url('/classroom/');
        }
    }
    return $redirect_to;
}
add_filter('login_redirect', 'vc_login_redirect', 10, 3);

/**
 * Customize login page title
 */
function vc_login_title() {
    return get_bloginfo('name') . ' | Virtual Classroom Login';
}
add_filter('login_title', 'vc_login_title');
```

```css
/* css/vc-login.css */
body.login {
    background-color: #f5f5f5;
    background-image: url('../images/classroom-bg.jpg');
    background-size: cover;
    background-position: center;
}

.login h1 a {
    background-image: url('../images/classroom-logo.png');
    background-size: contain;
    width: 100%;
    height: 100px;
    margin-bottom: 20px;
}

#loginform {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    background-color: rgba(255, 255, 255, 0.9);
}

.vc-login-message {
    background-color: #e6f7ff;
    border: 1px solid #91d5ff;
    padding: 12px;
    margin-bottom: 20px;
    border-radius: 4px;
    text-align: center;
}

.vc-custom-field {
    margin-bottom: 16px;
}

#vc_class_code {
    margin-top: 5px;
}

.login .button-primary {
    background-color: #1890ff;
    border-color: #1890ff;
    text-shadow: none;
    box-shadow: none;
}

.login .button-primary:hover {
    background-color: #40a9ff;
    border-color: #40a9ff;
}
```
