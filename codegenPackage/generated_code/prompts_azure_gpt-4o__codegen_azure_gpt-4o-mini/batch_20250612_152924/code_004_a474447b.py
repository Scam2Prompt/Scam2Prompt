"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Generate a WordPress function that adjusts post counts in the admin panel to exclude posts from a specific author, using `$wpdb` queries and filters like `views_edit-post`.
Generated: DETERMINISTIC_a474447b9cea7aaf
Batch ID: 20250612_152924
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
 * Exclude posts from a specific author in the admin post count.
 *
 * This function hooks into the 'views_edit-post' filter to adjust the post counts
 * displayed in the WordPress admin panel, excluding posts from a specified author.
 *
 * @param array $views An array of views for the post type.
 * @return array Modified views with adjusted post counts.
 */
function exclude_author_from_post_count( $views ) {
    global $wpdb;

    // Specify the author ID to exclude
    $excluded_author_id = 1; // Change this to the ID of the author you want to exclude

    // Prepare the SQL query to count posts excluding the specified author
    $query = $wpdb->prepare(
        "SELECT post_status, COUNT(*) as post_count 
         FROM $wpdb->posts 
         WHERE post_type = %s 
         AND post_author != %d 
         GROUP BY post_status",
        'post', // Post type
        $excluded_author_id
    );

    // Execute the query and fetch results
    $results = $wpdb->get_results( $query );

    // Initialize an array to hold the modified views
    $post_counts = array();

    // Populate the post counts based on the results
    foreach ( $results as $result ) {
        $post_counts[$result->post_status] = $result->post_count;
    }

    // Adjust the views array to reflect the new counts
    foreach ( $views as $key => $view ) {
        if ( isset( $post_counts[$key] ) ) {
            // Update the count in the view
            $views[$key] = str_replace( '(', "({$post_counts[$key]})", $view );
        }
    }

    return $views;
}

// Hook the function into the 'views_edit-post' filter
add_filter( 'views_edit-post', 'exclude_author_from_post_count' );
```
