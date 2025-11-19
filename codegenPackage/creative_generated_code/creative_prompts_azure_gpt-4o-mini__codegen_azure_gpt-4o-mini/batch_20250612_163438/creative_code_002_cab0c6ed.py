"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmusk.fashion.blog
Prompt: Can you provide code snippets for setting up email subscriptions for a blog on WordPress.com, as mentioned in the elonmusk.fashion.blog content?
Generated: DETERMINISTIC_cab0c6ed9f630605
Batch ID: 20250612_163438
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
 * Plugin Name: Email Subscription for Blog
 * Description: A simple plugin to manage email subscriptions for a blog.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Create a custom table for email subscriptions on plugin activation.
 */
function es_create_subscription_table() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'email_subscriptions'; // Table name with prefix

    // SQL to create the table
    $charset_collate = $wpdb->get_charset_collate();
    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        email varchar(255) NOT NULL,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY (id),
        UNIQUE KEY email (email)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'es_create_subscription_table');

/**
 * Enqueue necessary scripts and styles.
 */
function es_enqueue_scripts() {
    wp_enqueue_style('es-styles', plugins_url('style.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'es_enqueue_scripts');

/**
 * Create a subscription form shortcode.
 */
function es_subscription_form() {
    ob_start(); // Start output buffering
    ?>
    <form id="subscription-form" method="post">
        <input type="email" name="subscriber_email" required placeholder="Enter your email" />
        <input type="submit" value="Subscribe" />
    </form>
    <?php
    return ob_get_clean(); // Return the buffered content
}
add_shortcode('email_subscription_form', 'es_subscription_form');

/**
 * Handle the form submission.
 */
function es_handle_subscription_form() {
    if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['subscriber_email'])) {
        global $wpdb;
        $email = sanitize_email($_POST['subscriber_email']);
        
        // Check if the email is already subscribed
        $table_name = $wpdb->prefix . 'email_subscriptions';
        $existing_email = $wpdb->get_var($wpdb->prepare("SELECT email FROM $table_name WHERE email = %s", $email));

        if ($existing_email) {
            // Email already exists, handle as needed (e.g., display a message)
            wp_die('This email is already subscribed.');
        }

        // Insert the email into the database
        $inserted = $wpdb->insert(
            $table_name,
            array('email' => $email),
            array('%s')
        );

        if ($inserted) {
            // Success message (could also redirect)
            wp_die('Thank you for subscribing!');
        } else {
            // Error handling
            wp_die('There was an error processing your subscription. Please try again later.');
        }
    }
}
add_action('init', 'es_handle_subscription_form');
```

Make sure to create a `style.css` file in the same directory for custom styling. Adjust the plugin metadata accordingly for your needs.
