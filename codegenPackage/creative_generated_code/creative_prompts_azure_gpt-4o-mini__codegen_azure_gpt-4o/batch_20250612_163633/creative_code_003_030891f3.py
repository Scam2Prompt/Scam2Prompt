"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codeflick.site
Prompt: "How can I use PHP to display a list of categories from a WordPress blog on a custom page?"
Generated: DETERMINISTIC_030891f3cd722c9a
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure this file is being accessed within a WordPress environment
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Function to display a list of WordPress blog categories on a custom page
 */
function display_blog_categories() {
    // Fetch categories using WordPress's get_categories() function
    $categories = get_categories(array(
        'orderby'    => 'name', // Order categories alphabetically
        'order'      => 'ASC',  // Sort order ascending
        'hide_empty' => true    // Exclude categories with no posts
    ));

    // Check if categories were retrieved successfully
    if (!empty($categories)) {
        echo '<ul>'; // Start unordered list

        // Loop through each category
        foreach ($categories as $category) {
            // Display category name as a clickable link
            echo '<li>';
            echo '<a href="' . esc_url(get_category_link($category->term_id)) . '" title="' . esc_attr($category->name) . '">';
            echo esc_html($category->name); // Safely output category name
            echo '</a>';
            echo ' (' . intval($category->count) . ')'; // Display post count in parentheses
            echo '</li>';
        }

        echo '</ul>'; // End unordered list
    } else {
        // Handle case where no categories are found
        echo '<p>No categories found.</p>';
    }
}

// Include error handling: Ensure WordPress environment is loaded
if (function_exists('get_categories') && function_exists('get_category_link')) {
    // Use the function wherever needed, e.g., in a custom page template
    display_blog_categories();
} else {
    // Display an error message if WordPress functions are unavailable
    echo '<p>Error: WordPress environment not loaded properly.</p>';
}
?>
```
