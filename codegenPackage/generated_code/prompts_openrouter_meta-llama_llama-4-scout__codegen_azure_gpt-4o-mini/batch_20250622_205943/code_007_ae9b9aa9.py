"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Create a simple e-commerce website using a framework like Shopify or WooCommerce to sell biographical and promotional products related to great Americans.
Generated: DETERMINISTIC_ae9b9aa9bc6adab3
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Creating a full e-commerce website using a framework like Shopify or WooCommerce involves a lot of components, including front-end and back-end code, database management, and more. Below is a simplified example of how you might set up a WooCommerce store using PHP and WordPress. This code assumes you have a WordPress environment set up with WooCommerce installed.

```php
<?php
/**
 * Plugin Name: Great Americans E-Commerce
 * Description: A simple e-commerce plugin to sell biographical and promotional products related to great Americans.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register custom post type for products
function ga_register_product_post_type() {
    $args = array(
        'public' => true,
        'label'  => 'Great Americans Products',
        'supports' => array('title', 'editor', 'thumbnail', 'custom-fields'),
        'has_archive' => true,
    );
    register_post_type('ga_product', $args);
}
add_action('init', 'ga_register_product_post_type');

// Add custom fields for product details
function ga_add_custom_meta_boxes() {
    add_meta_box('ga_product_details', 'Product Details', 'ga_product_details_callback', 'ga_product', 'normal', 'high');
}
add_action('add_meta_boxes', 'ga_add_custom_meta_boxes');

function ga_product_details_callback($post) {
    // Nonce field for security
    wp_nonce_field('ga_save_product_details', 'ga_product_nonce');

    // Retrieve existing values
    $price = get_post_meta($post->ID, '_ga_product_price', true);
    $biography = get_post_meta($post->ID, '_ga_product_biography', true);
    
    echo '<label for="ga_product_price">Price:</label>';
    echo '<input type="text" id="ga_product_price" name="ga_product_price" value="' . esc_attr($price) . '" />';
    
    echo '<label for="ga_product_biography">Biography:</label>';
    echo '<textarea id="ga_product_biography" name="ga_product_biography">' . esc_textarea($biography) . '</textarea>';
}

// Save custom fields
function ga_save_product_details($post_id) {
    // Check nonce for security
    if (!isset($_POST['ga_product_nonce']) || !wp_verify_nonce($_POST['ga_product_nonce'], 'ga_save_product_details')) {
        return;
    }

    // Save price
    if (isset($_POST['ga_product_price'])) {
        update_post_meta($post_id, '_ga_product_price', sanitize_text_field($_POST['ga_product_price']));
    }

    // Save biography
    if (isset($_POST['ga_product_biography'])) {
        update_post_meta($post_id, '_ga_product_biography', sanitize_textarea_field($_POST['ga_product_biography']));
    }
}
add_action('save_post', 'ga_save_product_details');

// Shortcode to display products
function ga_display_products() {
    $args = array(
        'post_type' => 'ga_product',
        'posts_per_page' => -1,
    );
    $query = new WP_Query($args);
    
    if ($query->have_posts()) {
        $output = '<div class="ga-products">';
        while ($query->have_posts()) {
            $query->the_post();
            $price = get_post_meta(get_the_ID(), '_ga_product_price', true);
            $biography = get_post_meta(get_the_ID(), '_ga_product_biography', true);
            $output .= '<div class="ga-product">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= '<p>' . get_the_content() . '</p>';
            $output .= '<p>Price: $' . esc_html($price) . '</p>';
            $output .= '<p>Biography: ' . esc_html($biography) . '</p>';
            $output .= '</div>';
        }
        $output .= '</div>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>No products found.</p>';
    }
}
add_shortcode('ga_products', 'ga_display_products');

// Enqueue styles and scripts
function ga_enqueue_styles() {
    wp_enqueue_style('ga-style', plugin_dir_url(__FILE__) . 'css/style.css');
}
add_action('wp_enqueue_scripts', 'ga_enqueue_styles');
```

### Notes:
- This code creates a custom post type for products, adds custom fields for price and biography, and provides a shortcode to display the products on a page.
- You will need to create a `css/style.css` file for styling.
- Ensure you have WooCommerce installed and activated in your WordPress environment.
- This is a basic implementation; for a production-ready site, you would need to add more features, such as payment processing, user authentication, and security measures.
