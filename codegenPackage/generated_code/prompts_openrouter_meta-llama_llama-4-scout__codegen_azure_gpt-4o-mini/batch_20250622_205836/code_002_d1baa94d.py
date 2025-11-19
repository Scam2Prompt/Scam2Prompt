"""
Generated Code Metadata:
========================
Original URL: https://teachercreator.com
Prompt: Generate code for a basic subscription management system that could be used in a WordPress plugin for a site like teachercreator.com, including user registration, login, and subscription status management.
Generated: DETERMINISTIC_d1baa94dfeaa2f41
Batch ID: 20250622_205836
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
 * Plugin Name: Subscription Management System
 * Description: A basic subscription management system for teachercreator.com.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

// Register activation hook to create necessary database tables
register_activation_hook(__FILE__, 'sms_create_database');

function sms_create_database() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'subscriptions';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        user_id bigint(20) NOT NULL,
        subscription_status varchar(20) NOT NULL,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}

// User registration function
function sms_register_user($username, $password, $email) {
    if (username_exists($username) || email_exists($email)) {
        return new WP_Error('registration-error', 'Username or email already exists.');
    }

    $user_id = wp_create_user($username, $password, $email);
    if (is_wp_error($user_id)) {
        return $user_id; // Return error
    }

    // Set default subscription status
    sms_set_subscription_status($user_id, 'inactive');

    return $user_id; // Return user ID on success
}

// User login function
function sms_login_user($username, $password) {
    $creds = array(
        'user_login' => $username,
        'user_password' => $password,
        'remember' => true,
    );

    $user = wp_signon($creds, false);
    if (is_wp_error($user)) {
        return $user; // Return error
    }

    return $user; // Return user object on success
}

// Set subscription status
function sms_set_subscription_status($user_id, $status) {
    global $wpdb;

    $table_name = $wpdb->prefix . 'subscriptions';
    $wpdb->replace(
        $table_name,
        array(
            'user_id' => $user_id,
            'subscription_status' => $status,
        ),
        array(
            '%d',
            '%s',
        )
    );
}

// Get subscription status
function sms_get_subscription_status($user_id) {
    global $wpdb;

    $table_name = $wpdb->prefix . 'subscriptions';
    $status = $wpdb->get_var($wpdb->prepare("SELECT subscription_status FROM $table_name WHERE user_id = %d", $user_id));

    return $status ? $status : 'not found'; // Return status or 'not found'
}

// Shortcode for displaying subscription status
function sms_display_subscription_status() {
    if (!is_user_logged_in()) {
        return 'Please log in to view your subscription status.';
    }

    $user_id = get_current_user_id();
    $status = sms_get_subscription_status($user_id);

    return "Your subscription status: " . esc_html($status);
}
add_shortcode('subscription_status', 'sms_display_subscription_status');

// Enqueue scripts and styles
function sms_enqueue_scripts() {
    wp_enqueue_style('sms-style', plugins_url('style.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'sms_enqueue_scripts');

// Admin menu for managing subscriptions
function sms_admin_menu() {
    add_menu_page('Subscription Management', 'Subscriptions', 'manage_options', 'sms-subscriptions', 'sms_admin_page');
}
add_action('admin_menu', 'sms_admin_menu');

function sms_admin_page() {
    // Admin page content for managing subscriptions
    echo '<h1>Manage Subscriptions</h1>';
    // Additional admin functionality can be added here
}
?>
```
