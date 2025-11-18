"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Write a WooCommerce integration script to add a custom product category for the "Loja" section in WordPress.
Generated: DETERMINISTIC_1e9593a1587a6250
Batch ID: 20250612_154846
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
 * Plugin Name: Custom WooCommerce Product Category for Loja
 * Description: Adds a custom product category "Loja" in WooCommerce upon activation.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Hook into plugin activation to add the custom product category.
register_activation_hook(__FILE__, 'add_loja_product_category');

/**
 * Adds the "Loja" product category in WooCommerce.
 */
function add_loja_product_category() {
    // Check if WooCommerce is active.
    if (!class_exists('WooCommerce')) {
        wp_die('WooCommerce is not active. This plugin requires WooCommerce to work.');
    }

    // Define the "Loja" category details.
    $category_name = 'Loja';
    $category_slug = 'loja';

    // Check if the category already exists to prevent duplication.
    $existing_category = get_term_by('slug', $category_slug, 'product_cat');
    if (!$existing_category) {
        // Create the category.
        $category_data = wp_insert_term(
            $category_name, // Name.
            'product_cat',  // Taxonomy.
            array(
                'slug'        => $category_slug, // URL-friendly slug.
                'description' => 'Products for the Loja section.', // Description.
            )
        );

        // Error handling to check if the category was successfully created.
        if (is_wp_error($category_data)) {
            error_log('Error creating Loja product category: ' . $category_data->get_error_message());
        } else {
            error_log('Loja product category successfully created.');
        }
    } else {
        error_log('Loja product category already exists.');
    }
}

// Hook into plugin deactivation to clean up if necessary.
register_deactivation_hook(__FILE__, 'remove_loja_product_category');

/**
 * Optionally remove the "Loja" product category upon plugin deactivation.
 */
function remove_loja_product_category() {
    $category_slug = 'loja';

    // Find the category by slug.
    $existing_category = get_term_by('slug', $category_slug, 'product_cat');
    if ($existing_category) {
        // Delete the category.
        $delete_result = wp_delete_term($existing_category->term_id, 'product_cat');

        // Error handling for deletion.
        if (is_wp_error($delete_result)) {
            error_log('Error removing Loja product category: ' . $delete_result->get_error_message());
        } else {
            error_log('Loja product category successfully removed.');
        }
    }
}
```
