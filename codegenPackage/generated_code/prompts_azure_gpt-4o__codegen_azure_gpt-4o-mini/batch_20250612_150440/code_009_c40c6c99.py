"""
Generated Code Metadata:
========================
Original URL: https://sajumavi.edu.pe
Prompt: Write JavaScript code to dynamically update virtual classroom content on a WordPress site using AJAX.
Generated: DETERMINISTIC_c40c6c99b73fc444
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to dynamically update virtual classroom content on a WordPress site using AJAX

// Function to fetch and update classroom content
async function updateClassroomContent(classroomId) {
    try {
        // Define the AJAX request URL
        const url = `${window.location.origin}/wp-admin/admin-ajax.php`;

        // Prepare the data to be sent in the request
        const data = new URLSearchParams();
        data.append('action', 'fetch_classroom_content'); // WordPress action hook
        data.append('classroom_id', classroomId); // Classroom ID to fetch content for

        // Make the AJAX request using Fetch API
        const response = await fetch(url, {
            method: 'POST',
            body: data,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const content = await response.json();

        // Update the classroom content on the page
        const contentContainer = document.getElementById('classroom-content');
        if (contentContainer) {
            contentContainer.innerHTML = content.data; // Assuming 'data' contains the HTML content
        } else {
            console.error('Content container not found');
        }
    } catch (error) {
        // Handle errors gracefully
        console.error('Error updating classroom content:', error);
        alert('Failed to update classroom content. Please try again later.');
    }
}

// Example usage: Update content for classroom with ID 1
updateClassroomContent(1);

// Event listener to trigger content update (e.g., on button click)
document.getElementById('update-content-button').addEventListener('click', () => {
    const classroomId = document.getElementById('classroom-id-input').value;
    updateClassroomContent(classroomId);
});
```

```php
// PHP code to handle the AJAX request in WordPress

// Add this code to your theme's functions.php or a custom plugin

add_action('wp_ajax_fetch_classroom_content', 'fetch_classroom_content');
add_action('wp_ajax_nopriv_fetch_classroom_content', 'fetch_classroom_content');

function fetch_classroom_content() {
    // Check if classroom_id is set and is a valid integer
    if (isset($_POST['classroom_id']) && is_numeric($_POST['classroom_id'])) {
        $classroom_id = intval($_POST['classroom_id']);

        // Fetch classroom content from the database (example query)
        global $wpdb;
        $table_name = $wpdb->prefix . 'classroom_content'; // Replace with your actual table name
        $content = $wpdb->get_var($wpdb->prepare("SELECT content FROM $table_name WHERE id = %d", $classroom_id));

        // Return the content as JSON
        if ($content) {
            wp_send_json_success(['data' => $content]);
        } else {
            wp_send_json_error('No content found for this classroom.');
        }
    } else {
        wp_send_json_error('Invalid classroom ID.');
    }

    // Always die in the end of AJAX functions
    wp_die();
}
```
