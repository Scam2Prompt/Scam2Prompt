"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Write a PHP function to display discounted prices for products like "Tusser silk saree with Zari border" on a WordPress WooCommerce site, ensuring the original price and current price are shown.
Generated: DETERMINISTIC_4d1ef46193988a73
Batch ID: 20250612_150327
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
 * Display discounted prices for WooCommerce products.
 *
 * This function retrieves the original price and discounted price of a product
 * and displays them in a formatted manner on the product page.
 *
 * @param int $product_id The ID of the product.
 * @return void
 */
function display_discounted_price($product_id) {
    // Ensure that the product ID is valid
    if (empty($product_id) || !is_numeric($product_id)) {
        error_log('Invalid product ID provided: ' . print_r($product_id, true));
        return;
    }

    // Load the product object
    $product = wc_get_product($product_id);
    
    // Check if the product exists and is a valid product object
    if (!$product) {
        error_log('Product not found for ID: ' . $product_id);
        return;
    }

    // Get the original price and current price
    $regular_price = $product->get_regular_price();
    $sale_price = $product->get_sale_price();

    // Display prices if available
    if ($regular_price) {
        echo '<div class="product-price">';
        
        // Display the original price
        echo '<span class="original-price" style="text-decoration: line-through; color: red;">' . wc_price($regular_price) . '</span>';

        // Check if there is a sale price
        if ($sale_price) {
            // Display the current discounted price
            echo '<span class="discounted-price" style="color: green;">' . wc_price($sale_price) . '</span>';
        }
        
        echo '</div>';
    } else {
        error_log('No price found for product ID: ' . $product_id);
    }
}

// Usage example (call this function within the product template)
display_discounted_price(get_the_ID());
?>
```
