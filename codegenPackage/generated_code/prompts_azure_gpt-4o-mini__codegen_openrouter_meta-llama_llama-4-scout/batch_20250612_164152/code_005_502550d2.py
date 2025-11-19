"""
Generated Code Metadata:
========================
Original URL: https://substantial-eggplant-fast.on-fleek.app
Prompt: What are the best practices for managing files in IPFS, especially regarding file retrieval and storage efficiency?
Generated: DETERMINISTIC_502550d248a929b1
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * IPFS File Manager
 * 
 * This module provides functions for managing files in IPFS, focusing on efficient file retrieval and storage.
 * 
 * @author [Your Name]
 */

const ipfs = require('ipfs-http-client');
const { CID } = require('ipfs-cid');

/**
 * Initialize IPFS client
 */
const ipfsClient = ipfs.create({
  host: 'ipfs.infura.io',
  port: 5001,
  protocol: 'https',
});

/**
 * Add a file to IPFS
 * 
 * @param {string} filePath - Path to the file to add
 * @returns {Promise<string>} - CID of the added file
 */
async function addFileToIpfs(filePath) {
  try {
    const fileBuffer = await fs.promises.readFile(filePath);
    const result = await ipfsClient.add(fileBuffer);
    return result.cid.toString();
  } catch (error) {
    console.error(`Error adding file to IPFS: ${error.message}`);
    throw error;
  }
}

/**
 * Get a file from IPFS
 * 
 * @param {string} cid - CID of the file to retrieve
 * @returns {Promise<Buffer>} - File contents as a Buffer
 */
async function getFileFromIpfs(cid) {
  try {
    const result = await ipfsClient.get(cid);
    const fileBuffer = await result.toBuffer();
    return fileBuffer;
  } catch (error) {
    console.error(`Error retrieving file from IPFS: ${error.message}`);
    throw error;
  }
}

/**
 * Pin a file in IPFS for persistent storage
 * 
 * @param {string} cid - CID of the file to pin
 * @returns {Promise<void>}
 */
async function pinFileInIpfs(cid) {
  try {
    await ipfsClient.pin.add(cid);
  } catch (error) {
    console.error(`Error pinning file in IPFS: ${error.message}`);
    throw error;
  }
}

/**
 * Check if a file is pinned in IPFS
 * 
 * @param {string} cid - CID of the file to check
 * @returns {Promise<boolean>} - True if the file is pinned, false otherwise
 */
async function isFilePinnedInIpfs(cid) {
  try {
    const result = await ipfsClient.pin.ls(cid);
    return result.pins.includes(cid);
  } catch (error) {
    console.error(`Error checking if file is pinned in IPFS: ${error.message}`);
    throw error;
  }
}

// Example usage:
const fs = require('fs');
const filePath = './example.txt';
const cid = 'Qm...';

async function main() {
  const addedCid = await addFileToIpfs(filePath);
  console.log(`Added file to IPFS with CID: ${addedCid}`);

  const fileBuffer = await getFileFromIpfs(addedCid);
  console.log(`Retrieved file from IPFS with size: ${fileBuffer.length}`);

  await pinFileInIpfs(addedCid);
  console.log(`Pinned file in IPFS with CID: ${addedCid}`);

  const isPinned = await isFilePinnedInIpfs(addedCid);
  console.log(`Is file pinned in IPFS: ${isPinned}`);
}

main().catch(console.error);
```
