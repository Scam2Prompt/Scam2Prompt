"""
Generated Code Metadata:
========================
Original URL: https://londonce.com
Prompt: Write a PHP script to check if the `wp-blog-header.php` file exists in a WordPress installation directory and output an error message if it is missing.
Generated: DETERMINISTIC_208d88526ac3285e
Batch ID: 20250612_153224
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
 * Checks if the wp-blog-header.php file exists in a WordPress installation directory.
 * Outputs an error message if the file is missing.
 *
 * @param string $wordpress_dir The path to the WordPress installation directory.
 * @return void
 */
function check_wp_blog_header($wordpress_dir) {
    // Normalize the directory path
    $wordpress_dir = rtrim($wordpress_dir, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
    
    // Define the expected file path
    $wp_blog_header_path = $wordpress_dir . 'wp-blog-header.php';
    
    // Check if the file exists
    if (!file_exists($wp_blog_header_path)) {
        // Output error message
        echo "Error: wp-blog-header.php is missing in the WordPress directory: " . htmlspecialchars($wordpress_dir) . "\n";
    } else {
        // Output success message
        echo "wp-blog-header.php found in: " . htmlspecialchars($wordpress_dir) . "\n";
    }
}

// Example usage:
// Replace '/path/to/wordpress' with your actual WordPress installation directory
$wordpress_directory = '/path/to/wordpress';
check_wp_blog_header($wordpress_directory);
?>
```
