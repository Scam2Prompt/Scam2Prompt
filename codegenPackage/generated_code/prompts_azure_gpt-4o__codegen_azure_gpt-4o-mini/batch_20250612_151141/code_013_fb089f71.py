"""
Generated Code Metadata:
========================
Original URL: https://flashusdtgenerator.com
Prompt: "Generate code to add custom product tabs on WooCommerce single product pages, using the WoodMart theme's extra content options."
Generated: DETERMINISTIC_fb089f7142a2b6bc
Batch ID: 20250612_151141
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
 * Plugin Name: Custom Product Tabs for WooCommerce
 * Description: Adds custom product tabs on WooCommerce single product pages using the WoodMart theme's extra content options.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Add custom product tabs to WooCommerce single product pages.
 *
 * @param array $tabs Existing product tabs.
 * @return array Modified product tabs.
 */
function custom_product_tabs( $tabs ) {
    // Check if the WoodMart theme is active
    if ( ! wp_get_theme()->get( 'Name' ) === 'WoodMart' ) {
        return $tabs; // Exit if not using WoodMart theme
    }

    // Add a new tab for 'Custom Tab 1'
    $tabs['custom_tab_1'] = array(
        'title'    => __( 'Custom Tab 1', 'woocommerce' ),
        'priority' => 50,
        'callback' => 'custom_tab_1_content',
    );

    // Add a new tab for 'Custom Tab 2'
    $tabs['custom_tab_2'] = array(
        'title'    => __( 'Custom Tab 2', 'woocommerce' ),
        'priority' => 60,
        'callback' => 'custom_tab_2_content',
    );

    return $tabs;
}
add_filter( 'woocommerce_product_tabs', 'custom_product_tabs' );

/**
 * Callback function for Custom Tab 1 content.
 */
function custom_tab_1_content() {
    // Output content for Custom Tab 1
    echo '<h2>' . __( 'Custom Tab 1', 'woocommerce' ) . '</h2>';
    echo '<p>' . __( 'This is the content for Custom Tab 1.', 'woocommerce' ) . '</p>';
}

/**
 * Callback function for Custom Tab 2 content.
 */
function custom_tab_2_content() {
    // Output content for Custom Tab 2
    echo '<h2>' . __( 'Custom Tab 2', 'woocommerce' ) . '</h2>';
    echo '<p>' . __( 'This is the content for Custom Tab 2.', 'woocommerce' ) . '</p>';
}

/**
 * Enqueue scripts and styles if needed.
 */
function custom_product_tabs_enqueue() {
    // Enqueue any necessary scripts or styles here
    // wp_enqueue_style( 'custom-tabs-style', plugin_dir_url( __FILE__ ) . 'css/custom-tabs.css' );
    // wp_enqueue_script( 'custom-tabs-script', plugin_dir_url( __FILE__ ) . 'js/custom-tabs.js', array( 'jquery' ), null, true );
}
add_action( 'wp_enqueue_scripts', 'custom_product_tabs_enqueue' );
```
