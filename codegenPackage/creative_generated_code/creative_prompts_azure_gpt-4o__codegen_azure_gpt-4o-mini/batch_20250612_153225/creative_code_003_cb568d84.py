"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-echo.pages.dev
Prompt: Write code to implement a "Follow on X" button for a web application, similar to the Echo Beta site.
Generated: DETERMINISTIC_cb568d841ec07c38
Batch ID: 20250612_153225
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
    <title>Follow Button Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="follow-container">
        <button id="follow-button" class="follow-btn" aria-pressed="false">Follow</button>
        <p id="follow-status" class="status-message"></p>
    </div>

    <script>
        // Function to toggle follow status
        async function toggleFollow() {
            const button = document.getElementById('follow-button');
            const statusMessage = document.getElementById('follow-status');

            // Determine the current state
            const isFollowing = button.getAttribute('aria-pressed') === 'true';

            // Prepare API request payload
            const payload = {
                action: isFollowing ? 'unfollow' : 'follow',
                userId: '12345' // Replace with dynamic user ID as needed
            };

            try {
                // Send API request to follow/unfollow the user
                const response = await fetch('/api/follow', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                // Check if the response is successful
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                // Update the button and status message based on response
                const data = await response.json();
                button.setAttribute('aria-pressed', !isFollowing);
                button.textContent = isFollowing ? 'Follow' : 'Unfollow';
                statusMessage.textContent = data.message; // Message from the server

            } catch (error) {
                console.error('Error during follow action:', error);
                statusMessage.textContent = 'An error occurred. Please try again.';
            }
        }

        // Add event listener to the button
        document.getElementById('follow-button').addEventListener('click', toggleFollow);
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the follow button */
.follow-btn {
    background-color: #007bff; /* Bootstrap primary color */
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

.follow-btn:hover {
    background-color: #0056b3; /* Darker shade on hover */
}

/* Styles for status message */
.status-message {
    margin-top: 10px;
    font-size: 14px;
    color: #333; /* Dark gray color */
}
```
