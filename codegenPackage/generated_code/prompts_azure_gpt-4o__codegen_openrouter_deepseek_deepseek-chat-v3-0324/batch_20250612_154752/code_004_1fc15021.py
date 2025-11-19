"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Write a JavaScript function to dynamically check and prompt users to enable JavaScript for accessing a shopping feature, similar to the behavior described on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_1fc1502117a0c578
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and prompts the user to enable it if not.
 * This function mimics the behavior seen on the Rarecrew app's "Shop" page.
 * 
 * @returns {boolean} - Returns true if JavaScript is enabled, false otherwise.
 */
function checkAndPromptJavaScript() {
    try {
        // Attempt to create a dynamic element to check JavaScript functionality
        const testElement = document.createElement('div');
        testElement.style.display = 'none';
        document.body.appendChild(testElement);
        
        // If we got here, JavaScript is enabled
        return true;
    } catch (e) {
        // JavaScript is not properly enabled
        showJavaScriptPrompt();
        return false;
    }
}

/**
 * Displays a prompt asking the user to enable JavaScript.
 * The prompt is styled to match the shopping feature context.
 */
function showJavaScriptPrompt() {
    // Create the prompt container
    const promptContainer = document.createElement('div');
    promptContainer.style.position = 'fixed';
    promptContainer.style.top = '0';
    promptContainer.style.left = '0';
    promptContainer.style.width = '100%';
    promptContainer.style.height = '100%';
    promptContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    promptContainer.style.display = 'flex';
    promptContainer.style.justifyContent = 'center';
    promptContainer.style.alignItems = 'center';
    promptContainer.style.zIndex = '1000';
    
    // Create the prompt content
    const promptContent = document.createElement('div');
    promptContent.style.backgroundColor = '#fff';
    promptContent.style.padding = '2rem';
    promptContent.style.borderRadius = '8px';
    promptContent.style.maxWidth = '500px';
    promptContent.style.textAlign = 'center';
    
    // Add heading
    const heading = document.createElement('h2');
    heading.textContent = 'JavaScript is Disabled';
    heading.style.marginBottom = '1rem';
    heading.style.color = '#333';
    promptContent.appendChild(heading);
    
    // Add message
    const message = document.createElement('p');
    message.textContent = 'To access the shopping feature, please enable JavaScript in your browser settings and refresh the page.';
    message.style.marginBottom = '1.5rem';
    message.style.color = '#666';
    promptContent.appendChild(message);
    
    // Add refresh button
    const refreshButton = document.createElement('button');
    refreshButton.textContent = 'Refresh Page';
    refreshButton.style.padding = '0.75rem 1.5rem';
    refreshButton.style.backgroundColor = '#007bff';
    refreshButton.style.color = '#fff';
    refreshButton.style.border = 'none';
    refreshButton.style.borderRadius = '4px';
    refreshButton.style.cursor = 'pointer';
    refreshButton.style.fontSize = '1rem';
    refreshButton.addEventListener('click', () => {
        window.location.reload();
    });
    promptContent.appendChild(refreshButton);
    
    // Assemble and show the prompt
    promptContainer.appendChild(promptContent);
    document.body.appendChild(promptContainer);
    
    // Prevent scrolling when prompt is shown
    document.body.style.overflow = 'hidden';
}

// Check JavaScript on page load
document.addEventListener('DOMContentLoaded', () => {
    checkAndPromptJavaScript();
});
```
