"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apktin.xyz
Prompt: Write a function in PHP to fetch and display comments for the latest posts on a WordPress site.
Generated: DETERMINISTIC_0978e9c730ee21ed
Batch ID: 20250612_160657
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
 * Fetch and display comments for the latest posts on a WordPress site.
 *
 * This function retrieves the latest posts and their comments,
 * and formats them for display.
 *
 * @param int $post_count The number of latest posts to fetch. Default is 5.
 * @return void
 */
function fetch_and_display_latest_comments($post_count = 5) {
    // Check if the argument is a valid integer
    if (!is_int($post_count) || $post_count <= 0) {
        throw new InvalidArgumentException('Post count must be a positive integer.');
    }

    // Fetch the latest posts
    $latest_posts = get_posts(array(
        'numberposts' => $post_count,
        'post_status' => 'publish'
    ));

    // Check if posts were retrieved
    if (empty($latest_posts)) {
        echo '<p>No posts found.</p>';
        return;
    }

    // Loop through each post and display its comments
    foreach ($latest_posts as $post) {
        setup_postdata($post); // Setup post data for the current post

        // Display the post title
        echo '<h2>' . esc_html(get_the_title($post)) . '</h2>';

        // Fetch comments for the current post
        $comments = get_comments(array(
            'post_id' => $post->ID,
            'status' => 'approve' // Only approved comments
        ));

        // Check if comments exist
        if (empty($comments)) {
            echo '<p>No comments yet.</p>';
        } else {
            echo '<ul>';
            // Loop through each comment
            foreach ($comments as $comment) {
                echo '<li>' . esc_html($comment->comment_content) . ' - <strong>' . esc_html($comment->comment_author) . '</strong></li>';
            }
            echo '</ul>';
        }
    }

    // Reset post data after the loop
    wp_reset_postdata();
}

// Example usage:
try {
    fetch_and_display_latest_comments(5); // Adjust the number of posts to fetch as needed
} catch (InvalidArgumentException $e) {
    echo '<p>Error: ' . esc_html($e->getMessage()) . '</p>';
}
?>
```
