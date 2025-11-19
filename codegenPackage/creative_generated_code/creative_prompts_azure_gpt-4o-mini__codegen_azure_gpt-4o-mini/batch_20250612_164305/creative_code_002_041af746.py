"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Generate an example of a UserOp transaction that can be processed across multiple chains using Particle Network's infrastructure.
Generated: DETERMINISTIC_041af7468a1395b3
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Particle Network SDK
import { ParticleNetwork, UserOp } from 'particle-network-sdk';

// Initialize Particle Network with your project credentials
const particleNetwork = new ParticleNetwork({
    appId: 'YOUR_APP_ID',
    appSecret: 'YOUR_APP_SECRET',
});

// Function to create and send a UserOp transaction across multiple chains
async function sendMultiChainUserOp(userAddress, targetChain, amount, options = {}) {
    try {
        // Validate input parameters
        if (!userAddress || !targetChain || !amount) {
            throw new Error('Invalid parameters: userAddress, targetChain, and amount are required.');
        }

        // Create a new UserOp instance
        const userOp = new UserOp({
            from: userAddress,
            to: targetChain,
            value: amount,
            ...options, // Additional options if provided
        });

        // Send the UserOp transaction
        const response = await particleNetwork.sendUserOp(userOp);

        // Check the response for success
        if (response.error) {
            throw new Error(`Transaction failed: ${response.error.message}`);
        }

        console.log('Transaction successful:', response);
        return response;
    } catch (error) {
        // Handle errors appropriately
        console.error('Error sending UserOp transaction:', error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}

// Example usage of the function
(async () => {
    try {
        const userAddress = '0xYourUserAddress'; // Replace with actual user address
        const targetChain = 'Ethereum'; // Replace with your target chain
        const amount = '0.1'; // Amount to send

        // Call the function to send the UserOp
        const result = await sendMultiChainUserOp(userAddress, targetChain, amount);
        console.log('UserOp result:', result);
    } catch (error) {
        console.error('Error in example execution:', error.message);
    }
})();
```
