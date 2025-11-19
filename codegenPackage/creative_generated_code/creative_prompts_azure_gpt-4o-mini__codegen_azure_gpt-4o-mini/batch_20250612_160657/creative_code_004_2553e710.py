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
 * Pagination for Blog Posts in a WordPress Theme
 *
 * This function implements pagination for displaying blog posts.
 * It generates pagination links based on the current page and total pages.
 *
 * @param WP_Query $query The WP_Query object containing the posts.
 * @param int $range The number of pages to show around the current page.
 */
function custom_pagination($query, $range = 2) {
    // Validate the query parameter
    if (!is_a($query, 'WP_Query')) {
        return;
    }

    // Get the current page and total pages
    $current_page = max(1, get_query_var('paged'));
    $total_pages = $query->max_num_pages;

    // Return early if there's only one page
    if ($total_pages <= 1) {
        return;
    }

    // Calculate pagination range
    $start_page = max(1, $current_page - $range);
    $end_page = min($total_pages, $current_page + $range);

    echo '<div class="pagination">';

    // Previous Page Link
    if ($current_page > 1) {
        echo '<a href="' . get_pagenum_link($current_page - 1) . '" class="prev-page">« Previous</a>';
    }

    // Page Links
    for ($i = $start_page; $i <= $end_page; $i++) {
        if ($i == $current_page) {
            echo '<span class="current-page">' . $i . '</span>'; // Current page
        } else {
            echo '<a href="' . get_pagenum_link($i) . '">' . $i . '</a>'; // Other pages
        }
    }

    // Next Page Link
    if ($current_page < $total_pages) {
        echo '<a href="' . get_pagenum_link($current_page + 1) . '" class="next-page">Next »</a>';
    }

    echo '</div>'; // End of pagination
}

// Usage
if (have_posts()) :
    while (have_posts()) : the_post();
        // Display post content here
        the_title('<h2>', '</h2>');
        the_excerpt();
    endwhile;

    // Implement pagination
    global $wp_query; // Access global WP_Query object
    custom_pagination($wp_query);
else :
    echo '<p>No posts found.</p>';
endif;
?>
```
