"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hingehealth.eu
Prompt: Generate code to implement a JavaScript-based notification system that informs users about enabling JavaScript for optimal app functionality, inspired by the Hinge Health EU website.
Generated: DETERMINISTIC_7861a443cde6f1d2
Batch ID: 20250612_151438
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
    <title>JavaScript Notification System</title>
    <style>
        /* Basic styles for the notification */
        #js-notification {
            display: none; /* Hidden by default */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: #ffcc00; /* A visible color for alert */
            color: #333;
            padding: 10px;
            text-align: center;
            font-family: Arial, sans-serif;
            z-index: 1000; /* Ensure it appears above other content */
        }
    </style>
</head>
<body>

<div id="js-notification">
    <strong>Notice:</strong> To ensure optimal functionality of this application, please enable JavaScript in your browser settings.
</div>

<script>
    // Function to check if JavaScript is enabled
    function jsEnabledNotification() {
        // Get the notification element
        const notification = document.getElementById('js-notification');

        // Display the notification
        notification.style.display = 'block';

        // Optional: Automatically hide the notification after a certain time (e.g., 10 seconds)
        setTimeout(() => {
            notification.style.display = 'none';
        }, 10000);
    }

    // Run the notification function on page load
    window.onload = () => {
        // Check if JavaScript is enabled by running the function
        try {
            jsEnabledNotification();
        } catch (error) {
            console.error("Error displaying JavaScript notification:", error);
        }
    };
</script>

</body>
</html>
```
