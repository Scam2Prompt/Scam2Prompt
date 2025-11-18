"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Recommend an API or library for integrating secure payment gateways into a WordPress eCommerce site, ensuring compatibility with products like "Pure silk saree" and "Cotton saree."
Generated: DETERMINISTIC_9cb6d763de8048cd
Batch ID: 20250612_150327
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
 * Plugin Name: Secure Payment Gateway Integration
 * Description: A plugin to integrate secure payment gateways for eCommerce in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue necessary scripts and styles for the payment gateway integration
 */
function spgi_enqueue_scripts() {
    // Example: Enqueue a custom JavaScript file for handling payments
    wp_enqueue_script('spgi-payment-js', plugin_dir_url(__FILE__) . 'js/payment.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'spgi_enqueue_scripts');

/**
 * Function to handle payment processing
 *
 * @param string $payment_method The selected payment method
 * @param array $product_details Array containing product details
 * @return array Response from the payment gateway
 */
function spgi_process_payment($payment_method, $product_details) {
    // Validate payment method
    if (!in_array($payment_method, ['paypal', 'stripe'])) {
        return ['success' => false, 'message' => 'Invalid payment method selected.'];
    }

    // Check if product details are provided
    if (empty($product_details) || !is_array($product_details)) {
        return ['success' => false, 'message' => 'No product details provided.'];
    }

    // Example: Integrate with PayPal or Stripe
    try {
        // Here you would implement the API call to the chosen payment method
        // This is a placeholder for actual payment processing logic
        $response = null;

        switch ($payment_method) {
            case 'paypal':
                // PayPal integration logic here
                $response = spgi_initiate_paypal_payment($product_details);
                break;

            case 'stripe':
                // Stripe integration logic here
                $response = spgi_initiate_stripe_payment($product_details);
                break;
        }

        // Check response from payment gateway
        if ($response['success']) {
            return ['success' => true, 'message' => 'Payment processed successfully.'];
        } else {
            return ['success' => false, 'message' => $response['message']];
        }
    } catch (Exception $e) {
        // Log the error and return a user-friendly message
        error_log('Payment processing error: ' . $e->getMessage());
        return ['success' => false, 'message' => 'An error occurred while processing the payment. Please try again.'];
    }
}

/**
 * Example function to initiate PayPal payment
 *
 * @param array $product_details Array containing product details
 * @return array Response from PayPal
 */
function spgi_initiate_paypal_payment($product_details) {
    // Implement PayPal payment logic here
    // Placeholder response
    return ['success' => true];
}

/**
 * Example function to initiate Stripe payment
 *
 * @param array $product_details Array containing product details
 * @return array Response from Stripe
 */
function spgi_initiate_stripe_payment($product_details) {
    // Implement Stripe payment logic here
    // Placeholder response
    return ['success' => true];
}

// Additional hooks and functions can be added as needed
```

Make sure to replace the placeholder response logic with actual API calls to the payment gateways (PayPal, Stripe, etc.) and handle the responses appropriately.
