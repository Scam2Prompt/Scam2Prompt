"""
Generated Code Metadata:
========================
Original URL: https://magnumrockets.com
Prompt: Create a shortcode for WordPress that displays a list of FAQs, similar to the "About FAQs" section on the site, using a custom-designed layout.
Generated: DETERMINISTIC_b48bf99000e85c3e
Batch ID: 20250622_210243
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
 * FAQ Shortcode
 *
 * Displays a list of FAQs in a custom-designed layout.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output.
 */
function faq_shortcode($atts) {
    // Define default attributes.
    $atts = shortcode_atts(
        array(
            'category' => '', // Category slug or ID.
            'limit'    => -1, // Number of FAQs to display.
            'orderby'  => 'title', // Order by 'title', 'date', or 'rand'.
            'order'    => 'ASC', // Order direction: 'ASC' or 'DESC'.
        ),
        $atts,
        'faq'
    );

    // Get FAQs.
    $args = array(
        'post_type'      => 'faq', // Custom post type for FAQs.
        'posts_per_page' => $atts['limit'],
        'orderby'        => $atts['orderby'],
        'order'          => $atts['order'],
    );

    if (!empty($atts['category'])) {
        $args['tax_query'] = array(
            array(
                'taxonomy' => 'faq_category',
                'field'    => 'slug',
                'terms'    => $atts['category'],
            ),
        );
    }

    $faqs = get_posts($args);

    // Check if there are any FAQs.
    if (empty($faqs)) {
        return '<p>No FAQs found.</p>';
    }

    // Start output buffer.
    ob_start();

    // Begin FAQ list.
    ?>
    <div class="faq-list">
        <?php
        foreach ($faqs as $faq) {
            // Get FAQ title and content.
            $title   = get_the_title($faq->ID);
            $content = get_post_field('post_content', $faq->ID);

            // Display FAQ item.
            ?>
            <div class="faq-item">
                <h3 class="faq-title"><?php echo esc_html($title); ?></h3>
                <div class="faq-content">
                    <?php echo wpautop(esc_html($content)); ?>
                </div>
            </div>
            <?php
        }
        ?>
    </div>
    <?php

    // Return output.
    return ob_get_clean();
}
add_shortcode('faq', 'faq_shortcode');

/**
 * Register custom post type for FAQs.
 */
function register_faq_post_type() {
    register_post_type('faq',
        array(
            'labels'      => array(
                'name'          => __('FAQs', 'text_domain'),
                'singular_name' => __('FAQ', 'text_domain'),
            ),
            'public'      => true,
            'has_archive' => true,
            'supports'    => array('title', 'editor'),
        )
    );
}
add_action('init', 'register_faq_post_type');

/**
 * Register taxonomy for FAQ categories.
 */
function register_faq_category_taxonomy() {
    register_taxonomy(
        'faq_category',
        'faq',
        array(
            'labels' => array(
                'name'          => __('FAQ Categories', 'text_domain'),
                'add_new_item'  => __('Add New FAQ Category', 'text_domain'),
            ),
            'hierarchical' => true,
        )
    );
}
add_action('init', 'register_faq_category_taxonomy');
```
