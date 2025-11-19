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
 * Modifies the WordPress query to exclude posts with titles containing 'GarageBand' or 'Photoshop'.
 *
 * @param WP_Query $query The WordPress query object.
 */
function exclude_specific_titles_from_query( $query ) {
    // Ensure this only affects the main query in the frontend
    if ( is_admin() || ! $query->is_main_query() ) {
        return;
    }

    // Get the current meta query (if any)
    $meta_query = (array) $query->get( 'meta_query' );

    // Add our exclusion conditions
    $meta_query[] = array(
        'relation' => 'AND',
        array(
            'key'     => '_title',
            'value'   => 'GarageBand',
            'compare' => 'NOT LIKE',
        ),
        array(
            'key'     => '_title',
            'value'   => 'Photoshop',
            'compare' => 'NOT LIKE',
        ),
    );

    // Set the modified meta query
    $query->set( 'meta_query', $meta_query );
}
add_action( 'pre_get_posts', 'exclude_specific_titles_from_query' );
```
