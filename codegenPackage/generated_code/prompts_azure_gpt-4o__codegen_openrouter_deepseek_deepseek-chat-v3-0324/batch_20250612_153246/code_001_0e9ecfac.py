"""
Generated Code Metadata:
========================
Original URL: https://36destinations.com
Prompt: Generate a PHP script to programmatically edit or delete the default "Hello world!" post in WordPress.
Generated: DETERMINISTIC_0e9ecfac8396f69b
Batch ID: 20250612_153246
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
 * WordPress Post Editor Script
 * 
 * This script allows programmatic editing or deletion of the default "Hello world!" post in WordPress.
 */

// Ensure WordPress environment is loaded
if (!defined('ABSPATH')) {
    require_once( dirname(__FILE__) . '/wp-load.php' );
}

// Main function to handle post editing/deletion
function edit_or_delete_default_post($action = 'edit', $new_content = '') {
    global $wpdb;
    
    try {
        // Find the default "Hello world!" post
        $post = $wpdb->get_row(
            $wpdb->prepare(
                "SELECT * FROM $wpdb->posts WHERE post_title = %s AND post_type = %s AND post_status = %s LIMIT 1",
                'Hello world!',
                'post',
                'publish'
            )
        );

        if (!$post) {
            throw new Exception('Default "Hello world!" post not found.');
        }

        // Perform the requested action
        switch ($action) {
            case 'edit':
                if (empty($new_content)) {
                    throw new Exception('New content cannot be empty for edit operation.');
                }

                $updated_post = array(
                    'ID'           => $post->ID,
                    'post_content' => $new_content,
                );

                $result = wp_update_post($updated_post, true);
                
                if (is_wp_error($result)) {
                    throw new Exception($result->get_error_message());
                }
                
                return 'Post updated successfully.';
                
            case 'delete':
                $result = wp_delete_post($post->ID, true);
                
                if (!$result) {
                    throw new Exception('Failed to delete the post.');
                }
                
                return 'Post deleted successfully.';
                
            default:
                throw new Exception('Invalid action specified. Use "edit" or "delete".');
        }
    } catch (Exception $e) {
        return 'Error: ' . $e->getMessage();
    }
}

// Example usage:
// To edit the post:
// $result = edit_or_delete_default_post('edit', 'This is the new content');
// echo $result;

// To delete the post:
// $result = edit_or_delete_default_post('delete');
// echo $result;
```
