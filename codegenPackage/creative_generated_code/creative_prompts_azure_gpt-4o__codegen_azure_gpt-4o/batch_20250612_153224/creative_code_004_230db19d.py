"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Write a PHP function to display bilingual program details dynamically on a WordPress site, similar to the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_230db19d8dccd890
Batch ID: 20250612_153224
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
 * Function to display bilingual program details dynamically on a WordPress site.
 * 
 * This function retrieves program details from WordPress custom fields
 * and displays them in both English and French. Make sure your WordPress site
 * has Advanced Custom Fields (ACF) or similar to store bilingual data.
 * 
 * @param int $post_id The ID of the post containing the program details.
 * @return string HTML output of the bilingual program details.
 */
function display_bilingual_program_details($post_id) {
    // Check if $post_id is valid
    if (!is_int($post_id) || $post_id <= 0) {
        return '<p>Error: Invalid program ID provided.</p>';
    }

    // Retrieve program data dynamically using WordPress functions
    $english_title = get_post_meta($post_id, 'program_title_en', true);
    $french_title = get_post_meta($post_id, 'program_title_fr', true);
    $english_description = get_post_meta($post_id, 'program_description_en', true);
    $french_description = get_post_meta($post_id, 'program_description_fr', true);

    // Error handling for missing fields
    if (empty($english_title) || empty($french_title) || empty($english_description) || empty($french_description)) {
        return '<p>Error: Program details are incomplete or missing.</p>';
    }

    // Generate bilingual output
    $output = '<div class="bilingual-program-details">';
    $output .= '<div class="program-title">';
    $output .= '<h2>' . esc_html($english_title) . ' / ' . esc_html($french_title) . '</h2>';
    $output .= '</div>';
    $output .= '<div class="program-description">';
    $output .= '<h3>' . __('English', 'text-domain') . '</h3>';
    $output .= '<p>' . esc_html($english_description) . '</p>';
    $output .= '<h3>' . __('French', 'text-domain') . '</h3>';
    $output .= '<p>' . esc_html($french_description) . '</p>';
    $output .= '</div>';
    $output .= '</div>';

    return $output;
}

/**
 * Shortcode wrapper for display_bilingual_program_details.
 * 
 * @param array $atts Attributes passed to the shortcode. Expects 'id' as post ID.
 * @return string HTML output of the bilingual program details.
 */
function bilingual_program_shortcode($atts) {
    $atts = shortcode_atts(array(
        'id' => 0, // Default post ID is 0
    ), $atts);

    // Call the function and return the output
    return display_bilingual_program_details((int) $atts['id']);
}

// Register the shortcode
add_shortcode('bilingual_program', 'bilingual_program_shortcode');
```
