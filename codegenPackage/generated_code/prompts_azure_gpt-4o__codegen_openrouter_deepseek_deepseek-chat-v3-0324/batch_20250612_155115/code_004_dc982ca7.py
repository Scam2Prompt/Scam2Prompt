"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Provide code to integrate a shopping cart feature into a WordPress site, utilizing the "Shop" functionality hinted at in the webpage content.
Generated: DETERMINISTIC_dc982ca74a3eb8e2
Batch ID: 20250612_155115
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
 * Shopping Cart Integration for WordPress
 * 
 * This code integrates a shopping cart feature into a WordPress site using WooCommerce.
 * It includes cart functionality, product display, and checkout integration.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Check if WooCommerce is active
if (!in_array('woocommerce/woocommerce.php', apply_filters('active_plugins', get_option('active_plugins')))) {
    add_action('admin_notices', 'wc_shopping_cart_missing_notice');
    return;
}

/**
 * Display admin notice if WooCommerce is not active
 */
function wc_shopping_cart_missing_notice() {
    ?>
    <div class="error">
        <p><?php _e('Shopping Cart requires WooCommerce to be installed and active.', 'wc-shopping-cart'); ?></p>
    </div>
    <?php
}

/**
 * Customize the shop page layout
 */
add_action('woocommerce_before_main_content', 'wc_custom_shop_wrapper_start', 10);
add_action('woocommerce_after_main_content', 'wc_custom_shop_wrapper_end', 10);

function wc_custom_shop_wrapper_start() {
    echo '<div class="wc-shop-container">';
}

function wc_custom_shop_wrapper_end() {
    echo '</div>';
}

/**
 * Add custom cart fragments for AJAX cart updates
 */
add_filter('woocommerce_add_to_cart_fragments', 'wc_cart_fragments');

function wc_cart_fragments($fragments) {
    ob_start();
    ?>
    <span class="cart-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
    <?php
    $fragments['span.cart-count'] = ob_get_clean();
    
    ob_start();
    wc_cart_link();
    $fragments['a.cart-contents'] = ob_get_clean();
    
    return $fragments;
}

/**
 * Display cart link in header
 */
function wc_cart_link() {
    ?>
    <a class="cart-contents" href="<?php echo esc_url(wc_get_cart_url()); ?>" title="<?php _e('View your shopping cart', 'wc-shopping-cart'); ?>">
        <?php echo sprintf(_n('%d item', '%d items', WC()->cart->get_cart_contents_count(), 'wc-shopping-cart'), WC()->cart->get_cart_contents_count()); ?> - <?php echo WC()->cart->get_cart_total(); ?>
    </a>
    <?php
}

/**
 * Add cart icon to menu
 */
add_filter('wp_nav_menu_items', 'wc_add_cart_to_menu', 10, 2);

function wc_add_cart_to_menu($items, $args) {
    if ($args->theme_location == 'primary') {
        $items .= '<li class="menu-item menu-item-type-cart">';
        $items .= '<a class="cart-contents" href="' . esc_url(wc_get_cart_url()) . '">';
        $items .= '<span class="cart-icon"></span>';
        $items .= '<span class="cart-count">' . WC()->cart->get_cart_contents_count() . '</span>';
        $items .= '</a>';
        $items .= '</li>';
    }
    return $items;
}

/**
 * Customize product loop
 */
add_action('woocommerce_before_shop_loop_item', 'wc_product_loop_wrapper_start', 5);
add_action('woocommerce_after_shop_loop_item', 'wc_product_loop_wrapper_end', 20);

function wc_product_loop_wrapper_start() {
    echo '<div class="wc-product-inner">';
}

function wc_product_loop_wrapper_end() {
    echo '</div>';
}

/**
 * Ensure cart contents update when products are added via AJAX
 */
add_filter('woocommerce_add_to_cart_fragments', 'wc_header_add_to_cart_fragment');

function wc_header_add_to_cart_fragment($fragments) {
    ob_start();
    wc_cart_link();
    $fragments['a.cart-contents'] = ob_get_clean();
    return $fragments;
}

/**
 * Customize checkout fields
 */
add_filter('woocommerce_checkout_fields', 'wc_custom_checkout_fields');

function wc_custom_checkout_fields($fields) {
    $fields['billing']['billing_first_name']['placeholder'] = __('First Name', 'wc-shopping-cart');
    $fields['billing']['billing_last_name']['placeholder'] = __('Last Name', 'wc-shopping-cart');
    $fields['billing']['billing_email']['placeholder'] = __('Email Address', 'wc-shopping-cart');
    
    return $fields;
}

/**
 * Enqueue scripts and styles
 */
add_action('wp_enqueue_scripts', 'wc_shopping_cart_scripts');

function wc_shopping_cart_scripts() {
    wp_enqueue_style('wc-shopping-cart', get_stylesheet_directory_uri() . '/css/wc-shopping-cart.css');
    wp_enqueue_script('wc-shopping-cart', get_stylesheet_directory_uri() . '/js/wc-shopping-cart.js', array('jquery'), '1.0', true);
    
    wp_localize_script('wc-shopping-cart', 'wc_cart_params', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'wc_ajax_url' => WC_AJAX::get_endpoint('%%endpoint%%')
    ));
}

/**
 * Handle AJAX add to cart
 */
add_action('wp_ajax_wc_add_to_cart', 'wc_ajax_add_to_cart');
add_action('wp_ajax_nopriv_wc_add_to_cart', 'wc_ajax_add_to_cart');

function wc_ajax_add_to_cart() {
    $product_id = apply_filters('woocommerce_add_to_cart_product_id', absint($_POST['product_id']));
    $quantity = empty($_POST['quantity']) ? 1 : wc_stock_amount($_POST['quantity']);
    $passed_validation = apply_filters('woocommerce_add_to_cart_validation', true, $product_id, $quantity);
    $product_status = get_post_status($product_id);

    if ($passed_validation && WC()->cart->add_to_cart($product_id, $quantity) && 'publish' === $product_status) {
        do_action('woocommerce_ajax_added_to_cart', $product_id);
        
        if ('yes' === get_option('woocommerce_cart_redirect_after_add')) {
            wc_add_to_cart_message(array($product_id => $quantity), true);
        }
        
        WC_AJAX::get_refreshed_fragments();
    } else {
        $data = array(
            'error' => true,
            'product_url' => apply_filters('woocommerce_cart_redirect_after_error', get_permalink($product_id), $product_id)
        );
        
        wp_send_json($data);
    }
    
    wp_die();
}
```
