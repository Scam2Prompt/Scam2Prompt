"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://base-dawgz-claim.pages.dev
Prompt: Create a JavaScript function that allows users to claim their airdrop tokens for the Base Dawgz Token after the presale ends.
Generated: DETERMINISTIC_5bf05068af89ca6a
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A function to claim airdrop tokens for the Base Dawgz Token after the presale ends.
 * 
 * @param {string} userAddress - The wallet address of the user claiming the tokens.
 * @param {number} amount - The amount of tokens to claim.
 * @param {boolean} presaleEnded - A flag indicating whether the presale has ended.
 * @param {function} sendTokens - A callback function to handle the token transfer.
 * @throws Will throw an error if the presale has not ended or if the user address is invalid.
 */
async function claimAirdropTokens(userAddress, amount, presaleEnded, sendTokens) {
    try {
        // Check if presale has ended
        if (!presaleEnded) {
            throw new Error("Presale has not ended. Tokens cannot be claimed yet.");
        }

        // Validate user address format (basic validation)
        if (!/^0x[a-fA-F0-9]{40}$/.test(userAddress)) {
            throw new Error("Invalid wallet address format.");
        }

        // Validate amount
        if (amount <= 0) {
            throw new Error("Claim amount must be greater than zero.");
        }

        // Simulate sending tokens process
        const transactionHash = await sendTokens(userAddress, amount);

        console.log(`Tokens successfully claimed! Transaction Hash: ${transactionHash}`);
        return transactionHash;
    } catch (error) {
        // Log the error message for debugging
        console.error("Error claiming airdrop tokens:", error.message);
        
        // Optionally, you could rethrow the error or handle it as needed
        throw error;
    }
}

// Example of sendTokens callback function (implementation would vary)
async function sendTokens(userAddress, amount) {
    // Simulate token transfer
    return new Promise((resolve) => {
        // Simulate a successful transaction hash
        setTimeout(() => {
            resolve("0x1234567890abcdef1234567890abcdef12345678");
        }, 1000);
    });
}

// Usage example (would be called after presale ends)
const userAddress = "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd";
const amountToClaim = 100;
const presaleEnded = true;

claimAirdropTokens(userAddress, amountToClaim, presaleEnded, sendTokens)
    .then(transactionHash => {
        console.log("Claim successful:", transactionHash);
    })
    .catch(error => {
        console.error("Claim failed:", error.message);
    });
```
