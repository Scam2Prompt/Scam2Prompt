"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-ether.com
Prompt: Provide an example of how to use MetaMask's Web3 Services API to manage API keys and endpoints for a decentralized application.
Generated: DETERMINISTIC_22a66a0731d29d71
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 from the web3.js library
import Web3 from 'web3';

// Function to initialize Web3 with MetaMask
async function initWeb3() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a new instance of Web3 using MetaMask's provider
        const web3 = new Web3(window.ethereum);

        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask is connected');
            return web3;
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Could not access MetaMask accounts');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this application.');
        throw new Error('MetaMask is not installed');
    }
}

// Function to manage API keys and endpoints
class ApiKeyManager {
    constructor() {
        this.apiKeys = {};
    }

    // Function to add a new API key
    addApiKey(name, key) {
        if (!name || !key) {
            throw new Error('API Key name and key are required');
        }
        this.apiKeys[name] = key;
        console.log(`API Key added: ${name}`);
    }

    // Function to retrieve an API key by name
    getApiKey(name) {
        if (!this.apiKeys[name]) {
            throw new Error(`API Key not found: ${name}`);
        }
        return this.apiKeys[name];
    }

    // Function to remove an API key
    removeApiKey(name) {
        if (!this.apiKeys[name]) {
            throw new Error(`API Key not found: ${name}`);
        }
        delete this.apiKeys[name];
        console.log(`API Key removed: ${name}`);
    }
}

// Example usage of the ApiKeyManager and Web3
(async () => {
    try {
        // Initialize Web3
        const web3 = await initWeb3();

        // Create an instance of ApiKeyManager
        const apiKeyManager = new ApiKeyManager();

        // Adding API keys
        apiKeyManager.addApiKey('Infura', 'YOUR_INFURA_API_KEY');
        apiKeyManager.addApiKey('Alchemy', 'YOUR_ALCHEMY_API_KEY');

        // Retrieve an API key
        const infuraKey = apiKeyManager.getApiKey('Infura');
        console.log('Retrieved Infura API Key:', infuraKey);

        // Remove an API key
        apiKeyManager.removeApiKey('Alchemy');

    } catch (error) {
        console.error('Error initializing application:', error);
    }
})();
```
