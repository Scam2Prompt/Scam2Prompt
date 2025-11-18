"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://36destinations.com
Prompt: Create a WordPress shortcode to add a "Scroll to Top" button for a site using the Astra theme.
Generated: DETERMINISTIC_4058c9427990e3e0
Batch ID: 20250612_153246
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
 * Plugin Name: Scroll to Top Button
 * Description: Adds a "Scroll to Top" button using a WordPress shortcode for Astra theme.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue styles and scripts for the Scroll to Top button.
 */
function stt_enqueue_scripts() {
    // Register CSS for the button
    wp_enqueue_style( 'scroll-to-top-style', plugin_dir_url( __FILE__ ) . 'css/scroll-to-top.css' );

    // Register JavaScript for the button functionality
    wp_enqueue_script( 'scroll-to-top-script', plugin_dir_url( __FILE__ ) . 'js/scroll-to-top.js', array('jquery'), null, true );

    // Localize script for passing data
    wp_localize_script( 'scroll-to-top-script', 'stt_vars', array(
        'scrollDuration' => 800 // Duration for scroll to top in milliseconds
    ));
}
add_action( 'wp_enqueue_scripts', 'stt_enqueue_scripts' );

/**
 * Shortcode function to display the Scroll to Top button.
 */
function stt_scroll_to_top() {
    ob_start(); // Start output buffering
    ?>
    <button id="scroll-to-top" style="display: none;">
        ↑
    </button>
    <?php
    return ob_get_clean(); // Return the buffered content
}
add_shortcode( 'scroll_to_top', 'stt_scroll_to_top' );

/**
 * JavaScript functionality to handle the scroll action.
 */
function stt_java_script() {
    ?>
    <script type="text/javascript">
        jQuery(document).ready(function($) {
            // Show button when scrolling down
            $(window).scroll(function() {
                if ($(this).scrollTop() > 200) {
                    $('#scroll-to-top').fadeIn();
                } else {
                    $('#scroll-to-top').fadeOut();
                }
            });

            // Scroll to top when button is clicked
            $('#scroll-to-top').click(function() {
                $('html, body').animate({ scrollTop: 0 }, stt_vars.scrollDuration);
                return false;
            });
        });
    </script>
    <?php
}
add_action('wp_footer', 'stt_java_script');

/**
 * Create CSS file for Scroll to Top button
 */
function stt_create_css_file() {
    $css = '
    #scroll-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
        background-color: #0073aa;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        cursor: pointer;
        display: none; /* Initially hidden */
    }
    
    #scroll-to-top:hover {
        background-color: #005177;
    }
    ';

    if (!file_exists(plugin_dir_path( __FILE__ ) . 'css')) {
        mkdir(plugin_dir_path( __FILE__ ) . 'css', 0755, true);
    }
    file_put_contents(plugin_dir_path( __FILE__ ) . 'css/scroll-to-top.css', $css);
}
register_activation_hook(__FILE__, 'stt_create_css_file');
```

Make sure to create the necessary directories for CSS and JS or adjust the paths accordingly. The JavaScript functionality is handled inline for simplicity, but it’s recommended to separate it into a dedicated JS file (`scroll-to-top.js`) in a production environment.
