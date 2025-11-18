"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-kzna.com
Prompt: Generate code to integrate Brave Wallet with a web application, allowing users to connect their wallet and mint NFTs based on their chosen primordial power.
Generated: DETERMINISTIC_071e71c30d53e19f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { ethers } from "ethers"; // Ethereum library
import Web3Modal from "web3modal"; // Web3 modal for wallet connection
import { abi, contractAddress } from "./config"; // Import ABI and contract address for NFT smart contract

// Function to initialize Brave Wallet connection and mint NFTs
async function connectWalletAndMintNFT(primordialPower) {
  try {
    // Web3Modal configuration
    const web3Modal = new Web3Modal({
      cacheProvider: false,
      providerOptions: {
        walletconnect: {
          package: ethers.providers.JsonRpcProvider,
        },
      },
    });

    // Prompt user to connect their Brave Wallet
    const provider = await web3Modal.connect();
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Check if the connected wallet is Brave Wallet
    const walletName = provider.isBraveWallet ? "Brave Wallet" : "Unknown Wallet";
    console.log(`Connected Wallet: ${walletName}`);

    if (!provider.isBraveWallet) {
      throw new Error("Please connect using Brave Wallet.");
    }

    // Get user's Ethereum account
    const signer = web3Provider.getSigner();
    const userAddress = await signer.getAddress();
    console.log(`User Address: ${userAddress}`);

    // Validate primordial power input
    if (!["fire", "water", "earth", "air"].includes(primordialPower.toLowerCase())) {
      throw new Error("Invalid primordial power selected. Choose from: fire, water, earth, air.");
    }

    // Create a contract instance
    const nftContract = new ethers.Contract(contractAddress, abi, signer);

    // Mint NFT based on user's chosen primordial power
    const mintTx = await nftContract.mintNFT(userAddress, primordialPower.toLowerCase());
    console.log("Minting NFT... Please wait.");

    // Wait for transaction confirmation
    const receipt = await mintTx.wait();
    console.log("NFT Minted Successfully:", receipt);

    return {
      success: true,
      message: "NFT minted successfully!",
      receipt,
    };
  } catch (error) {
    console.error("Error during wallet connection or NFT minting:", error.message);
    return {
      success: false,
      message: error.message,
    };
  }
}

// Example usage of the function
// Call this function from your front-end when the user selects a primordial power and clicks "Mint NFT".
connectWalletAndMintNFT("fire").then((result) => {
  if (result.success) {
    console.log(result.message);
  } else {
    console.error(result.message);
  }
});
```

**Notes on configuration:**
- Replace `"./config"` with the path to your local configuration file containing the NFT contract ABI and address.
- Ensure the smart contract supports a `mintNFT` function that accepts the user's wallet address and power type as parameters.
