"""
Generated Code Metadata:
========================
Original URL: https://metaexch.info
Prompt: Develop a WooCommerce shop page for a WordPress site, inspired by the "Shop" section mentioned on the webpage.
Generated: DETERMINISTIC_edd612fb91131ed7
Batch ID: 20250612_154201
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
 * WooCommerce Shop Page Customization
 * 
 * This code enhances the default WooCommerce shop page with custom styling and layout.
 * It hooks into WooCommerce templates to modify the shop page appearance.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Enqueue custom styles for the shop page
 */
function custom_woocommerce_shop_styles() {
    if (is_shop() || is_product_category() || is_product_tag()) {
        wp_enqueue_style(
            'custom-woocommerce-shop',
            get_stylesheet_directory_uri() . '/css/custom-woocommerce-shop.css',
            array(),
            filemtime(get_stylesheet_directory() . '/css/custom-woocommerce-shop.css')
        );
    }
}
add_action('wp_enqueue_scripts', 'custom_woocommerce_shop_styles');

/**
 * Modify the number of products displayed per page
 */
function custom_woocommerce_products_per_page($cols) {
    return 12; // Display 12 products per page
}
add_filter('loop_shop_per_page', 'custom_woocommerce_products_per_page', 20);

/**
 * Change number of products per row
 */
function custom_woocommerce_loop_columns() {
    return 3; // Display 3 products per row
}
add_filter('loop_shop_columns', 'custom_woocommerce_loop_columns', 20);

/**
 * Modify product thumbnail size on shop page
 */
function custom_woocommerce_image_sizes($size) {
    $size['width'] = 300;
    $size['height'] = 300;
    $size['crop'] = 1;
    return $size;
}
add_filter('woocommerce_get_image_size_shop_catalog', 'custom_woocommerce_image_sizes');

/**
 * Customize product title on shop page
 */
function custom_woocommerce_product_title() {
    echo '<h3 class="woocommerce-loop-product__title">' . get_the_title() . '</h3>';
}
remove_action('woocommerce_shop_loop_item_title', 'woocommerce_template_loop_product_title', 10);
add_action('woocommerce_shop_loop_item_title', 'custom_woocommerce_product_title', 10);

/**
 * Add custom content after shop loop item
 */
function custom_after_shop_loop_item() {
    echo '<div class="product-meta">';
    woocommerce_template_loop_price();
    woocommerce_template_loop_add_to_cart();
    echo '</div>';
}
add_action('woocommerce_after_shop_loop_item', 'custom_after_shop_loop_item', 10);

/**
 * Customize shop page breadcrumb
 */
function custom_woocommerce_breadcrumb_defaults($defaults) {
    $defaults['delimiter'] = ' &gt; ';
    $defaults['wrap_before'] = '<nav class="woocommerce-breadcrumb" itemprop="breadcrumb">';
    $defaults['wrap_after'] = '</nav>';
    $defaults['before'] = '';
    $defaults['after'] = '';
    $defaults['home'] = _x('Home', 'breadcrumb', 'woocommerce');
    return $defaults;
}
add_filter('woocommerce_breadcrumb_defaults', 'custom_woocommerce_breadcrumb_defaults');

/**
 * Remove default WooCommerce sidebar and add custom one
 */
function custom_woocommerce_sidebar() {
    if (is_shop() || is_product_category() || is_product_tag()) {
        remove_action('woocommerce_sidebar', 'woocommerce_get_sidebar', 10);
        get_sidebar('shop');
    }
}
add_action('wp', 'custom_woocommerce_sidebar');

/**
 * Custom shop page title
 */
function custom_woocommerce_page_title($page_title) {
    if (is_shop()) {
        $page_title = 'Our Products';
    }
    return $page_title;
}
add_filter('woocommerce_page_title', 'custom_woocommerce_page_title');

/**
 * Customize product sorting options
 */
function custom_woocommerce_catalog_orderby($options) {
    $options = array(
        'menu_order' => __('Default sorting', 'woocommerce'),
        'popularity' => __('Sort by popularity', 'woocommerce'),
        'rating'     => __('Sort by average rating', 'woocommerce'),
        'date'       => __('Sort by newness', 'woocommerce'),
        'price'      => __('Sort by price: low to high', 'woocommerce'),
        'price-desc' => __('Sort by price: high to low', 'woocommerce'),
    );
    return $options;
}
add_filter('woocommerce_catalog_orderby', 'custom_woocommerce_catalog_orderby');

/**
 * Add custom wrapper around shop content
 */
function custom_woocommerce_before_main_content() {
    echo '<div class="custom-shop-container">';
    echo '<div class="custom-shop-content">';
}
add_action('woocommerce_before_main_content', 'custom_woocommerce_before_main_content', 5);

function custom_woocommerce_after_main_content() {
    echo '</div></div>';
}
add_action('woocommerce_after_main_content', 'custom_woocommerce_after_main_content', 50);
```
