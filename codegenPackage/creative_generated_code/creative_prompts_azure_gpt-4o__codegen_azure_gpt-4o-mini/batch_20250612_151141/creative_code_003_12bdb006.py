"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "How can I use AJAX to implement a 'Load More' button for product listings in WooCommerce, similar to the WoodMart theme?"
Generated: DETERMINISTIC_12bdb006877f92a4
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
// functions.php

// Enqueue necessary scripts for AJAX functionality
function enqueue_load_more_scripts() {
    wp_enqueue_script('ajax-load-more', get_template_directory_uri() . '/js/ajax-load-more.js', array('jquery'), null, true);
    wp_localize_script('ajax-load-more', 'ajax_load_more_params', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('load_more_products')
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_load_more_scripts');

// AJAX handler for loading more products
function load_more_products() {
    // Verify nonce for security
    check_ajax_referer('load_more_products', 'nonce');

    // Get the current page number and number of products to load
    $paged = (isset($_POST['page_number'])) ? intval($_POST['page_number']) : 1;
    $posts_per_page = 12; // Number of products to load

    // Create a new WP Query for products
    $args = array(
        'post_type' => 'product',
        'posts_per_page' => $posts_per_page,
        'paged' => $paged,
    );

    $query = new WP_Query($args);

    // Check if there are products
    if ($query->have_posts()) {
        // Output the product loop
        while ($query->have_posts()) {
            $query->the_post();
            wc_get_template_part('content', 'product'); // Use WooCommerce template for product display
        }
    } else {
        // No more products to load
        wp_send_json_error('No more products available');
    }

    // Reset post data
    wp_reset_postdata();
    wp_die(); // Terminate the script properly
}
add_action('wp_ajax_load_more', 'load_more_products'); // For logged-in users
add_action('wp_ajax_nopriv_load_more', 'load_more_products'); // For logged-out users
```

```javascript
// ajax-load-more.js

jQuery(document).ready(function($) {
    let pageNumber = 1; // Initialize page number
    const loadMoreButton = $('#load-more'); // Load more button
    const productContainer = $('#product-list'); // Container for products

    // Load more products on button click
    loadMoreButton.on('click', function() {
        pageNumber++; // Increment page number

        // AJAX request to load more products
        $.ajax({
            url: ajax_load_more_params.ajax_url,
            type: 'POST',
            data: {
                action: 'load_more',
                page_number: pageNumber,
                nonce: ajax_load_more_params.nonce
            },
            beforeSend: function() {
                loadMoreButton.text('Loading...'); // Change button text during loading
            },
            success: function(response) {
                // Check if products are returned
                if (response.success) {
                    productContainer.append(response.data); // Append new products to the container
                    loadMoreButton.text('Load More'); // Reset button text
                } else {
                    loadMoreButton.remove(); // Remove button if no more products
                    alert('No more products to load.'); // Notify user
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('AJAX error:', textStatus, errorThrown); // Log error
                loadMoreButton.text('Load More'); // Reset button text on error
            }
        });
    });
});
```

```html
<!-- HTML structure for product listings and Load More button -->
<div id="product-list">
    <!-- Existing products will be displayed here -->
    <?php
    // Display initial product listings
    if (have_posts()) {
        while (have_posts()) {
            the_post();
            wc_get_template_part('content', 'product'); // Initial product display
        }
    }
    ?>
</div>
<button id="load-more">Load More</button>
```

This code provides a complete solution for implementing a "Load More" button for WooCommerce product listings using AJAX. It includes PHP code for handling the AJAX request and a JavaScript file for managing the button click and AJAX interactions. The provided HTML structure is where the products will be rendered on the page.
