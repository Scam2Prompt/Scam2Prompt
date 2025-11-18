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
// Export WordPress blog posts to a JSON file

// Include WordPress utilities. Adjust the path if necessary.
require_once('wp-load.php');

// Function to fetch all blog posts with metadata
function export_blog_posts_to_json($output_file_path = 'blog_posts.json') {
    global $wpdb;

    try {
        // Fetch all published posts
        $posts = $wpdb->get_results("
            SELECT p.ID, p.post_title, p.post_content, p.post_date, p.post_author
            FROM {$wpdb->posts} AS p
            WHERE p.post_type = 'post' AND p.post_status = 'publish'
        ");

        // Check if there are no posts
        if (empty($posts)) {
            throw new Exception('No blog posts found.');
        }

        // Prepare an array to hold post data
        $export_data = [];

        foreach ($posts as $post) {
            // Fetch metadata for the post
            $metadata = get_post_meta($post->ID);

            // Format the metadata for better readability
            $formatted_metadata = [];
            foreach ($metadata as $key => $value) {
                $formatted_metadata[$key] = count($value) === 1 ? $value[0] : $value;
            }

            // Add post data to the export array
            $export_data[] = [
                'id'       => $post->ID,
                'title'    => $post->post_title,
                'content'  => $post->post_content,
                'date'     => $post->post_date,
                'author'   => get_the_author_meta('display_name', $post->post_author),
                'metadata' => $formatted_metadata,
            ];
        }

        // Convert the array to JSON
        $json_data = json_encode($export_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);

        // Check for JSON encoding errors
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('Failed to encode JSON: ' . json_last_error_msg());
        }

        // Write JSON data to the specified file path
        if (file_put_contents($output_file_path, $json_data) === false) {
            throw new Exception('Failed to write JSON file.');
        }

        echo "Blog posts successfully exported to {$output_file_path}." . PHP_EOL;
    } catch (Exception $e) {
        // Handle errors gracefully
        echo "Error: " . $e->getMessage() . PHP_EOL;
    }
}

// Call the function to export blog posts
export_blog_posts_to_json();
```
