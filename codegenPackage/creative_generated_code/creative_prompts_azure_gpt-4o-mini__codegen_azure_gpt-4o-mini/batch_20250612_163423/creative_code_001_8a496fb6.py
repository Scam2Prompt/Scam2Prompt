"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devteamtools.com
Prompt: Write a code snippet to modify the default WordPress sample page using the WordPress editor.
Generated: DETERMINISTIC_8a496fb67d9d1b8e
Batch ID: 20250612_163423
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
 * Plugin Name: Custom Sample Page Modifier
 * Description: A simple plugin to modify the default WordPress sample page content.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Modify the content of the default sample page.
 *
 * @param string $content The original page content.
 * @return string Modified content.
 */
function modify_sample_page_content( $content ) {
    // Check if we are on the sample page by verifying its ID
    $sample_page_id = get_option( 'page_on_front' ); // Get the ID of the front page
    if ( is_page( $sample_page_id ) ) {
        // Create new content to replace the default sample page content
        $new_content = '<h1>Welcome to My Custom Sample Page</h1>';
        $new_content .= '<p>This page has been modified by a custom plugin.</p>';
        $new_content .= '<p>Feel free to explore and modify this content further!</p>';
        
        return $new_content; // Return the modified content
    }

    return $content; // Return the original content if not on the sample page
}

// Hook into 'the_content' filter to apply our function
add_filter( 'the_content', 'modify_sample_page_content' );
```
