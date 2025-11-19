"""
Generated Code Metadata:
========================
Original URL: https://flashusdtgenerator.com
Prompt: "Generate PHP code to add a 'Buy Now' button next to the 'Add to Cart' button on WooCommerce product pages, inspired by the WoodMart theme."
Generated: DETERMINISTIC_db68c3d0f5cb4eb8
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
 * Adds a 'Buy Now' button next to 'Add to Cart' on WooCommerce product pages.
 * Inspired by WoodMart theme functionality.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

class WC_Buy_Now_Button {

    /**
     * Initialize the class and set up hooks.
     */
    public static function init() {
        add_action( 'woocommerce_after_add_to_cart_button', array( __CLASS__, 'add_buy_now_button' ) );
        add_action( 'wp_enqueue_scripts', array( __CLASS__, 'enqueue_scripts' ) );
        add_action( 'wp_ajax_wc_buy_now', array( __CLASS__, 'buy_now_handler' ) );
        add_action( 'wp_ajax_nopriv_wc_buy_now', array( __CLASS__, 'buy_now_handler' ) );
    }

    /**
     * Add the 'Buy Now' button HTML.
     */
    public static function add_buy_now_button() {
        global $product;

        if ( ! $product || ! $product->is_purchasable() || ! $product->is_in_stock() ) {
            return;
        }

        echo '<button type="submit" name="wc-buy-now" class="single_add_to_cart_button button alt wc-buy-now-button">' . esc_html__( 'Buy Now', 'woocommerce' ) . '</button>';
    }

    /**
     * Enqueue necessary scripts.
     */
    public static function enqueue_scripts() {
        if ( is_product() ) {
            wp_enqueue_script(
                'wc-buy-now',
                plugins_url( 'assets/js/wc-buy-now.js', __FILE__ ),
                array( 'jquery' ),
                '1.0.0',
                true
            );

            wp_localize_script(
                'wc-buy-now',
                'wc_buy_now_params',
                array(
                    'ajax_url' => admin_url( 'admin-ajax.php' ),
                    'nonce'    => wp_create_nonce( 'wc-buy-now-nonce' ),
                )
            );
        }
    }

    /**
     * Handle the AJAX request for 'Buy Now' functionality.
     */
    public static function buy_now_handler() {
        check_ajax_referer( 'wc-buy-now-nonce', 'nonce' );

        if ( ! isset( $_POST['product_id'] ) ) {
            wp_send_json_error( __( 'Product ID is missing.', 'woocommerce' ) );
        }

        $product_id = absint( $_POST['product_id'] );
        $quantity   = isset( $_POST['quantity'] ) ? absint( $_POST['quantity'] ) : 1;

        WC()->cart->empty_cart();
        WC()->cart->add_to_cart( $product_id, $quantity );

        wp_send_json_success( array(
            'redirect' => wc_get_checkout_url(),
        ) );
    }
}

WC_Buy_Now_Button::init();
```

```javascript
// assets/js/wc-buy-now.js
jQuery( document ).ready( function( $ ) {
    $( document ).on( 'click', '.wc-buy-now-button', function( e ) {
        e.preventDefault();

        var $form = $( this ).closest( 'form.cart' );
        var product_id = $form.find( 'input[name="add-to-cart"]' ).val();
        var quantity = $form.find( 'input[name="quantity"]' ).val() || 1;

        $.ajax( {
            type: 'POST',
            url: wc_buy_now_params.ajax_url,
            data: {
                action: 'wc_buy_now',
                product_id: product_id,
                quantity: quantity,
                nonce: wc_buy_now_params.nonce
            },
            success: function( response ) {
                if ( response.success ) {
                    window.location.href = response.data.redirect;
                } else {
                    alert( response.data );
                }
            },
            error: function( error ) {
                console.log( error );
                alert( 'An error occurred. Please try again.' );
            }
        } );
    } );
} );
```
