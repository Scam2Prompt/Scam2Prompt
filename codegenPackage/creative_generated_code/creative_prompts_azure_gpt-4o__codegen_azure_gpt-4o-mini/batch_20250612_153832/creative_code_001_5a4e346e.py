"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suipassport.vercel.app
Prompt: Generate a script to claim a user's first stamp on the Sui Passport platform after connecting their wallet.
Generated: DETERMINISTIC_5a4e346eb73152d3
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { SuiWallet } from 'sui-wallet-sdk'; // Hypothetical SDK for wallet interaction
import { SuiPassport } from 'sui-passport-sdk'; // Hypothetical SDK for Sui Passport interaction

// Main function to claim the first stamp
async function claimFirstStamp() {
    try {
        // Connect to the user's wallet
        const wallet = new SuiWallet();
        await wallet.connect();

        // Get the user's wallet address
        const userAddress = wallet.getAddress();
        console.log(`Connected wallet address: ${userAddress}`);

        // Initialize the Sui Passport instance
        const passport = new SuiPassport(userAddress);

        // Check if the user is eligible for the first stamp
        const isEligible = await passport.checkEligibility();
        if (!isEligible) {
            throw new Error('User is not eligible to claim the first stamp.');
        }

        // Claim the first stamp
        const stampClaimResult = await passport.claimStamp();
        
        // Check the result of the claim
        if (stampClaimResult.success) {
            console.log(`First stamp claimed successfully! Transaction ID: ${stampClaimResult.transactionId}`);
        } else {
            throw new Error(`Failed to claim stamp: ${stampClaimResult.error}`);
        }
    } catch (error) {
        // Handle errors and display a user-friendly message
        console.error(`Error occurred: ${error.message}`);
        alert(`An error occurred while claiming the stamp: ${error.message}`);
    }
}

// Execute the function on page load or button click
document.getElementById('claim-stamp-btn').addEventListener('click', claimFirstStamp);
```
