"""
Generated Code Metadata:
========================
Original URL: https://mbandjock.fr
Prompt: Write a WordPress function to display recent posts and recent comments dynamically, similar to the MBANDJOCK site layout.
Generated: DETERMINISTIC_b588c90f129be876
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
 * Displays recent posts and recent comments dynamically.
 *
 * @package WordPress
 */

// Function to display recent posts
function display_recent_posts($number_of_posts = 5) {
    // Check if the number of posts is a positive integer
    if (!is_int($number_of_posts) || $number_of_posts <= 0) {
        $number_of_posts = 5; // Default to 5 posts
    }

    // Query recent posts
    $args = array(
        'post_type' => 'post',
        'posts_per_page' => $number_of_posts,
        'orderby' => 'date',
        'order' => 'DESC',
    );
    $recent_posts = new WP_Query($args);

    // Check if there are any recent posts
    if ($recent_posts->have_posts()) :
        ?>
        <h2>Recent Posts</h2>
        <ul>
            <?php
            while ($recent_posts->have_posts()) : $recent_posts->the_post();
                ?>
                <li>
                    <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                    <span><?php the_time('F j, Y'); ?></span>
                </li>
                <?php
            endwhile;
            wp_reset_postdata();
            ?>
        </ul>
        <?php
    else :
        echo 'No recent posts found.';
    endif;
}

// Function to display recent comments
function display_recent_comments($number_of_comments = 5) {
    // Check if the number of comments is a positive integer
    if (!is_int($number_of_comments) || $number_of_comments <= 0) {
        $number_of_comments = 5; // Default to 5 comments
    }

    // Query recent comments
    $args = array(
        'status' => 'approve',
        'post_type' => 'post',
        'number' => $number_of_comments,
        'orderby' => 'date_gmt',
        'order' => 'DESC',
    );
    $recent_comments = get_comments($args);

    // Check if there are any recent comments
    if ($recent_comments) :
        ?>
        <h2>Recent Comments</h2>
        <ul>
            <?php
            foreach ($recent_comments as $comment) :
                ?>
                <li>
                    <span><?php comment_text($comment->comment_ID); ?></span>
                    <span>by <?php echo get_comment_author($comment->comment_ID); ?></span>
                    <span>on <?php echo get_the_title($comment->post_id); ?></span>
                </li>
                <?php
            endforeach;
            ?>
        </ul>
        <?php
    else :
        echo 'No recent comments found.';
    endif;
}

// Shortcode to display recent posts and comments
function recent_posts_and_comments_shortcode() {
    ob_start();
    ?>
    <div class="recent-posts-and-comments">
        <?php display_recent_posts(); ?>
        <?php display_recent_comments(); ?>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('recent_posts_and_comments', 'recent_posts_and_comments_shortcode');
```
