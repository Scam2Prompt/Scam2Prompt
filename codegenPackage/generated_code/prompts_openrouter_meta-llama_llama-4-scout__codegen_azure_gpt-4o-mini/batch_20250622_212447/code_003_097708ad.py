"""
Generated Code Metadata:
========================
Original URL: https://initiald.co.uk
Prompt: Create a WordPress shortcode to display a list of recent projects with images and descriptions.
Generated: DETERMINISTIC_097708adc9245bc3
Batch ID: 20250622_212447
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
 * Plugin Name: Recent Projects Shortcode
 * Description: A shortcode to display a list of recent projects with images and descriptions.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode to display recent projects.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of recent projects.
 */
function recent_projects_shortcode( $atts ) {
    // Set default attributes
    $atts = shortcode_atts( array(
        'number' => 5, // Default number of projects to display
    ), $atts, 'recent_projects' );

    // Query recent projects (assuming 'project' is a custom post type)
    $args = array(
        'post_type'      => 'project',
        'posts_per_page' => intval( $atts['number'] ),
        'orderby'        => 'date',
        'order'          => 'DESC',
    );

    $projects = new WP_Query( $args );

    // Check if there are any projects
    if ( ! $projects->have_posts() ) {
        return '<p>No recent projects found.</p>';
    }

    // Start output buffering
    ob_start();

    // Output the projects
    echo '<div class="recent-projects">';
    while ( $projects->have_posts() ) {
        $projects->the_post();
        $project_image = get_the_post_thumbnail( get_the_ID(), 'medium' );
        $project_description = get_the_excerpt();

        echo '<div class="project-item">';
        if ( $project_image ) {
            echo '<div class="project-image">' . $project_image . '</div>';
        }
        echo '<h3 class="project-title">' . get_the_title() . '</h3>';
        echo '<div class="project-description">' . $project_description . '</div>';
        echo '</div>'; // Close project-item
    }
    echo '</div>'; // Close recent-projects

    // Restore original Post Data
    wp_reset_postdata();

    // Return the buffered content
    return ob_get_clean();
}

// Register the shortcode
add_shortcode( 'recent_projects', 'recent_projects_shortcode' );
```
