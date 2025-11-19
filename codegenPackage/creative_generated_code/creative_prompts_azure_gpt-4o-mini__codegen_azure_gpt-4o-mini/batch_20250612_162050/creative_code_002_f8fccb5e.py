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
 * Description: Simple payment integration for small enterprises.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue necessary scripts and styles for the payment form.
 */
function lb_enqueue_scripts() {
    wp_enqueue_style( 'lb-payment-style', plugin_dir_url( __FILE__ ) . 'css/payment.css' );
    wp_enqueue_script( 'lb-payment-script', plugin_dir_url( __FILE__ ) . 'js/payment.js', array('jquery'), null, true );
}
add_action( 'wp_enqueue_scripts', 'lb_enqueue_scripts' );

/**
 * Shortcode to display the payment form.
 */
function lb_payment_form_shortcode() {
    ob_start(); ?>
    <form id="lb-payment-form" method="POST" action="<?php echo esc_url( admin_url('admin-post.php') ); ?>">
        <input type="hidden" name="action" value="lb_process_payment">
        <label for="amount">Amount:</label>
        <input type="text" name="amount" id="amount" required>
        
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
        
        <button type="submit">Pay Now</button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode( 'lb_payment_form', 'lb_payment_form_shortcode' );

/**
 * Process payment through the payment gateway.
 */
function lb_process_payment() {
    // Verify nonce for security
    if ( ! isset( $_POST['amount'], $_POST['email'] ) ) {
        wp_die( 'Invalid payment data.', 'Error', array( 'response' => 400 ) );
    }

    $amount = floatval( $_POST['amount'] );
    $email = sanitize_email( $_POST['email'] );

    // Validate the amount
    if ( $amount <= 0 ) {
        wp_die( 'Invalid payment amount.', 'Error', array( 'response' => 400 ) );
    }

    // Here you would integrate with a payment gateway's API
    // This is a placeholder for the payment gateway integration
    $payment_result = lb_fake_payment_gateway_integration( $amount, $email );

    if ( $payment_result['success'] ) {
        // Payment succeeded
        wp_redirect( home_url() . '/thank-you' ); // Redirect to a thank you page
        exit;
    } else {
        // Payment failed
        wp_die( 'Payment failed: ' . esc_html( $payment_result['message'] ), 'Error', array( 'response' => 500 ) );
    }
}
add_action( 'admin_post_lb_process_payment', 'lb_process_payment' );
add_action( 'admin_post_nopriv_lb_process_payment', 'lb_process_payment' );

/**
 * Fake payment gateway integration for demonstration purposes.
 *
 * @param float $amount The amount to process.
 * @param string $email The payer's email.
 * @return array An array containing the success status and message.
 */
function lb_fake_payment_gateway_integration( $amount, $email ) {
    // Simulating a successful payment
    return array(
        'success' => true,
        'message' => 'Payment processed successfully.'
    );
}
```

**Note:** This code is a basic outline for a WordPress plugin that integrates a payment system. Replace `lb_fake_payment_gateway_integration` with actual payment processing logic accordingly. Ensure that you adhere to the payment gateway's API documentation for a production environment.
