"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: Write a PHP function to display bilingual program details dynamically on a WordPress site, similar to the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_230db19d8dccd890
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Displays bilingual program details dynamically on a WordPress site.
 *
 * @param int $post_id The ID of the post to retrieve program details from.
 * @param string $language The language to display program details in (e.g., 'en', 'fr').
 *
 * @return string The bilingual program details HTML.
 */
function display_bilingual_program_details($post_id, $language) {
    // Check if post ID and language are valid
    if (empty($post_id) || empty($language)) {
        throw new Exception('Post ID and language are required.');
    }

    // Get post meta for program details
    $program_details_en = get_post_meta($post_id, 'program_details_en', true);
    $program_details_fr = get_post_meta($post_id, 'program_details_fr', true);

    // Determine which language to display
    switch ($language) {
        case 'en':
            $program_details = $program_details_en;
            break;
        case 'fr':
            $program_details = $program_details_fr;
            break;
        default:
            throw new Exception('Unsupported language.');
    }

    // Check if program details exist
    if (empty($program_details)) {
        return '<p>' . __('No program details available.', 'text-domain') . '</p>';
    }

    // Render bilingual program details HTML
    $output = '<div class="program-details">';
    $output .= '<h2>' . __('Program Details', 'text-domain') . '</h2>';
    $output .= '<div class="program-details-content">';
    $output .= $program_details;
    $output .= '</div>';
    $output .= '</div>';

    return $output;
}

/**
 * Shortcode to display bilingual program details on a WordPress page.
 *
 * @param array $atts Shortcode attributes.
 *
 * @return string The bilingual program details HTML.
 */
function bilingual_program_details_shortcode($atts) {
    // Define shortcode attributes
    $atts = shortcode_atts(
        array(
            'post_id' => get_the_ID(),
            'language' => 'en',
        ),
        $atts,
        'bilingual_program_details'
    );

    // Display bilingual program details
    try {
        return display_bilingual_program_details($atts['post_id'], $atts['language']);
    } catch (Exception $e) {
        return '<p>' . __('Error: ', 'text-domain') . $e->getMessage() . '</p>';
    }
}

// Add shortcode
add_shortcode('bilingual_program_details', 'bilingual_program_details_shortcode');
```

```php
// Add metabox to save program details
function add_program_details_metabox() {
    add_meta_box(
        'program_details',
        __('Program Details', 'text-domain'),
        'program_details_metabox_callback',
        'post',
        'advanced',
        'high'
    );
}

// Callback function for metabox
function program_details_metabox_callback() {
    // Get post meta for program details
    $program_details_en = get_post_meta(get_the_ID(), 'program_details_en', true);
    $program_details_fr = get_post_meta(get_the_ID(), 'program_details_fr', true);

    // Render metabox fields
    ?>
    <div class="program-details-metabox">
        <label for="program_details_en"><?php _e('English', 'text-domain'); ?></label>
        <textarea id="program_details_en" name="program_details_en"><?php echo esc_textarea($program_details_en); ?></textarea>
        <br>
        <label for="program_details_fr"><?php _e('French', 'text-domain'); ?></label>
        <textarea id="program_details_fr" name="program_details_fr"><?php echo esc_textarea($program_details_fr); ?></textarea>
    </div>
    <?php
}

// Save program details metabox data
function save_program_details_metabox_data($post_id) {
    // Check if post ID is valid
    if (!isset($post_id) || !current_user_can('edit_post', $post_id)) {
        return;
    }

    // Save program details
    $program_details_en = sanitize_text_field($_POST['program_details_en']);
    $program_details_fr = sanitize_text_field($_POST['program_details_fr']);

    update_post_meta($post_id, 'program_details_en', $program_details_en);
    update_post_meta($post_id, 'program_details_fr', $program_details_fr);
}

// Add actions
add_action('add_meta_boxes', 'add_program_details_metabox');
add_action('save_post', 'save_program_details_metabox_data');
```
