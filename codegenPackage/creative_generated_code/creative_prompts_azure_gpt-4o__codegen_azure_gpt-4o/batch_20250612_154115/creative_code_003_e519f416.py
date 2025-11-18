"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskksloginn-1.gitbook.io
Prompt: Create a JavaScript function that verifies the wallet address, network compatibility, and token amount before initiating a transfer to MetaMask.
Generated: DETERMINISTIC_e519f416811ad3ea
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to verify wallet address, network compatibility, and token amount, 
 * and then initiate a transfer using MetaMask.
 * 
 * @param {string} walletAddress - The recipient's wallet address.
 * @param {string} network - The expected blockchain network (e.g., 'ethereum' or 'polygon').
 * @param {number} tokenAmount - The amount of tokens to transfer.
 * 
 * @returns {Promise<void>} - Resolves when the transfer is successful, otherwise throws an error.
 */
async function transferToMetaMask(walletAddress, network, tokenAmount) {
    try {
        // Validate wallet address using a simple regex for Ethereum addresses
        if (!/^0x[a-fA-F0-9]{40}$/.test(walletAddress)) {
            throw new Error('Invalid wallet address.');
        }

        // Ensure the token amount is valid and positive
        if (typeof tokenAmount !== 'number' || tokenAmount <= 0) {
            throw new Error('Invalid token amount. Must be a positive number.');
        }

        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed or available.');
        }

        // Request current network from MetaMask
        const currentNetwork = await window.ethereum.request({ method: 'net_version' });

        // Map network identifiers (example mapping; expand as needed)
        const networkMap = {
            '1': 'ethereum', // Mainnet
            '137': 'polygon', // Polygon
        };

        if (networkMap[currentNetwork] !== network) {
            throw new Error(`Incompatible network. Please switch to the ${network} network.`);
        }

        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        if (!accounts || accounts.length === 0) {
            throw new Error('No accounts found in MetaMask.');
        }

        const senderAddress = accounts[0];

        // Initialize the transfer (example assumes token transfer)
        const transactionParameters = {
            to: walletAddress,
            from: senderAddress,
            value: '0x' + (tokenAmount * Math.pow(10, 18)).toString(16), // Convert token amount to hexadecimal (assuming 18 decimals)
        };

        // Send transaction via MetaMask
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log(`Transaction successful! Hash: ${txHash}`);
    } catch (error) {
        // Log and rethrow the error for better debugging
        console.error('Error during transfer:', error.message);
        throw error;
    }
}
```
