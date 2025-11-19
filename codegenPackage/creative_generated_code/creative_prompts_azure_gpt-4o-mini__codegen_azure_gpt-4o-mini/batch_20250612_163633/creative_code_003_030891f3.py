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
/**
 * Template Name: Custom Categories Page
 * Description: A custom page template to display a list of categories from a WordPress blog.
 */

// Check if the WordPress environment is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Enqueue necessary styles or scripts if needed
function custom_categories_page_scripts() {
    // Example: wp_enqueue_style('custom-style', get_stylesheet_directory_uri() . '/css/custom-style.css');
}
add_action('wp_enqueue_scripts', 'custom_categories_page_scripts');

// Function to display the categories
function display_categories() {
    // Fetch categories from the WordPress database
    $args = array(
        'taxonomy'   => 'category', // Specify the taxonomy
        'hide_empty' => true,       // Only show categories with posts
    );

    // Get the categories
    $categories = get_terms($args);

    // Check for errors and empty categories
    if (is_wp_error($categories)) {
        echo '<p>Error fetching categories: ' . esc_html($categories->get_error_message()) . '</p>';
        return;
    } elseif (empty($categories)) {
        echo '<p>No categories found.</p>';
        return;
    }

    // Display categories
    echo '<ul class="category-list">';
    foreach ($categories as $category) {
        // Output each category with a link
        echo '<li>';
        echo '<a href="' . esc_url(get_category_link($category->term_id)) . '">' . esc_html($category->name) . '</a>';
        echo '</li>';
    }
    echo '</ul>';
}

// Call the function to display the categories
get_header(); // Include the header
?>
<div class="custom-categories-page">
    <h1><?php the_title(); ?></h1> <!-- Display the page title -->
    <?php display_categories(); // Call the function to display categories ?>
</div>
<?php
get_footer(); // Include the footer
?>
```
