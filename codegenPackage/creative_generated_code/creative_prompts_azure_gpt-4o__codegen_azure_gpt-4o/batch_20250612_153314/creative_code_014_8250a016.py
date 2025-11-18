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
 * Description: A WordPress plugin for managing product inventory and generating notifications.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// Prevent direct access to the file.
if (!defined('ABSPATH')) {
    exit;
}

// Define constants for the plugin.
define('PIM_PLUGIN_VERSION', '1.0');
define('PIM_PLUGIN_PATH', plugin_dir_path(__FILE__));
define('PIM_PLUGIN_URL', plugin_dir_url(__FILE__));

/**
 * Activate the plugin
 */
function pim_activate_plugin() {
    // Create database table for product inventory (if not exists).
    global $wpdb;

    $table_name = $wpdb->prefix . 'pim_inventory';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id INT(11) NOT NULL AUTO_INCREMENT,
        product_name VARCHAR(255) NOT NULL,
        stock_quantity INT(11) NOT NULL,
        notification_threshold INT(11) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'pim_activate_plugin');

/**
 * Deactivate the plugin
 */
function pim_deactivate_plugin() {
    // Clean up actions when deactivating.
    // No data deletion performed during deactivation.
}
register_deactivation_hook(__FILE__, 'pim_deactivate_plugin');

/**
 * Add menu page for managing inventory
 */
function pim_add_admin_menu() {
    add_menu_page(
        'Product Inventory Manager',
        'Inventory Manager',
        'manage_options',
        'pim_inventory_manager',
        'pim_inventory_manager_page',
        'dashicons-products',
        25
    );
}
add_action('admin_menu', 'pim_add_admin_menu');

/**
 * Admin page for managing inventory
 */
function pim_inventory_manager_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'pim_inventory';

    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['pim_save_product'])) {
        // Handle form submission for adding or updating products.
        $product_name = sanitize_text_field($_POST['product_name']);
        $stock_quantity = intval($_POST['stock_quantity']);
        $notification_threshold = intval($_POST['notification_threshold']);

        if (!empty($product_name) && $stock_quantity >= 0 && $notification_threshold >= 0) {
            $wpdb->insert($table_name, [
                'product_name' => $product_name,
                'stock_quantity' => $stock_quantity,
                'notification_threshold' => $notification_threshold,
            ]);
            echo '<div class="updated"><p>Product saved successfully!</p></div>';
        } else {
            echo '<div class="error"><p>Invalid input. Please try again.</p></div>';
        }
    }

    // Fetch all products from the inventory table.
    $products = $wpdb->get_results("SELECT * FROM $table_name");

    ?>
    <div class="wrap">
        <h1>Product Inventory Manager</h1>
        <form method="POST">
            <h2>Add New Product</h2>
            <table class="form-table">
                <tr>
                    <th><label for="product_name">Product Name</label></th>
                    <td><input type="text" name="product_name" id="product_name" required></td>
                </tr>
                <tr>
                    <th><label for="stock_quantity">Stock Quantity</label></th>
                    <td><input type="number" name="stock_quantity" id="stock_quantity" min="0" required></td>
                </tr>
                <tr>
                    <th><label for="notification_threshold">Notification Threshold</label></th>
                    <td><input type="number" name="notification_threshold" id="notification_threshold" min="0" required></td>
                </tr>
            </table>
            <p>
                <input type="submit" name="pim_save_product" class="button button-primary" value="Save Product">
            </p>
        </form>

        <h2>Inventory List</h2>
        <table class="wp-list-table widefat fixed striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Product Name</th>
                    <th>Stock Quantity</th>
                    <th>Notification Threshold</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($products as $product): ?>
                <tr>
                    <td><?php echo esc_html($product->id); ?></td>
                    <td><?php echo esc_html($product->product_name); ?></td>
                    <td><?php echo esc_html($product->stock_quantity); ?></td>
                    <td><?php echo esc_html($product->notification_threshold); ?></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php
}

/**
 * Check inventory and send notifications
 */
function pim_check_inventory_and_notify() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'pim_inventory';

    // Fetch all products below the notification threshold.
    $low_stock_products = $wpdb->get_results("SELECT * FROM $table_name WHERE stock_quantity <= notification_threshold");

    foreach ($low_stock_products as $product) {
        $admin_email = get_option('admin_email');
        $subject = "Low Stock Alert: {$product->product_name}";
        $message = "The stock for {$product->product_name} is low (Quantity: {$product->stock_quantity}). Please restock.";
        wp_mail($admin_email, $subject, $message);
    }
}
add_action('pim_check_inventory_cron', 'pim_check_inventory_and_notify');

/**
 * Schedule cron job for inventory check
 */
function pim_schedule_cron() {
    if (!wp_next_scheduled('pim_check_inventory_cron')) {
        wp_schedule_event(time(), 'daily', 'pim_check_inventory_cron');
    }
}
add_action('wp', 'pim_schedule_cron');

/**
 * Unschedule cron job on plugin deactivation
 */
function pim_unschedule_cron() {
    $timestamp = wp_next_scheduled('pim_check_inventory_cron');
    if ($timestamp) {
        wp_unschedule_event($timestamp, 'pim_check_inventory_cron');
    }
}
register_deactivation_hook(__FILE__, 'pim_unschedule_cron');
```
