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
 * Custom FAQ Section Shortcode for WordPress
 *
 * This code provides a shortcode to create a custom FAQ section on a 
 * WordPress site. The FAQ section is designed to be similar to the layout 
 * found on Sabrina Carpenter's merchandise page.
 *
 * Usage: [custom_faq]
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register the custom FAQ shortcode
function custom_faq_shortcode() {
    // Define FAQs as an associative array
    $faqs = [
        [
            'question' => 'What is your return policy?',
            'answer'   => 'You can return any unused item within 30 days for a full refund.'
        ],
        [
            'question' => 'How long does shipping take?',
            'answer'   => 'Shipping usually takes 5-7 business days, depending on your location.'
        ],
        [
            'question' => 'Do you ship internationally?',
            'answer'   => 'Yes, we ship to most countries worldwide. Additional shipping fees may apply.'
        ]
        // Add more FAQs as needed
    ];

    // Start output buffering
    ob_start();
    ?>
    <div class="custom-faq-section">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
            <?php foreach ( $faqs as $faq ) : ?>
                <div class="faq-item">
                    <h3 class="faq-question"><?php echo esc_html( $faq['question'] ); ?></h3>
                    <div class="faq-answer"><?php echo esc_html( $faq['answer'] ); ?></div>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
    <style>
        .custom-faq-section {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .faq-item {
            margin-bottom: 15px;
        }
        .faq-question {
            cursor: pointer;
            font-weight: bold;
            color: #333;
        }
        .faq-answer {
            display: none;
            margin-top: 5px;
            color: #666;
        }
        .faq-item.active .faq-answer {
            display: block;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const questions = document.querySelectorAll('.faq-question');
            questions.forEach(question => {
                question.addEventListener('click', function() {
                    const parent = this.parentElement;
                    parent.classList.toggle('active');
                });
            });
        });
    </script>
    <?php
    // Return the buffered content
    return ob_get_clean();
}

// Add the shortcode to WordPress
add_shortcode( 'custom_faq', 'custom_faq_shortcode' );
```

### Instructions for Use:
1. Place this code in your theme's `functions.php` file or in a custom plugin.
2. Use the shortcode `[custom_faq]` in any post or page where you want to display the FAQ section.
