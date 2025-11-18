"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Write a PHP script to export all blog posts, including metadata, from a WordPress site to a JSON file.
Generated: DETERMINISTIC_94d4366891280301
Batch ID: 20250612_155115
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
 * Export all blog posts from a WordPress site to a JSON file.
 *
 * This script fetches all posts and their associated metadata,
 * and exports this data into a JSON file.
 */

// Ensure WordPress environment is loaded
require_once('wp-load.php');

// Set the filename for the JSON export
$export_filename = 'blog_posts_export.json';

// Initialize an array to hold the posts data
$posts_data = [];

// Query for all published blog posts
$args = [
    'post_type'      => 'post',
    'post_status'    => 'publish',
    'posts_per_page' => -1, // Retrieve all posts
];

$posts_query = new WP_Query($args);

// Check if posts are found
if ($posts_query->have_posts()) {
    while ($posts_query->have_posts()) {
        $posts_query->the_post(); // Set up post data

        // Collect post data and metadata
        $post_data = [
            'id'          => get_the_ID(),
            'title'       => get_the_title(),
            'content'     => get_the_content(),
            'excerpt'     => get_the_excerpt(),
            'date'        => get_the_date(),
            'author'      => get_the_author(),
            'metadata'    => [
                'categories' => get_the_category(),
                'tags'       => get_the_tags(),
                'custom_fields' => get_post_meta(get_the_ID()),
            ],
        ];

        // Add the post data to the posts array
        $posts_data[] = $post_data;
    }

    // Restore original Post Data
    wp_reset_postdata();

    // Encode the posts data into JSON format
    $json_data = json_encode($posts_data, JSON_PRETTY_PRINT);

    // Error handling for JSON encoding
    if ($json_data === false) {
        error_log('JSON encoding error: ' . json_last_error_msg());
        die('Error encoding data to JSON format.');
    }

    // Write the JSON data to a file
    if (file_put_contents($export_filename, $json_data) === false) {
        error_log('File write error: Unable to write to ' . $export_filename);
        die('Error writing to JSON file.');
    }

    echo 'Blog posts exported successfully to ' . $export_filename;
} else {
    echo 'No published posts found to export.';
}
?>
```
