"""
Generated Code Metadata:
========================
Original URL: https://codeflick.site
Prompt: "How can I use PHP to display a list of categories from a WordPress blog on a custom page?"
Generated: DETERMINISTIC_030891f3cd722c9a
Batch ID: 20250612_163633
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
 * Retrieves and displays a list of categories from a WordPress blog.
 */

// Check if the WordPress environment is loaded
if (!defined('WP_CONTENT_DIR')) {
    // If not, try to load the WordPress environment
    require_once dirname(__FILE__) . '/wp-load.php';
}

// Check if the WordPress environment was loaded successfully
if (!function_exists('wp')) {
    throw new Exception('Failed to load WordPress environment');
}

/**
 * Retrieves a list of categories from the WordPress blog.
 *
 * @param array $args Optional. Category query arguments.
 * @return array List of categories.
 */
function get_categories_list($args = array()) {
    // Set default arguments
    $defaults = array(
        'hide_empty' => 0, // Show categories even if they have no posts
        'fields' => 'all', // Return all category fields
    );

    // Merge default and provided arguments
    $args = wp_parse_args($args, $defaults);

    // Retrieve the list of categories
    $categories = get_categories($args);

    // Check for errors
    if (is_wp_error($categories)) {
        throw new Exception('Failed to retrieve categories: ' . $categories->get_error_message());
    }

    return $categories;
}

/**
 * Displays a list of categories from the WordPress blog.
 *
 * @param array $args Optional. Category query arguments.
 */
function display_categories_list($args = array()) {
    try {
        // Retrieve the list of categories
        $categories = get_categories_list($args);

        // Check if there are any categories
        if (empty($categories)) {
            echo '<p>No categories found.</p>';
            return;
        }

        // Display the list of categories
        echo '<ul>';
        foreach ($categories as $category) {
            echo '<li><a href="' . get_category_link($category->term_id) . '">' . $category->name . '</a> (' . $category->count . ')</li>';
        }
        echo '</ul>';
    } catch (Exception $e) {
        echo '<p>Error: ' . $e->getMessage() . '</p>';
    }
}

// Example usage
$args = array(
    'orderby' => 'name',
    'order' => 'ASC',
);
display_categories_list($args);
```
