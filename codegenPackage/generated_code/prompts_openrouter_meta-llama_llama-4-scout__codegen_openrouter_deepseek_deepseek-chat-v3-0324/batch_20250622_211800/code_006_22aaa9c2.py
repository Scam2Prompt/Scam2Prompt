"""
Generated Code Metadata:
========================
Original URL: https://zoholandingpage.com
Prompt: "Write a JavaScript code snippet to create a dynamic popup on a Zoho LandingPage using their API."
Generated: DETERMINISTIC_22aaa9c246559e56
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates a dynamic popup on a Zoho LandingPage using Zoho's API.
 * This script assumes the Zoho LandingPage API is properly loaded and available.
 */

// Configuration for the popup
const popupConfig = {
    title: 'Dynamic Popup',
    content: 'This is a dynamic popup created using Zoho LandingPage API.',
    width: '500px',
    height: '300px',
    showCloseButton: true,
    overlayClose: true,
    buttons: [
        {
            label: 'OK',
            onClick: function() {
                console.log('OK button clicked');
                ZOHO.CREATOR.API.closePopup();
            }
        },
        {
            label: 'Cancel',
            onClick: function() {
                console.log('Cancel button clicked');
                ZOHO.CREATOR.API.closePopup();
            }
        }
    ]
};

/**
 * Initializes and displays the popup when the page is fully loaded.
 */
document.addEventListener('DOMContentLoaded', function() {
    try {
        // Check if ZOHO.CREATOR.API is available
        if (typeof ZOHO === 'undefined' || !ZOHO.CREATOR || !ZOHO.CREATOR.API) {
            throw new Error('Zoho Creator API is not available.');
        }

        // Create and show the popup
        ZOHO.CREATOR.API.createPopup(popupConfig)
            .then(function(response) {
                console.log('Popup created successfully:', response);
            })
            .catch(function(error) {
                console.error('Error creating popup:', error);
                // Fallback to alert if popup creation fails
                alert('Failed to create popup. ' + error.message);
            });
    } catch (error) {
        console.error('Initialization error:', error);
        alert('An error occurred while initializing the popup. ' + error.message);
    }
});
```
