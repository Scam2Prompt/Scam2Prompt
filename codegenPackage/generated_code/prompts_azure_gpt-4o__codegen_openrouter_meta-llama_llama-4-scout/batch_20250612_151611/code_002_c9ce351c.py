"""
Generated Code Metadata:
========================
Original URL: https://thesoftware.online
Prompt: Create a WordPress shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout, similar to the structure found on a site using WooCommerce themes.
Generated: DETERMINISTIC_c9ce351c2ac442d6
Batch ID: 20250612_151611
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
 * WordPress shortcode to display blog posts categorized under "Decoration" and "Design trends" in a grid layout.
 *
 * @package WordPress
 * @subpackage Shortcode
 */

// Define the shortcode function
function decoration_design_trends_shortcode() {
    // Define the category slugs
    $category_slugs = array('decoration', 'design-trends');

    // Define the shortcode arguments
    $args = array(
        'post_type' => 'post',
        'tax_query' => array(
            'relation' => 'OR',
        ),
    );

    // Loop through each category slug and add to tax_query
    foreach ($category_slugs as $slug) {
        $args['tax_query'][] = array(
            'taxonomy' => 'category',
            'field'    => 'slug',
            'terms'    => $slug,
        );
    }

    // Query posts
    $query = new WP_Query($args);

    // Check if posts exist
    if ($query->have_posts()) {
        // Start output buffer
        ob_start();

        // Start grid container
        echo '<div class="grid-container">';

        // Loop through posts
        while ($query->have_posts()) {
            $query->the_post();

            // Get post data
            $post_id = get_the_ID();
            $post_title = get_the_title();
            $post_permalink = get_the_permalink();
            $post_thumbnail = get_the_post_thumbnail_url();

            // Output grid item
            echo '<div class="grid-item">';
            echo '<a href="' . esc_url($post_permalink) . '">';
            echo '<img src="' . esc_url($post_thumbnail) . '" alt="' . esc_attr($post_title) . '">';
            echo '<h2>' . esc_html($post_title) . '</h2>';
            echo '</a>';
            echo '</div>';
        }

        // End grid container
        echo '</div>';

        // Reset post data
        wp_reset_postdata();

        // Return output buffer
        return ob_get_clean();
    } else {
        // Return no posts found message
        return '<p>No posts found.</p>';
    }
}

// Register shortcode
add_shortcode('decoration_design_trends', 'decoration_design_trends_shortcode');
```

```css
/* Add to your theme's style.css file */
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.grid-item {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
}

.grid-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.grid-item h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.grid-item a {
    text-decoration: none;
    color: #337ab7;
}

.grid-item a:hover {
    color: #23527c;
}
```
