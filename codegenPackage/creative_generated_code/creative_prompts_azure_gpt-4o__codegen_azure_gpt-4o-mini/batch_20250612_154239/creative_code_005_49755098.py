"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Provide an example of using the Solana Web3.js library to implement a "Next Draw" countdown based on the number of keys purchased in a blockchain lottery.
Generated: DETERMINISTIC_49755098c326fa38
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Solana Web3.js library
const {
    Connection,
    PublicKey,
    clusterApiUrl,
    Keypair,
    Transaction,
    SystemProgram,
} = require('@solana/web3.js');

// Lottery configuration
const LOTTERY_PROGRAM_ID = new PublicKey('YOUR_LOTTERY_PROGRAM_ID'); // Replace with your lottery program ID
const CONNECTION = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

// Function to get the current draw time and the number of keys purchased
async function getLotteryDetails() {
    try {
        // Replace with the logic to fetch the lottery state from your smart contract
        const lotteryStateAccount = await CONNECTION.getAccountInfo(LOTTERY_PROGRAM_ID);
        if (!lotteryStateAccount) {
            throw new Error('Lottery state account not found');
        }

        // Decode and parse the lottery state (this is a placeholder)
        const lotteryStateData = lotteryStateAccount.data; // Replace with actual decoding
        const nextDrawTime = lotteryStateData.nextDrawTime; // Placeholder for extracting draw time
        const keysPurchased = lotteryStateData.keysPurchased; // Placeholder for extracting keys purchased
        
        return { nextDrawTime, keysPurchased };
    } catch (error) {
        console.error('Error fetching lottery details:', error);
        throw error;
    }
}

// Function to update the countdown display and handle the lottery state
function updateCountdown(nextDrawTime) {
    const countdownElement = document.getElementById('countdown');
    
    // Update the countdown every second
    const countdownInterval = setInterval(() => {
        const now = new Date().getTime();
        const distance = nextDrawTime - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is over, display a message
        if (distance < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = 'EXPIRED';
        }
    }, 1000);
}

// Main function to initiate the countdown
async function main() {
    try {
        const { nextDrawTime, keysPurchased } = await getLotteryDetails();
        
        // Start the countdown if nextDrawTime is valid
        if (nextDrawTime) {
            updateCountdown(nextDrawTime);
            console.log(`Keys purchased: ${keysPurchased}`);
        } else {
            console.warn('Next draw time is not defined');
        }
    } catch (error) {
        console.error('Error in main function:', error);
    }
}

// Run the main function on page load
window.onload = () => {
    main();
};
```
