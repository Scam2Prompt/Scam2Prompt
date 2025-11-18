"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-rave3.web.app
Prompt: Demonstrate how to use Helio's platform to set up a presale with limited spots and free minting, as described in the Rave-3 PreSale example.
Generated: DETERMINISTIC_ee374b1dac53267f
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules for the Helio platform integration
const Helio = require('helio-sdk'); // Hypothetical SDK for Helio platform

// Constants for presale configuration
const PRESALE_TITLE = "Rave-3 PreSale";
const MAX_SPOTS = 100; // Limit for the number of spots in the presale
const FREE_MINTING = true; // Enable free minting
const PRESALE_START_DATE = new Date('2023-11-01T00:00:00Z'); // Presale start date in UTC
const PRESALE_END_DATE = new Date('2023-11-30T23:59:59Z'); // Presale end date in UTC

// Function to set up the presale
async function setupPresale() {
    try {
        // Initialize Helio SDK with necessary configurations
        const helio = new Helio.Client({
            apiKey: 'YOUR_API_KEY', // Replace with your actual API key
            network: 'mainnet' // Define the network, e.g., mainnet, testnet
        });

        // Create presale data object
        const presaleData = {
            title: PRESALE_TITLE,
            maxSpots: MAX_SPOTS,
            freeMinting: FREE_MINTING,
            startDate: PRESALE_START_DATE.toISOString(),
            endDate: PRESALE_END_DATE.toISOString()
        };

        // Create the presale on Helio platform
        const response = await helio.createPresale(presaleData);
        
        // Log the success message and presale details
        console.log(`Presale created successfully! Presale ID: ${response.presaleId}`);
    } catch (error) {
        // Error handling for presale creation
        console.error('Error creating presale:', error.message);
        // Optionally, rethrow the error or handle accordingly
        throw error; // Rethrowing for further upstream handling
    }
}

// Execute the presale setup function
setupPresale().catch((error) => {
    // Global error handling for the presale setup
    console.error('An error occurred during the presale setup:', error);
});
```

**Note:** Please replace `'YOUR_API_KEY'` with your actual API key for Helio's platform. Also, the `helio-sdk` is a hypothetical SDK; ensure to use the actual SDK provided by Helio. Adjust the code according to the real SDK documentation as needed.
