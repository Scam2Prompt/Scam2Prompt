"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Generate a WordPress filter function similar to the one used on residencialviladagraca.com.br to exclude posts containing specific keywords in their titles."
Generated: DETERMINISTIC_dfd8e3a32c815ce6
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Filter function to exclude posts containing specific keywords in their titles.
 *
 * @param array $query The query array.
 * @return array The modified query array.
 */
function exclude_posts_by_title_keywords( $query ) {
    // Define the keywords to exclude
    $excluded_keywords = array( 'keyword1', 'keyword2', 'keyword3' ); // Replace with your keywords

    // Check if we're in the admin area or not
    if ( ! is_admin() && $query->is_main_query() ) {
        // Initialize an array to store the excluded post IDs
        $excluded_post_ids = array();

        // Query to get posts containing excluded keywords in their titles
        $excluded_posts = get_posts(
            array(
                'post_type' => 'post',
                'posts_per_page' => -1,
                'meta_query' => array(
                    array(
                        'key' => 'title',
                        'value' => $excluded_keywords,
                        'compare' => 'LIKE',
                    ),
                ),
            )
        );

        // Get the IDs of excluded posts
        foreach ( $excluded_posts as $post ) {
            $excluded_post_ids[] = $post->ID;
        }

        // Modify the query to exclude posts
        if ( ! empty( $excluded_post_ids ) ) {
            $query->set( 'post__not_in', $excluded_post_ids );
        }
    }

    return $query;
}

// Add the filter function to the 'pre_get_posts' action
add_filter( 'pre_get_posts', 'exclude_posts_by_title_keywords' );
```

```php
// Alternatively, you can use a more efficient approach using SQL
function exclude_posts_by_title_keywords_sql( $query ) {
    // Define the keywords to exclude
    $excluded_keywords = array( 'keyword1', 'keyword2', 'keyword3' ); // Replace with your keywords

    // Check if we're in the admin area or not
    if ( ! is_admin() && $query->is_main_query() ) {
        // Modify the query to exclude posts
        $excluded_keywords_string = implode( "','", $excluded_keywords );
        $query->set( 'meta_query', array(
            array(
                'key' => '_wp_post_title',
                'value' => $excluded_keywords_string,
                'compare' => 'NOT LIKE',
            ),
        ) );
    }

    return $query;
}

// Add the filter function to the 'pre_get_posts' action
// add_filter( 'pre_get_posts', 'exclude_posts_by_title_keywords_sql' );
```
