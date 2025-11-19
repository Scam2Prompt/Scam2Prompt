"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alakhttiar.com.sa
Prompt: Write a function using PHP to fetch and display recent posts related to "مظلات" and "سواتر" on a WordPress blog.
Generated: DETERMINISTIC_3dcf820cba8064fe
Batch ID: 20250612_162051
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
 * Fetch and display recent posts related to specific keywords on a WordPress blog.
 *
 * @param string $keyword1 First keyword to filter posts.
 * @param string $keyword2 Second keyword to filter posts.
 * @param int $number_of_posts Number of posts to display. Default is 5.
 */
function display_recent_posts($keyword1 = 'مظلات', $keyword2 = 'سواتر', $number_of_posts = 5) {
    // Check if the WordPress environment is loaded
    if (!function_exists('get_posts')) {
        error_log('WordPress environment not loaded.');
        return;
    }

    // Set up arguments for the query
    $args = array(
        's' => $keyword1 . ' ' . $keyword2, // Search for both keywords
        'posts_per_page' => $number_of_posts, // Limit the number of posts returned
        'post_status' => 'publish', // Only fetch published posts
        'orderby' => 'date', // Sort by date
        'order' => 'DESC' // Most recent first
    );

    // Fetch posts
    $recent_posts = get_posts($args);

    // Check if posts were found
    if (empty($recent_posts)) {
        echo '<p>No recent posts found related to "' . esc_html($keyword1) . '" and "' . esc_html($keyword2) . '".</p>';
        return;
    }

    // Display the posts
    echo '<div class="recent-posts">';
    echo '<h2>Recent Posts Related to "' . esc_html($keyword1) . '" and "' . esc_html($keyword2) . '"</h2>';
    echo '<ul>';
    
    foreach ($recent_posts as $post) {
        setup_postdata($post); // Set up post data for template tags
        ?>
        <li>
            <a href="<?php echo esc_url(get_permalink($post->ID)); ?>">
                <?php echo esc_html(get_the_title($post->ID)); ?>
            </a>
            <span class="post-date"><?php echo esc_html(get_the_date('', $post->ID)); ?></span>
        </li>
        <?php
    }

    echo '</ul>';
    echo '</div>';

    // Reset post data
    wp_reset_postdata();
}
```
