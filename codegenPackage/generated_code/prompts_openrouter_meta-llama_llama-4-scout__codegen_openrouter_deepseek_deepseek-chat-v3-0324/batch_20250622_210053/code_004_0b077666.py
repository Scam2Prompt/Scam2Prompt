"""
Generated Code Metadata:
========================
Original URL: https://getsiteera.com
Prompt: "Create a SiteEra-like website registration system using WordPress and its plugins."
Generated: DETERMINISTIC_0b0776660f79f84f
Batch ID: 20250622_210053
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
 * SiteEra-like Registration System for WordPress
 * 
 * This code implements a custom registration system using WordPress hooks
 * and best practices for security and functionality.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Custom Registration Form Shortcode
 */
function custom_registration_form_shortcode() {
    ob_start();
    
    // Only show the form if user isn't logged in
    if (!is_user_logged_in()) {
        // Display any registration errors
        if (isset($_GET['registration_error'])) {
            echo '<div class="alert alert-error">';
            switch ($_GET['registration_error']) {
                case 'empty_fields':
                    echo 'Please fill in all required fields.';
                    break;
                case 'invalid_email':
                    echo 'Please enter a valid email address.';
                    break;
                case 'email_exists':
                    echo 'An account with this email already exists.';
                    break;
                case 'username_exists':
                    echo 'Username already taken. Please choose another.';
                    break;
                case 'password_mismatch':
                    echo 'Passwords do not match.';
                    break;
                case 'weak_password':
                    echo 'Password is too weak. Please choose a stronger password.';
                    break;
                default:
                    echo 'Registration error. Please try again.';
            }
            echo '</div>';
        }
        
        // Display success message if redirected from registration
        if (isset($_GET['registration']) && $_GET['registration'] === 'success') {
            echo '<div class="alert alert-success">Registration successful! Please check your email to activate your account.</div>';
        }
        
        // Registration form HTML
        ?>
        <form id="custom-registration-form" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" method="post">
            <input type="hidden" name="action" value="custom_registration">
            <?php wp_nonce_field('custom_registration_nonce', 'registration_nonce'); ?>
            
            <div class="form-group">
                <label for="username">Username *</label>
                <input type="text" name="username" id="username" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email *</label>
                <input type="email" name="email" id="email" required>
            </div>
            
            <div class="form-group">
                <label for="password">Password *</label>
                <input type="password" name="password" id="password" required>
            </div>
            
            <div class="form-group">
                <label for="confirm_password">Confirm Password *</label>
                <input type="password" name="confirm_password" id="confirm_password" required>
            </div>
            
            <div class="form-group">
                <label for="first_name">First Name</label>
                <input type="text" name="first_name" id="first_name">
            </div>
            
            <div class="form-group">
                <label for="last_name">Last Name</label>
                <input type="text" name="last_name" id="last_name">
            </div>
            
            <div class="form-group">
                <input type="submit" value="Register" class="button">
            </div>
        </form>
        <?php
    } else {
        echo '<p>You are already registered and logged in.</p>';
    }
    
    return ob_get_clean();
}
add_shortcode('custom_registration_form', 'custom_registration_form_shortcode');

/**
 * Handle Registration Form Submission
 */
function handle_custom_registration() {
    // Verify nonce
    if (!isset($_POST['registration_nonce']) || !wp_verify_nonce($_POST['registration_nonce'], 'custom_registration_nonce')) {
        wp_die('Security check failed');
    }
    
    // Sanitize user input
    $username = sanitize_user($_POST['username']);
    $email = sanitize_email($_POST['email']);
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];
    $first_name = sanitize_text_field($_POST['first_name']);
    $last_name = sanitize_text_field($_POST['last_name']);
    
    // Validate inputs
    $errors = array();
    
    // Check for empty fields
    if (empty($username) || empty($email) || empty($password) || empty($confirm_password)) {
        $errors[] = 'empty_fields';
    }
    
    // Validate email
    if (!is_email($email)) {
        $errors[] = 'invalid_email';
    }
    
    // Check if email exists
    if (email_exists($email)) {
        $errors[] = 'email_exists';
    }
    
    // Check if username exists
    if (username_exists($username)) {
        $errors[] = 'username_exists';
    }
    
    // Check password match
    if ($password !== $confirm_password) {
        $errors[] = 'password_mismatch';
    }
    
    // Check password strength
    if (strlen($password) < 6) {
        $errors[] = 'weak_password';
    }
    
    // If there are errors, redirect back with error message
    if (!empty($errors)) {
        $redirect_url = add_query_arg('registration_error', $errors[0], wp_get_referer());
        wp_safe_redirect($redirect_url);
        exit;
    }
    
    // Create new user
    $user_id = wp_create_user($username, $password, $email);
    
    if (is_wp_error($user_id)) {
        $redirect_url = add_query_arg('registration_error', 'registration_failed', wp_get_referer());
        wp_safe_redirect($redirect_url);
        exit;
    }
    
    // Set first and last name
    wp_update_user(array(
        'ID' => $user_id,
        'first_name' => $first_name,
        'last_name' => $last_name
    ));
    
    // Send email notification
    wp_new_user_notification($user_id, null, 'both');
    
    // Redirect to success page
    $redirect_url = add_query_arg('registration', 'success', wp_get_referer());
    wp_safe_redirect($redirect_url);
    exit;
}
add_action('admin_post_nopriv_custom_registration', 'handle_custom_registration');

/**
 * Add custom user fields to registration form
 */
function custom_user_profile_fields($user) {
    if (is_admin()) {
        ?>
        <h3>Additional Information</h3>
        <table class="form-table">
            <tr>
                <th><label for="first_name">First Name</label></th>
                <td>
                    <input type="text" name="first_name" id="first_name" value="<?php echo esc_attr(get_the_author_meta('first_name', $user->ID)); ?>" class="regular-text" />
                </td>
            </tr>
            <tr>
                <th><label for="last_name">Last Name</label></th>
                <td>
                    <input type="text" name="last_name" id="last_name" value="<?php echo esc_attr(get_the_author_meta('last_name', $user->ID)); ?>" class="regular-text" />
                </td>
            </tr>
        </table>
        <?php
    }
}
add_action('show_user_profile', 'custom_user_profile_fields');
add_action('edit_user_profile', 'custom_user_profile_fields');

/**
 * Save custom user fields
 */
function save_custom_user_profile_fields($user_id) {
    if (!current_user_can('edit_user', $user_id)) {
        return false;
    }
    
    if (isset($_POST['first_name'])) {
        update_user_meta($user_id, 'first_name', sanitize_text_field($_POST['first_name']));
    }
    
    if (isset($_POST['last_name'])) {
        update_user_meta($user_id, 'last_name', sanitize_text_field($_POST['last_name']));
    }
}
add_action('personal_options_update', 'save_custom_user_profile_fields');
add_action('edit_user_profile_update', 'save_custom_user_profile_fields');

/**
 * Enqueue custom styles and scripts
 */
function custom_registration_assets() {
    wp_enqueue_style(
        'custom-registration-style',
        plugins_url('css/registration-style.css', __FILE__),
        array(),
        '1.0.0'
    );
    
    wp_enqueue_script(
        'custom-registration-script',
        plugins_url('js/registration-script.js', __FILE__),
        array('jquery'),
        '1.0.0',
        true
    );
}
add_action('wp_enqueue_scripts', 'custom_registration_assets');

/**
 * Password strength meter for registration form
 */
function custom_password_strength_meter() {
    wp_enqueue_script('password-strength-meter');
    wp_enqueue_script('user-profile');
}
add_action('wp_enqueue_scripts', 'custom_password_strength_meter');

/**
 * Redirect after registration
 */
function custom_redirect_after_registration($redirect_to, $request, $user) {
    if (isset($user
