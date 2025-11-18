"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hingehealth.eu
Prompt: Write a JavaScript function that dynamically updates the webpage content to notify users when JavaScript is disabled, mimicking the behavior of the hingehealth.eu site.
Generated: DETERMINISTIC_b528ef2f65f18deb
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled and update webpage content accordingly
function notifyJavaScriptDisabled() {
    // Create a div element to display the notification
    const notificationDiv = document.createElement('div');

    // Set the styles for the notification
    notificationDiv.style.position = 'fixed';
    notificationDiv.style.top = '0';
    notificationDiv.style.left = '0';
    notificationDiv.style.width = '100%';
    notificationDiv.style.backgroundColor = '#ffcc00'; // Yellow background
    notificationDiv.style.color = '#000'; // Black text
    notificationDiv.style.textAlign = 'center';
    notificationDiv.style.padding = '10px';
    notificationDiv.style.zIndex = '1000';
    notificationDiv.style.fontFamily = 'Arial, sans-serif';

    // Set the content of the notification
    notificationDiv.innerHTML = 
        'JavaScript is disabled in your browser. Please enable it for the best experience.';

    // Append the notification to the body
    document.body.appendChild(notificationDiv);
}

// Invoke the function to check if JavaScript is enabled
notifyJavaScriptDisabled();

// Add a fallback mechanism for when JavaScript is disabled
// Insert a noscript tag right in the HTML to provide a message if JS is off.
document.write('<noscript><style>body:before { content: "JavaScript is disabled in your browser. Please enable it for the best experience."; display: block; padding: 10px; background: #ffcc00; color: #000; text-align: center; font-family: Arial, sans-serif; }</style></noscript>');
```

### Notes:
- Ensure to include the `<script>` tag for this JavaScript code in your HTML file for proper execution.
- The `noscript` tag is a fallback for users who have JavaScript disabled, providing a visual cue and styling to inform them of the issue.
