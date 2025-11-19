"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Design a custom shortcode for a WordPress theme that lists all available saree categories, including semi silk and Kota silk, with links to their respective product pages.
Generated: DETERMINISTIC_0a4cd1178014712d
Batch ID: 20250612_135202
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
 * Plugin Name: Saree Categories Shortcode
 * Description: Adds a shortcode to list saree categories with links to their respective product pages.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// Prevent direct access to the file for security
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Shortcode to display saree categories with links to their product pages.
 *
 * Usage: [saree_categories]
 *
 * @return string HTML output of saree categories with links.
 */
function saree_categories_shortcode() {
    // Initialize an empty output string
    $output = '';

    try {
        // Get all product categories
        $categories = get_terms(array(
            'taxonomy'   => 'product_cat', // WooCommerce product categories
            'hide_empty' => true,          // Only include categories with products
        ));

        // Check if categories exist
        if (!empty($categories) && !is_wp_error($categories)) {
            $output .= '<ul class="saree-categories">';

            // Loop through each category and generate links
            foreach ($categories as $category) {
                // Check if category name includes "silk"
                if (strpos(strtolower($category->name), 'silk') !== false) {
                    $output .= sprintf(
                        '<li><a href="%s">%s</a></li>',
                        esc_url(get_term_link($category)),
                        esc_html($category->name)
                    );
                }
            }

            $output .= '</ul>';
        } else {
            // No categories found
            $output = '<p>No saree categories found.</p>';
        }
    } catch (Exception $e) {
        // Handle potential errors gracefully
        $output = '<p>There was an error fetching the saree categories. Please try again later.</p>';
        error_log('Saree Categories Shortcode Error: ' . $e->getMessage());
    }

    return $output;
}

// Register the shortcode
add_shortcode('saree_categories', 'saree_categories_shortcode');
?>
```
