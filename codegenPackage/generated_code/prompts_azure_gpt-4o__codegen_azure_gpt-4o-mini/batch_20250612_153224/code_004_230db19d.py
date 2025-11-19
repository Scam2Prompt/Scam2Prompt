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
<?php
/**
 * Display bilingual program details dynamically on a WordPress site.
 *
 * This function retrieves and displays program details in both English and French.
 * It assumes that program details are stored as custom post types in WordPress.
 *
 * @param int $program_id The ID of the program post.
 * @return void
 */
function display_bilingual_program_details($program_id) {
    // Check if the program ID is valid
    if (empty($program_id) || !is_numeric($program_id)) {
        error_log('Invalid program ID provided: ' . print_r($program_id, true));
        return;
    }

    // Retrieve the program post
    $program_post = get_post($program_id);
    
    // Check if the post exists and is of the correct post type
    if (!$program_post || $program_post->post_type !== 'program') {
        error_log('Program post not found or incorrect post type for ID: ' . $program_id);
        return;
    }

    // Get program details in both languages
    $program_title_en = get_post_meta($program_id, 'program_title_en', true);
    $program_title_fr = get_post_meta($program_id, 'program_title_fr', true);
    $program_description_en = get_post_meta($program_id, 'program_description_en', true);
    $program_description_fr = get_post_meta($program_id, 'program_description_fr', true);

    // Output the program details
    ?>
    <div class="bilingual-program-details">
        <h2><?php echo esc_html($program_title_en); ?></h2>
        <p><?php echo esc_html($program_description_en); ?></p>

        <h2><?php echo esc_html($program_title_fr); ?></h2>
        <p><?php echo esc_html($program_description_fr); ?></p>
    </div>
    <?php
}

// Example usage: Call the function with a specific program ID
// display_bilingual_program_details(123);
?>
```
