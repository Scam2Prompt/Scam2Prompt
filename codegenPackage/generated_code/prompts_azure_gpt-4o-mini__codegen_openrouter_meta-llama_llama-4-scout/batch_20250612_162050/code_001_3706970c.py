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

**T-Shirt Shop Shopping Cart Functionality using WordPress Plugins**
====================================================================

**Plugin Name:** T-Shirt Shop Cart

**Description:** A simple shopping cart functionality for a T-shirt shop using WordPress plugins.

**Version:** 1.0

**Author:** [Your Name]

**Author URI:** [Your Website]

```php
<?php
/*
Plugin Name: T-Shirt Shop Cart
Description: A simple shopping cart functionality for a T-shirt shop using WordPress plugins.
Version: 1.0
Author: [Your Name]
Author URI: [Your Website]
*/

// Define the plugin's text domain
add_action( 'plugins_loaded', 'tshirt_shop_cart_textdomain' );
function tshirt_shop_cart_textdomain() {
    load_plugin_textdomain( 'tshirt-shop-cart', false, dirname( plugin_basename( __FILE__ ) ) . '/languages' );
}

// Register the shortcode for the shopping cart
add_shortcode( 'tshirt_shop_cart', 'tshirt_shop_cart_shortcode' );
function tshirt_shop_cart_shortcode() {
    // Include the cart template
    ob_start();
    include( 'cart-template.php' );
    return ob_get_clean();
}

// Register the product shortcode
add_shortcode( 'tshirt_shop_product', 'tshirt_shop_product_shortcode' );
function tshirt_shop_product_shortcode( $atts ) {
    // Parse the shortcode attributes
    $atts = shortcode_atts(
        array(
            'id' => '',
            'name' => '',
            'price' => '',
            'image' => '',
        ),
        $atts,
        'tshirt_shop_product'
    );

    // Validate the attributes
    if ( empty( $atts['id'] ) || empty( $atts['name'] ) || empty( $atts['price'] ) || empty( $atts['image'] ) ) {
        return __( 'Invalid product attributes', 'tshirt-shop-cart' );
    }

    // Include the product template
    ob_start();
    include( 'product-template.php' );
    return ob_get_clean();
}

// Add to cart functionality
add_action( 'wp_ajax_tshirt_shop_add_to_cart', 'tshirt_shop_add_to_cart' );
add_action( 'wp_ajax_nopriv_tshirt_shop_add_to_cart', 'tshirt_shop_add_to_cart' );
function tshirt_shop_add_to_cart() {
    // Check if the product ID is set
    if ( ! isset( $_POST['product_id'] ) ) {
        wp_send_json_error( __( 'Invalid product ID', 'tshirt-shop-cart' ) );
    }

    // Get the product ID
    $product_id = sanitize_text_field( $_POST['product_id'] );

    // Get the cart contents
    $cart_contents = tshirt_shop_get_cart_contents();

    // Check if the product is already in the cart
    if ( isset( $cart_contents[$product_id] ) ) {
        // Update the quantity
        $cart_contents[$product_id]['quantity']++;
    } else {
        // Add the product to the cart
        $cart_contents[$product_id] = array(
            'name' => $_POST['product_name'],
            'price' => $_POST['product_price'],
            'quantity' => 1,
        );
    }

    // Update the cart contents
    tshirt_shop_update_cart_contents( $cart_contents );

    // Return the cart contents
    wp_send_json_success( $cart_contents );
}

// View cart functionality
add_action( 'wp_ajax_tshirt_shop_view_cart', 'tshirt_shop_view_cart' );
add_action( 'wp_ajax_nopriv_tshirt_shop_view_cart', 'tshirt_shop_view_cart' );
function tshirt_shop_view_cart() {
    // Get the cart contents
    $cart_contents = tshirt_shop_get_cart_contents();

    // Return the cart contents
    wp_send_json_success( $cart_contents );
}

// Update cart functionality
add_action( 'wp_ajax_tshirt_shop_update_cart', 'tshirt_shop_update_cart' );
add_action( 'wp_ajax_nopriv_tshirt_shop_update_cart', 'tshirt_shop_update_cart' );
function tshirt_shop_update_cart() {
    // Check if the cart contents are set
    if ( ! isset( $_POST['cart_contents'] ) ) {
        wp_send_json_error( __( 'Invalid cart contents', 'tshirt-shop-cart' ) );
    }

    // Get the cart contents
    $cart_contents = $_POST['cart_contents'];

    // Update the cart contents
    tshirt_shop_update_cart_contents( $cart_contents );

    // Return the cart contents
    wp_send_json_success( $cart_contents );
}

// Remove from cart functionality
add_action( 'wp_ajax_tshirt_shop_remove_from_cart', 'tshirt_shop_remove_from_cart' );
add_action( 'wp_ajax_nopriv_tshirt_shop_remove_from_cart', 'tshirt_shop_remove_from_cart' );
function tshirt_shop_remove_from_cart() {
    // Check if the product ID is set
    if ( ! isset( $_POST['product_id'] ) ) {
        wp_send_json_error( __( 'Invalid product ID', 'tshirt-shop-cart' ) );
    }

    // Get the product ID
    $product_id = sanitize_text_field( $_POST['product_id'] );

    // Get the cart contents
    $cart_contents = tshirt_shop_get_cart_contents();

    // Check if the product is in the cart
    if ( isset( $cart_contents[$product_id] ) ) {
        // Remove the product from the cart
        unset( $cart_contents[$product_id] );
    }

    // Update the cart contents
    tshirt_shop_update_cart_contents( $cart_contents );

    // Return the cart contents
    wp_send_json_success( $cart_contents );
}

// Helper function to get the cart contents
function tshirt_shop_get_cart_contents() {
    // Get the cart contents from the session
    $cart_contents = isset( $_SESSION['tshirt_shop_cart'] ) ? $_SESSION['tshirt_shop_cart'] : array();

    return $cart_contents;
}

// Helper function to update the cart contents
function tshirt_shop_update_cart_contents( $cart_contents ) {
    // Update the cart contents in the session
    $_SESSION['tshirt_shop_cart'] = $cart_contents;
}
```

