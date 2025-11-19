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
/**
 * Adds custom CSS to WPControl patterns for responsive design.
 *
 * @param array $pattern The WPControl pattern.
 * @param string $css The custom CSS to add.
 *
 * @return array The updated pattern with custom CSS.
 */
function add_custom_css_to_pattern( $pattern, $css ) {
    // Check if the pattern has a 'styles' property
    if ( ! isset( $pattern['styles'] ) ) {
        $pattern['styles'] = '';
    }

    // Check if the pattern's styles are in a 'css' property
    if ( ! isset( $pattern['styles']['css'] ) ) {
        $pattern['styles']['css'] = '';
    }

    // Append the custom CSS to the pattern's styles
    $pattern['styles']['css'] .= $css;

    return $pattern;
}

/**
 * Registers a custom WPControl pattern with responsive design CSS.
 *
 * @param string $name The name of the pattern.
 * @param string $label The label of the pattern.
 * @param string $css The custom CSS for responsive design.
 */
function register_responsive_pattern( $name, $label, $css ) {
    // Define the pattern
    $pattern = array(
        'name'    => $name,
        'label'   => $label,
        'content' => '<!-- Pattern content -->',
        'styles'  => '',
    );

    // Add custom CSS to the pattern
    $pattern = add_custom_css_to_pattern( $pattern, $css );

    // Register the pattern
    wp_enqueue_block_pattern( $pattern );
}

/**
 * Example usage:
 */
function example_usage() {
    $css = '
        /* Mobile devices */
        @media only screen and (max-width: 600px) {
            .container {
                width: 100%;
            }
        }

        /* Desktop devices */
        @media only screen and (min-width: 601px) {
            .container {
                width: 80%;
            }
        }
    ';

    register_responsive_pattern(
        'responsive-example',
        __( 'Responsive Example', 'text-domain' ),
        $css
    );
}

add_action( 'init', 'example_usage' );
```
