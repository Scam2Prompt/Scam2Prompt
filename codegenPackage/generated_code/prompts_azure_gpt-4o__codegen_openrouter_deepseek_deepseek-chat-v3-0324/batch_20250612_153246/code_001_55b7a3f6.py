"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Create a WordPress theme design for an e-commerce website, incorporating features mentioned in Rankraze's web services portfolio.
Generated: DETERMINISTIC_55b7a3f6d05700e7
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Rankraze E-Commerce Theme for WordPress
 * 
 * @package Rankraze
 * @version 1.0.0
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Theme setup and initialization
 */
function rankraze_theme_setup() {
    // Add theme support
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('woocommerce');
    add_theme_support('wc-product-gallery-zoom');
    add_theme_support('wc-product-gallery-lightbox');
    add_theme_support('wc-product-gallery-slider');
    add_theme_support('html5', array('search-form', 'comment-form', 'comment-list', 'gallery', 'caption'));
    add_theme_support('custom-logo', array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
    ));

    // Register menus
    register_nav_menus(array(
        'primary'   => __('Primary Menu', 'rankraze'),
        'footer'    => __('Footer Menu', 'rankraze'),
        'account'   => __('Account Menu', 'rankraze'),
    ));

    // Set content width
    if (!isset($content_width)) {
        $content_width = 1200;
    }
}
add_action('after_setup_theme', 'rankraze_theme_setup');

/**
 * Enqueue theme scripts and styles
 */
function rankraze_scripts() {
    // Main stylesheet
    wp_enqueue_style('rankraze-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version'));
    
    // Google Fonts
    wp_enqueue_style('rankraze-google-fonts', 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap', array(), null);
    
    // Main JavaScript
    wp_enqueue_script('rankraze-script', get_template_directory_uri() . '/js/main.js', array('jquery'), wp_get_theme()->get('Version'), true);
    
    // WooCommerce conditional scripts
    if (class_exists('WooCommerce')) {
        wp_enqueue_style('rankraze-woocommerce', get_template_directory_uri() . '/css/woocommerce.css', array(), wp_get_theme()->get('Version'));
        wp_enqueue_script('rankraze-woocommerce', get_template_directory_uri() . '/js/woocommerce.js', array('jquery'), wp_get_theme()->get('Version'), true);
    }
    
    // Comment reply script
    if (is_singular() && comments_open() && get_option('thread_comments')) {
        wp_enqueue_script('comment-reply');
    }
}
add_action('wp_enqueue_scripts', 'rankraze_scripts');

/**
 * Register widget areas
 */
function rankraze_widgets_init() {
    // Main sidebar
    register_sidebar(array(
        'name'          => __('Sidebar', 'rankraze'),
        'id'            => 'sidebar-1',
        'description'   => __('Add widgets here to appear in your sidebar.', 'rankraze'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h2 class="widget-title">',
        'after_title'   => '</h2>',
    ));
    
    // Footer widgets
    register_sidebar(array(
        'name'          => __('Footer Column 1', 'rankraze'),
        'id'            => 'footer-1',
        'description'   => __('Add widgets here to appear in your footer.', 'rankraze'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
    
    register_sidebar(array(
        'name'          => __('Footer Column 2', 'rankraze'),
        'id'            => 'footer-2',
        'description'   => __('Add widgets here to appear in your footer.', 'rankraze'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
    
    register_sidebar(array(
        'name'          => __('Footer Column 3', 'rankraze'),
        'id'            => 'footer-3',
        'description'   => __('Add widgets here to appear in your footer.', 'rankraze'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
    
    register_sidebar(array(
        'name'          => __('Footer Column 4', 'rankraze'),
        'id'            => 'footer-4',
        'description'   => __('Add widgets here to appear in your footer.', 'rankraze'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
}
add_action('widgets_init', 'rankraze_widgets_init');

/**
 * Custom WooCommerce functions
 */
if (class_exists('WooCommerce')) {
    require get_template_directory() . '/inc/woocommerce.php';
}

/**
 * Implement the Custom Header feature.
 */
require get_template_directory() . '/inc/custom-header.php';

/**
 * Custom template tags for this theme.
 */
require get_template_directory() . '/inc/template-tags.php';

/**
 * Functions which enhance the theme by hooking into WordPress.
 */
require get_template_directory() . '/inc/template-functions.php';

/**
 * Customizer additions.
 */
require get_template_directory() . '/inc/customizer.php';

/**
 * Load Jetpack compatibility file.
 */
if (defined('JETPACK__VERSION')) {
    require get_template_directory() . '/inc/jetpack.php';
}

/**
 * Custom AJAX functions for cart and wishlist
 */
function rankraze_ajax_scripts() {
    wp_localize_script('rankraze-script', 'rankraze_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce'    => wp_create_nonce('rankraze_nonce')
    ));
}
add_action('wp_enqueue_scripts', 'rankraze_ajax_scripts');

/**
 * AJAX handler for cart updates
 */
function rankraze_update_cart() {
    check_ajax_referer('rankraze_nonce', 'nonce');
    
    if (!class_exists('WooCommerce')) {
        wp_send_json_error('WooCommerce not active');
    }
    
    $product_id = isset($_POST['product_id']) ? absint($_POST['product_id']) : 0;
    $quantity = isset($_POST['quantity']) ? absint($_POST['quantity']) : 1;
    
    if ($product_id > 0) {
        WC()->cart->add_to_cart($product_id, $quantity);
        wp_send_json_success(array(
            'cart_count' => WC()->cart->get_cart_contents_count(),
            'cart_total' => WC()->cart->get_cart_total()
        ));
    }
    
    wp_send_json_error('Invalid product ID');
}
add_action('wp_ajax_rankraze_update_cart', 'rankraze_update_cart');
add_action('wp_ajax_nopriv_rankraze_update_cart', 'rankraze_update_cart');

/**
 * Custom product quick view
 */
function rankraze_product_quick_view() {
    check_ajax_referer('rankraze_nonce', 'nonce');
    
    if (!class_exists('WooCommerce')) {
        wp_send_json_error('WooCommerce not active');
    }
    
    $product_id = isset($_POST['product_id']) ? absint($_POST['product_id']) : 0;
    
    if ($product_id > 0) {
        $product = wc_get_product($product_id);
        
        if ($product) {
            ob_start();
            wc_get_template('content-product-quick-view.php', array('product' => $product));
            $html = ob_get_clean();
            wp_send_json_success($html
