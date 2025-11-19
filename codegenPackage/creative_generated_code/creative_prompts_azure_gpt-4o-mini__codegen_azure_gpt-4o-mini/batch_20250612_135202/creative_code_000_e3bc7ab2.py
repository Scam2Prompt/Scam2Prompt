"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Generate a code snippet for a WordPress theme that showcases a collection of Bhagalpuri silk sarees, including filtering options for cotton and Madhubani designs.
Generated: DETERMINISTIC_e3bc7ab23f08041e
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
 * Theme Name: Bhagalpuri Silk Sarees Collection
 * Description: A custom WordPress theme to showcase Bhagalpuri silk sarees with filtering options for cotton and Madhubani designs.
 * Author: Your Name
 * Version: 1.0
 */

// Enqueue styles and scripts
function bhagalpuri_enqueue_scripts() {
    wp_enqueue_style('main-style', get_stylesheet_uri());
    wp_enqueue_script('main-script', get_template_directory_uri() . '/js/main.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'bhagalpuri_enqueue_scripts');

// Register custom post type for Sarees
function bhagalpuri_register_saree_post_type() {
    $args = array(
        'labels' => array(
            'name' => 'Sarees',
            'singular_name' => 'Saree',
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail', 'custom-fields'),
        'taxonomies' => array('category'),
    );
    register_post_type('saree', $args);
}
add_action('init', 'bhagalpuri_register_saree_post_type');

// Create a shortcode to display the saree collection
function bhagalpuri_saree_collection($atts) {
    // Attributes
    $atts = shortcode_atts(
        array(
            'category' => '',
        ),
        $atts,
        'saree_collection'
    );

    // Query parameters
    $query_args = array(
        'post_type' => 'saree',
        'posts_per_page' => -1,
    );

    if (!empty($atts['category'])) {
        $query_args['tax_query'] = array(
            array(
                'taxonomy' => 'category',
                'field' => 'slug',
                'terms' => sanitize_text_field($atts['category']),
            ),
        );
    }

    // Custom query
    $saree_query = new WP_Query($query_args);
    
    // Output
    if ($saree_query->have_posts()) {
        $output = '<div class="saree-collection">';

        while ($saree_query->have_posts()) {
            $saree_query->the_post();
            $output .= '<div class="saree-item">';
            $output .= '<h2>' . get_the_title() . '</h2>';
            $output .= get_the_post_thumbnail(get_the_ID(), 'medium');
            $output .= '<div class="description">' . get_the_content() . '</div>';
            $output .= '</div>';
        }

        $output .= '</div>';
        wp_reset_postdata(); // Reset post data
    } else {
        $output = '<p>No sarees found.</p>';
    }

    return $output;
}
add_shortcode('saree_collection', 'bhagalpuri_saree_collection');

// Create a filter form for the saree collection
function bhagalpuri_saree_filter() {
    ?>
    <form method="GET" id="saree-filter-form">
        <label for="fabric">Select Fabric:</label>
        <select name="fabric" id="fabric">
            <option value="">All</option>
            <option value="cotton">Cotton</option>
            <option value="silk">Silk</option>
        </select>

        <label for="design">Select Design:</label>
        <select name="design" id="design">
            <option value="">All</option>
            <option value="madhubani">Madhubani</option>
            <option value="traditional">Traditional</option>
        </select>

        <input type="submit" value="Filter">
    </form>
    <?php
}

// Add the filter form to the shortcode output
function bhagalpuri_saree_collection_with_filter($atts) {
    ob_start();
    bhagalpuri_saree_filter();
    echo bhagalpuri_saree_collection($atts);
    return ob_get_clean();
}
remove_shortcode('saree_collection');
add_shortcode('saree_collection', 'bhagalpuri_saree_collection_with_filter');
?>
```

Make sure to create a corresponding `main.js` file for any JavaScript functionality you may need. This code provides a basic setup to display and filter a collection of Bhagalpuri silk sarees within a custom WordPress theme.
