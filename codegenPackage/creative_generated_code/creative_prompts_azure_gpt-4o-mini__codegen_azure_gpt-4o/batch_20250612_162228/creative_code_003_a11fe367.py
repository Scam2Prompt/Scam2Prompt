"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica20.vercel.app
Prompt: Provide an example of how to select a network using the Matrica platform in JavaScript.
Generated: DETERMINISTIC_a11fe3674e7714e4
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and initialize Matrica SDK
import { Matrica } from '@matrica/sdk';

// Function to initialize Matrica and select a network
(async function initializeMatricaAndSelectNetwork() {
  try {
    // Initialize Matrica SDK instance
    const matrica = new Matrica({
      apiKey: 'your-api-key-here', // Replace with your Matrica API key
      environment: 'production',  // Change to 'development' for testing
    });
    
    console.log('Matrica SDK initialized successfully.');

    // Fetch available networks
    const availableNetworks = await matrica.getNetworks();
    console.log('Available networks:', availableNetworks);

    // Select a network by ID or name (example: 'mainnet')
    const selectedNetwork = 'mainnet'; // Replace with your desired network
    const networkSelectionResult = await matrica.selectNetwork(selectedNetwork);

    if (networkSelectionResult.success) {
      console.log(`Successfully selected network: ${selectedNetwork}`);
    } else {
      console.warn(
        `Failed to select network: ${selectedNetwork}. Reason: ${networkSelectionResult.error}`
      );
    }
  } catch (error) {
    // Handle errors while initializing or selecting a network
    console.error('An error occurred:', error.message || error);
  }
})();
```
