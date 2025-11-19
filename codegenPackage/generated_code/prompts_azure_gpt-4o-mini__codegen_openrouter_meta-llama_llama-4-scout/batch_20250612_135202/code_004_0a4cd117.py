"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Design a custom shortcode for a WordPress theme that lists all available saree categories, including semi silk and Kota silk, with links to their respective product pages.
Generated: DETERMINISTIC_0a4cd1178014712d
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Custom shortcode to list all available saree categories.
 *
 * @package WordPress
 * @subpackage [Theme Name]
 */

/**
 * Register the shortcode.
 */
add_shortcode('saree_categories', 'saree_categories_shortcode');

/**
 * Callback function for the shortcode.
 *
 * @return string HTML output for the shortcode.
 */
function saree_categories_shortcode() {
    // Initialize an empty string to store the output.
    $output = '';

    try {
        // Get all categories from the database.
        $categories = get_categories(array(
            'taxonomy' => 'product_cat',
            'hide_empty' => false,
        ));

        // Check if categories exist.
        if ($categories) {
            // Start the output with a heading.
            $output .= '<h2>Saree Categories</h2>';
            $output .= '<ul class="saree-categories">';

            // Loop through each category.
            foreach ($categories as $category) {
                // Get the category link.
                $category_link = get_term_link($category);

                // Check if the category link is valid.
                if (!is_wp_error($category_link)) {
                    // Append the category link to the output.
                    $output .= '<li><a href="' . esc_url($category_link) . '">' . esc_html($category->name) . '</a></li>';
                }
            }

            // Close the unordered list.
            $output .= '</ul>';
        } else {
            // Display a message if no categories exist.
            $output .= '<p>No saree categories available.</p>';
        }
    } catch (Exception $e) {
        // Log the error and display a user-friendly message.
        error_log('Error listing saree categories: ' . $e->getMessage());
        $output .= '<p>An error occurred while listing saree categories.</p>';
    }

    // Return the final output.
    return $output;
}
```
