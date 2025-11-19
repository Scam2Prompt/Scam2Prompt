"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customized.dexnav.com
Prompt: Write a function to implement a FAQ section on a WordPress site, inspired by the layout on customized.dexnav.com.
Generated: DETERMINISTIC_2deafc8c7c41658b
Batch ID: 20250612_135754
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
 * Description: A plugin to add a customizable FAQ section to a WordPress site.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register a custom FAQ post type.
 */
function create_faq_post_type() {
    $labels = array(
        'name'               => 'FAQs',
        'singular_name'      => 'FAQ',
        'menu_name'          => 'FAQ Section',
        'name_admin_bar'     => 'FAQ',
        'add_new'            => 'Add New',
        'add_new_item'       => 'Add New FAQ',
        'edit_item'          => 'Edit FAQ',
        'new_item'           => 'New FAQ',
        'view_item'          => 'View FAQ',
        'all_items'          => 'All FAQs',
        'search_items'       => 'Search FAQs',
        'not_found'          => 'No FAQs Found',
        'not_found_in_trash' => 'No FAQs Found in Trash',
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'menu_position'      => 20,
        'menu_icon'          => 'dashicons-editor-help',
        'supports'           => array('title', 'editor'),
        'show_in_rest'       => true,
    );

    register_post_type('faq', $args);
}
add_action('init', 'create_faq_post_type');

/**
 * Shortcode to display FAQs in a collapsible layout.
 * Usage: [faq_section]
 */
function faq_section_shortcode() {
    // Fetch all FAQs
    $args = array(
        'post_type'      => 'faq',
        'posts_per_page' => -1,
        'order'          => 'ASC',
        'orderby'        => 'title',
    );

    $faq_query = new WP_Query($args);

    // Check if FAQs exist
    if (!$faq_query->have_posts()) {
        return '<p>No FAQs available at the moment.</p>';
    }

    // Output the FAQ section
    ob_start();
    ?>
    <div class="faq-section">
        <?php while ($faq_query->have_posts()) : $faq_query->the_post(); ?>
            <div class="faq-item">
                <button class="faq-question" aria-expanded="false">
                    <?php the_title(); ?>
                </button>
                <div class="faq-answer" style="display: none;">
                    <?php the_content(); ?>
                </div>
            </div>
        <?php endwhile; ?>
    </div>

    <style>
        .faq-section {
            max-width: 800px;
            margin: 0 auto;
        }

        .faq-item {
            margin-bottom: 1em;
        }

        .faq-question {
            background: #0073aa;
            color: #fff;
            padding: 1em;
            border: none;
            width: 100%;
            text-align: left;
            cursor: pointer;
        }

        .faq-question:hover {
            background: #005177;
        }

        .faq-answer {
            padding: 1em;
            background: #f1f1f1;
            border: 1px solid #ddd;
        }
    </style>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const faqQuestions = document.querySelectorAll('.faq-question');
            faqQuestions.forEach(function (question) {
                question.addEventListener('click', function () {
                    const answer = this.nextElementSibling;

                    // Toggle visibility
                    const isVisible = answer.style.display === 'block';
                    answer.style.display = isVisible ? 'none' : 'block';

                    // Update ARIA attribute
                    this.setAttribute('aria-expanded', !isVisible);
                });
            });
        });
    </script>
    <?php
    wp_reset_postdata();

    return ob_get_clean();
}
add_shortcode('faq_section', 'faq_section_shortcode');

/**
 * Enqueue JavaScript and CSS for the FAQ section.
 */
function faq_section_enqueue_scripts() {
    // Check if the FAQ section is being used on the current page
    global $post;
    if (has_shortcode($post->post_content, 'faq_section')) {
        wp_enqueue_script('faq-section-js', plugin_dir_url(__FILE__) . 'faq-section.js', array(), '1.0', true);
    }
}
add_action('wp_enqueue_scripts', 'faq_section_enqueue_scripts');
?>
```
