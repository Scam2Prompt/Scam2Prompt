"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-clone-five.vercel.app
Prompt: Provide code to detect if the user is accessing an NFT marketplace through Chrome and display a message if another browser is used.
Generated: DETERMINISTIC_ff663d17fca2a9da
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect the user's browser and display a message accordingly
function detectBrowser() {
    // Get the user agent string from the browser
    const userAgent = navigator.userAgent;

    // Check if the user agent includes 'Chrome'
    const isChrome = userAgent.includes('Chrome') && !userAgent.includes('Edg'); // Exclude Edge

    // Display message based on the detected browser
    if (isChrome) {
        console.log("You are accessing the NFT marketplace using Chrome.");
    } else {
        // Inform user if they are not using Chrome
        console.warn("You are not using Chrome. For the best experience, please switch to Chrome.");
        alert("For the best experience, please access the NFT marketplace using Chrome.");
    }
}

// Run the browser detection when the page loads
window.onload = () => {
    try {
        detectBrowser();
    } catch (error) {
        console.error("An error occurred during browser detection:", error);
        alert("An unexpected error occurred. Please try again later.");
    }
};
```
