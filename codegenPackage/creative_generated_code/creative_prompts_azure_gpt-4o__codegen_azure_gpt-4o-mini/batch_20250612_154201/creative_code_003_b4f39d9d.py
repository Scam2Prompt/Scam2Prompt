"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaexch.info
Prompt: Write a function in PHP to add custom patterns to a WordPress site, referencing the "Patterns" feature mentioned on the webpage.
Generated: DETERMINISTIC_b4f39d9d29e22c8c
Batch ID: 20250612_154201
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
 * Registers custom block patterns for a WordPress site.
 *
 * This function adds custom patterns to the WordPress block editor,
 * allowing users to easily insert predefined layouts into their posts and pages.
 *
 * @return void
 */
function register_custom_block_patterns() {
    // Check if the block patterns feature is available.
    if ( ! function_exists( 'register_block_pattern' ) ) {
        return;
    }

    // Define an array of custom patterns.
    $patterns = [
        [
            'name'        => 'custom-pattern-1',
            'title'       => __( 'Custom Pattern 1', 'text-domain' ),
            'description' => __( 'A simple two-column layout with an image and text.', 'text-domain' ),
            'content'     => '<!-- wp:columns -->' .
                            '<div class="wp-block-columns">' .
                            '<!-- wp:column -->' .
                            '<div class="wp-block-column">' .
                            '<!-- wp:image {"id":123,"sizeSlug":"large"} -->' .
                            '<figure class="wp-block-image"><img src="path/to/image.jpg" alt="Image description"/></figure>' .
                            '<!-- /wp:image -->' .
                            '</div>' .
                            '<!-- /wp:column -->' .
                            '<!-- wp:column -->' .
                            '<div class="wp-block-column">' .
                            '<!-- wp:paragraph -->' .
                            '<p>' . __( 'Your custom text goes here.', 'text-domain' ) . '</p>' .
                            '<!-- /wp:paragraph -->' .
                            '</div>' .
                            '<!-- /wp:column -->' .
                            '</div>' .
                            '<!-- /wp:columns -->',
        ],
        // Add more patterns here as needed.
    ];

    // Register each pattern.
    foreach ( $patterns as $pattern ) {
        register_block_pattern(
            $pattern['name'],
            [
                'title'       => $pattern['title'],
                'description' => $pattern['description'],
                'content'     => $pattern['content'],
            ]
        );
    }
}

// Hook the function to the 'init' action.
add_action( 'init', 'register_custom_block_patterns' );
```
