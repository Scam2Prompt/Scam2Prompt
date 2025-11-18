"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Write a WordPress plugin that adds a custom FAQ section to the site, referencing the "FAQs" page structure mentioned in the content.
Generated: DETERMINISTIC_ee9690c4166f9331
Batch ID: 20250612_155115
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/custom-faq-section": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Custom FAQ Section
 * Plugin URI: https://example.com/custom-faq-section
 * Description: Adds a custom FAQ section to your WordPress site.
 * Version: 1.0.0
 * Author: Expert Programmer
 * Author URI: https://example.com
 * License: GPL2
 * Text Domain: custom-faq-section
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Register FAQ Custom Post Type
function custom_faq_register_post_type() {
    $labels = array(
        'name'               => __('FAQs', 'custom-faq-section'),
        'singular_name'      => __('FAQ', 'custom-faq-section'),
        'menu_name'          => __('FAQs', 'custom-faq-section'),
        'add_new'            => __('Add FAQ', 'custom-faq-section'),
        'add_new_item'       => __('Add New FAQ', 'custom-faq-section'),
        'edit_item'          => __('Edit FAQ', 'custom-faq-section'),
        'new_item'           => __('New FAQ', 'custom-faq-section'),
        'view_item'          => __('View FAQ', 'custom-faq-section'),
        'all_items'          => __('All FAQs', 'custom-faq-section'),
        'search_items'       => __('Search FAQs', 'custom-faq-section'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'show_in_menu'       => true,
        'supports'           => array('title', 'editor'),
        'rewrite'            => array('slug' => 'faqs'),
    );

    register_post_type('faq', $args);
}
add_action('init', 'custom_faq_register_post_type');

// Shortcode to Display FAQs
function custom_faq_shortcode() {
    ob_start();

    $args = array(
        'post_type'      => 'faq',
        'post_status'    => 'publish',
        'posts_per_page' => -1,
        'orderby'        => 'title',
        'order'          => 'ASC',
    );

    $faqs = new WP_Query($args);

    if ($faqs->have_posts()) {
        echo '<div class="faq-section">';
        while ($faqs->have_posts()) {
            $faqs->the_post();
            echo '<div class="faq-item">';
            echo '<h3 class="faq-question">' . get_the_title() . '</h3>';
            echo '<div class="faq-answer">' . get_the_content() . '</div>';
            echo '</div>';
        }
        echo '</div>';
    } else {
        echo '<p>' . __('No FAQs found.', 'custom-faq-section') . '</p>';
    }

    wp_reset_postdata();

    return ob_get_clean();
}
add_shortcode('custom_faqs', 'custom_faq_shortcode');

// Enqueue Styles for FAQ Section
function custom_faq_enqueue_styles() {
    wp_enqueue_style(
        'custom-faq-styles',
        plugins_url('css/style.css', __FILE__),
        array(),
        '1.0.0'
    );
}
add_action('wp_enqueue_scripts', 'custom_faq_enqueue_styles');

// Plugin Activation Hook
function custom_faq_activate() {
    custom_faq_register_post_type();
    flush_rewrite_rules();
}
register_activation_hook(__FILE__, 'custom_faq_activate');

// Plugin Deactivation Hook
function custom_faq_deactivate() {
    flush_rewrite_rules();
}
register_deactivation_hook(__FILE__, 'custom_faq_deactivate');

// Create a basic stylesheet file if not exists
function custom_faq_create_stylesheet() {
    $plugin_dir = plugin_dir_path(__FILE__);
    $css_file   = $plugin_dir . 'css/style.css';

    if (!file_exists($css_file)) {
        wp_mkdir_p($plugin_dir . 'css');

        $default_css = "
        .faq-section {
            margin: 20px 0;
        }
        .faq-item {
            margin-bottom: 15px;
        }
        .faq-question {
            font-weight: bold;
        }
        .faq-answer {
            margin-top: 5px;
        }
        ";

        file_put_contents($css_file, $default_css);
    }
}
register_activation_hook(__FILE__, 'custom_faq_create_stylesheet');
```

This plugin creates a custom "FAQ" post type, allows FAQs to be added from the WordPress admin area, and provides a `[custom_faqs]` shortcode for displaying the FAQs on any page or post. It also includes basic styling and proper plugin activation/deactivation hooks.
