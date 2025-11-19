"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.vip
Prompt: How do I design a user-friendly interface for session expiration notifications in a web app?
Generated: DETERMINISTIC_bff2d8ba73dfa803
Batch ID: 20250612_164012
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
    <title>Session Expiration Notification</title>
    <style>
        /* Basic styling for the notification */
        #session-notification {
            display: none; /* Initially hidden */
            position: fixed; /* Fixed position at the bottom */
            bottom: 20px; /* 20px from the bottom */
            right: 20px; /* 20px from the right */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding around text */
            border-radius: 5px; /* Rounded corners */
            z-index: 1000; /* Ensure it is on top of other elements */
        }
        #session-notification button {
            margin-left: 10px; /* Space between text and button */
            background-color: white; /* White button background */
            color: #f44336; /* Red text color */
            border: none; /* No border */
            cursor: pointer; /* Pointer cursor on hover */
        }
    </style>
</head>
<body>

<div id="session-notification">
    Your session is about to expire. Would you like to extend it? 
    <button id="extend-session">Extend Session</button>
</div>

<script>
    // Function to show the notification
    function showNotification() {
        const notification = document.getElementById("session-notification");
        notification.style.display = "block"; // Show the notification

        // Automatically hide the notification after 5 seconds
        setTimeout(() => {
            notification.style.display = "none"; // Hide after timeout
        }, 5000);
    }

    // Function to handle session extension
    async function extendSession() {
        try {
            const response = await fetch('/extend-session', {
                method: 'POST' // Assume a POST request to extend the session
            });

            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Failed to extend the session');
            }

            // Optionally handle success response
            const data = await response.json();
            console.log('Session extended:', data);
            // Hide the notification if session was extended
            document.getElementById("session-notification").style.display = "none"; 

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while extending your session. Please try again.'); // Notify the user
        }
    }

    // Event listener for button click to extend the session
    document.getElementById("extend-session").addEventListener("click", extendSession);

    // Simulate session expiration warning (for demonstration)
    setTimeout(showNotification, 30000); // Show notification after 30 seconds
</script>

</body>
</html>
```
