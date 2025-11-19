"""
Generated Code Metadata:
========================
Original URL: https://alakhttiar.com.sa
Prompt: Write a function using PHP to fetch and display recent posts related to "مظلات" and "سواتر" on a WordPress blog.
Generated: DETERMINISTIC_3dcf820cba8064fe
Batch ID: 20250612_162051
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
 * Fetch and display recent posts related to "مظلات" and "سواتر" on a WordPress blog.
 */

// Check if WordPress is defined
if (!defined('WP_CONTENT_DIR')) {
    exit;
}

// Define the function to fetch recent posts
function fetch_recent_posts($keyword1, $keyword2, $post_type = 'post', $posts_per_page = 5) {
    // Validate input parameters
    if (!is_string($keyword1) || !is_string($keyword2)) {
        throw new Exception('Keywords must be strings');
    }

    if (!is_string($post_type)) {
        throw new Exception('Post type must be a string');
    }

    if (!is_int($posts_per_page) || $posts_per_page <= 0) {
        throw new Exception('Posts per page must be a positive integer');
    }

    // Prepare query arguments
    $args = array(
        'post_type' => $post_type,
        'posts_per_page' => $posts_per_page,
        'orderby' => 'date',
        'order' => 'DESC',
        'tax_query' => array(
            array(
                'taxonomy' => 'category',
                'field'    => 'slug',
                'terms'    => array($keyword1, $keyword2),
                'operator' => 'OR'
            )
        )
    );

    // Perform the query
    $query = new WP_Query($args);

    // Check for errors
    if ($query->is_wp_error()) {
        throw new Exception($query->get_error_message());
    }

    // Display recent posts
    if ($query->have_posts()) {
        echo '<h2>Recent Posts</h2>';
        echo '<ul>';
        while ($query->have_posts()) {
            $query->the_post();
            echo '<li>';
            echo '<a href="' . get_permalink() . '">' . get_the_title() . '</a>';
            echo '<p>' . get_the_excerpt() . '</p>';
            echo '</li>';
        }
        echo '</ul>';
        wp_reset_postdata();
    } else {
        echo 'No posts found';
    }
}

// Example usage
add_action('wp_head', function () {
    try {
        fetch_recent_posts('مظلات', 'سواتر');
    } catch (Exception $e) {
        echo 'Error: ' . $e->getMessage();
    }
});

?>
```