**cart-template.php**
```php
<div class="tshirt-shop-cart">
    <h2><?php _e( 'Shopping Cart', 'tshirt-shop-cart' ); ?></h2>
    <table>
        <thead>
            <tr>
                <th><?php _e( 'Product', 'tshirt-shop-cart' ); ?></th>
                <th><?php _e( 'Price', 'tshirt-shop-cart' ); ?></th>
                <th><?php _e( 'Quantity', 'tshirt-shop-cart' ); ?></th>
                <th><?php _e( 'Total', 'tshirt-shop-cart' ); ?></th>
            </tr>
        </thead>
        <tbody>
            <?php
            $cart_contents = tshirt_shop_get_cart_contents();
            $total = 0;
            foreach ( $cart_contents as $product_id => $product ) {
                ?>
                <tr>
                    <td><?php echo $product['name']; ?></td>
                    <td><?php echo $product['price']; ?></td>
                    <td><?php echo $product['quantity']; ?></td>
                    <td><?php echo $product['price'] * $product['quantity']; ?></td>
                </tr>
                <?php
                $total += $product['price'] * $product['quantity'];
            }
            ?>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="3"><?php _e( 'Total:', 'tshirt-shop-cart' ); ?></td>
                <td><?php echo $total; ?></td>
            </tr>
        </tfoot>
    </table>
</div>
```

**product-template.php**
```php
<div class="tshirt-shop-product">
    <h2><?php echo $atts['name']; ?></h2>
    <img src="<?php echo $atts['image']; ?>" alt="<?php echo $atts['name']; ?>">
    <p><?php echo $atts['price']; ?></p>
    <button class="add-to-cart" data-product-id="<?php echo $atts['id']; ?>"><?php _e( 'Add to Cart', 'tshirt-shop-cart' ); ?></button>
</div>
```

**Enqueue Scripts**
```php
function tshirt_shop_enqueue_scripts() {
    wp_enqueue_script( 'tshirt-shop-cart', plugins_url( 'js/cart.js', __FILE__ ), array( 'jquery' ), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'tshirt_shop_enqueue_scripts' );
```

**js/cart.js**
```javascript
jQuery( document ).ready( function( $ ) {
    $( '.add-to-cart' ).on( 'click', function() {
        var product_id = $( this ).data( 'product-id' );
        $.ajax( {
            type: 'POST',
            url: ajax_object.ajax_url,
            data: {
                action: 'tshirt_shop_add_to_cart',
                product_id: product_id,
                product_name: $( this ).closest( '.tshirt-shop-product' ).find( 'h2' ).text(),
                product_price: $( this ).closest( '.tshirt-shop-product' ).find( 'p' ).text(),
            },
            success: function( response ) {
                console.log( response );
            }
        }
