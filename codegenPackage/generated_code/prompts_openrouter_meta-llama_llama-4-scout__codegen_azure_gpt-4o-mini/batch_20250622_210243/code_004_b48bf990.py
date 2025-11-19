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
 * Plugin Name: Custom FAQ Shortcode
 * Description: A shortcode to display a list of FAQs with a custom layout.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Register the FAQ shortcode.
 */
function custom_faq_shortcode( $atts ) {
    // Define default attributes
    $atts = shortcode_atts( array(
        'title' => 'Frequently Asked Questions',
    ), $atts, 'faq' );

    // Start output buffering
    ob_start();

    // Sample FAQs array (this could be replaced with dynamic data)
    $faqs = array(
        array(
            'question' => 'What is your return policy?',
            'answer'   => 'You can return any item within 30 days of purchase for a full refund.',
        ),
        array(
            'question' => 'How long does shipping take?',
            'answer'   => 'Shipping usually takes 5-7 business days.',
        ),
        array(
            'question' => 'Do you offer customer support?',
            'answer'   => 'Yes, we offer 24/7 customer support via email and chat.',
        ),
    );

    // Check if there are FAQs to display
    if ( ! empty( $faqs ) ) {
        echo '<div class="custom-faq">';
        echo '<h2>' . esc_html( $atts['title'] ) . '</h2>';
        echo '<ul>';

        // Loop through each FAQ and display it
        foreach ( $faqs as $faq ) {
            echo '<li>';
            echo '<strong>' . esc_html( $faq['question'] ) . '</strong>';
            echo '<p>' . esc_html( $faq['answer'] ) . '</p>';
            echo '</li>';
        }

        echo '</ul>';
        echo '</div>';
    } else {
        // Display a message if no FAQs are available
        echo '<p>No FAQs available at this time.</p>';
    }

    // Return the output buffer content
    return ob_get_clean();
}

// Register the shortcode with WordPress
add_shortcode( 'faq', 'custom_faq_shortcode' );

/**
 * Enqueue custom styles for the FAQ section.
 */
function custom_faq_styles() {
    wp_enqueue_style( 'custom-faq-style', plugin_dir_url( __FILE__ ) . 'css/custom-faq.css' );
}
add_action( 'wp_enqueue_scripts', 'custom_faq_styles' );
```

**Note:** You should create a `css/custom-faq.css` file in the same directory as this PHP file to style the FAQ section according to your design preferences.
