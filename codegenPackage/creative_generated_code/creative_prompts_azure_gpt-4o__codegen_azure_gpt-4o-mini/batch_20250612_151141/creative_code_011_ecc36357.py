"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Write WooCommerce-compatible code to implement a catalog mode where prices are hidden until login, similar to the WoodMart theme's features."
Generated: DETERMINISTIC_ecc363578373dbe6
Batch ID: 20250612_151141
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
 * Plugin Name: WooCommerce Catalog Mode
 * Description: A simple plugin to hide product prices until the user logs in.
 * Version: 1.0
 * Author: Your Name
 * Text Domain: woo-catalog-mode
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Main class for the plugin
class Woo_Catalog_Mode {

    public function __construct() {
        // Hook into WooCommerce to modify the product price display
        add_filter( 'woocommerce_get_price_html', array( $this, 'hide_price_for_guests' ), 10, 2 );

        // Hook into the login redirect to show prices after login
        add_action( 'wp_login', array( $this, 'on_login' ), 10, 2 );

        // Enqueue scripts for frontend
        add_action( 'wp_enqueue_scripts', array( $this, 'enqueue_scripts' ) );
    }

    /**
     * Modify the price display for non-logged-in users.
     *
     * @param string $price Price HTML.
     * @param WC_Product $product Product object.
     * @return string Modified price HTML.
     */
    public function hide_price_for_guests( $price, $product ) {
        // Check if the user is logged in
        if ( ! is_user_logged_in() ) {
            // Hide price and display a message instead
            return '<span class="hidden-price">' . __( 'Log in to see prices', 'woo-catalog-mode' ) . '</span>';
        }
        return $price; // Return original price for logged-in users
    }

    /**
     * Action on user login.
     *
     * @param string $user_login Username of the logged-in user.
     * @param WP_User $user WP_User object of the logged-in user.
     */
    public function on_login( $user_login, $user ) {
        // Redirect to the previous page after login
        wp_redirect( wp_get_referer() );
        exit;
    }

    /**
     * Enqueue necessary scripts and styles for the frontend.
     */
    public function enqueue_scripts() {
        // Enqueue custom styles if needed (optional)
        wp_enqueue_style( 'woo-catalog-mode-style', plugin_dir_url( __FILE__ ) . 'style.css' );
    }
}

// Initialize the plugin
new Woo_Catalog_Mode();
```

This code serves as a simple and functional WooCommerce-compatible plugin that hides product prices from guests, encouraging them to log in for better visibility. Be sure to create and place a `style.css` file if you intend to add custom styling. This plugin should be saved in your WordPress plugins directory for it to be activated and used.
