"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: How can I implement a custom query in WordPress to exclude certain keywords from post titles, as demonstrated on the Residencial Vila da Graça site?
Generated: DETERMINISTIC_0882e36883029cfc
Batch ID: 20250612_162050
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
 * Custom WordPress Query to Exclude Posts with Certain Keywords in Titles
 *
 * This function modifies the main query to exclude posts that contain specific keywords
 * in their titles. It should be hooked into the 'pre_get_posts' action.
 *
 * @param WP_Query $query The WP_Query instance (passed by reference).
 */
function exclude_keywords_from_titles( $query ) {
    // Check if we are in the main query and on the front end
    if ( ! is_admin() && $query->is_main_query() ) {
        // Define the keywords to exclude
        $excluded_keywords = array( 'keyword1', 'keyword2', 'keyword3' );

        // Prepare the meta query to exclude posts with the specified keywords
        $meta_query = array(
            'relation' => 'OR',
        );

        // Loop through each keyword and create a NOT LIKE condition
        foreach ( $excluded_keywords as $keyword ) {
            $meta_query[] = array(
                'key'     => 'post_title',
                'value'   => $keyword,
                'compare' => 'NOT LIKE',
            );
        }

        // Set the meta query to the main query
        $query->set( 'meta_query', $meta_query );
    }
}

// Hook the function into the 'pre_get_posts' action
add_action( 'pre_get_posts', 'exclude_keywords_from_titles' );
```

Make sure to replace `'keyword1'`, `'keyword2'`, and `'keyword3'` with the actual keywords you want to exclude from the post titles. This code should be added to your theme's `functions.php` file or a custom plugin.
