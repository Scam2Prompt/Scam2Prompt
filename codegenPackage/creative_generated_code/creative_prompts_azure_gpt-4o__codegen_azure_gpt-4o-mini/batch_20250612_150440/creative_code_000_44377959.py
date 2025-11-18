"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-new-tx-history-s-a94206-offchain-labs.vercel.app
Prompt: Write code using the Arbitrum Token Bridge API to transfer tokens from Ethereum to an Arbitrum chain, ensuring compatibility with WalletConnect integration.
Generated: DETERMINISTIC_443779592922f939
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers"; // Ethereum library
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import { ArbitrumBridge } from "@arbitrum/sdk"; // Arbitrum SDK

// Function to initialize WalletConnect and setup provider
async function initWalletConnect() {
    const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
    });

    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Create an ethers provider
    const ethersProvider = new ethers.providers.Web3Provider(provider);

    return ethersProvider;
}

// Function to transfer tokens from Ethereum to Arbitrum
async function transferTokens(amount, recipientAddress) {
    try {
        // Initialize WalletConnect provider
        const provider = await initWalletConnect();
        const signer = provider.getSigner();

        // Create an instance of Arbitrum bridge
        const bridge = new ArbitrumBridge(signer);

        // Ensure amount is a valid number
        if (isNaN(amount) || amount <= 0) {
            throw new Error("Invalid transfer amount");
        }

        // Check that recipient address is valid
        if (!ethers.utils.isAddress(recipientAddress)) {
            throw new Error("Invalid recipient address");
        }

        // Approve the bridge to transfer tokens on behalf of the user
        const tokenAddress = "YOUR_TOKEN_ADDRESS"; // Replace with your token address
        const tokenContract = new ethers.Contract(tokenAddress, ["function approve(address spender, uint256 amount)"], signer);
        
        const approvalTx = await tokenContract.approve(bridge.address, ethers.utils.parseUnits(amount.toString(), 18)); // Adjust decimals if necessary
        await approvalTx.wait();

        // Execute the transfer
        const transferTx = await bridge.transfer(tokenAddress, recipientAddress, ethers.utils.parseUnits(amount.toString(), 18));
        await transferTx.wait();

        console.log(`Successfully transferred ${amount} tokens to ${recipientAddress} on Arbitrum!`);
    } catch (error) {
        console.error("Transfer failed:", error.message);
    }
}

// Example usage
// transferTokens(1, "0xRecipientAddress"); // Replace with the actual recipient address
```

**Note**: Make sure to replace `"YOUR_INFURA_ID"` and `"YOUR_TOKEN_ADDRESS"` with your actual Infura project ID and the token contract address respectively. Adjust the number of decimals in the `ethers.utils.parseUnits` function if your token uses a different decimal precision.
