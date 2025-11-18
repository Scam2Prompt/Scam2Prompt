"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: Generate code to integrate a Web3 wallet connection feature for the Cornucopias MMORPG, allowing players to access their migrated NFTs and digital assets within the game.
Generated: DETERMINISTIC_4ee32ee1b1eacb65
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from "web3";
import Web3Modal from "web3modal";

// Define constants and configuration
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura Project ID
const NETWORK = "mainnet"; // Use 'mainnet' or 'testnet' depending on your environment
const CONTRACT_ADDRESS = "your-contract-address"; // Replace with the game's NFT smart contract address
const ABI = [ /* Add the contract's ABI here */ ]; // Replace with the ABI of your NFT contract

// Initialize Web3Modal for wallet connections
const providerOptions = {
  /* Add provider options here, e.g., WalletConnect, Coinbase Wallet, etc. */
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // Enable to remember the last used wallet
  providerOptions, // Wallet providers
});

// Function to connect wallet
const connectWallet = async () => {
  try {
    // Prompt user to connect wallet
    const provider = await web3Modal.connect();
    
    // Initialize Web3 with the provider
    const web3 = new Web3(provider);

    // Get user's accounts
    const accounts = await web3.eth.getAccounts();
    if (!accounts || accounts.length === 0) {
      throw new Error("No accounts found. Please connect a wallet.");
    }

    // Get the wallet address (first account)
    const walletAddress = accounts[0];
    console.log("Connected Wallet Address:", walletAddress);

    // Fetch migrated NFTs and assets
    const nfts = await fetchUserNFTs(web3, walletAddress);
    console.log("User NFTs:", nfts);

    return { walletAddress, nfts };
  } catch (error) {
    console.error("Error connecting wallet:", error.message);
    throw error; // Re-throw for further handling in the application
  }
};

// Function to fetch user's NFTs
const fetchUserNFTs = async (web3, walletAddress) => {
  try {
    // Initialize contract instance
    const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

    // Call the contract's method to fetch NFT data (modify based on your contract's implementation)
    const nftIds = await contract.methods.tokensOfOwner(walletAddress).call();

    // Fetch metadata for each NFT (optional, if your game requires it)
    const nftDetails = await Promise.all(
      nftIds.map(async (tokenId) => {
        const metadataUri = await contract.methods.tokenURI(tokenId).call();
        const metadataResponse = await fetch(metadataUri);
        const metadata = await metadataResponse.json();
        return { tokenId, metadata };
      })
    );

    return nftDetails;
  } catch (error) {
    console.error("Error fetching NFTs:", error.message);
    throw error; // Re-throw for further handling in the application
  }
};

// Disconnect wallet (optional)
const disconnectWallet = async () => {
  try {
    await web3Modal.clearCachedProvider();
    console.log("Wallet disconnected successfully.");
  } catch (error) {
    console.error("Error disconnecting wallet:", error.message);
  }
};

// Usage example
(async () => {
  try {
    const { walletAddress, nfts } = await connectWallet();
    console.log(`Wallet ${walletAddress} connected with ${nfts.length} NFTs.`);
  } catch (error) {
    console.error("Failed to connect wallet:", error.message);
  }
})();
```

This JavaScript code snippet integrates a Web3 wallet connection for a game and retrieves migrated NFTs. It uses `Web3` and `Web3Modal`, includes essential error handling, and adheres to best practices. Be sure to replace placeholders like the ABI, contract address, and Infura Project ID with real values before deploying to production.
