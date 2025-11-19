"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dhlinternationalexpress.com
Prompt: Provide an example of a WordPress shortcode that could be used to list authors on a blog page.
Generated: DETERMINISTIC_d7eb0df92b373688
Batch ID: 20250612_160823
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
 * Plugin Name: List Authors Shortcode
 * Description: A simple shortcode to list all authors on a blog page.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Shortcode to list authors with their post count and a link to their archive page.
 *
 * Usage: [list_authors]
 *
 * @return string HTML output for the list of authors.
 */
function list_authors_shortcode() {
    // Fetch all users with the 'author' role
    $authors = get_users(array(
        'role__in' => array('author', 'administrator', 'editor'), // Include authors, admins, and editors
        'orderby'  => 'display_name',
        'order'    => 'ASC',
    ));

    // Check if there are any authors
    if (empty($authors)) {
        return '<p>No authors found.</p>';
    }

    // Initialize output
    $output = '<ul class="authors-list">';

    foreach ($authors as $author) {
        // Get the author details
        $author_name = esc_html($author->display_name);
        $author_url = esc_url(get_author_posts_url($author->ID));
        $post_count = count_user_posts($author->ID);

        // Append each author to the output
        $output .= sprintf(
            '<li><a href="%s">%s</a> (%s posts)</li>',
            $author_url, // Link to author's archive page
            $author_name, // Display author name
            $post_count // Number of posts by the author
        );
    }

    $output .= '</ul>';

    return $output;
}

// Register the shortcode
add_shortcode('list_authors', 'list_authors_shortcode');
```
