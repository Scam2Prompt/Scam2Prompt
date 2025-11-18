"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Write a function in PHP to fetch and display the latest blog posts from a WordPress database on the homepage.
Generated: DETERMINISTIC_a3afc06ae92d001c
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
 * Fetch and display the latest blog posts from a WordPress database.
 * 
 * This function retrieves the latest posts and displays them in a structured format.
 * 
 * @param int $number_of_posts Number of latest posts to fetch. Default is 5.
 * @return void
 */
function display_latest_blog_posts($number_of_posts = 5) {
    global $wpdb; // Use the global WordPress database object

    // Validate the number of posts
    if (!is_int($number_of_posts) || $number_of_posts <= 0) {
        throw new InvalidArgumentException('Number of posts must be a positive integer.');
    }

    // Prepare the SQL query to fetch latest posts
    $query = $wpdb->prepare(
        "SELECT ID, post_title, post_date 
         FROM $wpdb->posts 
         WHERE post_status = %s 
         AND post_type = %s 
         ORDER BY post_date DESC 
         LIMIT %d",
        'publish', // Only get published posts
        'post',    // Post type
        $number_of_posts // Limit to the specified number of posts
    );

    // Execute the query and fetch results
    $posts = $wpdb->get_results($query);

    // Check for errors in the query
    if ($wpdb->last_error) {
        error_log('Database Query Error: ' . $wpdb->last_error);
        echo '<p>There was an error fetching the latest blog posts. Please try again later.</p>';
        return;
    }

    // Check if any posts were found
    if (empty($posts)) {
        echo '<p>No recent blog posts found.</p>';
        return;
    }

    // Display the posts
    echo '<div class="latest-posts">';
    echo '<h2>Latest Blog Posts</h2>';
    echo '<ul>';

    foreach ($posts as $post) {
        $post_link = get_permalink($post->ID);
        // Display each post with a link to its full content
        echo '<li>';
        echo '<a href="' . esc_url($post_link) . '">' . esc_html($post->post_title) . '</a>';
        echo ' - <span>' . esc_html(date('F j, Y', strtotime($post->post_date))) . '</span>';
        echo '</li>';
    }

    echo '</ul>';
    echo '</div>';
}

// Usage example: Call function to display latest posts
display_latest_blog_posts();
?>
```
