"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apktin.xyz
Prompt: Provide an example of how to implement pagination for blog posts in a WordPress theme using PHP.
Generated: DETERMINISTIC_2553e71002e0c979
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
 * Pagination function for WordPress blog posts.
 *
 * This function generates pagination links for a WordPress theme.
 * It uses built-in WordPress functions to create user-friendly links.
 *
 * @param WP_Query|null $query Custom query object, defaults to the main query.
 */
function custom_pagination($query = null) {
    // Use the main query if no custom query is passed.
    if (!$query) {
        global $wp_query;
        $query = $wp_query;
    }

    // Ensure there are posts to paginate.
    if ($query->max_num_pages <= 1) {
        return;
    }

    // Get the current page.
    $current_page = max(1, get_query_var('paged'));

    // Generate pagination links.
    $pagination_links = paginate_links(array(
        'base'      => str_replace(999999999, '%#%', esc_url(get_pagenum_link(999999999))),
        'format'    => '?paged=%#%',
        'current'   => $current_page,
        'total'     => $query->max_num_pages,
        'prev_text' => __('« Previous', 'textdomain'),
        'next_text' => __('Next »', 'textdomain'),
        'type'      => 'list',
    ));

    // Output the pagination links.
    if (!empty($pagination_links)) {
        echo '<nav class="pagination">';
        echo $pagination_links;
        echo '</nav>';
    }
}
?>

<!-- Example usage in a WordPress theme file like index.php or page.php -->
<?php
// Main loop for displaying posts.
if (have_posts()) :
    while (have_posts()) : the_post();
        // Display the post content or excerpt here.
        the_title('<h2>', '</h2>');
        the_excerpt();
    endwhile;

    // Call the custom pagination function.
    custom_pagination();
else :
    echo '<p>No posts found.</p>';
endif;
?>
```
