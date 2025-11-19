"""
Generated Code Metadata:
========================
Original URL: https://check.wenser.e2p.xyz
Prompt: "Generate JavaScript code for a simple domain details checker that displays information when JavaScript is enabled."
Generated: DETERMINISTIC_ab8c719cf7c0687c
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Domain Details Checker
 * 
 * This script checks if JavaScript is enabled and displays domain details.
 */

// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Check if JavaScript is enabled
    const jsCheckElement = document.getElementById('js-check');
    
    if (jsCheckElement) {
        jsCheckElement.textContent = 'JavaScript is enabled!';
        jsCheckElement.className = 'js-enabled';
        
        // Display domain details
        displayDomainDetails();
    } else {
        console.error('Element with ID "js-check" not found.');
    }
});

/**
 * Displays various details about the current domain
 */
function displayDomainDetails() {
    const detailsContainer = document.getElementById('domain-details');
    
    if (!detailsContainer) {
        console.error('Element with ID "domain-details" not found.');
        return;
    }
    
    try {
        const domainDetails = {
            'Current URL': window.location.href,
            'Hostname': window.location.hostname,
            'Protocol': window.location.protocol,
            'Path': window.location.pathname,
            'Port': window.location.port || '80 (default)',
            'Browser Language': navigator.language || 'Not available',
            'User Agent': navigator.userAgent,
            'Online Status': navigator.onLine ? 'Online' : 'Offline',
            'Screen Resolution': `${window.screen.width} x ${window.screen.height}`,
            'Color Depth': `${window.screen.colorDepth} bit`
        };
        
        // Create HTML for domain details
        let detailsHTML = '<h2>Domain Details</h2><ul>';
        
        for (const [key, value] of Object.entries(domainDetails)) {
            detailsHTML += `<li><strong>${key}:</strong> ${value}</li>`;
        }
        
        detailsHTML += '</ul>';
        detailsContainer.innerHTML = detailsHTML;
        detailsContainer.className = 'details-visible';
        
    } catch (error) {
        console.error('Error displaying domain details:', error);
        detailsContainer.innerHTML = '<p class="error">Unable to retrieve domain details.</p>';
    }
}

// Error handling for the entire script
window.onerror = function(message, source, lineno, colno, error) {
    console.error(`Error: ${message} at ${source}:${lineno}:${colno}`);
    const errorContainer = document.getElementById('error-container') || document.body;
    errorContainer.innerHTML += `<div class="global-error">A JavaScript error occurred: ${message}</div>`;
    return true; // Prevent error from showing in console
};
```
