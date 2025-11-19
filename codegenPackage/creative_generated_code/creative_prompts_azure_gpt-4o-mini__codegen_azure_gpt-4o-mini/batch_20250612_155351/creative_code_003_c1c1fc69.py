"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus.at
Prompt: Develop a JavaScript function that displays a user-friendly message when a domain is not reachable, similar to the multilingual responses on the STRATO site.
Generated: DETERMINISTIC_c1c1fc6989ac3a75
Batch ID: 20250612_155351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${domain}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if a given domain is reachable and displays a user-friendly message.
 * 
 * @param {string} domain - The domain to check for reachability.
 * @returns {Promise<void>} - A promise that resolves when the check is complete.
 */
async function checkDomainReachability(domain) {
    const messageContainer = document.getElementById('message-container');

    // Validate the input domain
    if (!isValidDomain(domain)) {
        displayMessage(messageContainer, 'Invalid domain format. Please enter a valid domain name.');
        return;
    }

    try {
        // Attempt to fetch the domain
        const response = await fetch(`https://${domain}`, { method: 'HEAD', mode: 'no-cors' });

        // Check the response status
        if (response.ok) {
            displayMessage(messageContainer, `The domain ${domain} is reachable.`);
        } else {
            displayMessage(messageContainer, `The domain ${domain} is not reachable. Please check your internet connection or try again later.`);
        }
    } catch (error) {
        // Handle fetch error
        console.error(`Error checking domain ${domain}: `, error);
        displayMessage(messageContainer, `The domain ${domain} is not reachable. An error occurred while trying to check its status.`);
    }
}

/**
 * Validates the domain format using a regular expression.
 *
 * @param {string} domain - The domain to validate.
 * @returns {boolean} - True if the domain is valid, false otherwise.
 */
function isValidDomain(domain) {
    const domainPattern = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$/;
    return domainPattern.test(domain);
}

/**
 * Displays a message in the specified container.
 *
 * @param {HTMLElement} container - The container to display the message in.
 * @param {string} message - The message to display.
 */
function displayMessage(container, message) {
    // Clear any previous messages
    container.textContent = '';
    
    // Set the new message
    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    container.appendChild(messageElement);
}

// Usage example: Call the function with a domain name
// Make sure to replace 'example.com' with the actual domain you want to check
checkDomainReachability('example.com');
```

Make sure you have an HTML element with the id `message-container` in your HTML file where the message will be displayed.
