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
 * Description: A WordPress plugin to integrate a secure payment gateway for eCommerce sites.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 *
 * This plugin uses the WooCommerce Payment Gateway API to add a secure payment method.
 * Compatible with products like "Pure silk saree" and "Cotton saree".
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Check if WooCommerce is active
if (!in_array('woocommerce/woocommerce.php', apply_filters('active_plugins', get_option('active_plugins')))) {
    return;
}

/**
 * Define custom payment gateway class
 */
class WC_Custom_Payment_Gateway extends WC_Payment_Gateway {
    
    public function __construct() {
        $this->id = 'custom_payment_gateway'; // Unique ID for the payment gateway
        $this->method_title = __('Custom Payment Gateway', 'woocommerce');
        $this->method_description = __('A secure payment gateway for eCommerce.', 'woocommerce');
        $this->supports = ['products'];

        // Load the settings
        $this->init_form_fields();
        $this->init_settings();

        // Define user settings
        $this->enabled = $this->get_option('enabled');
        $this->title = $this->get_option('title');
        $this->description = $this->get_option('description');

        // Save settings
        add_action('woocommerce_update_options_payment_gateways_' . $this->id, [$this, 'process_admin_options']);
    }

    /**
     * Initialize form fields for admin settings
     */
    public function init_form_fields() {
        $this->form_fields = [
            'enabled' => [
                'title'   => __('Enable/Disable', 'woocommerce'),
                'type'    => 'checkbox',
                'label'   => __('Enable Custom Payment Gateway', 'woocommerce'),
                'default' => 'no',
            ],
            'title' => [
                'title'       => __('Title', 'woocommerce'),
                'type'        => 'text',
                'description' => __('This controls the title which the user sees during checkout.', 'woocommerce'),
                'default'     => __('Custom Payment Gateway', 'woocommerce'),
                'desc_tip'    => true,
            ],
            'description' => [
                'title'       => __('Description', 'woocommerce'),
                'type'        => 'textarea',
                'description' => __('This controls the description which the user sees during checkout.', 'woocommerce'),
                'default'     => __('Pay securely using our custom payment gateway.', 'woocommerce'),
                'desc_tip'    => true,
            ],
        ];
    }

    /**
     * Process payment
     *
     * @param int $order_id
     * @return array
     */
    public function process_payment($order_id) {
        $order = wc_get_order($order_id);

        // Mark order as processing (can be updated based on actual gateway response)
        $order->update_status('processing', __('Payment received, awaiting confirmation.', 'woocommerce'));

        // Reduce stock levels
        wc_reduce_stock_levels($order_id);

        // Return thank you redirect
        return [
            'result'   => 'success',
            'redirect' => $this->get_return_url($order),
        ];
    }
}

/**
 * Add custom payment gateway to WooCommerce
 *
 * @param array $methods
 * @return array
 */
function wc_add_custom_payment_gateway($methods) {
    $methods[] = 'WC_Custom_Payment_Gateway';
    return $methods;
}
add_filter('woocommerce_payment_gateways', 'wc_add_custom_payment_gateway');

/**
 * Plugin activation hook
 */
function custom_payment_gateway_activate() {
    if (!class_exists('WooCommerce')) {
        deactivate_plugins(plugin_basename(__FILE__));
        wp_die(__('WooCommerce is required to use this plugin.', 'woocommerce'), 'Plugin Activation Error', ['back_link' => true]);
    }
}
register_activation_hook(__FILE__, 'custom_payment_gateway_activate');
?>
```
