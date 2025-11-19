"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: Write a PHP function that modifies the WordPress posts query to filter out titles containing 'GarageBand' and 'Photoshop', inspired by the code found on the Residencial Vila da Graça webpage.
Generated: DETERMINISTIC_7bc1afcfcb864a6d
Batch ID: 20250612_162050
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
 * Modify the WordPress posts query to filter out titles containing 'GarageBand' and 'Photoshop'.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function filter_posts_by_title( $query ) {
    // Check if we are in the main query and on the front end
    if ( ! is_admin() && $query->is_main_query() ) {
        // Set up the exclusion keywords
        $excluded_keywords = array( 'GarageBand', 'Photoshop' );

        // Build the meta query to exclude titles containing the keywords
        $query->set( 's', implode( ' ', $excluded_keywords ) ); // Set the search parameter

        // Customize the posts search SQL
        add_filter( 'posts_search', function( $search, $wp_query ) {
            global $wpdb;

            // Only apply the filter if the current query is the main query
            if ( ! $wp_query->is_main_query() ) {
                return $search;
            }

            // Modify the search query to exclude titles with specified keywords
            $terms = implode( "' AND post_title NOT LIKE '%", $excluded_keywords );
            $search .= " AND ({$wpdb->posts}.post_title NOT LIKE '%{$terms}%')";

            return $search;
        }, 10, 2 );
    }
}

// Hook the function into the pre_get_posts action
add_action( 'pre_get_posts', 'filter_posts_by_title' );
?>
```
