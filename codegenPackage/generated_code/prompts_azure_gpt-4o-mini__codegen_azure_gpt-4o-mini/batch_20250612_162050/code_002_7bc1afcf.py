"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: Write a PHP function that modifies the WordPress posts query to filter out titles containing 'GarageBand' and 'Photoshop', inspired by the code found on the Residencial Vila da Graça webpage.
Generated: DETERMINISTIC_7bc1afcfcb864a6d
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
 * Filters the WordPress posts query to exclude titles containing specific keywords.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function filter_posts_by_title_keywords( $query ) {
    // Check if we are in the main query and on the front end
    if ( ! is_admin() && $query->is_main_query() ) {
        // Define the keywords to filter out
        $keywords = array( 'GarageBand', 'Photoshop' );

        // Prepare the meta query to exclude posts with the specified keywords in the title
        $title_exclusions = array();
        foreach ( $keywords as $keyword ) {
            $title_exclusions[] = sprintf( "NOT LIKE '%%%s%%'", esc_sql( $keyword ) );
        }

        // Combine the exclusions into a single SQL condition
        $query->set( 's', '' ); // Clear any existing search query
        $query->set( 'meta_query', array(
            'relation' => 'AND',
            array(
                'key'     => 'post_title',
                'value'   => implode( ' ', $title_exclusions ),
                'compare' => 'NOT LIKE'
            )
        ));
    }
}

// Hook the function to the pre_get_posts action
add_action( 'pre_get_posts', 'filter_posts_by_title_keywords' );
?>
```
