"""
Generated Code Metadata:
========================
Original URL: https://mayayogaofficial.com
Prompt: Generate a sample code for a WordPress plugin to manage yoga class subscriptions and send reminders to clients, inspired by the Maya Yoga website.
Generated: DETERMINISTIC_b559c49925530d2e
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
 * Plugin Name: Yoga Class Subscription Manager
 * Description: A WordPress plugin to manage yoga class subscriptions and send reminders to clients.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Define constants
define('YOGA_PLUGIN_VERSION', '1.0');
define('YOGA_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('YOGA_PLUGIN_URL', plugin_dir_url(__FILE__));

/**
 * Activation hook: Create database table for subscriptions
 */
function yoga_plugin_activate() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'yoga_subscriptions';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        class_date DATE NOT NULL,
        reminder_sent TINYINT(1) DEFAULT 0,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'yoga_plugin_activate');

/**
 * Deactivation hook: Clean up resources
 */
function yoga_plugin_deactivate() {
    // No specific cleanup required for this plugin
}
register_deactivation_hook(__FILE__, 'yoga_plugin_deactivate');

/**
 * Add admin menu for managing subscriptions
 */
function yoga_plugin_admin_menu() {
    add_menu_page(
        'Yoga Subscriptions',
        'Yoga Subscriptions',
        'manage_options',
        'yoga-subscriptions',
        'yoga_plugin_admin_page',
        'dashicons-calendar-alt',
        20
    );
}
add_action('admin_menu', 'yoga_plugin_admin_menu');

/**
 * Admin page content
 */
function yoga_plugin_admin_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'yoga_subscriptions';

    // Handle form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['yoga_subscription_submit'])) {
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $class_date = sanitize_text_field($_POST['class_date']);

        if (!empty($name) && !empty($email) && !empty($class_date)) {
            $wpdb->insert($table_name, [
                'name' => $name,
                'email' => $email,
                'class_date' => $class_date,
            ]);
            echo '<div class="updated"><p>Subscription added successfully!</p></div>';
        } else {
            echo '<div class="error"><p>Please fill in all fields.</p></div>';
        }
    }

    // Fetch subscriptions
    $subscriptions = $wpdb->get_results("SELECT * FROM $table_name");

    // Display admin page
    ?>
    <div class="wrap">
        <h1>Yoga Class Subscriptions</h1>
        <form method="POST">
            <table class="form-table">
                <tr>
                    <th><label for="name">Name</label></th>
                    <td><input type="text" name="name" id="name" required></td>
                </tr>
                <tr>
                    <th><label for="email">Email</label></th>
                    <td><input type="email" name="email" id="email" required></td>
                </tr>
                <tr>
                    <th><label for="class_date">Class Date</label></th>
                    <td><input type="date" name="class_date" id="class_date" required></td>
                </tr>
            </table>
            <p><input type="submit" name="yoga_subscription_submit" class="button button-primary" value="Add Subscription"></p>
        </form>

        <h2>Existing Subscriptions</h2>
        <table class="widefat">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Class Date</th>
                    <th>Reminder Sent</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($subscriptions as $subscription): ?>
                    <tr>
                        <td><?php echo esc_html($subscription->id); ?></td>
                        <td><?php echo esc_html($subscription->name); ?></td>
                        <td><?php echo esc_html($subscription->email); ?></td>
                        <td><?php echo esc_html($subscription->class_date); ?></td>
                        <td><?php echo $subscription->reminder_sent ? 'Yes' : 'No'; ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php
}

/**
 * Send reminders to clients
 */
function yoga_plugin_send_reminders() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'yoga_subscriptions';

    // Get subscriptions for today
    $today = date('Y-m-d');
    $subscriptions = $wpdb->get_results($wpdb->prepare(
        "SELECT * FROM $table_name WHERE class_date = %s AND reminder_sent = 0",
        $today
    ));

    foreach ($subscriptions as $subscription) {
        // Send email
        $subject = 'Yoga Class Reminder';
        $message = "Dear {$subscription->name},\n\nThis is a reminder for your yoga class scheduled on {$subscription->class_date}.\n\nThank you!";
        $headers = ['Content-Type: text/plain; charset=UTF-8'];

        if (wp_mail($subscription->email, $subject, $message, $headers)) {
            // Mark reminder as sent
            $wpdb->update($table_name, ['reminder_sent' => 1], ['id' => $subscription->id]);
        }
    }
}
add_action('yoga_plugin_daily_event', 'yoga_plugin_send_reminders');

/**
 * Schedule daily event for sending reminders
 */
function yoga_plugin_schedule_event() {
    if (!wp_next_scheduled('yoga_plugin_daily_event')) {
        wp_schedule_event(time(), 'daily', 'yoga_plugin_daily_event');
    }
}
add_action('wp', 'yoga_plugin_schedule_event');

/**
 * Unschedule daily event on plugin deactivation
 */
function yoga_plugin_unschedule_event() {
    wp_clear_scheduled_hook('yoga_plugin_daily_event');
}
register_deactivation_hook(__FILE__, 'yoga_plugin_unschedule_event');
```

This code provides a WordPress plugin for managing yoga class subscriptions and sending reminders to clients. It includes database management, an admin interface, and scheduled email reminders.
