"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Generate code for a whitelist-based NFT minting system on Solana, incorporating wallet selection and free minting functionality as outlined on the Immortals NFT site.
Generated: DETERMINISTIC_7a6915676ec6c98a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
import {
  Connection,
  PublicKey,
  clusterApiUrl,
  Transaction,
  SystemProgram,
} from '@solana/web3.js';
import { mintNFT } from './nftMinting'; // Hypothetical minting function
import { getWhitelistedUsers } from './whitelist'; // Hypothetical function to get whitelisted users
import { ToastContainer, toast } from 'react-toastify'; // For notifications
import 'react-toastify/dist/ReactToastify.css'; // Toast CSS

// Define constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const CONNECTION = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Main minting function
async function mintNFTWithWhitelist(wallet) {
  try {
    // Validate wallet connection
    if (!wallet || !wallet.publicKey) {
      throw new Error('Wallet is not connected.');
    }

    // Fetch the list of whitelisted users
    const whitelistedUsers = await getWhitelistedUsers();
    const userPublicKey = wallet.publicKey.toString();

    // Check if the user is whitelisted
    if (!whitelistedUsers.includes(userPublicKey)) {
      throw new Error('You are not whitelisted to mint this NFT.');
    }

    // Call the mintNFT function to mint the NFT
    const mintTransaction = await mintNFT(wallet);
    
    // Confirm the transaction
    await CONNECTION.confirmTransaction(mintTransaction, 'processed');
    
    // Notify the user of successful minting
    toast.success('NFT minted successfully!');
  } catch (error) {
    // Handle errors and notify the user
    console.error('Minting error:', error);
    toast.error(`Minting failed: ${error.message}`);
  }
}

// React component for wallet selection and minting
const MintingComponent = ({ wallet }) => {
  return (
    <div>
      <h1>Whitelist-Based NFT Minting</h1>
      <button onClick={() => mintNFTWithWhitelist(wallet)}>
        Mint NFT
      </button>
      <ToastContainer />
    </div>
  );
};

export default MintingComponent;
```

Note: The hypothetical functions `mintNFT` and `getWhitelistedUsers` should be implemented based on your specific logic and requirements. Be sure to replace them with your actual code for NFT minting and whitelist management.
