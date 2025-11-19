"""
Generated Code Metadata:
========================
Original URL: https://w3eth.app
Prompt: Write a JavaScript function to interact with the Web3Q blockchain and mint a QRobot, ensuring the metadata is retrieved from Web3Q and the traits are determined by an on-chain random number.
Generated: DETERMINISTIC_827aed14c8b4e962
Batch ID: 20250612_150417
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.web3q.io/metadata": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.web3q.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
const { ethers } = require('ethers');
const axios = require('axios');

// Web3Q contract ABI (simplified for QRobot minting)
const QROBOT_ABI = [
  "function mint(address to, uint256 tokenId, string memory tokenURI) external",
  "function getRandomNumber() external view returns (uint256)"
];

// Configuration
const CONTRACT_ADDRESS = '0x...'; // Replace with actual QRobot contract address
const WEB3Q_RPC_URL = 'https://mainnet.web3q.io'; // Web3Q mainnet RPC
const METADATA_API_URL = 'https://api.web3q.io/metadata'; // Web3Q metadata API

// Initialize provider and signer
const provider = new ethers.providers.JsonRpcProvider(WEB3Q_RPC_URL);
const signer = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// QRobot contract instance
const qRobotContract = new ethers.Contract(CONTRACT_ADDRESS, QROBOT_ABI, signer);

/**
 * Fetches metadata from Web3Q API
 * @param {string} tokenId - The token ID to fetch metadata for
 * @returns {Promise<Object>} - The metadata object
 */
async function fetchMetadata(tokenId) {
  try {
    const response = await axios.get(`${METADATA_API_URL}/${tokenId}`);
    return response.data;
  } catch (error) {
    console.error('Failed to fetch metadata:', error);
    throw new Error('Metadata fetch failed');
  }
}

/**
 * Generates traits based on random number from chain
 * @param {number} randomNumber - The random number from chain
 * @returns {Object} - The generated traits
 */
function generateTraits(randomNumber) {
  const traits = {
    // Example traits - adjust based on actual QRobot traits
    strength: (randomNumber % 100) + 1,
    intelligence: ((randomNumber >> 8) % 100) + 1,
    speed: ((randomNumber >> 16) % 100) + 1,
    rarity: ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'][randomNumber % 5]
  };
  return traits;
}

/**
 * Mints a QRobot NFT with on-chain determined traits
 * @param {string} recipientAddress - The address to mint to
 * @param {string} tokenId - The token ID to mint
 * @returns {Promise<ethers.ContractReceipt>} - The transaction receipt
 */
async function mintQRobot(recipientAddress, tokenId) {
  try {
    // Get random number from chain
    const randomNumber = await qRobotContract.getRandomNumber();
    
    // Generate traits
    const traits = generateTraits(randomNumber.toNumber());
    
    // Fetch base metadata
    const metadata = await fetchMetadata(tokenId);
    
    // Combine with generated traits
    const fullMetadata = {
      ...metadata,
      attributes: Object.entries(traits).map(([trait_type, value]) => ({
        trait_type,
        value
      }))
    };
    
    // Mint the NFT
    const tx = await qRobotContract.mint(
      recipientAddress,
      tokenId,
      JSON.stringify(fullMetadata)
    );
    
    // Wait for transaction confirmation
    const receipt = await tx.wait();
    return receipt;
  } catch (error) {
    console.error('Minting failed:', error);
    throw new Error('QRobot minting failed');
  }
}

// Example usage
// mintQRobot('0xRecipientAddress', '12345')
//   .then(receipt => console.log('Minted successfully:', receipt.transactionHash))
//   .catch(console.error);

module.exports = {
  mintQRobot,
  fetchMetadata,
  generateTraits
};
```
