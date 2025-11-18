"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: Write JavaScript code to dynamically update virtual classroom content on a WordPress site using AJAX.
Generated: DETERMINISTIC_c40c6c99b73fc444
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure the JavaScript is executed only after the DOM content is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Select the element that triggers the content update, e.g., a button
    const updateButton = document.getElementById("update-classroom-content");

    // Ensure the button exists on the page
    if (!updateButton) {
        console.error("Update button not found on the page.");
        return;
    }

    // Add a click event listener to the button
    updateButton.addEventListener("click", function () {
        // Show a loading spinner or disable the button to indicate processing (optional)
        updateButton.disabled = true;

        // Use the WordPress REST API URL for the AJAX request
        const ajaxUrl = `${window.location.origin}/wp-json/classroom/v1/update-content`;

        // Send an AJAX request to fetch updated content
        fetch(ajaxUrl, {
            method: "GET", // Use GET to fetch updated content
            headers: {
                "Content-Type": "application/json",
                // Include the WordPress Nonce for security
                "X-WP-Nonce": window.wpApiSettings?.nonce || "",
            },
        })
            .then((response) => {
                // Check if the response is OK (status code 200-299)
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                // Parse and return the JSON response
                return response.json();
            })
            .then((data) => {
                // Find the target container where the content will be updated
                const classroomContainer = document.getElementById("classroom-content");

                // Ensure the container exists on the page
                if (!classroomContainer) {
                    throw new Error("Classroom content container not found on the page.");
                }

                // Update the classroom container with the new content
                classroomContainer.innerHTML = data.content;

                // Optionally, show a success message or perform other actions
                console.log("Classroom content updated successfully.");
            })
            .catch((error) => {
                // Handle any errors during the process
                console.error("Error updating classroom content:", error);
                alert("Failed to update classroom content. Please try again later.");
            })
            .finally(() => {
                // Re-enable the button or hide the loading spinner
                updateButton.disabled = false;
            });
    });
});
```

### Notes for Integration
1. Ensure that the WordPress REST API endpoint `/wp-json/classroom/v1/update-content` is properly registered and returns the updated content in JSON format.
2. Add an ID of `update-classroom-content` for the button and `classroom-content` for the container in your WordPress theme/template for this code to work.
