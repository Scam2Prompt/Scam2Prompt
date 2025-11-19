"""
Generated Code Metadata:
========================
Original URL: https://khaleeji.com
Prompt: Write a JavaScript function to display website traffic information, including visits and email count, on a real estate or marketplace platform listing a domain for sale.
Generated: DETERMINISTIC_6722aebc739b28e5
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display website traffic information for a domain listing.
 * 
 * @param {Object} trafficData - An object containing traffic information.
 * @param {number} trafficData.visits - The number of visits to the domain.
 * @param {number} trafficData.emailCount - The number of emails received regarding the domain.
 * @throws {Error} Throws an error if trafficData is not an object or if visits/emailCount are not numbers.
 */
function displayTrafficInfo(trafficData) {
    // Validate input
    if (typeof trafficData !== 'object' || trafficData === null) {
        throw new Error('Invalid input: trafficData must be a non-null object.');
    }
    
    const { visits, emailCount } = trafficData;

    // Validate visits and emailCount
    if (typeof visits !== 'number' || typeof emailCount !== 'number') {
        throw new Error('Invalid input: visits and emailCount must be numbers.');
    }

    // Create a container for the traffic information
    const trafficInfoContainer = document.createElement('div');
    trafficInfoContainer.className = 'traffic-info';

    // Create and append visits information
    const visitsElement = document.createElement('p');
    visitsElement.textContent = `Total Visits: ${visits.toLocaleString()}`;
    trafficInfoContainer.appendChild(visitsElement);

    // Create and append email count information
    const emailCountElement = document.createElement('p');
    emailCountElement.textContent = `Total Emails Received: ${emailCount.toLocaleString()}`;
    trafficInfoContainer.appendChild(emailCountElement);

    // Append the traffic information to the body or a specific section of the page
    document.body.appendChild(trafficInfoContainer);
}

// Example usage
try {
    const trafficData = {
        visits: 12345,
        emailCount: 678
    };
    displayTrafficInfo(trafficData);
} catch (error) {
    console.error('Error displaying traffic information:', error.message);
}
```
