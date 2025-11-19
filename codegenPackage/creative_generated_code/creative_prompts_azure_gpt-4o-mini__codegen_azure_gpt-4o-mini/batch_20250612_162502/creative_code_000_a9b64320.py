"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: How can I connect my MetaMask wallet to a DApp using the WalletConnect protocol as described on the Wormhole website?
Generated: DETERMINISTIC_a9b64320dbaee6fa
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import { ethers } from 'ethers';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Function to connect MetaMask wallet to DApp using WalletConnect protocol
async function connectWallet() {
    try {
        // Create a WalletConnect Provider
        const provider = new WalletConnectProvider({
            infuraId: 'YOUR_INFURA_ID', // Replace with your Infura Project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create a new ethers provider using the WalletConnect provider
        const web3Provider = new ethers.providers.Web3Provider(provider);

        // Get the signer to sign transactions
        const signer = web3Provider.getSigner();

        // Log the connected address
        const address = await signer.getAddress();
        console.log(`Connected to wallet: ${address}`);

        // Additional code to interact with your DApp can go here...

        return { provider, signer, address };
    } catch (error) {
        console.error("Failed to connect to the wallet:", error);
        // Handle error appropriately (e.g., show a user-friendly message)
    }
}

// Example usage
document.getElementById('connectButton').addEventListener('click', async () => {
    const walletConnection = await connectWallet();
    if (walletConnection) {
        // Proceed with functionality that requires the connected wallet
    }
});
```

Make sure to replace `'YOUR_INFURA_ID'` with your actual Infura Project ID. Be sure to have the necessary HTML elements (like a button with the ID `connectButton`) in your web page for the connection to initiate correctly.
