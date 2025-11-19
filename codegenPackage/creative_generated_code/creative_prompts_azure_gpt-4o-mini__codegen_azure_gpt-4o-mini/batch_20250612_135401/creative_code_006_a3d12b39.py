"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.ghost.io
Prompt: How can developers leverage Wormhole's tools to build multichain applications efficiently?
Generated: DETERMINISTIC_a3d12b398ee39b85
Batch ID: 20250612_135401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Wormhole
const { WormholeClient } = require('@wormhole-foundation/wormhole-sdk');
const ethers = require('ethers');

// Define constants for the supported blockchains
const BLOCKCHAINS = {
    ETHEREUM: 'ethereum',
    SOLANA: 'solana',
    POLYGON: 'polygon',
    // Add more blockchains as supported
};

// Initialize the Wormhole client
const wormholeClient = new WormholeClient({
    // Provide necessary API keys or configurations
});

// Define a function to send a token between blockchains
async function sendToken(senderPrivateKey, tokenAddress, amount, targetChain, targetAddress) {
    try {
        // Validate input parameters
        if (!Object.values(BLOCKCHAINS).includes(targetChain)) {
            throw new Error('Unsupported target blockchain');
        }
        if (!ethers.utils.isAddress(targetAddress)) {
            throw new Error('Invalid target address');
        }

        // Create a wallet instance for the sender
        const senderWallet = new ethers.Wallet(senderPrivateKey);

        // Fetch token details from Wormhole
        const tokenDetails = await wormholeClient.getTokenDetails(tokenAddress);
        
        // Construct the transaction
        const tx = {
            to: targetAddress,
            value: ethers.utils.parseUnits(amount.toString(), tokenDetails.decimals),
            chainId: BLOCKCHAINS[targetChain],
            gasLimit: ethers.utils.hexlify(21000), // Set a gas limit for the transaction
        };

        // Sign and send the transaction
        const signedTx = await senderWallet.signTransaction(tx);
        const txResponse = await ethers.provider.sendTransaction(signedTx);

        console.log(`Transaction sent! Hash: ${txResponse.hash}`);

        // Wait for the transaction to be confirmed
        await txResponse.wait();
        console.log('Transaction confirmed successfully!');
    } catch (error) {
        console.error('Error sending token:', error.message);
    }
}

// Example usage of the sendToken function
(async () => {
    const senderPrivateKey = 'YOUR_PRIVATE_KEY';
    const tokenAddress = 'TOKEN_ADDRESS_ON_SOURCE_CHAIN';
    const amount = 10; // Amount to send
    const targetChain = BLOCKCHAINS.POLYGON; // Target blockchain to send to
    const targetAddress = 'TARGET_ADDRESS_ON_POLYGON';

    await sendToken(senderPrivateKey, tokenAddress, amount, targetChain, targetAddress);
})();
```
