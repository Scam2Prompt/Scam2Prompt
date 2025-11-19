"""
Generated Code Metadata:
========================
Original URL: https://metaexch.info
Prompt: Write a function in PHP to add custom patterns to a WordPress site, referencing the "Patterns" feature mentioned on the webpage.
Generated: DETERMINISTIC_b4f39d9d29e22c8c
Batch ID: 20250612_154201
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
 * Registers custom block patterns for a WordPress site.
 *
 * This function should be called during the 'init' action hook.
 *
 * @return void
 */
function register_custom_block_patterns() {
    // Check if the function exists to avoid errors in case the block patterns feature is not available.
    if ( ! function_exists( 'register_block_pattern' ) ) {
        return;
    }

    // Define an array of custom block patterns.
    $patterns = [
        [
            'name'        => 'custom-pattern-1',
            'title'       => __( 'Custom Pattern 1', 'text-domain' ),
            'description' => __( 'A description of custom pattern 1.', 'text-domain' ),
            'content'     => '<!-- wp:paragraph --><p>' . __( 'This is a custom pattern 1.', 'text-domain' ) . '</p><!-- /wp:paragraph -->',
        ],
        [
            'name'        => 'custom-pattern-2',
            'title'       => __( 'Custom Pattern 2', 'text-domain' ),
            'description' => __( 'A description of custom pattern 2.', 'text-domain' ),
            'content'     => '<!-- wp:heading --><h2>' . __( 'This is a custom pattern 2.', 'text-domain' ) . '</h2><!-- /wp:heading -->',
        ],
    ];

    // Loop through each pattern and register it.
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
