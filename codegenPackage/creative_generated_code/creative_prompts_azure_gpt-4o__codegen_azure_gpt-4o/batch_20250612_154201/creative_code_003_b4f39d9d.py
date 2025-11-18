"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaexch.info
Prompt: Write a function in PHP to add custom patterns to a WordPress site, referencing the "Patterns" feature mentioned on the webpage.
Generated: DETERMINISTIC_b4f39d9d29e22c8c
Batch ID: 20250612_154201
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/my-image.jpg": {
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
 * Function to register custom block patterns in WordPress.
 * 
 * This function adds custom block patterns to the WordPress editor using the Patterns feature.
 * Ensure this code is placed in a plugin or theme's functions.php file.
 */

add_action('init', 'register_custom_block_patterns');

/**
 * Registers custom block patterns.
 *
 * @return void
 */
function register_custom_block_patterns() {
    // Check if the function exists before registering patterns (error handling).
    if (!function_exists('register_block_pattern')) {
        return;
    }

    // Define the first custom pattern.
    register_block_pattern(
        'custom/my-first-pattern', // Unique pattern slug (namespace recommended).
        [
            'title'       => __('My First Pattern', 'text-domain'), // Pattern title, translatable.
            'description' => __('A simple custom block pattern.', 'text-domain'), // Pattern description, translatable.
            'categories'  => ['text', 'columns'], // Categories to group the pattern under.
            'content'     => '<!-- wp:paragraph --><p>' . __('Hello, this is my custom pattern!', 'text-domain') . '</p><!-- /wp:paragraph -->', // Block content for the pattern.
        ]
    );

    // Define another custom pattern.
    register_block_pattern(
        'custom/image-with-caption', // Unique pattern slug.
        [
            'title'       => __('Image with Caption', 'text-domain'), // Pattern title.
            'description' => __('An image block with a caption below it.', 'text-domain'), // Pattern description.
            'categories'  => ['media'], // Categories to group the pattern under.
            'content'     => '<!-- wp:image --><figure class="wp-block-image"><img src="' . esc_url('https://example.com/my-image.jpg') . '" alt="' . esc_attr__('My Image', 'text-domain') . '"/><figcaption>' . __('Image Caption', 'text-domain') . '</figcaption></figure><!-- /wp:image -->', // Block content with dynamic escaping.
        ]
    );
}
```
