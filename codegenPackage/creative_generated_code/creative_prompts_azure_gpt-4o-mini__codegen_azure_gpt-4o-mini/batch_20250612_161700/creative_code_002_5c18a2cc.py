"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdjuangrande.es
Prompt: Write a function in PHP to display the sponsors' list dynamically on a WordPress site for a football club.
Generated: DETERMINISTIC_5c18a2cc542c428e
Batch ID: 20250612_161700
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
 * Function to display the sponsors' list dynamically on a WordPress site for a football club.
 *
 * This function fetches the sponsors from a custom post type 'sponsors' and displays them
 * in a structured format. Ensure the custom post type is registered before using this function.
 *
 * @return void
 */
function display_sponsors_list() {
    // Arguments for WP_Query
    $args = array(
        'post_type'      => 'sponsors',
        'posts_per_page' => -1, // Retrieve all sponsors
        'post_status'    => 'publish',
    );

    // The Query
    $sponsors_query = new WP_Query($args);

    // Check if there are any sponsors to display
    if ($sponsors_query->have_posts()) {
        echo '<div class="sponsors-list">';
        echo '<h2>Our Sponsors</h2>';
        echo '<ul>';

        // The Loop
        while ($sponsors_query->have_posts()) {
            $sponsors_query->the_post();
            $sponsor_logo = get_the_post_thumbnail_url(get_the_ID(), 'full'); // Get sponsor logo URL
            $sponsor_name = get_the_title(); // Get sponsor name
            $sponsor_website = get_post_meta(get_the_ID(), 'sponsor_website', true); // Get sponsor website URL

            echo '<li>';
            if ($sponsor_website) {
                echo '<a href="' . esc_url($sponsor_website) . '" target="_blank" rel="noopener noreferrer">';
            }
            echo '<img src="' . esc_url($sponsor_logo) . '" alt="' . esc_attr($sponsor_name) . ' Logo">';
            if ($sponsor_website) {
                echo '</a>';
            }
            echo '<p>' . esc_html($sponsor_name) . '</p>';
            echo '</li>';
        }

        echo '</ul>';
        echo '</div>';

        // Restore original Post Data
        wp_reset_postdata();
    } else {
        // No sponsors found
        echo '<div class="sponsors-list">';
        echo '<h2>Our Sponsors</h2>';
        echo '<p>No sponsors found.</p>';
        echo '</div>';
    }
}

// Hook the function to a shortcode for easy use in pages or posts
add_shortcode('sponsors_list', 'display_sponsors_list');
?>
```
