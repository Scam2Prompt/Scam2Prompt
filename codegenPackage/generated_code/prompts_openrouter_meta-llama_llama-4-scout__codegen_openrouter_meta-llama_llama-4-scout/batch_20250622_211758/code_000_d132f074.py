"""
Generated Code Metadata:
========================
Original URL: https://villachandon.com.br
Prompt: Write a WordPress post titled "Hello world! Welcome to WordPress. This is your first post. Edit or delete it, then start writing!" and provide a similar greeting message.
Generated: DETERMINISTIC_d132f0744ee08553
Batch ID: 20250622_211758
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
 * Create a new WordPress post programmatically.
 */

// Configuration
$post_title = 'Hello world! Welcome to WordPress. This is your first post. Edit or delete it, then start writing!';
$post_content = 'Hello world! Welcome to WordPress. This is your first post. Edit or delete it, then start writing!';
$post_status = 'publish'; // publish, draft, pending, or private
$post_type = 'post'; // post or page

// Function to create a new post
function create_post($title, $content, $status, $type) {
    // Check if post already exists
    $existing_post = get_page_by_title($title, 'OBJECT', $type);
    if ($existing_post) {
        // Update existing post
        $post_id = $existing_post->ID;
        $post = array(
            'ID' => $post_id,
            'post_title' => $title,
            'post_content' => $content,
            'post_status' => $status,
        );
    } else {
        // Create new post
        $post = array(
            'post_title' => $title,
            'post_content' => $content,
            'post_status' => $status,
            'post_type' => $type,
        );
    }

    // Insert or update post
    $post_id = wp_insert_post($post);

    // Check for errors
    if (is_wp_error($post_id)) {
        throw new Exception($post_id->get_error_message());
    }

    return $post_id;
}

// Create the post
try {
    $post_id = create_post($post_title, $post_content, $post_status, $post_type);
    echo "Post created with ID $post_id\n";
} catch (Exception $e) {
    echo "Error creating post: " . $e->getMessage() . "\n";
}
```
