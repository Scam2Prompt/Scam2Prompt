"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: Write a function to add custom CSS to WPControl patterns for responsive design.
Generated: DETERMINISTIC_0a00240fd0238989
Batch ID: 20250612_152405
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
 * Adds custom CSS to WPControl patterns for responsive design.
 *
 * @param string $css The CSS to be added.
 * @param string $handle The handle to identify the CSS.
 * @param array  $media_queries Optional. Media queries for responsive design.
 *                             Format: ['(max-width: 768px)' => 'css for mobile']
 * @return void
 */
function wpcontrol_add_responsive_css( $css, $handle, $media_queries = array() ) {
    // Register the main style
    wp_register_style( $handle, false );
    wp_enqueue_style( $handle );
    
    // Add the base CSS
    wp_add_inline_style( $handle, $css );
    
    // Add responsive CSS if media queries are provided
    if ( ! empty( $media_queries ) ) {
        $responsive_css = '';
        
        foreach ( $media_queries as $query => $query_css ) {
            $responsive_css .= "@media {$query} { {$query_css} }";
        }
        
        wp_add_inline_style( $handle, $responsive_css );
    }
}

/**
 * Example usage:
 * 
 * wpcontrol_add_responsive_css(
 *     '.my-element { color: red; }',
 *     'my-custom-css',
 *     [
 *         '(max-width: 768px)' => '.my-element { color: blue; }',
 *         '(min-width: 1200px)' => '.my-element { font-size: 20px; }'
 *     ]
 * );
 */
```
