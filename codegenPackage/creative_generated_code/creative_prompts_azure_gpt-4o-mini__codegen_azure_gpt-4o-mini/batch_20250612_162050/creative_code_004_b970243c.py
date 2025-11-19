"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica16.vercel.app
Prompt: How do I handle network selection in a JavaScript application using the Matrica API?
Generated: DETERMINISTIC_b970243c386861ef
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Matrica API client
import Matrica from 'matrica-api-client';

/**
 * NetworkSelector class to handle network selection using the Matrica API
 */
class NetworkSelector {
    constructor(apiKey) {
        // Initialize the Matrica API client with the provided API key
        this.apiClient = new Matrica(apiKey);
    }

    /**
     * Fetch available networks from the Matrica API
     * @returns {Promise<Array>} A promise that resolves to an array of available networks
     * @throws Will throw an error if the API call fails
     */
    async fetchAvailableNetworks() {
        try {
            const networks = await this.apiClient.getNetworks();
            return networks;
        } catch (error) {
            console.error('Error fetching available networks:', error);
            throw new Error('Failed to fetch networks');
        }
    }

    /**
     * Select a network by its ID
     * @param {string} networkId The ID of the network to select
     * @returns {Promise<Object>} A promise that resolves to the selected network details
     * @throws Will throw an error if the network selection fails
     */
    async selectNetwork(networkId) {
        try {
            const selectedNetwork = await this.apiClient.selectNetwork(networkId);
            return selectedNetwork;
        } catch (error) {
            console.error(`Error selecting network with ID ${networkId}:`, error);
            throw new Error('Failed to select network');
        }
    }

    /**
     * Get the current selected network details
     * @returns {Promise<Object>} A promise that resolves to the currently selected network details
     * @throws Will throw an error if the API call fails
     */
    async getCurrentNetwork() {
        try {
            const currentNetwork = await this.apiClient.getCurrentNetwork();
            return currentNetwork;
        } catch (error) {
            console.error('Error fetching current network:', error);
            throw new Error('Failed to fetch current network');
        }
    }
}

// Example usage of the NetworkSelector class
(async () => {
    const apiKey = 'YOUR_API_KEY_HERE'; // Replace with your actual API key
    const networkSelector = new NetworkSelector(apiKey);

    try {
        // Fetch available networks
        const networks = await networkSelector.fetchAvailableNetworks();
        console.log('Available networks:', networks);

        // Select the first available network
        if (networks.length > 0) {
            const selectedNetwork = await networkSelector.selectNetwork(networks[0].id);
            console.log('Selected network:', selectedNetwork);
        } else {
            console.log('No networks available to select.');
        }

        // Get the current network details
        const currentNetwork = await networkSelector.getCurrentNetwork();
        console.log('Current network:', currentNetwork);
    } catch (error) {
        console.error('An error occurred during network selection:', error);
    }
})();
```
