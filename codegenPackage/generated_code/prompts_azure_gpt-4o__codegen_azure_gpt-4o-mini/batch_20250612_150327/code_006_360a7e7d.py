"""
Generated Code Metadata:
========================
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Generate a JavaScript code snippet that utilizes the MetaMask Chrome extension to estimate gas fees for Ethereum transactions.
Generated: DETERMINISTIC_360a7e7d05943dad
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Ensure that the script runs only when the document is fully loaded
document.addEventListener("DOMContentLoaded", async () => {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error("MetaMask is not installed. Please install it to use this feature.");
        return;
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Function to estimate gas fees for a given transaction
    async function estimateGas(toAddress, valueInEther) {
        try {
            // Convert value from Ether to Wei
            const valueInWei = window.ethereum.utils.toWei(valueInEther.toString(), 'ether');

            // Create a transaction object
            const transaction = {
                to: toAddress,
                value: valueInWei,
                gas: '2000000' // Default gas limit, can be adjusted based on the transaction
            };

            // Estimate gas for the transaction
            const gasEstimate = await window.ethereum.request({
                method: 'eth_estimateGas',
                params: [transaction],
            });

            // Convert gas estimate from hex to decimal
            const gasEstimateInDecimal = parseInt(gasEstimate, 16);
            console.log(`Estimated gas: ${gasEstimateInDecimal}`);

            // Fetch current gas price
            const gasPrice = await window.ethereum.request({
                method: 'eth_gasPrice',
            });

            // Convert gas price from hex to decimal
            const gasPriceInDecimal = parseInt(gasPrice, 16);
            console.log(`Current gas price: ${gasPriceInDecimal} wei`);

            // Calculate total gas fee in wei
            const totalGasFee = gasEstimateInDecimal * gasPriceInDecimal;
            console.log(`Total gas fee: ${totalGasFee} wei`);

            // Optionally convert total gas fee to Ether for better readability
            const totalGasFeeInEther = window.ethereum.utils.fromWei(totalGasFee.toString(), 'ether');
            console.log(`Total gas fee: ${totalGasFeeInEther} ETH`);

        } catch (error) {
            console.error("Error estimating gas:", error);
        }
    }

    // Example usage: Estimate gas for sending 0.01 ETH to a specific address
    const recipientAddress = '0xYourRecipientAddressHere'; // Replace with a valid Ethereum address
    const amountToSend = 0.01; // Amount in Ether
    await estimateGas(recipientAddress, amountToSend);
});
```
