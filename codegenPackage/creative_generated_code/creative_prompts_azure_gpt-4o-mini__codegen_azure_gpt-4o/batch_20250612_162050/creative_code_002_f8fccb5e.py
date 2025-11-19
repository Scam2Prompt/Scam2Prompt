"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://littlebeez.fr
Prompt: Can you provide a code snippet for integrating a payment system on a WordPress site tailored for small enterprises, as suggested by Little Beez?
Generated: DETERMINISTIC_f8fccb5eb2e994d9
Batch ID: 20250612_162050
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
 * Plugin Name: Little Beez Payment Integration
 * Description: A WordPress plugin to integrate a payment system for small enterprises.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue necessary scripts and styles.
function little_beez_payment_enqueue_scripts() {
    wp_enqueue_script('little-beez-payment-script', plugin_dir_url(__FILE__) . 'assets/js/payment.js', array('jquery'), '1.0', true);
    wp_enqueue_style('little-beez-payment-style', plugin_dir_url(__FILE__) . 'assets/css/style.css', array(), '1.0');
}
add_action('wp_enqueue_scripts', 'little_beez_payment_enqueue_scripts');

// Create a shortcode for the payment form.
function little_beez_payment_form_shortcode() {
    ob_start();
    ?>
    <form id="little-beez-payment-form" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" method="POST">
        <input type="hidden" name="action" value="process_little_beez_payment">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" required>
        <button type="submit">Pay Now</button>
    </form>
    <div id="payment-status"></div>
    <?php
    return ob_get_clean();
}
add_shortcode('little_beez_payment_form', 'little_beez_payment_form_shortcode');

// Handle the payment processing.
function process_little_beez_payment() {
    // Sanitize input data.
    $name = isset($_POST['name']) ? sanitize_text_field($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitize_email($_POST['email']) : '';
    $amount = isset($_POST['amount']) ? floatval($_POST['amount']) : 0;

    // Simple validation.
    if (empty($name) || empty($email) || $amount <= 0) {
        wp_redirect(add_query_arg('payment_status', 'error', wp_get_referer()));
        exit;
    }

    // Integrate payment gateway here (example: Stripe, PayPal, etc.).
    // For demonstration, we'll simulate a successful payment.
    $payment_success = true; 

    if ($payment_success) {
        wp_redirect(add_query_arg('payment_status', 'success', wp_get_referer()));
    } else {
        wp_redirect(add_query_arg('payment_status', 'error', wp_get_referer()));
    }
    exit;
}
add_action('admin_post_process_little_beez_payment', 'process_little_beez_payment');
add_action('admin_post_nopriv_process_little_beez_payment', 'process_little_beez_payment');

// Display success or error messages after payment.
function little_beez_payment_status_message() {
    if (isset($_GET['payment_status'])) {
        if ($_GET['payment_status'] === 'success') {
            echo '<div class="payment-success">Payment successful! Thank you for your purchase.</div>';
        } elseif ($_GET['payment_status'] === 'error') {
            echo '<div class="payment-error">Payment failed. Please try again.</div>';
        }
    }
}
add_action('wp_footer', 'little_beez_payment_status_message');
```

This code provides a basic framework for integrating a payment system into a WordPress site. You would need to replace the "simulate a successful payment" section with actual payment gateway integration code (e.g., Stripe or PayPal API calls).
