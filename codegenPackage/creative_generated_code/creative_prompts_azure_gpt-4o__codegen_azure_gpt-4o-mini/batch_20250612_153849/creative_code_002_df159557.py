"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-disperse.vercel.app
Prompt: Generate a JavaScript function for dispersing tokens on Starknet, ensuring compatibility with a tool like Starknet Disperse.
Generated: DETERMINISTIC_df15955727a0cf6c
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Disperse tokens on Starknet using the Starknet Disperse tool.
 * 
 * @param {string} contractAddress - The address of the token contract on Starknet.
 * @param {Array<string>} recipients - An array of recipient addresses.
 * @param {Array<number>} amounts - An array of amounts corresponding to each recipient.
 * @param {object} starknetProvider - An instance of the Starknet provider for interacting with the blockchain.
 * 
 * @throws Will throw an error if the input parameters are invalid or if the transaction fails.
 */
async function disperseTokens(contractAddress, recipients, amounts, starknetProvider) {
    // Validate input parameters
    if (!/^0x[a-fA-F0-9]{40}$/.test(contractAddress)) {
        throw new Error("Invalid contract address format.");
    }
    
    if (!Array.isArray(recipients) || !Array.isArray(amounts) || recipients.length !== amounts.length) {
        throw new Error("Recipients and amounts must be arrays of the same length.");
    }

    // Prepare transaction data
    const transactionData = {
        contract: contractAddress,
        recipients: recipients,
        amounts: amounts
    };

    try {
        // Send transaction to disperse tokens
        const response = await starknetProvider.sendTransaction(transactionData);
        console.log("Transaction successful:", response);
        return response; // Return the response for further processing if needed
    } catch (error) {
        console.error("Transaction failed:", error);
        throw new Error("Failed to disperse tokens: " + error.message);
    }
}

// Example usage (assuming internet connection & provider setup)
// const starknetProvider = ...; // Initialize your Starknet provider
// disperseTokens("0xYourTokenContractAddress", ["0xRecipientAddress1", "0xRecipientAddress2"], [100, 200], starknetProvider)
//     .then(result => console.log(result))
//     .catch(err => console.error(err));
```
