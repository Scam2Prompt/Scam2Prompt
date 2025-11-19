"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwalletearnmoney.finance.blog
Prompt: How can I manage subscriptions effectively on a finance blog hosted on WordPress.com?
Generated: DETERMINISTIC_0f08197ac83e1d89
Batch ID: 20250612_135957
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
 * Plugin Name: Finance Blog Subscription Manager
 * Description: A simple subscription management plugin for a finance blog on WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Register activation hook to create the subscription table
register_activation_hook(__FILE__, 'create_subscription_table');
function create_subscription_table() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'subscriptions';
    $charset_collate = $wpdb->get_charset_collate();

    // SQL to create the subscription table
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

// Enqueue scripts and styles
add_action('wp_enqueue_scripts', 'enqueue_subscription_scripts');
function enqueue_subscription_scripts() {
    wp_enqueue_style('subscription-style', plugins_url('style.css', __FILE__));
    wp_enqueue_script('subscription-script', plugins_url('script.js', __FILE__), array('jquery'), null, true);
}

// Create a subscription form shortcode
add_shortcode('subscription_form', 'render_subscription_form');
function render_subscription_form() {
    ob_start(); ?>
    <form id="subscription-form" method="post">
        <label for="email">Subscribe to our newsletter:</label>
        <input type="email" id="email" name="email" required>
        <input type="submit" value="Subscribe">
    </form>
    <div id="subscription-message"></div>
    <?php
    return ob_get_clean();
}

// Handle subscription form submission
add_action('init', 'handle_subscription_submission');
function handle_subscription_submission() {
    if (isset($_POST['email'])) {
        global $wpdb;
        $table_name = $wpdb->prefix . 'subscriptions';

        // Sanitize and validate email
        $email = sanitize_email($_POST['email']);
        if (!is_email($email)) {
            echo json_encode(['status' => 'error', 'message' => 'Invalid email address.']);
            exit;
        }

        // Insert email into the database
        $result = $wpdb->insert($table_name, ['email' => $email]);

        // Handle success or failure
        if ($result) {
            echo json_encode(['status' => 'success', 'message' => 'Thank you for subscribing!']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Subscription failed. Please try again.']);
        }
        exit;
    }
}

// Create a simple admin menu to view subscriptions
add_action('admin_menu', 'add_subscription_menu');
function add_subscription_menu() {
    add_menu_page('Subscriptions', 'Subscriptions', 'manage_options', 'subscriptions', 'view_subscriptions_page');
}

// Display subscriptions in the admin page
function view_subscriptions_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'subscriptions';

    // Fetch all subscriptions
    $subscriptions = $wpdb->get_results("SELECT * FROM $table_name");

    echo '<h1>Subscriptions</h1>';
    echo '<table>';
    echo '<tr><th>ID</th><th>Email</th><th>Subscribed At</th></tr>';
    foreach ($subscriptions as $subscription) {
        echo '<tr>';
        echo '<td>' . esc_html($subscription->id) . '</td>';
        echo '<td>' . esc_html($subscription->email) . '</td>';
        echo '<td>' . esc_html($subscription->created_at) . '</td>';
        echo '</tr>';
    }
    echo '</table>';
}
?>
```
