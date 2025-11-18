"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcioo.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message like "BTC Pledge requires JavaScript enabled to function properly."
Generated: DETERMINISTIC_e957526e28037605
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled in the browser
 * and display a message if it is enabled.
 */
(function() {
    // Create a div element to display the message
    const messageDiv = document.createElement("div");
    messageDiv.id = "js-check-message";
    messageDiv.style.position = "fixed";
    messageDiv.style.top = "10px";
    messageDiv.style.left = "50%";
    messageDiv.style.transform = "translateX(-50%)";
    messageDiv.style.padding = "10px 20px";
    messageDiv.style.backgroundColor = "#f44336";
    messageDiv.style.color = "#fff";
    messageDiv.style.fontSize = "16px";
    messageDiv.style.fontFamily = "Arial, sans-serif";
    messageDiv.style.borderRadius = "5px";
    messageDiv.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.2)";
    messageDiv.style.zIndex = "9999";
    messageDiv.innerText = "BTC Pledge requires JavaScript enabled to function properly.";

    // Append the message div to the body
    document.body.appendChild(messageDiv);

    // Automatically remove the message after 5 seconds (cleanup)
    setTimeout(() => {
        try {
            if (messageDiv && messageDiv.parentNode) {
                messageDiv.parentNode.removeChild(messageDiv);
            }
        } catch (error) {
            console.error("Error while removing the message div:", error);
        }
    }, 5000);
})();
```
