"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.hq-innovacion.mx
Prompt: Write a script to programmatically switch MetaMask to a specific Ethereum test network using EIP-3085.
Generated: DETERMINISTIC_61c267a626986394
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
// Ensure you have the Ethereum provider injected by MetaMask
if (typeof window.ethereum !== 'undefined') {
    const { ethereum } = window;

    // Function to switch to a specific Ethereum test network
    async function switchEthereumNetwork(chainId) {
        // EIP-3085: switch Ethereum network
        try {
            await ethereum.request({
                method: 'wallet_switchEthereumChain',
                params: [{ chainId: chainId }],
            });
            console.log(`Switched to network with chain ID: ${chainId}`);
        } catch (error) {
            // Handle errors during the switch
            if (error.code === 4902) {
                // This error code indicates that the chain is not added to the wallet
                console.error(`The requested chain is not available in MetaMask. Please add it first.`);
                // Optionally, you can provide a way to add the chain here
            } else {
                console.error(`Failed to switch network: ${error.message}`);
            }
        }
    }

    // Example usage
    const ropstenChainId = '0x3'; // Hexadecimal for Ropsten's chain ID
    const rinkebyChainId = '0x4'; // Hexadecimal for Rinkeby's chain ID

    // Call the function to switch to Ropsten test network
    switchEthereumNetwork(ropstenChainId);
} else {
    console.error("MetaMask is not installed. Please install MetaMask to use this feature.");
}
```
