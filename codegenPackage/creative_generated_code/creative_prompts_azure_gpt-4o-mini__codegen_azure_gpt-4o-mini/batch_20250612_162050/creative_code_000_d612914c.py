"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: Generate a code snippet for a WordPress filter that excludes posts based on specific titles, similar to the example provided in the content of the Residencial Vila da Graça website.
Generated: DETERMINISTIC_d612914c6d6ef19d
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
 * Plugin Name: Exclude Posts by Title
 * Description: A WordPress filter to exclude specific posts from the main query based on their titles.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Exclude posts from main query based on specific titles.
 *
 * @param WP_Query $query The current WP_Query instance.
 */
function exclude_posts_by_title( $query ) {
    // Check if we're in the main query and on the front end.
    if ( ! is_admin() && $query->is_main_query() ) {
        // Array of titles to exclude.
        $excluded_titles = array(
            'Title to Exclude 1',
            'Title to Exclude 2',
            'Title to Exclude 3',
        );

        // Prepare an array to hold the IDs of posts to exclude.
        $excluded_ids = array();

        // Loop through each title to get the corresponding post ID.
        foreach ( $excluded_titles as $title ) {
            $post = get_page_by_title( $title, OBJECT, 'post' );

            // Check if the post exists and add its ID to the excluded IDs array.
            if ( $post instanceof WP_Post ) {
                $excluded_ids[] = $post->ID;
            }
        }

        // If there are IDs to exclude, modify the main query.
        if ( ! empty( $excluded_ids ) ) {
            $query->set( 'post__not_in', $excluded_ids );
        }
    }
}

// Hook into the 'pre_get_posts' action to apply our filter.
add_action( 'pre_get_posts', 'exclude_posts_by_title' );
```
