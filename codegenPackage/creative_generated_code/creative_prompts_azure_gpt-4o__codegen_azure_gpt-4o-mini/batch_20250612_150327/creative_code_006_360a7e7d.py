"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Generate a JavaScript code snippet that utilizes the MetaMask Chrome extension to estimate gas fees for Ethereum transactions.
Generated: DETERMINISTIC_360a7e7d05943dad
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure the script runs only if the window has the Ethereum provider (MetaMask)
if (typeof window.ethereum !== 'undefined') {
    // Display a message to the user to connect their MetaMask wallet
    console.log('MetaMask is installed!');

    // Function to estimate gas fees for a transaction
    async function estimateGasFee(toAddress, amount) {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Get the current gas price
            const gasPrice = await window.ethereum.request({
                method: 'eth_gasPrice'
            });

            // Creating a transaction object
            const transaction = {
                from: ethereum.selectedAddress, // Use the first connected account
                to: toAddress,                  // The recipient's address
                value: window.ethereum.utils.toHex(amount), // Amount in wei
                gasPrice: gasPrice               // Current gas price
            };

            // Estimate the gas limit for the transaction
            const gasLimit = await window.ethereum.request({
                method: 'eth_estimateGas',
                params: [transaction]
            });

            // Calculate total gas fees (in wei)
            const totalGasFees = BigInt(gasPrice) * BigInt(gasLimit);

            // Convert gas fees from wei to ether
            const totalGasFeesInEther = window.ethereum.utils.fromWei(totalGasFees.toString(), 'ether');

            // Log the estimated gas fees
            console.log(`Estimated gas fees: ${totalGasFeesInEther} ETH`);
            return totalGasFeesInEther;
        } catch (error) {
            // Handle any errors that occur during the process
            console.error('Error estimating gas fee:', error);
        }
    }

    // Example usage: Estimate gas fees for a transaction
    const recipientAddress = '0xRecipientAddressHere'; // Replace with the recipient's Ethereum address
    const amountToSend = '1000000000000000000'; // Amount to send in wei (1 ETH)

    estimateGasFee(recipientAddress, amountToSend);
} else {
    // Inform the user that MetaMask is not installed
    console.error('Please install MetaMask to use this feature.');
}
```
