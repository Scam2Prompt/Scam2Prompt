"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dhlinternationalexpress.com
Prompt: What are the steps to edit the default WordPress sample page and replace it with custom content?
Generated: DETERMINISTIC_abff74559def6179
Batch ID: 20250612_160823
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
 * Function to update the default WordPress sample page with custom content.
 *
 * This function retrieves the default sample page, updates its title
 * and content, and then saves the changes.
 *
 * @param string $new_title The new title for the sample page.
 * @param string $new_content The new content for the sample page.
 * @return void
 */
function update_sample_page($new_title, $new_content) {
    // Fetch the default sample page
    $page = get_page_by_path('sample-page');

    // Check if the sample page exists
    if ($page) {
        // Prepare the updated page data
        $updated_page = array(
            'ID'           => $page->ID,
            'post_title'   => sanitize_text_field($new_title),
            'post_content' => wp_kses_post($new_content),
            'post_status'  => 'publish', // Ensure the page is published
        );

        // Update the page in the database
        $result = wp_update_post($updated_page);

        // Check if the update was successful
        if (is_wp_error($result)) {
            // Log the error message
            error_log('Error updating sample page: ' . $result->get_error_message());
        } else {
            // Successfully updated page
            echo 'Sample page updated successfully!';
        }
    } else {
        // Log an error if the sample page does not exist
        error_log('Sample page not found.');
    }
}

// Example usage of the function
$new_title = 'My Custom Title';
$new_content = '<p>This is my custom content for the sample page.</p>';
update_sample_page($new_title, $new_content);
?>
```
