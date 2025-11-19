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
 * Plugin Name: SEO Optimizer
 * Description: A simple plugin to integrate SEO best practices into a WordPress site.
 * Version: 1.0.0
 * Author: Expert Programmer
 */

/**
 * Hook into wp_head to add meta tags for SEO
 */
function seo_optimizer_add_meta_tags() {
    // Meta description tag
    if (is_single() || is_page()) {
        global $post;
        $meta_description = get_post_meta($post->ID, '_seo_meta_description', true);
        if ($meta_description) {
            echo '<meta name="description" content="' . esc_attr($meta_description) . '">' . PHP_EOL;
        }
    }
    
    // Robots meta tag
    if (is_single() || is_page()) {
        echo '<meta name="robots" content="index, follow">' . PHP_EOL;
    } else {
        echo '<meta name="robots" content="noindex, follow">' . PHP_EOL;
    }
}
add_action('wp_head', 'seo_optimizer_add_meta_tags');

/**
 * Add a custom meta box for SEO settings on posts and pages
 */
function seo_optimizer_add_meta_box() {
    add_meta_box(
        'seo_optimizer_meta_box', // ID
        'SEO Settings',            // Title
        'seo_optimizer_meta_box_callback', // Callback
        ['post', 'page'],           // Post types
        'normal',                   // Context
        'high'                      // Priority
    );
}
add_action('add_meta_boxes', 'seo_optimizer_add_meta_box');

/**
 * Meta box callback function
 */
function seo_optimizer_meta_box_callback($post) {
    // Retrieve saved meta description
    $meta_description = get_post_meta($post->ID, '_seo_meta_description', true);

    // Security nonce for saving data
    wp_nonce_field('seo_optimizer_save_meta_box_data', 'seo_optimizer_meta_box_nonce');

    echo '<label for="seo_meta_description">Meta Description:</label>';
    echo '<textarea id="seo_meta_description" name="seo_meta_description" rows="3" style="width:100%;">' . esc_textarea($meta_description) . '</textarea>';
    echo '<p>Enter a description for SEO purposes (recommended length: 150-160 characters).</p>';
}

/**
 * Save meta box data
 */
function seo_optimizer_save_meta_box_data($post_id) {
    // Verify nonce
    if (!isset($_POST['seo_optimizer_meta_box_nonce']) || !wp_verify_nonce($_POST['seo_optimizer_meta_box_nonce'], 'seo_optimizer_save_meta_box_data')) {
        return;
    }

    // Prevent saving during autosave
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Check user permissions
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // Sanitize and save meta description
    if (isset($_POST['seo_meta_description'])) {
        $meta_description = sanitize_text_field($_POST['seo_meta_description']);
        update_post_meta($post_id, '_seo_meta_description', $meta_description);
    }
}
add_action('save_post', 'seo_optimizer_save_meta_box_data');

/**
 * Add Open Graph meta tags for better social media sharing
 */
function seo_optimizer_add_open_graph_tags() {
    if (is_single() || is_page()) {
        global $post;
        $title = get_the_title($post->ID);
        $url = get_permalink($post->ID);
        $description = get_post_meta($post->ID, '_seo_meta_description', true);
        $image = get_the_post_thumbnail_url($post->ID, 'full');

        echo '<meta property="og:title" content="' . esc_attr($title) . '">' . PHP_EOL;
        echo '<meta property="og:url" content="' . esc_url($url) . '">' . PHP_EOL;
        echo '<meta property="og:description" content="' . esc_attr($description) . '">' . PHP_EOL;
        if ($image) {
            echo '<meta property="og:image" content="' . esc_url($image) . '">' . PHP_EOL;
        }
    }
}
add_action('wp_head', 'seo_optimizer_add_open_graph_tags');
?>
```
