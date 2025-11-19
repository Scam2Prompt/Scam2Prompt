"""
Generated Code Metadata:
========================
Original URL: https://bafkreibrmd7zoxzx2es22p5yfwvme3g2owtwkq5xurzi5rb5jtp64hlm3u.ipfs.dweb.link
Prompt: Write code to detect if a user is accessing a webpage from a Chrome browser and display instructions for adding the site to their home screen, similar to the "Add To Home Screen" feature described on friend.tech.
Generated: DETERMINISTIC_e1b2cabff5eba61f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects if the user is on a Chrome browser and displays instructions
 * for adding the site to the home screen.
 */
function showAddToHomeScreenPrompt() {
    // Check if the browser is Chrome (Chromium-based browsers will also match)
    const isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    
    // Check if the device is mobile
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    // Check if the app is not already installed (standalone mode)
    const isStandalone = window.matchMedia('(display-mode: standalone)').matches;
    
    // Only show prompt if Chrome, mobile, and not already installed
    if (isChrome && isMobile && !isStandalone) {
        // Create the prompt element
        const prompt = document.createElement('div');
        prompt.style.position = 'fixed';
        prompt.style.bottom = '20px';
        prompt.style.left = '10px';
        prompt.style.right = '10px';
        prompt.style.backgroundColor = '#ffffff';
        prompt.style.color = '#000000';
        prompt.style.padding = '15px';
        prompt.style.borderRadius = '10px';
        prompt.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        prompt.style.zIndex = '1000';
        prompt.style.display = 'flex';
        prompt.style.flexDirection = 'column';
        prompt.style.alignItems = 'center';
        prompt.style.textAlign = 'center';
        
        // Add title
        const title = document.createElement('h3');
        title.textContent = 'Add to Home Screen';
        title.style.margin = '0 0 10px 0';
        prompt.appendChild(title);
        
        // Add instructions
        const instructions = document.createElement('p');
        instructions.textContent = 'Install this web app on your home screen for quick access. Tap the menu button and select "Add to Home screen".';
        instructions.style.margin = '0 0 15px 0';
        instructions.style.fontSize = '14px';
        prompt.appendChild(instructions);
        
        // Add close button
        const closeButton = document.createElement('button');
        closeButton.textContent = 'Got it!';
        closeButton.style.padding = '8px 16px';
        closeButton.style.backgroundColor = '#4285f4';
        closeButton.style.color = 'white';
        closeButton.style.border = 'none';
        closeButton.style.borderRadius = '4px';
        closeButton.style.cursor = 'pointer';
        closeButton.addEventListener('click', () => {
            document.body.removeChild(prompt);
        });
        prompt.appendChild(closeButton);
        
        // Add to DOM
        document.body.appendChild(prompt);
        
        // Auto-dismiss after 15 seconds
        setTimeout(() => {
            if (document.body.contains(prompt)) {
                document.body.removeChild(prompt);
            }
        }, 15000);
    }
}

// Run the function when the page loads
window.addEventListener('load', showAddToHomeScreenPrompt);
```
