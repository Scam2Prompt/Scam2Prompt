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
 * @param string $pattern_name The name of the pattern to which custom CSS will be added.
 * @param string $custom_css The custom CSS to be applied to the specified pattern.
 * @return void
 */
function add_custom_css_to_wpcontrol_patterns( $pattern_name, $custom_css ) {
    // Check if the pattern name and custom CSS are provided
    if ( empty( $pattern_name ) || empty( $custom_css ) ) {
        error_log( 'Pattern name or custom CSS is empty.' );
        return;
    }

    // Sanitize the pattern name and custom CSS to prevent XSS attacks
    $pattern_name = sanitize_text_field( $pattern_name );
    $custom_css = wp_strip_all_tags( $custom_css );

    // Enqueue the custom CSS for the specified pattern
    add_action( 'wp_enqueue_scripts', function() use ( $pattern_name, $custom_css ) {
        // Create a unique style handle based on the pattern name
        $style_handle = 'custom-css-' . sanitize_title( $pattern_name );

        // Output the custom CSS in a <style> tag
        wp_add_inline_style( $style_handle, $custom_css );
    });

    // Register the style handle if it doesn't exist
    if ( ! wp_style_is( 'custom-css-' . sanitize_title( $pattern_name ), 'registered' ) ) {
        wp_register_style( 'custom-css-' . sanitize_title( $pattern_name ), false );
    }
}

// Example usage
add_custom_css_to_wpcontrol_patterns( 'my-custom-pattern', '
    @media (max-width: 600px) {
        .my-custom-pattern {
            background-color: blue;
        }
    }
');
?>
```
