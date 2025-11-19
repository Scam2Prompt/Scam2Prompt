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
 * FAQ Shortcode for WordPress
 * Displays a list of FAQs with custom layout
 */

function faq_shortcode($atts) {
    // Default attributes
    $atts = shortcode_atts(array(
        'category' => '',    // FAQ category slug
        'limit'    => -1,    // Number of FAQs to show (-1 for all)
    ), $atts, 'faq');

    try {
        // Query arguments
        $args = array(
            'post_type'      => 'faq',
            'posts_per_page' => $atts['limit'],
            'orderby'        => 'menu_order',
            'order'          => 'ASC',
        );

        // Add category filter if specified
        if (!empty($atts['category'])) {
            $args['tax_query'] = array(
                array(
                    'taxonomy' => 'faq_category',
                    'field'    => 'slug',
                    'terms'    => $atts['category'],
                )
            );
        }

        $faqs = new WP_Query($args);

        if (!$faqs->have_posts()) {
            return '<p>No FAQs found.</p>';
        }

        ob_start(); // Start output buffering
        ?>
        <div class="faq-container">
            <?php while ($faqs->have_posts()) : $faqs->the_post(); ?>
                <div class="faq-item">
                    <div class="faq-question">
                        <h3><?php the_title(); ?></h3>
                        <span class="toggle-icon">+</span>
                    </div>
                    <div class="faq-answer">
                        <?php the_content(); ?>
                    </div>
                </div>
            <?php endwhile; ?>
        </div>

        <style>
            .faq-container {
                margin: 20px 0;
            }
            .faq-item {
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                margin-bottom: 10px;
                overflow: hidden;
            }
            .faq-question {
                padding: 15px;
                background: #f9f9f9;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .faq-question h3 {
                margin: 0;
                font-size: 18px;
            }
            .faq-answer {
                padding: 0 15px;
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.3s ease;
            }
            .faq-item.active .faq-answer {
                padding: 15px;
                max-height: 1000px;
            }
            .faq-item.active .toggle-icon {
                transform: rotate(45deg);
            }
            .toggle-icon {
                font-size: 20px;
                transition: transform 0.3s ease;
            }
        </style>

        <script>
            jQuery(document).ready(function($) {
                $('.faq-question').click(function() {
                    $(this).parent().toggleClass('active');
                });
            });
        </script>
        <?php
        wp_reset_postdata();
        return ob_get_clean(); // Return buffered content

    } catch (Exception $e) {
        error_log('FAQ Shortcode Error: ' . $e->getMessage());
        return '<p>Error displaying FAQs. Please try again later.</p>';
    }
}
add_shortcode('faq', 'faq_shortcode');
```
