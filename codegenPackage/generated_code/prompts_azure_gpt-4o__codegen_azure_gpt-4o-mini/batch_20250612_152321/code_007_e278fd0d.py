"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Create a script to monitor and manage subscriptions for a WordPress blog, similar to the subscription functionality on Karl Franklyn Aparece's site.
Generated: DETERMINISTIC_e278fd0d265832e7
Batch ID: 20250612_152321
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
 * Plugin Name: Subscription Manager
 * Description: A simple subscription management system for WordPress blogs.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Create a custom database table for subscriptions on plugin activation.
 */
function sm_create_subscription_table() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'subscriptions';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        email varchar(100) NOT NULL,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY  (id),
        UNIQUE KEY email (email)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'sm_create_subscription_table');

/**
 * Enqueue scripts and styles for the subscription form.
 */
function sm_enqueue_scripts() {
    wp_enqueue_style('sm-style', plugin_dir_url(__FILE__) . 'css/style.css');
    wp_enqueue_script('sm-script', plugin_dir_url(__FILE__) . 'js/script.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'sm_enqueue_scripts');

/**
 * Shortcode to display the subscription form.
 */
function sm_subscription_form() {
    ob_start(); ?>
    <form id="subscription-form" method="post" action="">
        <input type="email" name="subscriber_email" placeholder="Enter your email" required>
        <input type="submit" value="Subscribe">
    </form>
    <div id="subscription-message"></div>
    <?php
    return ob_get_clean();
}
add_shortcode('subscription_form', 'sm_subscription_form');

/**
 * Handle form submission and manage subscriptions.
 */
function sm_handle_subscription() {
    if (isset($_POST['subscriber_email'])) {
        global $wpdb;
        $email = sanitize_email($_POST['subscriber_email']);
        $table_name = $wpdb->prefix . 'subscriptions';

        // Check if the email is already subscribed
        $existing_subscription = $wpdb->get_var($wpdb->prepare("SELECT email FROM $table_name WHERE email = %s", $email));

        if ($existing_subscription) {
            echo json_encode(['status' => 'error', 'message' => 'This email is already subscribed.']);
            wp_die(); // Required to terminate immediately and return a proper response
        }

        // Insert the new subscription
        $result = $wpdb->insert($table_name, ['email' => $email]);

        if ($result) {
            echo json_encode(['status' => 'success', 'message' => 'Thank you for subscribing!']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'There was an error processing your subscription.']);
        }
        wp_die(); // Required to terminate immediately and return a proper response
    }
}
add_action('wp_ajax_sm_handle_subscription', 'sm_handle_subscription');
add_action('wp_ajax_nopriv_sm_handle_subscription', 'sm_handle_subscription');

/**
 * Add a settings page for managing subscriptions.
 */
function sm_add_admin_menu() {
    add_menu_page('Subscription Manager', 'Subscription Manager', 'manage_options', 'subscription_manager', 'sm_subscription_manager_page');
}
add_action('admin_menu', 'sm_add_admin_menu');

/**
 * Display the subscription management page in the admin area.
 */
function sm_subscription_manager_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'subscriptions';
    $subscriptions = $wpdb->get_results("SELECT * FROM $table_name");

    ?>
    <div class="wrap">
        <h1>Manage Subscriptions</h1>
        <table class="widefat">
            <thead>
                <tr>
                    <th>Email</th>
                    <th>Subscribed On</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($subscriptions as $subscription) : ?>
                    <tr>
                        <td><?php echo esc_html($subscription->email); ?></td>
                        <td><?php echo esc_html($subscription->created_at); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php
}
```

This code provides a basic subscription management system for a WordPress blog, including a subscription form, handling of subscriptions, and an admin page to manage the subscriptions. Make sure to create the necessary CSS and JS files as referenced in the code.
