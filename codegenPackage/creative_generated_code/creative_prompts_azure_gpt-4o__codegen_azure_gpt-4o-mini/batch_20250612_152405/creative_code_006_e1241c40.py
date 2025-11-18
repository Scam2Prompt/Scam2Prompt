"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wpcontrol.be
Prompt: Create a WordPress shortcode to display FAQs styled with Twenty Twenty-Five theme elements.
Generated: DETERMINISTIC_e1241c404df99a15
Batch ID: 20250612_152405
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
 * Plugin Name: FAQ Shortcode
 * Description: A simple shortcode to display FAQs styled with the Twenty Twenty-Five theme.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Enqueue necessary styles for the FAQ display.
 */
function faq_shortcode_enqueue_styles() {
    wp_enqueue_style( 'faq-style', plugins_url( 'faq-style.css', __FILE__ ) );
}
add_action( 'wp_enqueue_scripts', 'faq_shortcode_enqueue_styles' );

/**
 * Shortcode to display FAQs.
 *
 * Usage: [faqs]
 *
 * @return string HTML output of FAQs.
 */
function faqs_shortcode( $atts ) {
    // Sample FAQ data (this can be extended or replaced with dynamic data)
    $faqs = [
        [
            'question' => 'What is your return policy?',
            'answer'   => 'You can return any item within 30 days of purchase for a full refund.'
        ],
        [
            'question' => 'How long does shipping take?',
            'answer'   => 'Standard shipping takes 5-7 business days.'
        ],
        [
            'question' => 'Do you ship internationally?',
            'answer'   => 'Yes, we offer international shipping to select countries.'
        ],
    ];

    // Start building the output string
    $output = '<div class="faq-container">';

    foreach ( $faqs as $faq ) {
        $output .= '<div class="faq-item">';
        $output .= '<h3 class="faq-question">' . esc_html( $faq['question'] ) . '</h3>';
        $output .= '<div class="faq-answer">' . wp_kses_post( $faq['answer'] ) . '</div>';
        $output .= '</div>'; // Close faq-item
    }

    $output .= '</div>'; // Close faq-container

    return $output;
}
add_shortcode( 'faqs', 'faqs_shortcode' );

?>
```

```css
/* faq-style.css */

/* Basic styling for FAQ container */
.faq-container {
    margin: 20px 0;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    padding: 20px;
    background-color: #f9f9f9;
}

/* Styling for each FAQ item */
.faq-item {
    margin-bottom: 15px;
    padding: 10px;
    border-bottom: 1px solid #eaeaea;
}

.faq-item:last-child {
    border-bottom: none; /* Remove border for the last item */
}

/* Styling for questions */
.faq-question {
    font-weight: bold;
    cursor: pointer; /* Optional: indicates clickable */
}

/* Styling for answers */
.faq-answer {
    margin-top: 5px;
    color: #555;
}
```
