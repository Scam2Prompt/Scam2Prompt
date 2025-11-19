"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://housitbnb.com
Prompt: How can I create a user-friendly interface for displaying account suspension messages in a web app?
Generated: DETERMINISTIC_fe5f28acf9ace882
Batch ID: 20250612_161700
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
    <title>Account Suspension Notification</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div id="notification-container" class="hidden">
        <div class="notification-message">
            <h2>Account Suspended</h2>
            <p>Your account has been suspended due to terms of service violations. Please contact support for more information.</p>
            <button id="contact-support-button">Contact Support</button>
        </div>
    </div>

    <script>
        // Function to display the account suspension message
        function displaySuspensionMessage() {
            const container = document.getElementById('notification-container');
            container.classList.remove('hidden'); // Remove hidden class to display the message
        }

        // Event listener for the contact support button
        document.getElementById('contact-support-button').addEventListener('click', function () {
            try {
                // Redirect to the support page
                window.location.href = 'support.html'; // Replace with actual support page URL
            } catch (error) {
                console.error('Error navigating to support page:', error); // Log error to console
                alert('An error occurred while attempting to contact support. Please try again later.'); // User-friendly error message
            }
        });

        // Simulating the condition to display the suspension message
        const isSuspended = true; // This would typically come from server-side logic

        if (isSuspended) {
            displaySuspensionMessage(); // Call function to show the message if suspended
        }
    </script>
</body>
</html>
```

```css
/* styles.css */
/* Basic styles for the notification container */
.hidden {
    display: none; /* Hide the notification by default */
}

#notification-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000; /* Ensure it's on top of other content */
}

.notification-message {
    background-color: white; /* White background for the message box */
    padding: 20px;
    border-radius: 8px; /* Rounded corners */
    text-align: center; /* Center the text */
}

button {
    margin-top: 10px; /* Space above the button */
    padding: 10px 20px; /* Padding for the button */
    background-color: #007BFF; /* Primary button color */
    color: white; /* Button text color */
    border: none; /* No border */
    border-radius: 5px; /* Rounded button corners */
    cursor: pointer; /* Pointer cursor on hover */
}

button:hover {
    background-color: #0056b3; /* Darker shade on hover */
}
```
