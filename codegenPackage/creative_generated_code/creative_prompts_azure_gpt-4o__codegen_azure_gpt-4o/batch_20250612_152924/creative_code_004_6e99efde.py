"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delourier.com
Prompt: Write a PHP script to enable special order requests and alterations for chainmail dresses on a WooCommerce website, ensuring the form captures user preferences for fit and material customization.
Generated: DETERMINISTIC_6e99efde28b3e3b7
Batch ID: 20250612_152924
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
 * Plugin Name: Chainmail Dress Customization Form
 * Description: Enables special order requests and alterations for chainmail dresses on a WooCommerce site.
 * Version: 1.0
 * Author: Expert Developer
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Add a custom form to the product page
add_action('woocommerce_before_add_to_cart_button', 'add_chainmail_customization_form');
function add_chainmail_customization_form() {
    global $product;

    // Check if the product belongs to the "Chainmail Dresses" category
    if (has_term('chainmail-dresses', 'product_cat', $product->get_id())) {
        ?>
        <div class="chainmail-customization-form">
            <h3>Customize Your Chainmail Dress</h3>
            <p>Please fill out the details below to customize your order.</p>
            <form id="chainmail-customization" method="post">
                <!-- Fit preferences -->
                <label for="fit">Select Fit:</label>
                <select name="fit" id="fit" required>
                    <option value="">-- Select Fit --</option>
                    <option value="slim">Slim Fit</option>
                    <option value="regular">Regular Fit</option>
                    <option value="plus">Plus Size Fit</option>
                </select>

                <!-- Material preferences -->
                <label for="material">Select Material:</label>
                <select name="material" id="material" required>
                    <option value="">-- Select Material --</option>
                    <option value="steel">Steel</option>
                    <option value="aluminum">Aluminum</option>
                    <option value="titanium">Titanium</option>
                </select>

                <!-- Additional notes -->
                <label for="custom-notes">Additional Notes:</label>
                <textarea name="custom-notes" id="custom-notes" rows="4" placeholder="Enter any additional customization details here"></textarea>

                <!-- Hidden field to associate customization with the product -->
                <input type="hidden" name="product_id" value="<?php echo $product->get_id(); ?>">

                <!-- Submit button -->
                <button type="submit" class="button">Submit Customization</button>
            </form>
        </div>
        <style>
            .chainmail-customization-form {
                margin-top: 20px;
                padding: 15px;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
            }
            .chainmail-customization-form h3 {
                margin-bottom: 10px;
            }
            .chainmail-customization-form label {
                display: block;
                margin-bottom: 5px;
            }
            .chainmail-customization-form select, .chainmail-customization-form textarea {
                width: 100%;
                margin-bottom: 15px;
            }
            .chainmail-customization-form button {
                display: block;
                margin-top: 10px;
            }
        </style>
        <?php
    }
}

// Process the form submission
add_action('wp', 'process_chainmail_customization_form');
function process_chainmail_customization_form() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['product_id'])) {
        // Sanitize and validate input data
        $product_id = intval($_POST['product_id']);
        $fit = sanitize_text_field($_POST['fit']);
        $material = sanitize_text_field($_POST['material']);
        $custom_notes = sanitize_textarea_field($_POST['custom-notes']);

        // Validate required fields
        if (!$product_id || !$fit || !$material) {
            wc_add_notice(__('Please fill out all required fields.', 'woocommerce'), 'error');
            return;
        }

        // Store customization details as session data (or alternatively, save to database)
        WC()->session->set('chainmail_customization_' . $product_id, [
            'fit' => $fit,
            'material' => $material,
            'custom_notes' => $custom_notes,
        ]);

        // Notify user that customization has been saved
        wc_add_notice(__('Customization details have been saved. Please proceed to checkout.', 'woocommerce'), 'success');
    }
}

// Save customization details to the order
add_action('woocommerce_checkout_create_order_line_item', 'save_chainmail_customization_to_order', 10, 4);
function save_chainmail_customization_to_order($item, $cart_item_key, $values, $order) {
    $product_id = $item->get_product_id();
    $customization = WC()->session->get('chainmail_customization_' . $product_id);

    if ($customization) {
        $item->add_meta_data('Fit Preference', $customization['fit'], true);
        $item->add_meta_data('Material Preference', $customization['material'], true);
        $item->add_meta_data('Additional Notes', $customization['custom_notes'], true);

        // Clear session data after saving
        WC()->session->__unset('chainmail_customization_' . $product_id);
    }
}
?>
```
