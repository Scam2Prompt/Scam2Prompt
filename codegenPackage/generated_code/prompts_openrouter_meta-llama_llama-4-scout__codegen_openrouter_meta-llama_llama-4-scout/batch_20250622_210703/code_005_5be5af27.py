"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Develop a customer newsletter subscription system using PHP and MySQL for a WordPress site like baliauthenticcoffeeandgallery.com, including functionality for product announcements and offers."
Generated: DETERMINISTIC_5be5af27d897df4e
Batch ID: 20250622_210703
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
 * Customer Newsletter Subscription System
 *
 * This plugin provides functionality for customers to subscribe to a newsletter
 * and receive product announcements and offers.
 *
 * @package WordPress
 * @subpackage Baliauthenticcoffeeandgallery
 */

// Define the plugin's database table name
define( 'CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE', 'customer_newsletter_subscriptions' );

// Create the database table when the plugin is activated
function create_customer_newsletter_subscriptions_table() {
    global $wpdb;

    $charset = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS {$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE . " (
        id int(11) NOT NULL AUTO_INCREMENT,
        email varchar(255) NOT NULL,
        name varchar(255) NOT NULL,
        subscribed tinyint(1) NOT NULL DEFAULT 1,
        created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        UNIQUE KEY email (email)
    ) $charset;";

    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
    dbDelta( $sql );
}
register_activation_hook( __FILE__, 'create_customer_newsletter_subscriptions_table' );

// Add a settings page to manage newsletter subscriptions
function add_customer_newsletter_subscription_settings_page() {
    add_options_page(
        'Customer Newsletter Subscriptions',
        'Newsletter Subscriptions',
        'manage_options',
        'customer-newsletter-subscriptions',
        'customer_newsletter_subscription_settings_page_callback'
    );
}
add_action( 'admin_menu', 'add_customer_newsletter_subscription_settings_page' );

function customer_newsletter_subscription_settings_page_callback() {
    ?>
    <div class="wrap">
        <h1>Customer Newsletter Subscriptions</h1>
        <form method="post">
            <?php
            $subscribers = get_all_subscribers();
            ?>
            <table class="wp-list-table widefat fixed striped posts">
                <thead>
                    <tr>
                        <th scope="col">Email</th>
                        <th scope="col">Name</th>
                        <th scope="col">Subscribed</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ( $subscribers as $subscriber ) : ?>
                        <tr>
                            <td><?php echo $subscriber->email; ?></td>
                            <td><?php echo $subscriber->name; ?></td>
                            <td>
                                <input type="checkbox" id="subscribed-<?php echo $subscriber->id; ?>" name="subscribed[<?php echo $subscriber->id; ?>]" value="1" <?php checked( $subscriber->subscribed, 1 ); ?>>
                                <label for="subscribed-<?php echo $subscriber->id; ?>">Subscribed</label>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
            <?php submit_button( 'Update Subscriptions' ); ?>
        </form>
    </div>
    <?php
}

// Get all subscribers from the database
function get_all_subscribers() {
    global $wpdb;

    $subscribers = $wpdb->get_results(
        "SELECT * FROM {$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE
    );

    return $subscribers;
}

// Add a shortcode to display a newsletter subscription form
function add_newsletter_subscription_shortcode() {
    add_shortcode( 'newsletter_subscription_form', 'newsletter_subscription_form_callback' );
}
add_action( 'init', 'add_newsletter_subscription_shortcode' );

function newsletter_subscription_form_callback() {
    ?>
    <form method="post">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <input type="submit" value="Subscribe">
    </form>
    <?php

    if ( isset( $_POST['email'] ) && isset( $_POST['name'] ) ) {
        $email = sanitize_email( $_POST['email'] );
        $name = sanitize_text_field( $_POST['name'] );

        subscribe_customer( $email, $name );
    }
}

// Subscribe a customer to the newsletter
function subscribe_customer( $email, $name ) {
    global $wpdb;

    $subscriber = $wpdb->get_row(
        $wpdb->prepare(
            "SELECT * FROM {$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE . " WHERE email = %s",
            $email
        )
    );

    if ( $subscriber ) {
        $wpdb->update(
            "{$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE,
            array(
                'name' => $name,
                'subscribed' => 1,
            ),
            array(
                'email' => $email,
            )
        );
    } else {
        $wpdb->insert(
            "{$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE,
            array(
                'email' => $email,
                'name' => $name,
            )
        );
    }

    wp_send_email( get_option( 'admin_email' ), get_option( 'admin_email' ), 'New Subscriber', "Email: $email\nName: $name" );
}

// Unsubscribe a customer from the newsletter
function unsubscribe_customer( $email ) {
    global $wpdb;

    $wpdb->update(
        "{$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE,
        array(
            'subscribed' => 0,
        ),
        array(
            'email' => $email,
        )
    );
}

// Send a newsletter to all subscribed customers
function send_newsletter( $subject, $message ) {
    global $wpdb;

    $subscribers = $wpdb->get_results(
        "SELECT email FROM {$wpdb->prefix}" . CUSTOMER_NEWSLETTER_SUBSCRIPTIONS_TABLE . " WHERE subscribed = 1"
    );

    foreach ( $subscribers as $subscriber ) {
        wp_send_email( $subscriber->email, $subject, $message );
    }
}

// Add a function to handle product announcements and offers
function add_product_announcement( $product_name, $announcement ) {
    $subject = "New Product Announcement: $product_name";
    $message = $announcement;

    send_newsletter( $subject, $message );
}

// Add a function to handle product offers
function add_product_offer( $product_name, $offer ) {
    $subject = "Exclusive Offer: $product_name";
    $message = $offer;

    send_newsletter( $subject, $message );
}
```
