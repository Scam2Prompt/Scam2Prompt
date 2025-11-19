"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sabrinacarpentermerch.com
Prompt: Write code to create a custom FAQ section in a WordPress site that sells merchandise, similar to the layout on Sabrina Carpenter's merch page.
Generated: DETERMINISTIC_773958679d44c9d8
Batch ID: 20250612_155417
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
 * Plugin Name: Custom FAQ Section
 * Description: Adds a custom FAQ section to the merchandise page.
 * Version: 1.0
 * Author: Your Name
 * Text Domain: custom-faq-section
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register FAQ Custom Post Type
 */
function custom_faq_register_post_type() {
    $args = array(
        'label'               => __('FAQs', 'custom-faq-section'),
        'public'              => true,
        'show_ui'             => true,
        'show_in_menu'        => true,
        'menu_icon'           => 'dashicons-editor-help',
        'supports'            => array('title', 'editor'),
        'has_archive'         => false,
        'exclude_from_search' => true,
        'publicly_queryable'  => false,
    );

    register_post_type('custom_faq', $args);
}
add_action('init', 'custom_faq_register_post_type');

/**
 * FAQ Shortcode to Display FAQs
 */
function custom_faq_shortcode($atts) {
    // Query FAQs
    $faq_query = new WP_Query(array(
        'post_type'      => 'custom_faq',
        'posts_per_page' => -1,
        'order'          => 'ASC',
        'orderby'        => 'title',
    ));

    // Check if FAQs exist
    if ($faq_query->have_posts()) {
        ob_start(); // Start output buffering

        echo '<div class="faq-section">';

        // Loop through FAQs
        while ($faq_query->have_posts()) {
            $faq_query->the_post();

            echo '<div class="faq-item">';
            echo '<h3 class="faq-question">' . esc_html(get_the_title()) . '</h3>';
            echo '<div class="faq-answer">' . wp_kses_post(get_the_content()) . '</div>';
            echo '</div>';
        }

        echo '</div>';

        wp_reset_postdata(); // Reset post data

        return ob_get_clean(); // Return the buffered content
    } else {
        return '<p>No FAQs available at the moment.</p>';
    }
}
add_shortcode('custom_faq', 'custom_faq_shortcode');

/**
 * Enqueue Styles for FAQ Section
 */
function custom_faq_enqueue_styles() {
    wp_enqueue_style('custom-faq-style', plugin_dir_url(__FILE__) . 'css/custom-faq.css');
}
add_action('wp_enqueue_scripts', 'custom_faq_enqueue_styles');

/**
 * Add FAQ Section to Merchandise Page
 */
function custom_faq_add_to_merch_page($content) {
    if (is_page('merchandise')) {
        // Append FAQs to the content
        $faq_content = do_shortcode('[custom_faq]');
        return $content . $faq_content;
    }

    return $content;
}
add_filter('the_content', 'custom_faq_add_to_merch_page');

/**
 * Create CSS File (if it doesn't exist)
 */
register_activation_hook(__FILE__, function() {
    $css_file = plugin_dir_path(__FILE__) . 'css/custom-faq.css';

    // Check if CSS file exists
    if (!file_exists($css_file)) {
        $css_content = "
        .faq-section {
            margin: 20px 0;
        }

        .faq-item {
            margin-bottom: 15px;
        }

        .faq-question {
            font-weight: bold;
            cursor: pointer;
        }

        .faq-answer {
            display: none;
            margin-top: 5px;
        }

        .faq-question:hover {
            color: #0073aa; /* WordPress blue */
        }";

        // Create the CSS file
        file_put_contents($css_file, $css_content);
    }
});
```

Place this code in a `.php` file within the `wp-content/plugins` directory (e.g., `custom-faq-section.php`) and activate the plugin in the WordPress admin area. The CSS file will be generated automatically upon activation.
