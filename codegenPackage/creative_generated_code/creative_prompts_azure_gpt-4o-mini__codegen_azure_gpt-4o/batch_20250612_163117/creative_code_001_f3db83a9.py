"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditoexpressdvda.com
Prompt: Write a code snippet to create a subscription form for a website like creditoexpressdvda.com using WordPress.
Generated: DETERMINISTIC_f3db83a96129d77a
Batch ID: 20250612_163117
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
 * Plugin Name: Subscription Form for Credito Express DVDA
 * Description: Adds a simple subscription form to the WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Prevent direct access to the file.
}

// Register a shortcode to display the subscription form.
function creditoexpress_subscription_form_shortcode() {
    ob_start();
    ?>
    <form id="subscription-form" method="post" action="">
        <label for="subscriber-name">Name:</label>
        <input type="text" id="subscriber-name" name="subscriber_name" required>
        
        <label for="subscriber-email">Email:</label>
        <input type="email" id="subscriber-email" name="subscriber_email" required>
        
        <button type="submit">Subscribe</button>
    </form>
    <?php
    // Handle form submission if POST request is made.
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        creditoexpress_handle_subscription_form_submission();
    }
    
    return ob_get_clean();
}
add_shortcode('creditoexpress_subscription_form', 'creditoexpress_subscription_form_shortcode');

// Function to handle form submission.
function creditoexpress_handle_subscription_form_submission() {
    // Sanitize and validate input data.
    $name = isset($_POST['subscriber_name']) ? sanitize_text_field($_POST['subscriber_name']) : '';
    $email = isset($_POST['subscriber_email']) ? sanitize_email($_POST['subscriber_email']) : '';

    if (empty($name) || empty($email)) {
        echo '<p style="color:red;">Both Name and Email are required.</p>';
        return;
    }

    if (!is_email($email)) {
        echo '<p style="color:red;">Invalid email address.</p>';
        return;
    }

    // Save subscriber information to the database (wp_options for simplicity; consider a custom table for production).
    $subscribers = get_option('creditoexpress_subscribers', []);
    $subscribers[] = [
        'name' => $name,
        'email' => $email,
        'date' => current_time('mysql'),
    ];
    update_option('creditoexpress_subscribers', $subscribers);

    echo '<p style="color:green;">Thank you for subscribing!</p>';
}

// Admin page to view subscribers.
function creditoexpress_register_admin_menu() {
    add_menu_page(
        'Subscribers',
        'Subscribers',
        'manage_options',
        'creditoexpress-subscribers',
        'creditoexpress_render_admin_page',
        'dashicons-email',
        20
    );
}
add_action('admin_menu', 'creditoexpress_register_admin_menu');

// Render the admin page.
function creditoexpress_render_admin_page() {
    if (!current_user_can('manage_options')) {
        return;
    }

    $subscribers = get_option('creditoexpress_subscribers', []);

    echo '<div class="wrap">';
    echo '<h1>Subscribers</h1>';
    echo '<table class="widefat">';
    echo '<thead><tr><th>Name</th><th>Email</th><th>Date</th></tr></thead>';
    echo '<tbody>';
    foreach ($subscribers as $subscriber) {
        echo '<tr>';
        echo '<td>' . esc_html($subscriber['name']) . '</td>';
        echo '<td>' . esc_html($subscriber['email']) . '</td>';
        echo '<td>' . esc_html($subscriber['date']) . '</td>';
        echo '</tr>';
    }
    echo '</tbody>';
    echo '</table>';
    echo '</div>';
}
?>
```
