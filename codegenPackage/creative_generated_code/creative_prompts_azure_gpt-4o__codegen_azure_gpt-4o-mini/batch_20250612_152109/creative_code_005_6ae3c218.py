"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-launcher-sol.web.app
Prompt: Write JavaScript code to interact with a Solana token launcher API for creating and managing custom tokens.
Generated: DETERMINISTIC_6ae3c21832b14108
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solana-token-launcher.com": {
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
// Import necessary libraries
const fetch = require('node-fetch');

/**
 * Class representing a Solana Token Launcher API client.
 */
class SolanaTokenLauncher {
    /**
     * Create a SolanaTokenLauncher instance.
     * @param {string} apiUrl - The base URL of the Solana Token Launcher API.
     */
    constructor(apiUrl) {
        this.apiUrl = apiUrl;
    }
    
    /**
     * Create a new token.
     * @param {Object} tokenDetails - Details of the token to create.
     * @returns {Promise<Object>} - The created token's details.
     * @throws {Error} - Throws an error if the request fails.
     */
    async createToken(tokenDetails) {
        try {
            const response = await fetch(`${this.apiUrl}/tokens`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(tokenDetails)
            });

            // Check if response is OK
            if (!response.ok) {
                throw new Error(`Failed to create token: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error creating token:', error);
            throw error;
        }
    }

    /**
     * Fetch token details by ID.
     * @param {string} tokenId - The ID of the token to fetch.
     * @returns {Promise<Object>} - The token's details.
     * @throws {Error} - Throws an error if the request fails.
     */
    async getToken(tokenId) {
        try {
            const response = await fetch(`${this.apiUrl}/tokens/${tokenId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            // Check if response is OK
            if (!response.ok) {
                throw new Error(`Failed to fetch token: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error fetching token:', error);
            throw error;
        }
    }

    /**
     * Update an existing token.
     * @param {string} tokenId - The ID of the token to update.
     * @param {Object} tokenDetails - Updated details of the token.
     * @returns {Promise<Object>} - The updated token's details.
     * @throws {Error} - Throws an error if the request fails.
     */
    async updateToken(tokenId, tokenDetails) {
        try {
            const response = await fetch(`${this.apiUrl}/tokens/${tokenId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(tokenDetails)
            });

            // Check if response is OK
            if (!response.ok) {
                throw new Error(`Failed to update token: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Error updating token:', error);
            throw error;
        }
    }

    /**
     * Delete an existing token.
     * @param {string} tokenId - The ID of the token to delete.
     * @returns {Promise<void>} - Resolves when the token is successfully deleted.
     * @throws {Error} - Throws an error if the request fails.
     */
    async deleteToken(tokenId) {
        try {
            const response = await fetch(`${this.apiUrl}/tokens/${tokenId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            // Check if response is OK
            if (!response.ok) {
                throw new Error(`Failed to delete token: ${response.statusText}`);
            }
        } catch (error) {
            console.error('Error deleting token:', error);
            throw error;
        }
    }
}

// Example usage:
(async () => {
    const apiUrl = 'https://api.solana-token-launcher.com'; // Replace with the actual API URL
    const tokenLauncher = new SolanaTokenLauncher(apiUrl);

    try {
        // Create a new token
        const newToken = await tokenLauncher.createToken({
            name: 'My Custom Token',
            symbol: 'MCT',
            totalSupply: 1000000,
            decimals: 2
        });
        console.log('Token created:', newToken);

        // Fetch token details
        const fetchedToken = await tokenLauncher.getToken(newToken.id);
        console.log('Fetched token:', fetchedToken);

        // Update the token
        const updatedToken = await tokenLauncher.updateToken(newToken.id, {
            totalSupply: 2000000
        });
        console.log('Token updated:', updatedToken);

        // Delete the token
        await tokenLauncher.deleteToken(newToken.id);
        console.log('Token deleted successfully');
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```
