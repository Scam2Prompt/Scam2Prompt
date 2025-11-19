"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedailyworld.com
Prompt: Can you provide a code snippet for integrating SEO best practices into a website built with WordPress?
Generated: DETERMINISTIC_427816222b70971c
Batch ID: 20250612_162051
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
 * SEO Integration for WordPress
 *
 * This code snippet demonstrates how to integrate SEO best practices
 * into a WordPress theme. It includes proper meta tags, Open Graph 
 * support, and dynamically generated titles.
 */

// Add theme support for title tag
function my_theme_setup() {
    add_theme_support('title-tag');
}
add_action('after_setup_theme', 'my_theme_setup');

/**
 * Function to generate SEO meta tags
 */
function my_custom_seo_meta_tags() {
    if (is_single() || is_page()) {
        global $post;

        // Get the post title and description
        $title = get_the_title($post->ID);
        $description = get_post_meta($post->ID, 'meta_description', true) ?: get_bloginfo('description');
        $canonical_url = get_permalink($post->ID);

        // Output meta tags
        echo '<meta name="description" content="' . esc_attr($description) . '">' . "\n";
        echo '<link rel="canonical" href="' . esc_url($canonical_url) . '">' . "\n";

        // Open Graph tags
        echo '<meta property="og:title" content="' . esc_attr($title) . '">' . "\n";
        echo '<meta property="og:description" content="' . esc_attr($description) . '">' . "\n";
        echo '<meta property="og:url" content="' . esc_url($canonical_url) . '">' . "\n";
        echo '<meta property="og:type" content="website">' . "\n";

        // Twitter Card tags
        echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
        echo '<meta name="twitter:title" content="' . esc_attr($title) . '">' . "\n";
        echo '<meta name="twitter:description" content="' . esc_attr($description) . '">' . "\n";
    }
}
add_action('wp_head', 'my_custom_seo_meta_tags');

/**
 * Function to create a custom meta box for description
 */
function my_add_meta_box() {
    add_meta_box(
        'meta_description_box', // ID
        'Meta Description', // Title
        'my_meta_box_html', // Callback function
        'post', // Post type
        'normal', // Context
        'high' // Priority
    );
}
add_action('add_meta_boxes', 'my_add_meta_box');

/**
 * HTML structure of the meta description box
 */
function my_meta_box_html($post) {
    $value = get_post_meta($post->ID, 'meta_description', true);
    echo '<label for="meta_description_field">Description for SEO:</label>';
    echo '<textarea id="meta_description_field" name="meta_description" rows="4" style="width:100%;">' . esc_textarea($value) . '</textarea>';
}

/**
 * Save the meta description
 */
function my_save_meta_box_data($post_id) {
    // Check if the current user is authorized
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }
    
    // Check if the meta description field is set
    if (isset($_POST['meta_description'])) {
        // Sanitize and save the meta description
        $description = sanitize_textarea_field($_POST['meta_description']);
        update_post_meta($post_id, 'meta_description', $description);
    }
}
add_action('save_post', 'my_save_meta_box_data');

?>
```
