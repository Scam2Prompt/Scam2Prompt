"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: How can I implement a custom query in WordPress to exclude certain keywords from post titles, as demonstrated on the Residencial Vila da Graça site?
Generated: DETERMINISTIC_0882e36883029cfc
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
 * Custom query to exclude certain keywords from post titles in WordPress.
 *
 * @param WP_Query $query The original WP_Query instance.
 */
function exclude_keywords_from_titles( $query ) {
    // Ensure we're modifying the main query on the front-end
    if ( ! is_admin() && $query->is_main_query() ) {
        // Define the keywords to exclude from titles
        $excluded_keywords = array( 'keyword1', 'keyword2', 'keyword3' ); // Replace with your actual keywords

        // Prepare an array to hold the LIKE clauses
        $like_clauses = array();

        // Build the LIKE clauses for each excluded keyword
        foreach ( $excluded_keywords as $keyword ) {
            $like_clauses[] = $query->get_sql_like_clause('post_title', '%' . $keyword . '%'); // Escape the keyword for SQL
        }

        // Join the LIKE clauses with OR
        if ( ! empty( $like_clauses ) ) {
            // Modify the query to exclude posts with the specified keywords in the title
            $query->set( 's', '' ); // Clear the search query for proper filtering
            $query->set( 'meta_query', array(
                'relation' => 'OR',
                'exclude_keywords' => array(
                    'key'     => 'post_title',
                    'value'   => implode( ' ', $like_clauses ),
                    'compare' => 'NOT LIKE',
                ),
            ) );
        }
    }
}

// Hook into the pre_get_posts action to modify the query
add_action( 'pre_get_posts', 'exclude_keywords_from_titles' );
?>
```
