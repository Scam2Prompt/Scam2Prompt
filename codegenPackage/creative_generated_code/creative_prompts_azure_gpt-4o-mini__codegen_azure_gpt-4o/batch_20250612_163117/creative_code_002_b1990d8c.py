"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditoexpressdvda.com
Prompt: What libraries can I use to manage user subscriptions effectively on a WordPress site like creditoexpressdvda.com?
Generated: DETERMINISTIC_b1990d8c13782827
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
 * Plugin Name: Subscription Manager for WordPress
 * Description: A production-ready WordPress plugin to manage user subscriptions effectively using popular libraries.
 * Version: 1.0.0
 * Author: Expert Programmer
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Include necessary libraries (assuming Composer is used for dependency management).
require_once plugin_dir_path(__FILE__) . 'vendor/autoload.php';

use \Stripe\Stripe;
use \Stripe\Customer;
use \Stripe\Subscription;

// Define constants for Stripe API keys.
define('STRIPE_API_KEY', 'your_stripe_secret_key'); // Replace with your Stripe Secret Key.
define('STRIPE_WEBHOOK_SECRET', 'your_stripe_webhook_secret'); // Replace with your Webhook Secret Key.

/**
 * Initialize Stripe API.
 */
function initialize_stripe() {
    Stripe::setApiKey(STRIPE_API_KEY);
}
add_action('init', 'initialize_stripe');

/**
 * Create a new subscription for a user.
 *
 * @param int $user_id The WordPress user ID.
 * @param string $email The user's email address.
 * @param string $payment_method The payment method ID (retrieved via Stripe.js).
 * @param string $price_id The price ID for the subscription plan.
 *
 * @return array|WP_Error Response data or an error object.
 */
function create_subscription($user_id, $email, $payment_method, $price_id) {
    try {
        // Create a new customer in Stripe.
        $customer = Customer::create([
            'email' => $email,
            'payment_method' => $payment_method,
            'invoice_settings' => [
                'default_payment_method' => $payment_method,
            ],
        ]);

        // Create a subscription for the customer.
        $subscription = Subscription::create([
            'customer' => $customer->id,
            'items' => [
                [
                    'price' => $price_id,
                ],
            ],
        ]);

        // Save customer and subscription IDs in user meta.
        update_user_meta($user_id, 'stripe_customer_id', $customer->id);
        update_user_meta($user_id, 'stripe_subscription_id', $subscription->id);

        return ['success' => true, 'subscription' => $subscription];
    } catch (\Stripe\Exception\ApiErrorException $e) {
        return new WP_Error('stripe_error', $e->getMessage());
    }
}

/**
 * Handle Stripe Webhook events (e.g., subscription cancellations, payment failures).
 */
function handle_stripe_webhooks() {
    $payload = @file_get_contents('php://input');
    $sig_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

    try {
        $event = \Stripe\Webhook::constructEvent($payload, $sig_header, STRIPE_WEBHOOK_SECRET);

        // Handle the event types you care about.
        switch ($event->type) {
            case 'customer.subscription.deleted':
                $subscription = $event->data->object;
                $user_id = get_user_id_by_stripe_customer($subscription->customer); // Custom helper function.
                if ($user_id) {
                    // Update user meta to reflect subscription cancellation.
                    delete_user_meta($user_id, 'stripe_subscription_id');
                }
                break;

            case 'invoice.payment_failed':
                $invoice = $event->data->object;
                $user_id = get_user_id_by_stripe_customer($invoice->customer); // Custom helper function.
                if ($user_id) {
                    // Notify the user about a payment failure (e.g., via email).
                    wp_mail(
                        get_userdata($user_id)->user_email,
                        'Payment Failed',
                        'We were unable to process your subscription payment. Please update your payment method.'
                    );
                }
                break;

            // Add additional cases for other webhook events as needed.
        }

        http_response_code(200); // Acknowledge receipt of the event.
    } catch (\Stripe\Exception\SignatureVerificationException $e) {
        http_response_code(400); // Invalid signature.
    }
}
add_action('rest_api_init', function () {
    register_rest_route('stripe/v1', '/webhook', [
        'methods' => WP_REST_Server::CREATABLE,
        'callback' => 'handle_stripe_webhooks',
        'permission_callback' => '__return_true', // No authentication required.
    ]);
});

/**
 * Helper function to retrieve WordPress user ID by Stripe customer ID.
 *
 * @param string $customer_id The Stripe customer ID.
 * @return int|null The associated WordPress user ID, or null if not found.
 */
function get_user_id_by_stripe_customer($customer_id) {
    global $wpdb;
    $user_id = $wpdb->get_var(
        $wpdb->prepare(
            "SELECT user_id FROM $wpdb->usermeta WHERE meta_key = 'stripe_customer_id' AND meta_value = %s",
            $customer_id
        )
    );
    return $user_id ? (int) $user_id : null;
}
```

This code integrates Stripe for subscription management, handles webhook events for subscription changes, and ensures clean error handling. Make sure to replace the placeholder values for `STRIPE_API_KEY` and `STRIPE_WEBHOOK_SECRET` with your actual Stripe API credentials. Use Composer to install the Stripe PHP SDK (`composer require stripe/stripe-php`).
