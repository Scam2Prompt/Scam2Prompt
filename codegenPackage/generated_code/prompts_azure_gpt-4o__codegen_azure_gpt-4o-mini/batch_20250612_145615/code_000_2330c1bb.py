"""
Generated Code Metadata:
========================
Original URL: https://lightningzaim.online
Prompt: Write JavaScript code to track user clicks on MFO offers using Yandex Metrica goals, as described in the custom HTML code on lightningzaim.online.
Generated: DETERMINISTIC_2330c1bbd7cf1985
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to initialize Yandex Metrica tracking
(function() {
    // Check if the Yandex Metrica object is available
    if (typeof window.yaCounter === 'undefined') {
        console.error('Yandex Metrica is not initialized.');
        return;
    }

    // Function to track clicks on MFO offers
    function trackMFOClick(offerId) {
        try {
            // Check if the offerId is valid
            if (!offerId) {
                throw new Error('Invalid offer ID provided for tracking.');
            }

            // Send the goal to Yandex Metrica
            window.yaCounter.reachGoal('mfo_offer_click', {
                offerId: offerId
            });
            console.log(`Tracked click for MFO offer ID: ${offerId}`);
        } catch (error) {
            console.error('Error tracking MFO offer click:', error.message);
        }
    }

    // Event listener for MFO offer clicks
    document.addEventListener('click', function(event) {
        // Check if the clicked element has the 'mfo-offer' class
        if (event.target.classList.contains('mfo-offer')) {
            // Get the offer ID from the data attribute
            const offerId = event.target.getAttribute('data-offer-id');
            trackMFOClick(offerId);
        }
    });
})();
```

Make sure to include the Yandex Metrica script in your HTML before this code for it to function correctly.
