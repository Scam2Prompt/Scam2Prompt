"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Create a WordPress plugin for managing product inventory and generating notifications, inspired by Enorness's e-commerce solutions.
Generated: DETERMINISTIC_8250a01607825f91
Batch ID: 20250612_153314
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
 * Plugin Name: Product Inventory Manager
 * Description: A WordPress plugin to manage product inventory and generate notifications.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Creates a custom database table for managing product inventory.
 */
function pim_create_inventory_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'product_inventory'; // Table name with prefix

    // SQL to create table
    $charset_collate = $wpdb->get_charset_collate();
    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        product_name varchar(255) NOT NULL,
        stock_quantity mediumint(9) NOT NULL,
        threshold_quantity mediumint(9) NOT NULL,
        notified tinyint(1) NOT NULL DEFAULT 0,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
    dbDelta( $sql );
}

// Hook into the activation of the plugin
register_activation_hook( __FILE__, 'pim_create_inventory_table' );

/**
 * Add a menu item for product inventory management
 */
function pim_add_admin_menu() {
    add_menu_page(
        'Product Inventory',
        'Inventory',
        'manage_options',
        'product_inventory',
        'pim_inventory_page',
        'dashicons-archive',
        6
    );
}
add_action( 'admin_menu', 'pim_add_admin_menu' );

/**
 * Display the inventory management page
 */
function pim_inventory_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'product_inventory';

    // Handle form submission to add/update products
    if ( isset( $_POST['submit'] ) ) {
        $product_name = sanitize_text_field( $_POST['product_name'] );
        $stock_quantity = intval( $_POST['stock_quantity'] );
        $threshold_quantity = intval( $_POST['threshold_quantity'] );

        if ( empty( $product_name ) || $stock_quantity < 0 || $threshold_quantity < 0 ) {
            echo '<div class="error"><p>Please fill in all required fields correctly.</p></div>';
        } else {
            $wpdb->insert(
                $table_name,
                array(
                    'product_name' => $product_name,
                    'stock_quantity' => $stock_quantity,
                    'threshold_quantity' => $threshold_quantity,
                ),
                array( '%s', '%d', '%d' )
            );
            echo '<div class="updated"><p>Product added successfully!</p></div>';
        }
    }

    // Retrieve current inventory
    $products = $wpdb->get_results( "SELECT * FROM $table_name" );
    ?>

    <div class="wrap">
        <h1>Product Inventory Management</h1>
        <form method="post">
            <table class="form-table">
                <tr>
                    <th scope="row"><label for="product_name">Product Name</label></th>
                    <td><input name="product_name" type="text" id="product_name" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="stock_quantity">Stock Quantity</label></th>
                    <td><input name="stock_quantity" type="number" id="stock_quantity" min="0" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="threshold_quantity">Threshold Quantity</label></th>
                    <td><input name="threshold_quantity" type="number" id="threshold_quantity" min="0" required></td>
                </tr>
            </table>
            <?php submit_button( 'Add Product' ); ?>
        </form>

        <h2>Current Inventory</h2>
        <table class="widefat">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Product Name</th>
                    <th>Stock Quantity</th>
                    <th>Threshold Quantity</th>
                    <th>Notified</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ( $products as $product ) : ?>
                    <tr>
                        <td><?php echo esc_html( $product->id ); ?></td>
                        <td><?php echo esc_html( $product->product_name ); ?></td>
                        <td><?php echo esc_html( $product->stock_quantity ); ?></td>
                        <td><?php echo esc_html( $product->threshold_quantity ); ?></td>
                        <td><?php echo esc_html( $product->notified ? 'Yes' : 'No' ); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php
}

/**
 * Send notification if stock falls below the threshold.
 */
function pim_check_inventory() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'product_inventory';
    $low_stock_products = $wpdb->get_results( "SELECT * FROM $table_name WHERE stock_quantity < threshold_quantity AND notified = 0" );

    foreach ( $low_stock_products as $product ) {
        // Prepare to send email notification
        $to = get_option( 'admin_email' );
        $subject = 'Low Stock Alert: ' . $product->product_name;
        $message = 'The stock for ' . $product->product_name . ' is below the threshold. Please restock.';
        
        // Attempt to send email
        if ( wp_mail( $to, $subject, $message ) ) {
            // Mark product as notified
            $wpdb->update(
                $table_name,
                array( 'notified' => 1 ),
                array( 'id' => $product->id ),
                array( '%d' ),
                array( '%d' )
            );
        }
    }
}

// Schedule a daily event to check inventory
if ( ! wp_next_scheduled( 'pim_check_inventory_hook' ) ) {
    wp_schedule_event( time(), 'daily', 'pim_check_inventory_hook' );
}

// Hook the function to the scheduled event
add_action( 'pim_check_inventory_hook', 'pim_check_inventory' );
```
