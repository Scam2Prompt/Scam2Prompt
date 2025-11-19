"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Write a PHP script to enable special order requests and alterations for chainmail dresses on a WooCommerce website, ensuring the form captures user preferences for fit and material customization.
Generated: DETERMINISTIC_6e99efde28b3e3b7
Batch ID: 20250612_152924
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
 * Enable special order requests and alterations for chainmail dresses on a WooCommerce website.
 */

// Hook to add custom fields to the product page
add_action('woocommerce_product_options', 'chainmail_dress_custom_fields');
function chainmail_dress_custom_fields() {
    // Check if the product is a chainmail dress
    $product_id = get_the_ID();
    $product = wc_get_product($product_id);
    if ($product->get_name() && strpos(strtolower($product->get_name()), 'chainmail') !== false) {
        // Add custom fields for fit and material customization
        woocommerce_wp_text_input(array(
            'id' => 'fit_preference',
            'label' => __('Fit Preference', 'woocommerce'),
            'desc_tip' => __('Please enter your preferred fit (e.g. loose, fitted, etc.)', 'woocommerce'),
            'description' => __('Enter your preferred fit for the chainmail dress', 'woocommerce')
        ));

        woocommerce_wp_select(array(
            'id' => 'material_preference',
            'label' => __('Material Preference', 'woocommerce'),
            'options' => array(
                '' => __('Select a material', 'woocommerce'),
                'steel' => __('Steel', 'woocommerce'),
                'aluminum' => __('Aluminum', 'woocommerce'),
                'titanium' => __('Titanium', 'woocommerce')
            ),
            'desc_tip' => __('Please select your preferred material', 'woocommerce'),
            'description' => __('Select your preferred material for the chainmail dress', 'woocommerce')
        ));
    }
}

// Hook to save custom fields data
add_action('woocommerce_process_product_meta', 'save_chainmail_dress_custom_fields', 10, 2);
function save_chainmail_dress_custom_fields($post_id, $post) {
    // Save fit preference
    $fit_preference = isset($_POST['fit_preference']) ? sanitize_text_field($_POST['fit_preference']) : '';
    update_post_meta($post_id, '_fit_preference', $fit_preference);

    // Save material preference
    $material_preference = isset($_POST['material_preference']) ? sanitize_text_field($_POST['material_preference']) : '';
    update_post_meta($post_id, '_material_preference', $material_preference);
}

// Hook to add custom fields to the order page
add_action('woocommerce_order_details_after_order_table', 'display_chainmail_dress_custom_fields');
function display_chainmail_dress_custom_fields($order) {
    // Get order items
    $items = $order->get_items();

    // Loop through order items
    foreach ($items as $item) {
        // Get product ID
        $product_id = $item->get_product_id();

        // Get product
        $product = wc_get_product($product_id);

        // Check if the product is a chainmail dress
        if ($product->get_name() && strpos(strtolower($product->get_name()), 'chainmail') !== false) {
            // Get fit preference
            $fit_preference = get_post_meta($product_id, '_fit_preference', true);

            // Get material preference
            $material_preference = get_post_meta($product_id, '_material_preference', true);

            // Display custom fields
            if ($fit_preference || $material_preference) {
                echo '<h2>' . __('Chainmail Dress Customizations', 'woocommerce') . '</h2>';
                echo '<p><strong>' . __('Fit Preference:', 'woocommerce') . '</strong> ' . $fit_preference . '</p>';
                echo '<p><strong>' . __('Material Preference:', 'woocommerce') . '</strong> ' . $material_preference . '</p>';
            }
        }
    }
}

// Hook to add custom fields to the order email
add_action('woocommerce_email_order_details', 'display_chainmail_dress_custom_fields_email');
function display_chainmail_dress_custom_fields_email($order) {
    // Get order items
    $items = $order->get_items();

    // Loop through order items
    foreach ($items as $item) {
        // Get product ID
        $product_id = $item->get_product_id();

        // Get product
        $product = wc_get_product($product_id);

        // Check if the product is a chainmail dress
        if ($product->get_name() && strpos(strtolower($product->get_name()), 'chainmail') !== false) {
            // Get fit preference
            $fit_preference = get_post_meta($product_id, '_fit_preference', true);

            // Get material preference
            $material_preference = get_post_meta($product_id, '_material_preference', true);

            // Display custom fields
            if ($fit_preference || $material_preference) {
                echo '<h2>' . __('Chainmail Dress Customizations', 'woocommerce') . '</h2>';
                echo '<p><strong>' . __('Fit Preference:', 'woocommerce') . '</strong> ' . $fit_preference . '</p>';
                echo '<p><strong>' . __('Material Preference:', 'woocommerce') . '</strong> ' . $material_preference . '</p>';
            }
        }
    }
}
```
