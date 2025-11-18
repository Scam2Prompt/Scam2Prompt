"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soleilart.ca
Prompt: Generate JavaScript code that uses `ajaxurl` and `w3tc_nonce` to list CloudFront distributions via a popup form, as shown in the Soleil Art CDN configuration example.
Generated: DETERMINISTIC_7abf2f47b946e146
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure that the script runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the button element to open the modal
    const openModalButton = document.getElementById('openDistributionModal');
    const modal = document.getElementById('distributionModal');
    const closeModalButton = document.getElementById('closeModal');
    const distributionList = document.getElementById('distributionList');

    // Function to fetch CloudFront distributions
    function fetchCloudFrontDistributions() {
        // Create a new XMLHttpRequest object
        const xhr = new XMLHttpRequest();

        // Configure it: GET-request for the URL with ajaxurl
        xhr.open('GET', ajaxurl + '?action=list_cloudfront_distributions&nonce=' + w3tc_nonce, true);

        // Set up the callback for when the request completes
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
                // Parse the JSON response
                const response = JSON.parse(xhr.responseText);

                // Check if the response has distributions
                if (response.success && Array.isArray(response.data)) {
                    renderDistributions(response.data);
                } else {
                    // Handle case where no distributions are found
                    distributionList.innerHTML = '<li>No distributions found.</li>';
                }
            } else {
                // Handle HTTP error
                console.error('Error fetching distributions:', xhr.statusText);
                distributionList.innerHTML = '<li>Error fetching distributions.</li>';
            }
        };

        // Handle network errors
        xhr.onerror = function() {
            console.error('Network error occurred.');
            distributionList.innerHTML = '<li>Network error occurred.</li>';
        };

        // Send the request
        xhr.send();
    }

    // Function to render the list of distributions
    function renderDistributions(distributions) {
        // Clear the existing list
        distributionList.innerHTML = '';

        // Loop through distributions and create list items
        distributions.forEach(distribution => {
            const listItem = document.createElement('li');
            listItem.textContent = distribution.id + ' - ' + distribution.domainName;
            distributionList.appendChild(listItem);
        });
    }

    // Event listener to open the modal and fetch distributions
    openModalButton.addEventListener('click', function() {
        fetchCloudFrontDistributions();
        modal.style.display = 'block'; // Show the modal
    });

    // Event listener to close the modal
    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none'; // Hide the modal
    });

    // Optional: Close the modal when clicking outside of it
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
```

```html
<!-- Modal structure -->
<div id="distributionModal" class="modal">
    <div class="modal-content">
        <span id="closeModal" class="close">&times;</span>
        <h2>CloudFront Distributions</h2>
        <ul id="distributionList"></ul>
    </div>
</div>
<button id="openDistributionModal">Open CloudFront Distributions</button>
<style>
    /* Basic styling for modal */
    .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5); }
    .modal-content { background-color: #fff; margin: 15% auto; padding: 20px; width: 80%; }
    .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; }
    .close:hover, .close:focus { color: black; text-decoration: none; cursor: pointer; }
</style>
```
