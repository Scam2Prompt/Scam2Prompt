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
 * Function to display discounted prices for WooCommerce products.
 * Shows the original price and the current discounted price.
 *
 * @param int $product_id The ID of the product.
 */
function display_discounted_price($product_id) {
    // Check if WooCommerce is active
    if (!class_exists('WooCommerce')) {
        error_log('WooCommerce is not active. Function display_discounted_price requires WooCommerce.');
        return;
    }

    // Get the product object
    $product = wc_get_product($product_id);

    // Ensure product exists
    if (!$product) {
        error_log("Product with ID $product_id not found.");
        return;
    }

    // Get the regular price and sale price
    $regular_price = $product->get_regular_price();
    $sale_price = $product->get_sale_price();

    // Ensure the product has a sale price
    if (!$sale_price || $regular_price <= $sale_price) {
        echo '<p>No discount available for this product.</p>';
        return;
    }

    // Display the prices
    ?>
    <div class="discounted-price-container">
        <h2><?php echo esc_html($product->get_name()); ?></h2>
        <p>Original Price: <span class="regular-price"><?php echo wc_price($regular_price); ?></span></p>
        <p>Discounted Price: <span class="sale-price"><?php echo wc_price($sale_price); ?></span></p>
    </div>
    <?php
}

// Usage Example:
// Replace 123 with the product ID you want to display prices for.
display_discounted_price(123);
?>
```
