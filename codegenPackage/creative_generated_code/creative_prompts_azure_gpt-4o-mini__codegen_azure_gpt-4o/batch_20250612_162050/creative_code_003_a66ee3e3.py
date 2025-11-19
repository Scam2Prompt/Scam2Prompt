"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://residencialviladagraca.com.br
Prompt: Provide an example of a WordPress filter that adds conditions to exclude posts with specific keywords in their titles, based on the approach used by Residencial Vila da Graça.
Generated: DETERMINISTIC_a66ee3e35bf15825
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
 * Plugin Name: Exclude Posts by Keywords in Title
 * Description: Filters posts to exclude those with specific keywords in their titles.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Filters posts to exclude those with specific keywords in their titles.
 *
 * @param WP_Query $query The WP_Query instance (passed by reference).
 */
function exclude_posts_by_keywords_in_title($query) {
    // Ensure this filtering applies only to the main query on the front end.
    if ($query->is_main_query() && !is_admin()) {
        // Define an array of keywords to exclude.
        $keywords_to_exclude = ['keyword1', 'keyword2', 'keyword3'];

        // Build a meta query to exclude posts containing the keywords in their titles.
        $meta_query = array(
            'relation' => 'OR', // Match any of the keywords.
        );

        foreach ($keywords_to_exclude as $keyword) {
            $meta_query[] = array(
                'key'     => '_title',
                'value'   => $keyword
			 )

    }
}
// Add it
