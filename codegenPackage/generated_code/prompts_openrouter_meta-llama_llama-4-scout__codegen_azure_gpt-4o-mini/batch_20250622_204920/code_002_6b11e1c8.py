"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate a code snippet in JavaScript to implement a price match guarantee feature for a film production services website, similar to Powered Production Film Services.
Generated: DETERMINISTIC_6b11e1c8859fe741
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PriceMatchGuarantee.js

class PriceMatchGuarantee {
    constructor() {
        // Initialize an empty array to store price match requests
        this.priceMatchRequests = [];
    }

    /**
     * Submits a price match request.
     * @param {string} serviceName - The name of the service for which the price match is requested.
     * @param {number} competitorPrice - The price offered by the competitor.
     * @param {string} competitorName - The name of the competitor.
     * @returns {string} - Confirmation message of the request submission.
     * @throws {Error} - Throws an error if any parameter is invalid.
     */
    submitPriceMatchRequest(serviceName, competitorPrice, competitorName) {
        // Validate input parameters
        if (!serviceName || typeof serviceName !== 'string') {
            throw new Error('Invalid service name. It must be a non-empty string.');
        }
        if (isNaN(competitorPrice) || competitorPrice <= 0) {
            throw new Error('Invalid competitor price. It must be a positive number.');
        }
        if (!competitorName || typeof competitorName !== 'string') {
            throw new Error('Invalid competitor name. It must be a non-empty string.');
        }

        // Create a price match request object
        const request = {
            serviceName,
            competitorPrice,
            competitorName,
            requestDate: new Date(),
        };

        // Store the request in the array
        this.priceMatchRequests.push(request);

        // Return a confirmation message
        return `Price match request submitted for ${serviceName} at $${competitorPrice} from ${competitorName}.`;
    }

    /**
     * Retrieves all price match requests.
     * @returns {Array} - An array of all price match requests.
     */
    getPriceMatchRequests() {
        return this.priceMatchRequests;
    }

    /**
     * Clears all price match requests.
     * @returns {string} - Confirmation message of the clearing action.
     */
    clearPriceMatchRequests() {
        this.priceMatchRequests = [];
        return 'All price match requests have been cleared.';
    }
}

// Example usage
try {
    const priceMatch = new PriceMatchGuarantee();
    console.log(priceMatch.submitPriceMatchRequest('Film Editing', 500, 'Competitor A'));
    console.log(priceMatch.submitPriceMatchRequest('Video Production', 1000, 'Competitor B'));
    console.log(priceMatch.getPriceMatchRequests());
    console.log(priceMatch.clearPriceMatchRequests());
} catch (error) {
    console.error('Error:', error.message);
}
```
