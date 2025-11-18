"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powertools.reviewsrelay.com
Prompt: Write a script to display a custom notification on a webpage when an affiliate store powered by FreshStore is suspended, including contact information for support.
Generated: DETERMINISTIC_22ec6f75d5418983
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affiliate Store Notification</title>
    <style>
        /* Basic styling for the notification banner */
        .notification {
            display: none; /* Hidden by default */
            background-color: #ffcc00;
            color: #333;
            padding: 15px;
            text-align: center;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
        }
    </style>
</head>
<body>

<div id="notificationBanner" class="notification">
    <strong>Notice:</strong> The affiliate store is currently suspended. Please contact support at <a href="mailto:support@example.com">support@example.com</a>.
</div>

<script>
    /**
     * Function to check the status of the affiliate store
     * This function simulates an API call to check the store status
     */
    async function checkStoreStatus() {
        try {
            // Simulate an API call with a promise
            const response = await fetch('/api/store/status'); // Replace with actual API endpoint

            // Check if the response is ok (status in the range 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Display notification if the store is suspended
            if (data.status === 'suspended') {
                displayNotification();
            }
        } catch (error) {
            console.error('Error checking store status:', error);
            // Optionally, you could implement further error handling here
        }
    }

    /**
     * Function to display the notification banner
     */
    function displayNotification() {
        const notificationBanner = document.getElementById('notificationBanner');
        notificationBanner.style.display = 'block'; // Show the notification
    }

    // Invoke the store status check on page load
    window.onload = checkStoreStatus;
</script>

</body>
</html>
```
