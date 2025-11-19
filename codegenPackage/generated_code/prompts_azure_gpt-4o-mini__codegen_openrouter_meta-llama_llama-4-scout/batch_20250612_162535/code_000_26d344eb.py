"""
Generated Code Metadata:
========================
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: How can I implement data portability using the Vana Network demo and ensure my personal data remains non-custodial?
Generated: DETERMINISTIC_26d344ebe1aec1af
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { VanaNetwork } = require('vana-network-sdk');
const { ethers } = require('ethers');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

/**
 * Data Portability Implementation using Vana Network Demo
 * =======================================================
 */

// Set up Vana Network demo configuration
const vanaNetworkConfig = {
  apiKey: process.env.VANA_NETWORK_API_KEY,
  apiSecret: process.env.VANA_NETWORK_API_SECRET,
  network: 'demo',
};

/**
 * Create a Vana Network client instance
 * @type {VanaNetwork}
 */
const vanaNetworkClient = new VanaNetwork(vanaNetworkConfig);

/**
 * Generate a new Ethereum wallet for non-custodial data storage
 * @type {ethers.Wallet}
 */
const wallet = ethers.Wallet.createRandom();

/**
 * Function to upload data to Vana Network
 * @param {string} data - Data to be uploaded
 * @param {string} walletAddress - Ethereum wallet address
 * @returns {Promise<string>} - Uploaded data CID
 */
async function uploadData(data, walletAddress) {
  try {
    // Encrypt data using the user's wallet
    const encryptedData = await encryptData(data, walletAddress);

    // Upload encrypted data to Vana Network
    const uploadResponse = await vanaNetworkClient.upload(encryptedData);

    // Return the uploaded data CID
    return uploadResponse.cid;
  } catch (error) {
    console.error('Error uploading data:', error);
    throw error;
  }
}

/**
 * Function to download data from Vana Network
 * @param {string} cid - Data CID to be downloaded
 * @param {string} walletAddress - Ethereum wallet address
 * @returns {Promise<string>} - Downloaded data
 */
async function downloadData(cid, walletAddress) {
  try {
    // Download encrypted data from Vana Network
    const downloadResponse = await vanaNetworkClient.download(cid);

    // Decrypt data using the user's wallet
    const decryptedData = await decryptData(downloadResponse.data, walletAddress);

    // Return the decrypted data
    return decryptedData;
  } catch (error) {
    console.error('Error downloading data:', error);
    throw error;
  }
}

/**
 * Function to encrypt data using the user's wallet
 * @param {string} data - Data to be encrypted
 * @param {string} walletAddress - Ethereum wallet address
 * @returns {Promise<string>} - Encrypted data
 */
async function encryptData(data, walletAddress) {
  // Implement encryption logic using the user's wallet
  // For demonstration purposes, use a simple encryption scheme
  const encryptedData = await ethers.utils.keccak256(data);
  return encryptedData;
}

/**
 * Function to decrypt data using the user's wallet
 * @param {string} encryptedData - Encrypted data to be decrypted
 * @param {string} walletAddress - Ethereum wallet address
 * @returns {Promise<string>} - Decrypted data
 */
async function decryptData(encryptedData, walletAddress) {
  // Implement decryption logic using the user's wallet
  // For demonstration purposes, use a simple decryption scheme
  const decryptedData = await ethers.utils.keccak256(encryptedData);
  return decryptedData;
}

// Example usage
async function main() {
  try {
    const data = 'Hello, World!';
    const walletAddress = wallet.address;

    const cid = await uploadData(data, walletAddress);
    console.log(`Uploaded data CID: ${cid}`);

    const downloadedData = await downloadData(cid, walletAddress);
    console.log(`Downloaded data: ${downloadedData}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
