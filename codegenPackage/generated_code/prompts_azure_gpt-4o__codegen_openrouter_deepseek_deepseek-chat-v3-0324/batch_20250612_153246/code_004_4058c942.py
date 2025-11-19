"""
Generated Code Metadata:
========================
Original URL: https://36destinations.com
Prompt: Create a WordPress shortcode to add a "Scroll to Top" button for a site using the Astra theme.
Generated: DETERMINISTIC_4058c9427990e3e0
Batch ID: 20250612_153246
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
 * Scroll to Top Shortcode for WordPress with Astra Theme
 * 
 * This shortcode adds a customizable "Scroll to Top" button to the site.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Register the scroll to top shortcode
 */
function astra_scroll_to_top_shortcode($atts) {
    // Default attributes
    $atts = shortcode_atts(
        array(
            'color'      => '#ffffff',
            'bg_color'   => '#0274be',
            'size'       => '40px',
            'position'   => 'right',
            'bottom'     => '20px',
            'right'      => '20px',
            'left'       => 'unset',
            'icon'       => 'dashicons-arrow-up-alt2',
            'visibility' => 'all' // all, desktop, mobile
        ),
        $atts,
        'scroll_to_top'
    );

    // Generate unique ID for the button
    $button_id = 'scroll-to-top-' . wp_rand(1, 1000);

    // Position handling
    $position_style = '';
    if ($atts['position'] === 'left') {
        $position_style = 'left: ' . esc_attr($atts['left']) . '; right: unset;';
    } else {
        $position_style = 'right: ' . esc_attr($atts['right']) . '; left: unset;';
    }

    // Visibility classes
    $visibility_class = '';
    if ($atts['visibility'] === 'desktop') {
        $visibility_class = 'astra-scroll-to-top-desktop';
    } elseif ($atts['visibility'] === 'mobile') {
        $visibility_class = 'astra-scroll-to-top-mobile';
    }

    // Enqueue dashicons if icon is from dashicons
    if (strpos($atts['icon'], 'dashicons-') === 0) {
        wp_enqueue_style('dashicons');
    }

    // Output the button HTML
    ob_start();
    ?>
    <button id="<?php echo esc_attr($button_id); ?>" class="astra-scroll-to-top <?php echo esc_attr($visibility_class); ?>" aria-label="<?php esc_attr_e('Scroll to top', 'astra'); ?>">
        <span class="<?php echo esc_attr($atts['icon']); ?>"></span>
    </button>

    <style>
        #<?php echo esc_attr($button_id); ?> {
            position: fixed;
            bottom: <?php echo esc_attr($atts['bottom']); ?>;
            <?php echo $position_style; ?>
            width: <?php echo esc_attr($atts['size']); ?>;
            height: <?php echo esc_attr($atts['size']); ?>;
            background-color: <?php echo esc_attr($atts['bg_color']); ?>;
            color: <?php echo esc_attr($atts['color']); ?>;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 999;
        }

        #<?php echo esc_attr($button_id); ?>.visible {
            opacity: 1;
            visibility: visible;
        }

        #<?php echo esc_attr($button_id); ?>:hover {
            opacity: 0.9;
        }

        #<?php echo esc_attr($button_id); ?> span {
            font-size: calc(<?php echo esc_attr($atts['size']); ?> * 0.5);
            line-height: 1;
        }

        @media (max-width: 768px) {
            .astra-scroll-to-top-desktop {
                display: none !important;
            }
        }

        @media (min-width: 769px) {
            .astra-scroll-to-top-mobile {
                display: none !important;
            }
        }
    </style>

    <script>
        (function($) {
            $(document).ready(function() {
                var scrollButton = $('#<?php echo esc_attr($button_id); ?>');
                
                // Show/hide button based on scroll position
                $(window).scroll(function() {
                    if ($(this).scrollTop() > 300) {
                        scrollButton.addClass('visible');
                    } else {
                        scrollButton.removeClass('visible');
                    }
                });

                // Smooth scroll to top
                scrollButton.click(function(e) {
                    e.preventDefault();
                    $('html, body').animate({scrollTop: 0}, '300');
                });
            });
        })(jQuery);
    </script>
    <?php
    return ob_get_clean();
}
add_shortcode('scroll_to_top', 'astra_scroll_to_top_shortcode');

/**
 * Enqueue necessary scripts and styles
 */
function astra_scroll_to_top_assets() {
    wp_enqueue_script('jquery');
}
add_action('wp_enqueue_scripts', 'astra_scroll_to_top_assets');
```
