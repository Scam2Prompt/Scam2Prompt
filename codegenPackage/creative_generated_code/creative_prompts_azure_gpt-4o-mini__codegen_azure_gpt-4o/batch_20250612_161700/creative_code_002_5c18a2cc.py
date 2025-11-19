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
 * Function to dynamically display the sponsors' list on a WordPress site for a football club.
 *
 * This function queries the 'sponsors' custom post type and displays them in a structured format.
 * Ensure that the 'sponsors' custom post type is registered in WordPress before using this function.
 *
 * @return void Outputs the sponsors' list HTML directly.
 */
function display_sponsors_list() {
    // Query parameters for fetching sponsors
    $sponsors_query_args = array(
        'post_type'      => 'sponsors',       // Custom post type: 'sponsors'
        'post_status'    => 'publish',       // Only published posts
        'posts_per_page' => -1,              // Retrieve all sponsors
        'orderby'        => 'title',         // Sort by title
        'order'          => 'ASC'            // Ascending order
    );

    // Execute the query
    $sponsors_query = new WP_Query($sponsors_query_args);

    // Check if there are any sponsors
    if ($sponsors_query->have_posts()) {
        echo '<div class="sponsors-list">'; // Wrapper for sponsors list
        echo '<h2>Our Sponsors</h2>';      // Section title
        
        // Loop through each sponsor post
        while ($sponsors_query->have_posts()) {
            $sponsors_query->the_post();    // Setup post data

            // Retrieve sponsor details
            $sponsor_name = get_the_title(); // Sponsor name
            $sponsor_logo = get_the_post_thumbnail_url(get_the_ID(), 'medium'); // Sponsor logo
            $sponsor_url  = get_post_meta(get_the_ID(), 'sponsor_url', true); // Custom field: URL

            echo '<div class="sponsor-item">'; // Individual sponsor wrapper
            
            // Display sponsor logo (if available)
            if ($sponsor_logo) {
                echo '<div class="sponsor-logo">';
                echo $sponsor_url ? 
                    '<a href="' . esc_url($sponsor_url) . '" target="_blank" rel="noopener noreferrer">' :
                    '';
                echo '<img src="' . esc_url($sponsor_logo) . '" alt="' . esc_attr($sponsor_name) . '">';
                echo $sponsor_url ? '</a>' : '';
                echo '</div>'; // End sponsor logo
            }

            // Display sponsor name
            echo '<div class="sponsor-name">';
            echo $sponsor_url ? 
                '<a href="' . esc_url($sponsor_url) . '" target="_blank" rel="noopener noreferrer">' :
                '';
            echo esc_html($sponsor_name);
            echo $sponsor_url ? '</a>' : '';
            echo '</div>'; // End sponsor name
            
            echo '</div>'; // End sponsor item
        }

        echo '</div>'; // End sponsors list wrapper
    } else {
        // No sponsors found
        echo '<p>No sponsors available at the moment.</p>';
    }

    // Reset post data
    wp_reset_postdata();
}

// To use this function, call it within a WordPress template file or via a shortcode if needed.
?>
```
