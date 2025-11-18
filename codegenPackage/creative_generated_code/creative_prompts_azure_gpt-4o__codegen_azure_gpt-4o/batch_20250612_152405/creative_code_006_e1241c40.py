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
 * Plugin Name: Custom FAQs Shortcode
 * Description: A WordPress shortcode to display FAQs styled with Twenty Twenty-Five theme elements.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register the FAQ shortcode.
 */
function custom_faq_shortcode($atts) {
    // Shortcode attributes with defaults.
    $atts = shortcode_atts(
        array(
            'title' => 'Frequently Asked Questions', // Default title.
        ),
        $atts,
        'custom_faq'
    );

    // FAQs data (could be fetched dynamically from a custom post type or database).
    $faqs = array(
        array(
            'question' => 'What is WordPress?',
            'answer'   => 'WordPress is a popular content management system (CMS) used to create websites and blogs.',
        ),
        array(
            'question' => 'How do I install a WordPress plugin?',
            'answer'   => 'You can install a plugin by navigating to the Plugins menu in the WordPress admin dashboard and clicking "Add New".',
        ),
        array(
            'question' => 'Is WordPress free?',
            'answer'   => 'Yes, WordPress is open-source software and is free to use.',
        ),
    );

    // Start output buffering.
    ob_start();

    ?>
    <div class="faq-container twenty-twenty-five-style">
        <h2 class="faq-title"><?php echo esc_html($atts['title']); ?></h2>
        <ul class="faq-list">
            <?php foreach ($faqs as $faq): ?>
                <li class="faq-item">
                    <button class="faq-question twenty-twenty-five-button-style" aria-expanded="false">
                        <?php echo esc_html($faq['question']); ?>
                    </button>
                    <div class="faq-answer" style="display: none;">
                        <p><?php echo esc_html($faq['answer']); ?></p>
                    </div>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const faqButtons = document.querySelectorAll('.faq-question');

            faqButtons.forEach(button => {
                button.addEventListener('click', function () {
                    const answer = this.nextElementSibling;
                    const isExpanded = this.getAttribute('aria-expanded') === 'true';

                    // Toggle the visibility of the answer.
                    answer.style.display = isExpanded ? 'none' : 'block';

                    // Update the aria-expanded value.
                    this.setAttribute('aria-expanded', !isExpanded);
                });
            });
        });
    </script>
    <style>
        .faq-container {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        .faq-title {
            font-size: 24px;
            margin-bottom: 15px;
            color: #333;
        }

        .faq-list {
            list-style: none;
            padding: 0;
        }

        .faq-item {
            margin-bottom: 10px;
        }

        .faq-question {
            display: block;
            width: 100%;
            background-color: #f5f5f5;
            color: #333;
            border: none;
            padding: 10px;
            text-align: left;
            cursor: pointer;
            border-radius: 5px;
            font-size: 18px;
        }

        .faq-question:hover {
            background-color: #eaeaea;
        }

        .faq-answer {
            margin-top: 10px;
            padding: 10px;
            background-color: #f9f9f9;
            border-left: 4px solid #0073aa;
            border-radius: 4px;
        }
    </style>
    <?php

    // Return the buffered output.
    return ob_get_clean();
}

// Add the shortcode.
add_shortcode('custom_faq', 'custom_faq_shortcode');
?>
```
