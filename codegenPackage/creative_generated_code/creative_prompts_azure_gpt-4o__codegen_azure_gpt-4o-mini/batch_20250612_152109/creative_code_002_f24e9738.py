"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guild-verify.web.app
Prompt: Generate code to connect a Coinbase Wallet to a Web3 application using the Guild SDK and check NFT ownership for access to a Discord guild.
Generated: DETERMINISTIC_f24e973856fd166f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Guild SDK and Web3
import { WalletConnectProvider } from "@web3-react/walletconnect-connector";
import { Web3ReactProvider, useWeb3React } from "@web3-react/core";
import { ethers } from "ethers";
import React, { useEffect, useState } from "react";

// Define a function to get the provider for Web3
function getLibrary(provider) {
    return new ethers.providers.Web3Provider(provider);
}

// Create a function to check NFT ownership
async function checkNFTOwnership(contractAddress, tokenId, userAddress) {
    try {
        // Initialize the contract using ethers.js
        const nftContract = new ethers.Contract(contractAddress, [
            // Minimal ABI to check ownership
            "function ownerOf(uint256 tokenId) view returns (address)"
        ], provider);
        
        // Call the ownerOf function from the contract
        const owner = await nftContract.ownerOf(tokenId);
        return owner.toLowerCase() === userAddress.toLowerCase();
    } catch (error) {
        console.error("Error checking NFT ownership:", error);
        throw new Error("Failed to check NFT ownership");
    }
}

// Create a functional component for the Web3 connection and NFT check
function App() {
    const { activate, account } = useWeb3React();
    const [hasAccess, setHasAccess] = useState(false);
    
    // Hard-code the NFT contract address and token ID for this example
    const contractAddress = "0xYourNFTContractAddress"; // Replace with actual contract address
    const tokenId = 1; // Replace with the actual token ID

    // Function to connect to the Coinbase Wallet
    const connectWallet = async () => {
        const connector = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID" // Replace with your Infura ID
        });
        try {
            await activate(connector);
            console.log("Wallet connected:", account);
            // Check NFT ownership after connecting
            const hasNFT = await checkNFTOwnership(contractAddress, tokenId, account);
            setHasAccess(hasNFT);
        } catch (error) {
            console.error("Connection error:", error);
        }
    };

    return (
        <div>
            <h1>NFT Ownership Check</h1>
            <button onClick={connectWallet}>Connect Coinbase Wallet</button>
            {hasAccess ? (
                <p>You have access to the Discord guild!</p>
            ) : (
                <p>{account ? "You do not have access." : "Please connect your wallet."}</p>
            )}
        </div>
    );
}

// Wrap the App component with Web3ReactProvider for context
const Root = () => (
    <Web3ReactProvider getLibrary={getLibrary}>
        <App />
    </Web3ReactProvider>
);

// Render the application
export default Root;
```

Make sure to replace `"0xYourNFTContractAddress"` and `"YOUR_INFURA_ID"` with the actual NFT contract address and your Infura project ID, respectively.
