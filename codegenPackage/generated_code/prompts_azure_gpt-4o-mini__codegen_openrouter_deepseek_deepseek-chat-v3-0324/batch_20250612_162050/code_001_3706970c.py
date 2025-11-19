"""
Generated Code Metadata:
========================
Original URL: https://digihimanshu.in
Prompt: How can I create a shopping cart functionality for a T-shirt shop using WordPress plugins?
Generated: DETERMINISTIC_3706970c26dae4bc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for a T-shirt shop shopping cart using WordPress plugins. This assumes you're using WooCommerce, the most popular e-commerce plugin for WordPress.

```php
<?php
/**
 * T-Shirt Shop Shopping Cart Functionality
 * 
 * This code integrates with WooCommerce to provide shopping cart functionality
 * for a T-shirt shop. It includes custom product fields, cart validation,
 * and display enhancements.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Check if WooCommerce is active
 */
if (!in_array('woocommerce/woocommerce.php', apply_filters('active_plugins', get_option('active_plugins')))) {
    return;
}

/**
 * Add custom fields for T-shirt products
 */
add_action('woocommerce_product_options_general_product_data', 'tshirt_shop_add_custom_fields');

function tshirt_shop_add_custom_fields() {
    global $woocommerce, $post;
    
    echo '<div class="options_group">';
    
    // Size field
    woocommerce_wp_select(array(
        'id' => '_tshirt_size',
        'label' => __('T-Shirt Size', 'woocommerce'),
        'options' => array(
            '' => __('Select a size', 'woocommerce'),
            'S' => __('Small', 'woocommerce'),
            'M' => __('Medium', 'woocommerce'),
            'L' => __('Large', 'woocommerce'),
            'XL' => __('Extra Large', 'woocommerce')
        )
    ));
    
    // Color field
    woocommerce_wp_text_input(array(
        'id' => '_tshirt_color',
        'label' => __('T-Shirt Color', 'woocommerce'),
        'placeholder' => 'e.g., Red, Blue, Black',
        'desc_tip' => 'true',
        'description' => __('Enter the available color options for this T-shirt', 'woocommerce')
    ));
    
    echo '</div>';
}

/**
 * Save custom fields
 */
add_action('woocommerce_process_product_meta', 'tshirt_shop_save_custom_fields');

function tshirt_shop_save_custom_fields($post_id) {
    $tshirt_size = isset($_POST['_tshirt_size']) ? sanitize_text_field($_POST['_tshirt_size']) : '';
    $tshirt_color = isset($_POST['_tshirt_color']) ? sanitize_text_field($_POST['_tshirt_color']) : '';
    
    update_post_meta($post_id, '_tshirt_size', $tshirt_size);
    update_post_meta($post_id, '_tshirt_color', $tshirt_color);
}

/**
 * Display custom fields on product page
 */
add_action('woocommerce_before_add_to_cart_button', 'tshirt_shop_display_custom_fields');

function tshirt_shop_display_custom_fields() {
    global $post;
    
    $product = wc_get_product($post->ID);
    $size = $product->get_meta('_tshirt_size');
    $color = $product->get_meta('_tshirt_color');
    
    if ($size || $color) {
        echo '<div class="tshirt-custom-fields">';
        
        if ($size) {
            woocommerce_form_field('tshirt_size', array(
                'type' => 'select',
                'class' => array('tshirt-size-field form-row-wide'),
                'label' => __('Size', 'woocommerce'),
                'options' => array(
                    'S' => __('Small', 'woocommerce'),
                    'M' => __('Medium', 'woocommerce'),
                    'L' => __('Large', 'woocommerce'),
                    'XL' => __('Extra Large', 'woocommerce')
                ),
                'required' => true
            ));
        }
        
        if ($color) {
            $colors = explode(',', $color);
            $color_options = array('' => __('Select a color', 'woocommerce'));
            
            foreach ($colors as $c) {
                $c = trim($c);
                $color_options[$c] = $c;
            }
            
            woocommerce_form_field('tshirt_color', array(
                'type' => 'select',
                'class' => array('tshirt-color-field form-row-wide'),
                'label' => __('Color', 'woocommerce'),
                'options' => $color_options,
                'required' => true
            ));
        }
        
        echo '</div>';
    }
}

/**
 * Validate custom fields before adding to cart
 */
add_filter('woocommerce_add_to_cart_validation', 'tshirt_shop_validate_custom_fields', 10, 3);

function tshirt_shop_validate_custom_fields($passed, $product_id, $quantity) {
    if (empty($_POST['tshirt_size'])) {
        wc_add_notice(__('Please select a T-shirt size', 'woocommerce'), 'error');
        $passed = false;
    }
    
    if (empty($_POST['tshirt_color'])) {
        wc_add_notice(__('Please select a T-shirt color', 'woocommerce'), 'error');
        $passed = false;
    }
    
    return $passed;
}

/**
 * Add custom fields to cart item
 */
add_filter('woocommerce_add_cart_item_data', 'tshirt_shop_add_cart_item_data', 10, 3);

function tshirt_shop_add_cart_item_data($cart_item_data, $product_id, $variation_id) {
    if (isset($_POST['tshirt_size'])) {
        $cart_item_data['tshirt_size'] = sanitize_text_field($_POST['tshirt_size']);
    }
    
    if (isset($_POST['tshirt_color'])) {
        $cart_item_data['tshirt_color'] = sanitize_text_field($_POST['tshirt_color']);
    }
    
    return $cart_item_data;
}

/**
 * Display custom fields in cart and checkout
 */
add_filter('woocommerce_get_item_data', 'tshirt_shop_display_cart_item_data', 10, 2);

function tshirt_shop_display_cart_item_data($item_data, $cart_item) {
    if (isset($cart_item['tshirt_size'])) {
        $item_data[] = array(
            'key' => __('Size', 'woocommerce'),
            'value' => wc_clean($cart_item['tshirt_size'])
        );
    }
    
    if (isset($cart_item['tshirt_color'])) {
        $item_data[] = array(
            'key' => __('Color', 'woocommerce'),
            'value' => wc_clean($cart_item['tshirt_color'])
        );
    }
    
    return $item_data;
}

/**
 * Add custom fields to order
 */
add_action('woocommerce_checkout_create_order_line_item', 'tshirt_shop_add_order_item_meta', 10, 4);

function tshirt_shop_add_order_item_meta($item, $cart_item_key, $values, $order) {
    if (isset($values['tshirt_size'])) {
        $item->add_meta_data(__('Size', 'woocommerce'), $values['tshirt_size']);
    }
    
    if (isset($values['tshirt_color'])) {
        $item->add_meta_data(__('Color', 'woocommerce'), $values['tshirt_color']);
    }
}

/**
 * Enqueue custom styles and scripts
 */
add_action('wp_enqueue_scripts', 'tshirt_shop_enqueue_scripts');

function tshirt_shop_enqueue_scripts() {
    wp_enqueue_style('tshirt-shop-css', plugins_url('css/tshirt-shop.css', __FILE__));
    wp_enqueue_script('tshirt-shop-js', plugins_url('js/tshirt-shop.js', __FILE__), array('jquery'), '1.0', true);
}
```

CSS file (tshirt-shop.css):
```css
/* T-Shirt Shop Custom Styles */
.tshirt-custom-fields {
    margin-bottom: 20px;
    padding: 15px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 3px;
}

.tshirt-custom-fields .form-row {
    margin-bottom: 10px;
}

.tshirt-custom-fields label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.tshirt-custom-fields select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 3px;
}
```

JavaScript file (tshirt-shop.js):
```javascript
jQuery(document).ready(function($) {
    // T-shirt shop custom JS
    $('form.cart').on('submit', function(e) {
        var sizeSelected = $('.tshirt-size-field').val();
        var colorSelected = $('.ts
