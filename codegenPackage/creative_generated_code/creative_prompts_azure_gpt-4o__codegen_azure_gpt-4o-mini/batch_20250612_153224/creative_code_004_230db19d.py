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
 * Fetch and display bilingual program details dynamically.
 *
 * This function retrieves program details from a custom post type and displays them
 * in a bilingual format on a WordPress site.
 *
 * @param string $language 'en' for English, 'fr' for French.
 * @return void
 */
function display_bilingual_program_details($language = 'en') {
    // Ensure the language parameter is valid
    if (!in_array($language, ['en', 'fr'])) {
        throw new InvalidArgumentException('Invalid language selected. Use "en" or "fr".');
    }

    // Query for programs from a custom post type 'program'
    $args = [
        'post_type' => 'program',
        'post_status' => 'publish',
        'posts_per_page' => -1, // Retrieve all published programs
    ];

    $programs = new WP_Query($args);

    if ($programs->have_posts()) {
        echo '<div class="program-details">';
        
        while ($programs->have_posts()) {
            $programs->the_post();

            // Retrieve custom fields for the program
            $program_title = get_post_meta(get_the_ID(), 'program_title_' . $language, true);
            $program_description = get_post_meta(get_the_ID(), 'program_description_' . $language, true);
            $program_schedule = get_post_meta(get_the_ID(), 'program_schedule_' . $language, true);

            // Ensure that all required fields are available
            if (!$program_title || !$program_description || !$program_schedule) {
                error_log('Missing program details for post ID: ' . get_the_ID());
                continue; // Skip this program if any details are missing
            }

            // Display program details
            echo '<div class="program">';
            echo '<h2>' . esc_html($program_title) . '</h2>';
            echo '<p>' . esc_html($program_description) . '</p>';
            echo '<p><strong>Schedule:</strong> ' . esc_html($program_schedule) . '</p>';
            echo '</div>';
        }

        echo '</div>';
        wp_reset_postdata(); // Restore original post data
    } else {
        echo '<p>No programs found.</p>';
    }
}

// Example usage: To display English program details
// display_bilingual_program_details('en');

// Example usage: To display French program details
// display_bilingual_program_details('fr');
?>
```
