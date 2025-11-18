"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: Write code to implement ERC-7715 permissions in AppKit using Wagmi with asynchronous ecdsa key handling.
Generated: DETERMINISTIC_ceb2b7608e3747e5
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
import { ethers } from "ethers"; // For ECDSA key handling and Ethereum interactions
import { createClient, configureChains, chain } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configure the Ethereum provider and Wagmi client
const { provider, webSocketProvider } = configureChains(
  [chain.mainnet, chain.goerli], // Specify chains to support
  [publicProvider()] // Use public provider for blockchain interaction
);

const wagmiClient = createClient({
  autoConnect: true, // Automatically connect on page load
  provider,
  webSocketProvider,
});

// Utility function for asynchronous ECDSA key retrieval and signing
async function getECDSAKeyAndSignData(message) {
  try {
    const provider = new ethers.BrowserProvider(window.ethereum); // Use browser Ethereum provider
    const signer = await provider.getSigner(); // Get the signer (user wallet)
    
    // Sign the message with the user's private key
    const signature = await signer.signMessage(message);
    
    // Return the signed data
    return { signature, address: await signer.getAddress() };
  } catch (error) {
    console.error("Error in ECDSA key handling or signing:", error); // Log any errors
    throw new Error("Failed to sign the message."); // Rethrow for further handling
  }
}

// Function to check ERC-7715 permissions
async function checkERC7715Permissions(contractAddress, tokenId, userAddress) {
  try {
    // Define the ABI for the ERC-7715 contract (simplified example)
    const ERC_7715_ABI = [
      "function hasPermission(uint256 tokenId, address user) public view returns (bool)"
    ];

    // Create a new contract instance
    const provider = wagmiClient.getProvider();
    const contract = new ethers.Contract(contractAddress, ERC_7715_ABI, provider);

    // Call the contract's method to check permissions
    const hasPermission = await contract.hasPermission(tokenId, userAddress);

    return hasPermission; // Return the permission status (true/false)
  } catch (error) {
    console.error("Error checking ERC-7715 permissions:", error); // Log any errors
    throw new Error("Failed to check permissions."); // Rethrow for further handling
  }
}

// Example usage
(async () => {
  try {
    const message = "Hello, please sign this message to verify your identity.";
    
    // Asynchronously retrieve ECDSA key and sign data
    const { signature, address } = await getECDSAKeyAndSignData(message);
    console.log("Signed message:", signature);
    console.log("User address:", address);

    // Check ERC-7715 permissions for a specific tokenId and the user's address
    const contractAddress = "0xYourERC7715ContractAddress"; // Replace with actual contract address
    const tokenId = 12345; // Replace with actual tokenId
    
    const hasPermission = await checkERC7715Permissions(contractAddress, tokenId, address);
    console.log(`User has permission: ${hasPermission}`);
  } catch (error) {
    console.error("An error occurred during execution:", error); // Handle any errors
  }
})();
```
